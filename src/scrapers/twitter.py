"""Twitter scraper: direct X GraphQL API via httpx (no extra libraries needed).

Auth: TWITTER_AUTH_TOKEN + TWITTER_CT0 cookies (set once in GitHub Secrets).
Falls back to Apify (batched) when those env vars are absent.
"""

import asyncio
import json
import logging
import os
from datetime import datetime, timezone
from html import unescape
from typing import List, Optional

from dateutil.parser import isoparse
import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, TwitterConfig

logger = logging.getLogger(__name__)

# ── Twitter GraphQL constants (stable; sourced from Scweet's manifest) ───────
_BEARER = (
    "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs"
    "%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
)
_USER_LOOKUP_URL = (
    "https://x.com/i/api/graphql/IGgvgiOx4QZndDHuD3x9TQ/UserByScreenName"
)
_TIMELINE_URL = (
    "https://x.com/i/api/graphql/O0epvwaQPUx-bT9YlqlL6w/UserTweets"
)
_LOOKUP_FEATURES = '{"rweb_video_screen_enabled":false,"profile_label_improvements_pcf_label_in_post_enabled":true,"responsive_web_profile_redirect_enabled":false,"rweb_tipjar_consumption_enabled":false,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":false,"responsive_web_grok_analyze_post_followups_enabled":true,"responsive_web_jetfuel_frame":true,"responsive_web_grok_share_attachment_enabled":true,"responsive_web_grok_annotations_enabled":false,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"responsive_web_grok_show_grok_translated_post":false,"responsive_web_grok_analysis_button_from_backend":true,"post_ctas_fetch_enabled":true,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_grok_image_annotation_enabled":true,"responsive_web_grok_imagine_annotation_enabled":true,"responsive_web_grok_community_note_auto_translation_is_enabled":false,"responsive_web_enhance_cards_enabled":false,"hidden_profile_subscriptions_enabled":true,"subscriptions_verification_info_is_identity_verified_enabled":true,"subscriptions_verification_info_verified_since_enabled":true,"highlights_tweets_tab_ui_enabled":true,"responsive_web_twitter_article_notes_tab_enabled":true,"subscriptions_feature_can_gift_premium":true}'
_TIMELINE_FEATURES = '{"rweb_video_screen_enabled":false,"profile_label_improvements_pcf_label_in_post_enabled":true,"responsive_web_profile_redirect_enabled":false,"rweb_tipjar_consumption_enabled":false,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":false,"responsive_web_grok_analyze_post_followups_enabled":true,"responsive_web_jetfuel_frame":true,"responsive_web_grok_share_attachment_enabled":true,"responsive_web_grok_annotations_enabled":false,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"responsive_web_grok_show_grok_translated_post":false,"responsive_web_grok_analysis_button_from_backend":true,"post_ctas_fetch_enabled":true,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_grok_image_annotation_enabled":true,"responsive_web_grok_imagine_annotation_enabled":true,"responsive_web_grok_community_note_auto_translation_is_enabled":false,"responsive_web_enhance_cards_enabled":false}'

# ── Apify constants (fallback) ────────────────────────────────────────────────
_APIFY_BASE = "https://api.apify.com/v2"
_POLL_INTERVAL = 3.0
_MAX_WAIT = 180


def _extract_handle(user_entry: str) -> str:
    s = user_entry.strip()
    if s.startswith("http"):
        s = s.rstrip("/").split("/")[-1]
    return s.lstrip("@")


def _build_headers(ct0: str) -> dict:
    return {
        "Authorization": f"Bearer {_BEARER}",
        "X-Csrf-Token": ct0,
        "X-Twitter-Active-User": "yes",
        "X-Twitter-Auth-Type": "OAuth2Session",
        "X-Twitter-Client-Language": "en",
        "Content-Type": "application/json",
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
    }


