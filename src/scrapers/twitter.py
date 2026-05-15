"""Twitter scraper: twikit (primary) or Apify altimis/scweet (fallback)."""

import asyncio
import logging
import os
import re
from datetime import datetime, timezone
from html import unescape
from typing import List, Optional

from dateutil.parser import isoparse
import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, TwitterConfig

logger = logging.getLogger(__name__)

# ── Apify constants (fallback path) ──────────────────────────────────────────
_APIFY_BASE = "https://api.apify.com/v2"
_POLL_INTERVAL = 3.0
_MAX_WAIT = 180


def _extract_handle(user_entry: str) -> str:
    """Extract bare @-free handle from 'https://x.com/foo', '@foo', or 'foo'."""
    s = user_entry.strip()
    if s.startswith("http"):
        s = s.rstrip("/").split("/")[-1]
    return s.lstrip("@")


class TwitterScraper(BaseScraper):
    """Fetch tweets via twikit (cookie auth) with Apify as fallback."""

    def __init__(self, config: TwitterConfig, http_client: httpx.AsyncClient):
        super().__init__(config, http_client)
        self.config = config

    # ─────────────────────────────────────────────────────────────────────────
    # Public interface
    # ─────────────────────────────────────────────────────────────────────────

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.config.enabled:
            return []

        handles = [_extract_handle(u) for u in self.config.users if u.strip()]
        if not handles:
            logger.debug("No Twitter users configured, skipping.")
            return []

        auth_token = os.environ.get("TWITTER_AUTH_TOKEN", "").strip()
        ct0 = os.environ.get("TWITTER_CT0", "").strip()
        apify_token = os.environ.get(self.config.apify_token_env, "").strip()

        if auth_token and ct0:
            logger.info("Twitter: using twikit (cookie auth)")
            return await self._fetch_twikit(handles, since, auth_token, ct0)
        elif apify_token:
            logger.info("Twitter: TWITTER_AUTH_TOKEN not set, falling back to Apify")
            return await self._fetch_apify(handles, since, apify_token)
        else:
            logger.warning(
                "Twitter: neither TWITTER_AUTH_TOKEN+TWITTER_CT0 nor %s found. Skipping.",
                self.config.apify_token_env,
            )
            return []

    # ─────────────────────────────────────────────────────────────────────────
    # twikit path
    # ─────────────────────────────────────────────────────────────────────────

    async def _fetch_twikit(
        self, handles: List[str], since: datetime, auth_token: str, ct0: str
    ) -> List[ContentItem]:
        try:
            from twikit import Client  # type: ignore
        except ImportError:
            logger.error("twikit is not installed. Run: pip install twikit")
            return []

        client = Client("en-US")
        client.set_cookies({"auth_token": auth_token, "ct0": ct0})

        items: List[ContentItem] = []
        per_user = max(20, self.config.fetch_limit)

        for handle in handles:
            try:
                user = await client.get_user_by_screen_name(handle)
                tweets = await client.get_user_tweets(user.id, "Tweets", count=per_user)
                for tweet in tweets:
                    parsed = self._parse_twikit_tweet(tweet, since)
                    if parsed:
                        items.append(parsed)
                logger.debug(f"@{handle}: fetched {len(tweets)} tweets")
                await asyncio.sleep(1.5)  # gentle rate-limit throttle
            except Exception as exc:
                logger.warning(f"twikit: failed to fetch @{handle}: {exc}")

        logger.info(f"twikit: {len(items)} tweets pass 48h filter across {len(handles)} accounts")
        return items

    def _parse_twikit_tweet(self, tweet, since: datetime) -> Optional[ContentItem]:
        try:
            # twikit's created_at_datetime is already UTC-aware
            published_at: datetime = tweet.created_at_datetime
            if published_at.tzinfo is None:
                published_at = published_at.replace(tzinfo=timezone.utc)
            if published_at < since:
                return None

            tweet_id = str(tweet.id)
            user = tweet.user
            screen_name = getattr(user, "screen_name", "unknown")
            author = getattr(user, "name", screen_name)
            text = unescape((tweet.full_text or tweet.text or "").strip())
            if not text:
                return None

            url = f"https://twitter.com/{screen_name}/status/{tweet_id}"
            title_body = text[:50].replace("\n", " ")
            if len(text) > 50:
                title_body += "..."

            return ContentItem(
                id=self._generate_id(SourceType.TWITTER.value, "tweet", tweet_id),
                source_type=SourceType.TWITTER,
                title=f"@{screen_name}: {title_body}",
                url=url,
                content=text,
                author=author,
                published_at=published_at,
                metadata={
                    "tweet_id": tweet_id,
                    "conversation_id": tweet_id,
                    "favorite_count": getattr(tweet, "favorite_count", 0) or 0,
                    "retweet_count": getattr(tweet, "retweet_count", 0) or 0,
                    "reply_count": getattr(tweet, "reply_count", 0) or 0,
                    "view_count": getattr(tweet, "view_count", None),
                    "is_reply": bool(getattr(tweet, "in_reply_to", None)),
                },
            )
        except Exception as exc:
            logger.debug(f"Failed to parse twikit tweet: {exc}")
            return None

    # ─────────────────────────────────────────────────────────────────────────
    # Apify fallback path (batched)
    # ─────────────────────────────────────────────────────────────────────────

    async def _fetch_apify(
        self, handles: List[str], since: datetime, token: str
    ) -> List[ContentItem]:
        # Convert bare handles back to full URLs for altimis~scweet
        users = [f"https://x.com/{h}" for h in handles]

        BATCH_SIZE = 5
        batches = [users[i : i + BATCH_SIZE] for i in range(0, len(users), BATCH_SIZE)]
        logger.info(f"Apify: {len(users)} accounts in {len(batches)} batches of {BATCH_SIZE}")

        all_items: List[ContentItem] = []
        seen_ids: set = set()

        for idx, batch in enumerate(batches):
            logger.info(f"  Batch {idx + 1}/{len(batches)}: {batch}")
            run_id, dataset_id = await self._apify_start_run(token, batch)
            if not run_id:
                continue
            if not await self._apify_wait(token, run_id):
                continue
            for raw in await self._apify_fetch_dataset(token, dataset_id):
                if isinstance(raw, dict) and raw.get("noResults"):
                    continue
                parsed = self._parse_apify_item(raw, since)
                if parsed and parsed.id not in seen_ids:
                    seen_ids.add(parsed.id)
                    all_items.append(parsed)

        logger.info(f"Apify: {len(all_items)} tweets after 48h filter")
        return all_items

    async def _apify_start_run(self, token: str, profile_urls: List[str]):
        payload = {
            "source_mode": "profiles",
            "profile_urls": profile_urls,
            "search_sort": "Latest",
            "max_items": max(100, self.config.fetch_limit) * len(profile_urls),
        }
        url = f"{_APIFY_BASE}/acts/{self.config.actor_id}/runs?token={token}"
        try:
            resp = await self.client.post(url, json=payload, timeout=30.0)
            resp.raise_for_status()
            data = resp.json()["data"]
            return data["id"], data["defaultDatasetId"]
        except Exception as exc:
            logger.error(f"Apify run start failed: {exc}")
            return None, None

    async def _apify_wait(self, token: str, run_id: str) -> bool:
        url = f"{_APIFY_BASE}/actor-runs/{run_id}?token={token}"
        elapsed = 0.0
        while elapsed < _MAX_WAIT:
            try:
                resp = await self.client.get(url, timeout=10.0)
                status = resp.json()["data"]["status"]
                if status == "SUCCEEDED":
                    return True
                if status in ("FAILED", "ABORTED", "TIMED-OUT"):
                    logger.error(f"Apify run {run_id} ended: {status}")
                    return False
            except Exception as exc:
                logger.warning(f"Apify poll error: {exc}")
            await asyncio.sleep(_POLL_INTERVAL)
            elapsed += _POLL_INTERVAL
        logger.warning(f"Apify run {run_id} timed out")
        return False

    async def _apify_fetch_dataset(self, token: str, dataset_id: str) -> list:
        url = f"{_APIFY_BASE}/datasets/{dataset_id}/items?token={token}"
        try:
            resp = await self.client.get(url, timeout=30.0)
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            logger.error(f"Apify dataset fetch failed: {exc}")
            return []

    def _parse_apify_item(self, item: dict, since: datetime) -> Optional[ContentItem]:
        try:
            created_at_str = item.get("created_at")
            if not created_at_str:
                return None
            try:
                published_at = datetime.strptime(created_at_str, "%a %b %d %H:%M:%S %z %Y")
            except ValueError:
                published_at = isoparse(created_at_str)
            if published_at.tzinfo is None:
                published_at = published_at.replace(tzinfo=timezone.utc)
            if published_at < since:
                return None

            tweet_id = str(item.get("id_str") or item.get("id") or "")
            if not tweet_id:
                return None
            raw_id = item.get("id") or ""
            numeric_id = str(raw_id).replace("tweet-", "") if str(raw_id).startswith("tweet-") else tweet_id

            user = item.get("user") or {}
            screen_name = (
                user.get("screen_name") or user.get("username") or user.get("handle")
                or item.get("handle") or "unknown"
            )
            author = user.get("name") or screen_name
            text = unescape((item.get("full_text") or item.get("text") or "").strip())
            if not text:
                return None

            url = item.get("url") or f"https://twitter.com/{screen_name}/status/{numeric_id}"
            title_body = text[:50].replace("\n", " ")
            if len(text) > 50:
                title_body += "..."

            return ContentItem(
                id=self._generate_id(SourceType.TWITTER.value, "tweet", numeric_id),
                source_type=SourceType.TWITTER,
                title=f"@{screen_name}: {title_body}",
                url=url,
                content=text,
                author=author,
                published_at=published_at,
                metadata={
                    "tweet_id": numeric_id,
                    "conversation_id": str(item.get("conversation_id") or numeric_id),
                    "favorite_count": item.get("favorite_count", 0),
                    "retweet_count": item.get("retweet_count", 0),
                    "reply_count": item.get("reply_count", 0),
                    "view_count": item.get("view_count"),
                    "is_reply": item.get("is_reply", False),
                },
            )
        except Exception as exc:
            logger.debug(f"Apify item parse failed: {exc}")
            return None

    # ─────────────────────────────────────────────────────────────────────────
    # Reply enrichment (twikit not supported; Apify only)
    # ─────────────────────────────────────────────────────────────────────────

    async def fetch_replies_for_item(self, item: ContentItem) -> List[str]:
        if not self.config.fetch_reply_text:
            return []
        token = os.environ.get(self.config.apify_token_env, "")
        if not token:
            return []
        conversation_id = str(item.metadata.get("conversation_id") or "")
        if not conversation_id:
            return []
        max_replies = max(self.config.max_replies_per_tweet, 0)
        if max_replies == 0:
            return []
        max_items = max(100, max_replies * 5)
        payload = {
            "source_mode": "search",
            "search_query": f"conversation_id:{conversation_id}",
            "search_sort": "Latest",
            "max_items": max_items,
        }
        url = f"{_APIFY_BASE}/acts/{self.config.actor_id}/runs?token={token}"
        try:
            resp = await self.client.post(url, json=payload, timeout=30.0)
            resp.raise_for_status()
            data = resp.json()["data"]
            run_id = data["id"]
            dataset_id = data["defaultDatasetId"]
        except Exception as exc:
            logger.warning(f"Reply run start failed: {exc}")
            return []
        if not await self._apify_wait(token, run_id):
            return []
        rows = await self._apify_fetch_dataset(token, dataset_id)
        return self._extract_reply_lines(item, rows, max_replies)

    def _extract_reply_lines(self, item: ContentItem, rows: list, max_replies: int) -> List[str]:
        min_likes = max(self.config.reply_min_likes, 0)
        tweet_id = str(item.metadata.get("tweet_id") or "")
        own_author = (item.author or "").lstrip("@")
        candidates = []
        for row in rows:
            if not isinstance(row, dict) or row.get("noResults"):
                continue
            row_id = str(row.get("id") or "").replace("tweet-", "")
            if tweet_id and row_id == tweet_id:
                continue
            user = row.get("user") or {}
            handle = user.get("handle") or row.get("handle") or "unknown"
            if handle and own_author and handle.lower() == own_author.lower():
                continue
            text = unescape((row.get("text") or "").strip())
            if not text:
                continue
            likes = int(row.get("favorite_count") or 0)
            if likes < min_likes:
                continue
            replies = int(row.get("reply_count") or 0)
            candidates.append((likes * 2 + replies, f"[@{handle} | ❤️ {likes} | 💬 {replies}] {text[:280]}"))
        candidates.sort(reverse=True)
        return [line for _, line in candidates[:max_replies]]

    @staticmethod
    def append_discussion_content(item: ContentItem, reply_lines: List[str]) -> bool:
        if not reply_lines:
            return False
        existing = item.content or ""
        marker = "--- Top Comments ---"
        block = "\n".join(reply_lines)
        if marker in existing:
            if block in existing:
                return False
            item.content = existing + "\n" + block
            return True
        item.content = existing + (f"\n\n{marker}\n" if existing else f"{marker}\n") + block
        return True
