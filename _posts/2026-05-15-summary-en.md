---
layout: default
title: "Horizon Summary: 2026-05-15 (EN)"
date: 2026-05-15
lang: en
---

> From 18 items, 13 important content pieces were selected

---

1. [First Public macOS Kernel Exploit on Apple M5](#item-1) ⭐️ 9.0/10
2. [Bun Rewritten from Zig to Rust in Major PR](#item-2) ⭐️ 9.0/10
3. [Mullvad VPN Exit IPs Enable User Fingerprinting](#item-3) ⭐️ 8.0/10
4. [Removing Modem and GPS from 2024 RAV4 Hybrid](#item-4) ⭐️ 8.0/10
5. [RTX 5090 eGPU Works with M4 MacBook Air for Gaming and LLMs](#item-5) ⭐️ 8.0/10
6. [Nginx Rift Exploit Enables RCE via Rewrite Directives](#item-6) ⭐️ 8.0/10
7. [arXiv Imposes 1-Year Ban for Hallucinated References](#item-7) ⭐️ 8.0/10
8. [HDD Firmware Hacking Deep Dive](#item-8) ⭐️ 8.0/10
9. [Antirez Releases DS4: Minimal LLM Runtime for DeepSeek V4](#item-9) ⭐️ 7.0/10
10. [Codex Now Available in ChatGPT Mobile App](#item-10) ⭐️ 7.0/10
11. [GGUF Format: Single-File LLM Storage and Missing Features](#item-11) ⭐️ 7.0/10
12. [World Labs' image-blaster turns single images into 3D worlds](#item-12) ⭐️ 7.0/10
13. [Coding Agents Reduce Platform Lock-In Risk](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [First Public macOS Kernel Exploit on Apple M5](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

Calif researchers published the first public kernel memory corruption exploit targeting Apple's M5 chip, bypassing hardware and software protections built over five years. This exploit demonstrates that even Apple's latest M5 hardware with Memory Tagging Extension (MTE) can be compromised, highlighting the ongoing challenge of memory corruption vulnerabilities and potentially driving higher bug bounty payouts. The exploit was developed in one week and is valued between $100,000 and $1.5 million on Apple's bug bounty platform, depending on how it is packaged. The full 55-page technical report is forthcoming.

hackernews · quadrige · May 14, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48139219)

**Background**: Memory corruption is the most common vulnerability class in operating systems. Apple spent five years adding hardware and software mitigations, including MTE, to make such exploits harder. MTE, specified by Arm in 2019, uses tags to detect memory errors at runtime.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://news.ycombinator.com/item?id=48139219">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://www.reddit.com/r/apple/comments/1td7vvc/first_public_macos_kernel_memory_corruption/">First public macOS kernel memory corruption exploit on Apple M5</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise that Apple still does not fully adopt Swift for kernel code, and noted that LLMs may accelerate the discovery of complex vulnerabilities. Some were curious how the bug bypassed MTE, while others debated the exploit's potential bounty value.

**Tags**: `#macOS`, `#kernel exploit`, `#Apple M5`, `#security`, `#vulnerability`

---

<a id="item-2"></a>
## [Bun Rewritten from Zig to Rust in Major PR](https://github.com/oven-sh/bun/pull/30412) ⭐️ 9.0/10

A massive pull request has been merged that rewrites the Bun JavaScript runtime from Zig to Rust, replacing over 1 million lines of code. This rewrite promises improved memory safety and performance, addressing common bugs like use-after-free and double-free, and could set a new standard for JavaScript runtime development. The Rust codebase now contains 1,443 files with 929,213 lines of code, and the PR itself shows +1,009,257 -4,024 changes. The rewrite was prepared with detailed mapping instructions from Zig to Rust idioms.

hackernews · Chaoses · May 14, 08:15 · [Discussion](https://news.ycombinator.com/item?id=48132488)

**Background**: Bun is a fast all-in-one JavaScript runtime, bundler, test runner, and package manager designed as a drop-in replacement for Node.js. It was originally written in Zig, a systems programming language focused on robustness and optimality. Rust is another systems language known for memory safety without garbage collection.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the extensive preparation for the rewrite, with detailed mapping from Zig to Rust idioms. Some note the high number of unsafe blocks in the Rust code (10,428 occurrences), while maintainers acknowledge that Rust won't catch all bugs but will eliminate many common memory errors.

**Tags**: `#Bun`, `#Rust`, `#JavaScript runtime`, `#rewrite`, `#memory safety`

---

<a id="item-3"></a>
## [Mullvad VPN Exit IPs Enable User Fingerprinting](https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/) ⭐️ 8.0/10

A researcher discovered that Mullvad VPN deterministically assigns exit IPs based on a user's WireGuard key, which rotates infrequently (every 1-30 days) or never with third-party clients, creating a fingerprinting vector that links sessions across different servers. This undermines the privacy expectations of VPN users who assume each connection gets a random IP, and it enables website operators to track users across sessions even when they switch servers, similar to a persistent identifier. The exit IP is derived from the WireGuard public key via a hash function, producing a deterministic IP within a /24 subnet; overlapping IP ranges between sessions indicate the same user with >99% confidence.

hackernews · RGBCube · May 15, 02:35 · [Discussion](https://news.ycombinator.com/item?id=48143880)

**Background**: Mullvad is a popular VPN service that uses WireGuard, a modern VPN protocol. WireGuard uses public-key cryptography for authentication, and Mullvad assigns each user a unique WireGuard key. Normally, VPN exit IPs are expected to be random per connection to prevent tracking, but Mullvad's deterministic assignment breaks this assumption.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/docs/features/exit-nodes/mullvad-exit-nodes">Use Mullvad VPN endpoints as exit nodes for your tailnet.</a></li>
<li><a href="https://wiki.archlinux.org/title/WireGuard">WireGuard - ArchWiki</a></li>

</ul>
</details>

**Discussion**: Comments highlight that VPNs are not designed for anonymity like Tor, and that deterministic IP assignment is a known trade-off. Some users note that even Tor can be deanonymized by controlling exit nodes, while others express concern about the fingerprinting risk.

**Tags**: `#privacy`, `#VPN`, `#fingerprinting`, `#security`, `#networking`

---

<a id="item-4"></a>
## [Removing Modem and GPS from 2024 RAV4 Hybrid](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 8.0/10

A detailed guide describes physically removing the Data Communication Module (DCM) and GPS from a 2024 Toyota RAV4 Hybrid to prevent telemetry data collection, noting that Bluetooth connections can still leak data via the phone's internet, while wired USB CarPlay does not. This matters because modern vehicles increasingly collect and share sensitive data with manufacturers and third parties, often without meaningful user consent. The guide empowers owners to take control of their privacy through hardware modification, sparking broader discussion about automotive data rights. The DCM is located behind interior panels and contains an eSIM and GPS receiver; removing it disables telematics but may affect hands-free microphone and front right speaker. The author warns that Bluetooth pairing allows the car to use the phone's internet to send telemetry, whereas wired USB CarPlay does not.

hackernews · arkadiyt · May 14, 17:08 · [Discussion](https://news.ycombinator.com/item?id=48138136)

**Background**: Toyota vehicles from 2022 onward are equipped with a Data Communication Module (DCM) that includes an eSIM and GPS for connected services. This module continuously collects telemetry such as location, speed, and driving behavior, which can be shared with insurers or other third parties. Physical removal is a drastic but effective privacy measure.

<details><summary>References</summary>
<ul>
<li><a href="https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/">Removing the Modem and GPS from my 2024 RAV4 Hybrid</a></li>
<li><a href="https://www.justanswer.com/car/qkdpr-2024-toyota-rav4-hybrid-telematics-control-module-location.html">2024 Toyota RAV4 Hybrid Telematics Module: Location & Guide</a></li>
<li><a href="https://www.rav4world.com/threads/telematics-which-trims-and-how-can-i-opt-out.310379/">Telematics: Which trims and how can I opt out? | Toyota RAV4 Forums</a></li>

</ul>
</details>

**Discussion**: Commenters noted that CarPlay and Android Auto also capture vehicle telemetry, so even with the modem removed, data may still be collected via the phone. Some shared alternative approaches, such as pulling a fuse on the Ford Maverick, and others expressed frustration with Toyota's refusal to fix GPS issues.

**Tags**: `#privacy`, `#automotive`, `#telemetry`, `#hardware hacking`, `#Toyota`

---

<a id="item-5"></a>
## [RTX 5090 eGPU Works with M4 MacBook Air for Gaming and LLMs](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

A developer successfully connected an NVIDIA RTX 5090 eGPU to an M4 MacBook Air via Thunderbolt 5, enabling gaming and LLM inference that are otherwise impossible on Apple Silicon. The setup overcomes Apple's official lack of eGPU support for M-series Macs. This breakthrough demonstrates that eGPUs can work with Apple Silicon, potentially unlocking high-performance gaming and AI workloads on MacBooks. It also highlights the growing demand for local LLM inference, where the RTX 5090's CUDA cores significantly accelerate prompt processing compared to Apple's unified memory. The setup uses a Thunderbolt 5 enclosure (e.g., Gigabyte Aorus RTX 5090 AI Box) and requires custom driver workarounds, as Apple does not officially support eGPUs on M-series Macs. The RTX 5090's 32GB VRAM provides ample memory for large language models, and the eGPU enables playable frame rates in games like Doom that lack modern macOS graphics API support.

hackernews · allenleee · May 14, 15:47 · [Discussion](https://news.ycombinator.com/item?id=48137145)

**Background**: Apple Silicon Macs use a unified memory architecture where the CPU and GPU share memory, which is efficient for many tasks but limits GPU performance for gaming and AI. Apple officially only supports eGPUs on Intel-based Macs and only with AMD GPUs. Thunderbolt 5 offers up to 80 Gbps bandwidth, reducing the bottleneck that previously made eGPUs less effective on Apple Silicon.

<details><summary>References</summary>
<ul>
<li><a href="https://support.apple.com/en-au/102363">Use an external graphics processor with your Mac – Apple Support (AU)</a></li>
<li><a href="https://egpu.io/forums/thunderbolt-enclosures/tb5-thunderbolt-5-enclosure-gigabyte-aorus-rtx-5090-80-ai-box/">TB5/Thunderbolt 5 Enclosure: Gigabyte Aorus RTX 5090/80 AI Box | Thunderbolt & USB4 Enclosures</a></li>
<li><a href="https://www.techradar.com/pro/want-to-run-a-geforce-rtx-5090-on-your-ultra-thin-laptop-this-thunderbolt-5-egpu-enclosure-can-make-it-happen-but-it-wont-be-cheap">This monstrous Gigabyte RTX 5090 AI Box turns slim laptops into desktop-class gaming and AI beasts | TechRadar</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise that eGPUs work on Apple Silicon at all, with many noting Apple's official stance that they don't. Some highlighted the LLM performance improvements as the most practical benefit, while others discussed the technical challenges of VM GPU passthrough and OpenGL/Vulkan workarounds. Overall sentiment was positive and impressed by the achievement.

**Tags**: `#eGPU`, `#Apple Silicon`, `#gaming`, `#LLM`, `#hardware`

---

<a id="item-6"></a>
## [Nginx Rift Exploit Enables RCE via Rewrite Directives](https://github.com/DepthFirstDisclosures/Nginx-Rift) ⭐️ 8.0/10

A new exploit called Nginx Rift (CVE-2026-42945) has been disclosed that allows unauthenticated remote code execution via specially crafted rewrite and set directives in Nginx configuration. The vulnerability has been present for 18 years and affects Nginx Open Source and Nginx Plus. This vulnerability is critical because Nginx powers over 30% of all web servers, and the exploit requires only specific rewrite and set directives to be present, which are common in many configurations. Successful exploitation could lead to full server compromise, and the community discussion highlights potential ASLR bypass techniques, increasing the severity. The exploit requires a rewrite directive with a question mark in the replacement string followed by a set directive referencing an unnamed regex capture group (e.g., $1). The published proof-of-concept assumes ASLR is disabled, but the researchers claim a reliable ASLR bypass exists.

hackernews · hetsaraiya · May 14, 17:17 · [Discussion](https://news.ycombinator.com/item?id=48138268)

**Background**: Nginx's rewrite module compiles rewrite, set, if, and return directives into bytecode that runs per request. The vulnerability stems from a bug in the bytecode compiler that can cause memory corruption when processing certain patterns. ASLR (Address Space Layout Randomization) is a defense technique that randomizes memory addresses to make exploitation harder, but it can be bypassed using techniques like ROP (Return-Oriented Programming).

<details><summary>References</summary>
<ul>
<li><a href="https://devops-daily.com/posts/nginx-rift-cve-2026-42945-rewrite-rce">NGINX Rift (CVE-2026-42945): The 18-Year-Old Rewrite Bug That...</a></li>
<li><a href="https://thehackernews.com/2026/05/18-year-old-nginx-rewrite-module-flaw.html">18-Year-Old NGINX Rewrite Module Flaw Enables Unauthenticated...</a></li>
<li><a href="https://depthfirst.com/research/nginx-rift-achieving-nginx-rce-via-an-18-year-old-vulnerability">NGINX Rift: Achieving NGINX Remote Code Execution via... | depthfirst</a></li>

</ul>
</details>

**Discussion**: The community discussion is active, with users debating the severity and mitigations. Some argue that ASLR bypass is likely and should be assumed, while others note that the published PoC disables ASLR. Mitigations include using named captures instead of unnamed ones, and F5 has released patches for versions 1.31.0 and 1.30.1.

**Tags**: `#nginx`, `#security`, `#exploit`, `#vulnerability`, `#ASLR`

---

<a id="item-7"></a>
## [arXiv Imposes 1-Year Ban for Hallucinated References](https://twitter.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv has introduced a new policy that imposes a 1-year ban on authors who submit papers containing hallucinated references, followed by a requirement that future submissions must first be accepted at a reputable peer-reviewed venue. This policy directly addresses the growing problem of AI-generated hallucinated citations in academic papers, helping to preserve research integrity and trust in preprint repositories. The ban applies to authors found to have submitted papers with fabricated references, and after the ban, authors must have their work accepted at a reputable venue before resubmitting to arXiv.

hackernews · gjuggler · May 14, 20:39 · [Discussion](https://news.ycombinator.com/item?id=48140922)

**Background**: Hallucinated references are non-existent citations fabricated by AI language models, which have become a significant issue in academic publishing. arXiv is a widely used preprint repository that relies on voluntary moderation to maintain quality standards.

<details><summary>References</summary>
<ul>
<li><a href="https://info.arxiv.org/help/moderation/index.html">Content Moderation - arXiv info</a></li>
<li><a href="https://ref-check.org/">ref-check.org — Academic Reference Verification Tool</a></li>
<li><a href="https://arxiv.org/pdf/2604.16407">26-19 How unique are hallucinated citations 2026-03-31</a></li>

</ul>
</details>

**Discussion**: The community largely supports the policy, with some praising it as a necessary step for science. Others discuss alternatives to arXiv and emphasize the need to address the root cause, such as improving tools for correct citation creation.

**Tags**: `#arXiv`, `#research integrity`, `#academic publishing`, `#AI ethics`, `#policy`

---

<a id="item-8"></a>
## [HDD Firmware Hacking Deep Dive](https://icode4.coffee/?p=1465) ⭐️ 8.0/10

A technical article details methods for reverse engineering HDD firmware, including dumping, analyzing, and modifying firmware, as well as bypassing obfuscation and extracting decrypted firmware. This work exposes security weaknesses in HDD firmware, enabling researchers to find vulnerabilities and potentially improve device security. It also empowers users to understand and control their hardware. The article covers techniques such as using seccomp to intercept syscalls during firmware updates to capture decrypted firmware, and reverse engineering obfuscation algorithms. It also references a related decompilation of Samsung 840 EVO SSD firmware.

hackernews · jsploit · May 14, 16:19 · [Discussion](https://news.ycombinator.com/item?id=48137553)

**Background**: Hard disk drives (HDDs) and solid-state drives (SSDs) run firmware that controls their operation. Manufacturers often obfuscate or encrypt this firmware to prevent reverse engineering. Tools like hdd_firmware_tools on GitHub can extract firmware from Seagate drives, but many vendors keep firmware proprietary.

<details><summary>References</summary>
<ul>
<li><a href="https://icode4.coffee/?p=1465">HDD Firmware Hacking Part 1 – I Code 4 Coffee</a></li>
<li><a href="https://github.com/eurecom-s3/hdd_firmware_tools">GitHub - eurecom-s3/hdd_firmware_tools: Tools for viewing and extracting HDD firmware files · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters shared practical tips, such as using seccomp to capture decrypted firmware during updates, and referenced a decompiled Samsung SSD firmware manual. Some expressed frustration with vendor obfuscation practices and the lack of support for LVFS/fwupd.

**Tags**: `#firmware`, `#reverse engineering`, `#hardware hacking`, `#security`, `#storage`

---

<a id="item-9"></a>
## [Antirez Releases DS4: Minimal LLM Runtime for DeepSeek V4](https://antirez.com/news/165) ⭐️ 7.0/10

Antirez has released DS4 (DwarfStar4), a minimal and self-contained LLM inference runtime specifically designed for DeepSeek V4 Flash, optimized for MacBooks with 96GB RAM and supporting Metal, CUDA, and ROCm backends. DS4 demonstrates that a single developer can build a highly optimized inference engine for a specific model, outperforming general-purpose runtimes on desktop hardware, which could accelerate the trend toward local, private AI inference. DS4 is not a generic GGUF runner but a purpose-built engine with custom loading, prompt rendering, tool calling, and KV state handling, and it currently requires 96GB of VRAM to run DeepSeek V4 Flash.

hackernews · caust1c · May 14, 22:29 · [Discussion](https://news.ycombinator.com/item?id=48142108)

**Background**: DeepSeek V4 is a 1-trillion-parameter multimodal model with an Engram memory architecture, and running such large models locally typically requires significant hardware resources. DS4 builds on llama.cpp and GGML but is self-contained, targeting high-end Apple Silicon Macs and NVIDIA DGX Spark systems.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/antirez/ds4">GitHub - antirez/ds4: DeepSeek 4 Flash local inference engine for Metal and CUDA · GitHub</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/2253/ds4-antirez-deepseek-v4-flash-inference-engine">DwarfStar4 (DS4) Roadmap by antirez: DeepSeek V4 Flash on Apple Silicon and CUDA</a></li>
<li><a href="https://www.knightli.com/en/2026/05/11/deepseek-v4-flash-ds4-metal/">Running DeepSeek 4 Locally: Antirez's ds4 Experiment on Apple Silicon Mac</a></li>

</ul>
</details>

**Discussion**: Community comments highlight DS4's narrow focus and performance, with one user noting it feels close to Claude in quality despite being slower, and another discussing the potential saturation of model intelligence for coding tasks.

**Tags**: `#LLM`, `#inference`, `#DeepSeek`, `#open source`, `#AI`

---

<a id="item-10"></a>
## [Codex Now Available in ChatGPT Mobile App](https://openai.com/index/work-with-codex-from-anywhere/) ⭐️ 7.0/10

OpenAI has integrated its Codex coding agent into the ChatGPT mobile app, allowing developers to interact with coding agents remotely for free. This integration significantly improves developer workflow by enabling 'vibe coding' on the go, reducing the need to be tethered to a desktop. It also lowers the barrier to entry for AI-assisted coding, as Codex is free on the mobile app. Codex is available on the free tier of ChatGPT, though interactions may be used for training. The mobile app provides a remote interface to the same Codex agent that runs locally or via CLI.

hackernews · OpenAI Blog · May 14, 20:06 · [Discussion](https://news.ycombinator.com/item?id=48140529)

**Background**: Codex is a suite of AI-driven coding agents from OpenAI that automate software engineering tasks. It can be run locally via CLI or desktop app, and now via the ChatGPT mobile app, enabling remote access to coding assistance.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai / codex : Lightweight coding agent that runs in your...</a></li>
<li><a href="https://github.com/openai/codex/releases">Releases · openai / codex</a></li>

</ul>
</details>

**Discussion**: Community members are excited about the free access and remote capabilities, with some sharing workflows for using Codex from anywhere. However, some users note that results can be less effective on a small screen without a keyboard, and caution that easy remote access may make it harder to disconnect from work.

**Tags**: `#AI coding assistant`, `#ChatGPT`, `#mobile development`, `#developer tools`, `#OpenAI`

---

<a id="item-11"></a>
## [GGUF Format: Single-File LLM Storage and Missing Features](https://nobodywho.ooo/posts/whats-in-a-gguf/) ⭐️ 7.0/10

A technical deep-dive explores the GGUF file format for LLMs, highlighting its single-file advantage over formats like safetensors, and identifies missing features such as tool-calling support. GGUF is widely used in projects like llama.cpp for efficient LLM deployment, and addressing its limitations could streamline model distribution and enable agentic workflows. The article notes that GGUF's single-file design contrasts with safetensors repos that require multiple JSON files, but current GGUF lacks standardized tool-calling metadata, which is crucial for LLM agents.

hackernews · bashbjorn · May 14, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48138332)

**Background**: GGUF (GPT-Generated Unified Format) is a binary format optimized for quick loading and saving of LLMs, developed as an evolution of GGML. It is primarily used by llama.cpp and supported on Hugging Face Hub. Tool calling allows LLMs to invoke external functions with structured JSON arguments, enabling agentic behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">llama.cpp - Wikipedia</a></li>
<li><a href="https://huggingface.co/docs/hub/gguf">GGUF · Hugging Face</a></li>
<li><a href="https://blog.promptlayer.com/tool-calling-with-llms-how-and-when-to-use-it/">Tool Calling with LLMs: How and when to use it?</a></li>

</ul>
</details>

**Discussion**: Philpax, a GGUF designer, regrets that projection models ended up separate from the main file, contradicting the single-file ethos. Commenters appreciate the analysis and emphasize GGUF's importance for open-source ML, with sbinnee noting that tool-calling support would be a milestone for transitioning from LLMs to agents.

**Tags**: `#GGUF`, `#LLM`, `#machine learning`, `#file format`, `#open source`

---

<a id="item-12"></a>
## [World Labs' image-blaster turns single images into 3D worlds](https://twitter.com/drfeifei/status/tweet-2055022392569905411) ⭐️ 7.0/10

World Labs, co-founded by Fei-Fei Li, released image-blaster, a tool that converts a single image into a fully meshed 3D world in minutes. This tool significantly lowers the barrier for 3D content creation, enabling rapid prototyping and immersive experiences from everyday photos, which could impact gaming, VR, and digital twin industries. Image-blaster uses World Labs' Marble model (marble-1.1) to generate explorable environments, along with nano-banana for image cleanup and reference handling.

twitter · Fei-Fei Li · May 14, 20:28

**Background**: Single-image 3D reconstruction is a challenging computer vision task that traditionally requires multiple views or depth sensors. Recent AI models like One-2-3-45 and Hunyuan 3D have made progress, but World Labs' approach focuses on generating fully meshed worlds rather than just objects.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/neilsonnn/image-blaster">GitHub - neilsonnn/ image - blaster : An image-to- world skillset for...</a></li>
<li><a href="https://www.worldlabs.ai/">World Labs</a></li>

</ul>
</details>

**Tags**: `#3D reconstruction`, `#computer vision`, `#AI`, `#image processing`

---

<a id="item-13"></a>
## [Coding Agents Reduce Platform Lock-In Risk](https://simonwillison.net/2026/May/14/not-so-locked-in/#atom-everything) ⭐️ 6.0/10

A tech leader shared an anecdote about a company using coding agents to rewrite both iPhone and Android apps into React Native, arguing that the cost of switching back to native is now low enough to make platform lock-in less of a concern. This suggests that AI-assisted coding agents are fundamentally changing technology decisions by reducing the risk of long-term commitment to a specific framework or language, potentially accelerating adoption of cross-platform solutions. The company had legacy iPhone and Android apps that were rewritten using coding agents to React Native, which the team found covered all their needs. They believe that if the decision proves wrong, they can simply port back to native with the help of coding agents.

rss · Simon Willison · May 14, 22:53

**Background**: Platform lock-in occurs when a company becomes dependent on a specific technology, making it costly to switch. Coding agents are AI tools that can automatically generate or modify code, reducing the human effort required for large-scale rewrites. React Native is a framework that allows building mobile apps using JavaScript and React, sharing code across iOS and Android.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/senaiverse/claude-code-reactnative-expo-agent-system">GitHub - senaiverse/claude- code - reactnative -expo- agent -system...</a></li>
<li><a href="https://reactnative.dev/">React Native · Learn once, write anywhere</a></li>
<li><a href="https://thecodersblog.com/bun-runtime-migration-from-zig-to-rust-2026/">Bun 's Rust Pivot: What the Zig - to - Rust Migration Means for...</a></li>

</ul>
</details>

**Tags**: `#React Native`, `#coding agents`, `#technology decisions`, `#lock-in`

---