class TwitterScraper(BaseScraper):
    """Fetch tweets via X GraphQL API (httpx + cookies). Falls back to Apify."""

    def __init__(self, config: TwitterConfig, http_client: httpx.AsyncClient):
        super().__init__(config, http_client)
        self.config = config

    # ── public entry point ────────────────────────────────────────────────────

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.config.enabled:
            return []

        handles = [_extract_handle(u) for u in self.config.users if u.strip()]
        if not handles:
            return []

        auth_token = os.environ.get("TWITTER_AUTH_TOKEN", "").strip()
        ct0 = os.environ.get("TWITTER_CT0", "").strip()
        apify_token = os.environ.get(self.config.apify_token_env, "").strip()

        if auth_token and ct0:
            logger.info("Twitter: direct GraphQL path (%d accounts)", len(handles))
            return await self._fetch_graphql(handles, since, auth_token, ct0)
        elif apify_token:
            logger.info("Twitter: TWITTER_AUTH_TOKEN absent – Apify batched fallback")
            return await self._fetch_apify(handles, since, apify_token)
        else:
            logger.warning(
                "Twitter: no credentials found (set TWITTER_AUTH_TOKEN+TWITTER_CT0). Skipping."
            )
            return []

    # ── direct GraphQL path ───────────────────────────────────────────────────

    async def _fetch_graphql(
        self, handles: List[str], since: datetime, auth_token: str, ct0: str
    ) -> List[ContentItem]:
        headers = _build_headers(ct0)
        cookies = {"auth_token": auth_token, "ct0": ct0}
        per_user = max(20, self.config.fetch_limit)
        items: List[ContentItem] = []

        for handle in handles:
            try:
                user_id = await self._gql_get_user_id(handle, headers, cookies)
                if not user_id:
                    logger.warning("Twitter: could not resolve user_id for @%s", handle)
                    continue
                tweets = await self._gql_get_tweets(user_id, per_user, headers, cookies)
                count = 0
                for t in tweets:
                    parsed = self._parse_gql_tweet(t, since)
                    if parsed:
                        items.append(parsed)
                        count += 1
                logger.debug("@%s: %d recent tweets (of %d fetched)", handle, count, len(tweets))
                await asyncio.sleep(1.0)
            except Exception as exc:
                logger.warning("Twitter GraphQL: failed @%s – %s", handle, exc)

        logger.info(
            "Twitter GraphQL: %d items within 48h across %d accounts", len(items), len(handles)
        )
        return items

    async def _gql_get_user_id(
        self, handle: str, headers: dict, cookies: dict
    ) -> Optional[str]:
        variables = json.dumps(
            {"screen_name": handle, "withGrokTranslatedBio": False},
            separators=(",", ":"),
        )
        params = {"variables": variables, "features": _LOOKUP_FEATURES}
        resp = await self.client.get(
            _USER_LOOKUP_URL, params=params, headers=headers, cookies=cookies, timeout=15.0
        )
        if resp.status_code != 200:
            logger.warning("UserByScreenName @%s → HTTP %d", handle, resp.status_code)
            return None
        data = resp.json()
        try:
            return data["data"]["user"]["result"]["rest_id"]
        except (KeyError, TypeError):
            logger.warning("UserByScreenName @%s: unexpected shape: %s", handle, str(data)[:200])
            return None

    async def _gql_get_tweets(
        self, user_id: str, count: int, headers: dict, cookies: dict
    ) -> list:
        variables = json.dumps(
            {
                "userId": user_id,
                "count": count,
                "includePromotedContent": True,
                "withQuickPromoteEligibilityTweetFields": True,
                "withVoice": True,
            },
            separators=(",", ":"),
        )
        params = {"variables": variables, "features": _TIMELINE_FEATURES}
        resp = await self.client.get(
            _TIMELINE_URL, params=params, headers=headers, cookies=cookies, timeout=20.0
        )
        if resp.status_code != 200:
            logger.warning("UserTweets %s → HTTP %d: %s", user_id, resp.status_code, resp.text[:200])
            return []
        data = resp.json()
        return self._extract_tweet_entries(data)

    @staticmethod
    def _extract_tweet_entries(data: dict) -> list:
        """Walk the GraphQL timeline and collect raw tweet legacy dicts."""
        entries = []
        try:
            timeline = (
                data["data"]["user"]["result"]["timeline_v2"]["timeline"]["instructions"]
            )
        except (KeyError, TypeError):
            return entries
        for instruction in timeline:
            if instruction.get("type") != "TimelineAddEntries":
                continue
            for entry in instruction.get("entries", []):
                content = entry.get("content", {})
                item_content = content.get("itemContent", {})
                tweet_result = item_content.get("tweet_results", {}).get("result", {})
                # Unwrap retweets
                if tweet_result.get("__typename") == "TweetWithVisibilityResults":
                    tweet_result = tweet_result.get("tweet", tweet_result)
                legacy = tweet_result.get("legacy")
                if not legacy:
                    continue
                core = tweet_result.get("core", {})
                user_result = (
                    core.get("user_results", {}).get("result", {})
                )
                user_legacy = user_result.get("legacy", {})
                entries.append({"legacy": legacy, "user_legacy": user_legacy})
        return entries

    def _parse_gql_tweet(self, entry: dict, since: datetime) -> Optional[ContentItem]:
        try:
            legacy = entry.get("legacy", {})
            user_legacy = entry.get("user_legacy", {})

            created_at_str = legacy.get("created_at", "")
            if not created_at_str:
                return None
            try:
                published_at = datetime.strptime(
                    created_at_str, "%a %b %d %H:%M:%S %z %Y"
                )
            except ValueError:
                published_at = isoparse(created_at_str)
            if published_at.tzinfo is None:
                published_at = published_at.replace(tzinfo=timezone.utc)
            if published_at < since:
                return None

            tweet_id = str(legacy.get("id_str") or legacy.get("id") or "")
            if not tweet_id:
                return None

            screen_name = user_legacy.get("screen_name") or "unknown"
            author = user_legacy.get("name") or screen_name
            text = unescape(
                (legacy.get("full_text") or legacy.get("text") or "").strip()
            )
            if not text:
                return None

            title_body = text[:50].replace("\n", " ")
            if len(text) > 50:
                title_body += "..."

            return ContentItem(
                id=self._generate_id(SourceType.TWITTER.value, "tweet", tweet_id),
                source_type=SourceType.TWITTER,
                title=f"@{screen_name}: {title_body}",
                url=f"https://twitter.com/{screen_name}/status/{tweet_id}",
                content=text,
                author=author,
                published_at=published_at,
                metadata={
                    "tweet_id": tweet_id,
                    "conversation_id": str(legacy.get("conversation_id_str") or tweet_id),
                    "favorite_count": int(legacy.get("favorite_count") or 0),
                    "retweet_count": int(legacy.get("retweet_count") or 0),
                    "reply_count": int(legacy.get("reply_count") or 0),
                    "view_count": None,
                    "is_reply": bool(legacy.get("in_reply_to_status_id_str")),
                },
            )
        except Exception as exc:
            logger.debug("GQL tweet parse error: %s", exc)
            return None

    # ── Apify fallback (batched) ──────────────────────────────────────────────

    async def _fetch_apify(
        self, handles: List[str], since: datetime, token: str
    ) -> List[ContentItem]:
        users = [f"https://x.com/{h}" for h in handles]
        BATCH_SIZE = 5
        batches = [users[i : i + BATCH_SIZE] for i in range(0, len(users), BATCH_SIZE)]
        logger.info("Apify: %d accounts, %d batches", len(users), len(batches))

        all_items: List[ContentItem] = []
        seen: set = set()
        for idx, batch in enumerate(batches):
            logger.info(
                "  Batch %d/%d: %s", idx + 1, len(batches),
                [u.split("/")[-1] for u in batch]
            )
            run_id, ds_id = await self._apify_start_run(token, batch)
            if not run_id:
                continue
            if not await self._apify_wait(token, run_id):
                continue
            for raw in await self._apify_fetch_ds(token, ds_id):
                if isinstance(raw, dict) and raw.get("noResults"):
                    continue
                parsed = self._parse_apify_item(raw, since)
                if parsed and parsed.id not in seen:
                    seen.add(parsed.id)
                    all_items.append(parsed)
        logger.info("Apify: %d items after 48h filter", len(all_items))
        return all_items

    async def _apify_start_run(self, token: str, profile_urls: List[str]):
        payload = {
            "source_mode": "profiles",
            "profile_urls": profile_urls,
            "search_sort": "Latest",
            "max_items": max(100, self.config.fetch_limit) * len(profile_urls),
        }
        try:
            r = await self.client.post(
                f"{_APIFY_BASE}/acts/{self.config.actor_id}/runs?token={token}",
                json=payload, timeout=30.0,
            )
            r.raise_for_status()
            d = r.json()["data"]
            return d["id"], d["defaultDatasetId"]
        except Exception as exc:
            logger.error("Apify start_run: %s", exc)
            return None, None

    async def _apify_wait(self, token: str, run_id: str) -> bool:
        elapsed = 0.0
        while elapsed < _MAX_WAIT:
            try:
                r = await self.client.get(
                    f"{_APIFY_BASE}/actor-runs/{run_id}?token={token}", timeout=10.0
                )
                status = r.json()["data"]["status"]
                if status == "SUCCEEDED":
                    return True
                if status in ("FAILED", "ABORTED", "TIMED-OUT"):
                    logger.error("Apify run %s: %s", run_id, status)
                    return False
            except Exception as exc:
                logger.warning("Apify poll: %s", exc)
            await asyncio.sleep(_POLL_INTERVAL)
            elapsed += _POLL_INTERVAL
        logger.warning("Apify run %s timed out", run_id)
        return False

    async def _apify_fetch_ds(self, token: str, ds_id: str) -> list:
        try:
            r = await self.client.get(
                f"{_APIFY_BASE}/datasets/{ds_id}/items?token={token}", timeout=30.0
            )
            r.raise_for_status()
            return r.json()
        except Exception as exc:
            logger.error("Apify fetch_ds: %s", exc)
            return []

    def _parse_apify_item(self, item: dict, since: datetime) -> Optional[ContentItem]:
        try:
            s = item.get("created_at", "")
            if not s:
                return None
            try:
                pub = datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")
            except ValueError:
                pub = isoparse(s)
            if pub.tzinfo is None:
                pub = pub.replace(tzinfo=timezone.utc)
            if pub < since:
                return None
            tid = str(item.get("id_str") or item.get("id") or "")
            if not tid:
                return None
            nid = str(tid).replace("tweet-", "") if str(tid).startswith("tweet-") else tid
            user = item.get("user") or {}
            sn = user.get("screen_name") or user.get("handle") or item.get("handle") or "unknown"
            author = user.get("name") or sn
            text = unescape((item.get("full_text") or item.get("text") or "").strip())
            if not text:
                return None
            url = item.get("url") or f"https://twitter.com/{sn}/status/{nid}"
            tb = text[:50].replace("\n", " ") + ("..." if len(text) > 50 else "")
            return ContentItem(
                id=self._generate_id(SourceType.TWITTER.value, "tweet", nid),
                source_type=SourceType.TWITTER,
                title=f"@{sn}: {tb}",
                url=url,
                content=text,
                author=author,
                published_at=pub,
                metadata={
                    "tweet_id": nid,
                    "conversation_id": str(item.get("conversation_id") or nid),
                    "favorite_count": item.get("favorite_count", 0),
                    "retweet_count": item.get("retweet_count", 0),
                    "reply_count": item.get("reply_count", 0),
                    "view_count": item.get("view_count"),
                    "is_reply": item.get("is_reply", False),
                },
            )
        except Exception as exc:
            logger.debug("Apify item parse: %s", exc)
            return None

    # ── reply enrichment (Apify only) ────────────────────────────────────────

    async def fetch_replies_for_item(self, item: ContentItem) -> List[str]:
        if not self.config.fetch_reply_text:
            return []
        token = os.environ.get(self.config.apify_token_env, "")
        if not token:
            return []
        cid = str(item.metadata.get("conversation_id") or "")
        max_r = max(self.config.max_replies_per_tweet, 0)
        if not cid or not max_r:
            return []
        payload = {
            "source_mode": "search",
            "search_query": f"conversation_id:{cid}",
            "search_sort": "Latest",
            "max_items": max(100, max_r * 5),
        }
        try:
            r = await self.client.post(
                f"{_APIFY_BASE}/acts/{self.config.actor_id}/runs?token={token}",
                json=payload, timeout=30.0,
            )
            r.raise_for_status()
            d = r.json()["data"]
            run_id, ds_id = d["id"], d["defaultDatasetId"]
        except Exception as exc:
            logger.warning("Reply run: %s", exc)
            return []
        if not await self._apify_wait(token, run_id):
            return []
        return self._extract_reply_lines(item, await self._apify_fetch_ds(token, ds_id), max_r)

    def _extract_reply_lines(self, item: ContentItem, rows: list, max_r: int) -> List[str]:
        min_likes = max(self.config.reply_min_likes, 0)
        tid = str(item.metadata.get("tweet_id") or "")
        own = (item.author or "").lstrip("@").lower()
        cands = []
        for row in rows:
            if not isinstance(row, dict) or row.get("noResults"):
                continue
            if str(row.get("id") or "").replace("tweet-", "") == tid:
                continue
            u = row.get("user") or {}
            handle = u.get("handle") or row.get("handle") or "unknown"
            if handle.lower() == own:
                continue
            text = unescape((row.get("text") or "").strip())
            if not text:
                continue
            likes = int(row.get("favorite_count") or 0)
            if likes < min_likes:
                continue
            reps = int(row.get("reply_count") or 0)
            cands.append((likes * 2 + reps, f"[@{handle} | ❤️ {likes} | 💬 {reps}] {text[:280]}"))
        cands.sort(reverse=True)
        return [l for _, l in cands[:max_r]]

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
