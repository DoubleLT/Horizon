---
layout: default
title: "Horizon Summary: 2026-05-15 (EN)"
date: 2026-05-15
lang: en
---

> From 16 items, 12 important content pieces were selected

---

1. [First Public macOS Kernel Exploit on Apple M5](#item-1) ⭐️ 9.0/10
2. [Bun Rewritten from Zig to Rust, Merged into Main](#item-2) ⭐️ 9.0/10
3. [Removing Modem and GPS from 2024 RAV4 Hybrid](#item-3) ⭐️ 8.0/10
4. [Antirez Launches DS4: Specialized LLM Runtime for DeepSeek V4](#item-4) ⭐️ 8.0/10
5. [Frontier AI access may be limited by economics and security](#item-5) ⭐️ 8.0/10
6. [UK ditches Palantir for in-house refugee system](#item-6) ⭐️ 8.0/10
7. [RTX 5090 eGPU on M4 MacBook Air: Gaming & LLM Breakthrough](#item-7) ⭐️ 8.0/10
8. [Mullvad VPN Exit IPs Enable User Fingerprinting](#item-8) ⭐️ 8.0/10
9. [Critical Nginx RCE Exploit Published with ASLR Bypass Claim](#item-9) ⭐️ 8.0/10
10. [World Labs' image-blaster turns single image into 3D world](#item-10) ⭐️ 8.0/10
11. [Codex Now Available in ChatGPT Mobile App](#item-11) ⭐️ 7.0/10
12. [Coding Agents Reduce Technology Lock-In](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [First Public macOS Kernel Exploit on Apple M5](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

Security researchers at Calif have demonstrated the first public macOS kernel memory corruption exploit on Apple's M5 chip, surviving MIE (Memory Integrity Engine). This marks a significant security milestone as it is the first public kernel exploit for Apple's latest M5 silicon, potentially leading to high bug bounty payouts and highlighting the growing role of LLMs in vulnerability research. The exploit was developed in just five days with the help of Anthropic's Mythos Preview model, and the team shared a 20-second video of the exploit in action. The vulnerability report was presented to Apple at a meeting at Apple Park.

hackernews · quadrige · May 14, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48139219)

**Background**: The Apple M5 is Apple's latest ARM-based system-on-a-chip, built on third-generation 3nm technology, featuring a next-generation GPU with Neural Accelerators. Kernel memory corruption exploits are critical vulnerabilities that allow attackers to gain unauthorized access to protected parts of the operating system. MIE (Memory Integrity Engine) is a hardware security feature designed to prevent such memory corruption attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://9to5mac.com/2026/05/14/calif-team-details-how-anthropic-mythos-helped-build-a-working-macos-exploit-in-five-days/">Anthropic Mythos helped Calif build a macOS exploit in five days - 9to5Mac</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about the exploit and its implications, with some noting the potential for high bug bounty payouts (up to $1.5 million). There was also discussion about the role of LLMs like Anthropic's Mythos in accelerating vulnerability discovery, with one commenter noting that LLMs will produce 'amazing Rube Goldberg style vulnerabilities' in the future.

**Tags**: `#security`, `#macOS`, `#kernel exploit`, `#Apple M5`, `#bug bounty`

---

<a id="item-2"></a>
## [Bun Rewritten from Zig to Rust, Merged into Main](https://github.com/oven-sh/bun/pull/30412) ⭐️ 9.0/10

Bun's core has been rewritten from Zig to Rust and merged into the main branch, marking a major architectural shift for the JavaScript runtime. This rewrite promises to eliminate entire classes of memory bugs like use-after-free and double-free, improving safety and reliability for Bun users. It also positions Bun to leverage Rust's ecosystem and tooling, potentially accelerating development. The migration added over 1 million lines of Rust code, with the codebase now containing 1,443 Rust files and 1,298 Zig files. The Bun team had already prepared the codebase with internal smart pointer types that map 1-to-1 to Rust equivalents, facilitating the rewrite.

hackernews · Chaoses · May 14, 08:15 · [Discussion](https://news.ycombinator.com/item?id=48132488)

**Background**: Bun is a fast all-in-one JavaScript runtime, bundler, and package manager designed as a drop-in replacement for Node.js. It was originally written in Zig, a low-level language focused on simplicity and performance. Rust is a systems programming language known for its memory safety guarantees through ownership and borrowing, which can prevent common bugs at compile time.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**Discussion**: The community is highly engaged, with comments noting the extensive preparation (e.g., detailed Zig-to-Rust mapping instructions) and the scale of the rewrite (over 1M lines of Rust). Some users express concerns about software complexity, while others appreciate the safety improvements, though Bun's creator notes that Rust won't catch all bugs, especially those crossing the JS boundary.

**Tags**: `#Bun`, `#Rust`, `#Zig`, `#JavaScript Runtime`, `#Memory Safety`

---

<a id="item-3"></a>
## [Removing Modem and GPS from 2024 RAV4 Hybrid](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 8.0/10

A detailed guide was published on physically removing the modem (DCM) and GPS from a 2024 RAV4 Hybrid to prevent telemetry data collection by Toyota. This highlights growing privacy concerns in modern vehicles and provides a practical, if extreme, method for users to regain control over their data, potentially influencing automotive privacy discussions. Even after modem removal, connecting a phone via Bluetooth allows the car to use the phone's internet to send telemetry, but wired USB CarPlay does not. The author notes that CarPlay and Android Auto also capture their own telemetry.

hackernews · arkadiyt · May 14, 17:08 · [Discussion](https://news.ycombinator.com/item?id=48138136)

**Background**: Modern vehicles are equipped with telematics systems that collect and transmit data about driving behavior, location, and vehicle status to manufacturers. This data is often shared with third parties, including insurance companies, raising privacy concerns. Physical removal of the modem and GPS is a drastic measure to stop all data transmission at the hardware level.

<details><summary>References</summary>
<ul>
<li><a href="https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/">Removing the Modem and GPS from my 2024 RAV4 Hybrid</a></li>
<li><a href="https://www.cryptogon.com/?p=75142">cryptogon.com » “Removing the Modem and GPS from my 2024 RAV4 ...</a></li>

</ul>
</details>

**Discussion**: The community discussion (832 points, 427 comments) includes debate on Bluetooth vs USB telemetry risks, with some users noting that other vehicles like the Ford Maverick have a simpler fuse removal option. There are also concerns about Toyota sharing data with insurance companies, and some users express frustration with Toyota's handling of GPS issues.

**Tags**: `#privacy`, `#automotive`, `#telemetry`, `#hardware hacking`, `#security`

---

<a id="item-4"></a>
## [Antirez Launches DS4: Specialized LLM Runtime for DeepSeek V4](https://antirez.com/news/165) ⭐️ 8.0/10

Antirez announced DS4 (DwarfStar4), a small LLM inference runtime specifically designed for DeepSeek V4, optimized for MacBooks with 96GB RAM and supporting Metal, CUDA, and ROCm backends. DS4 provides a focused, high-performance inference solution for DeepSeek V4, a 1-trillion-parameter open-source model, enabling efficient local deployment on consumer hardware. This could accelerate adoption of large open-source models by reducing the barrier to running them locally. DS4's primary target is Metal on MacBooks with 96GB RAM, with CUDA support for DGX Spark and ROCm support in a separate branch maintained by the community. The project acknowledges llama.cpp and GGML as foundational dependencies.

hackernews · caust1c · May 14, 22:29 · [Discussion](https://news.ycombinator.com/item?id=48142108)

**Background**: LLM inference runtimes are software frameworks that execute trained language models to generate text. DeepSeek V4 is a 1-trillion-parameter open-source model that rivals proprietary models like GPT-5.5 and Claude Opus 4.7. DS4 is model-specific, unlike general-purpose runtimes like llama.cpp, aiming to maximize performance for DeepSeek V4.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48143570">DwarfStar4 is a small LLM inference runtime that can... | Hacker News</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V 4 : 1T Parameter AI Model Guide | Independent DeepSeek ...</a></li>
<li><a href="https://www.mindstudio.ai/blog/deepseek-v4-open-source-frontier-model">DeepSeek V 4 : The Open-Source Model Closing the Gap... | MindStudio</a></li>

</ul>
</details>

**Discussion**: Commenters noted DS4's narrow focus and hardware requirements, with some praising its performance closeness to Claude. Others questioned the need for a model-specific runtime versus using llama.cpp, given the effort required for a single model that may become obsolete.

**Tags**: `#LLM inference`, `#DeepSeek`, `#open source`, `#machine learning`, `#runtime`

---

<a id="item-5"></a>
## [Frontier AI access may be limited by economics and security](https://writing.antonleicht.me/p/cut-off) ⭐️ 8.0/10

An article argues that access to frontier AI models will soon be constrained by economic costs and security regulations, potentially limiting availability to a few powerful entities. This matters because restricted access could centralize AI power, stifle innovation, and create geopolitical divides, affecting startups, researchers, and nations without massive resources. The article does not mention open-weight models, which commenters argue are only months behind frontier models and could undercut the doom scenario. Additionally, datacenter availability is highlighted as a more fundamental bottleneck than model access.

hackernews · thoughtpeddler · May 15, 01:08 · [Discussion](https://news.ycombinator.com/item?id=48143284)

**Background**: Frontier AI models are the most advanced AI systems at a given time, trained on massive datasets to achieve state-of-the-art performance. Open-weight models make trained parameters publicly available, allowing others to use and modify them. The debate centers on whether open-weight models and sufficient datacenter capacity can democratize access to cutting-edge AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open-Weights Model? | AI21</a></li>

</ul>
</details>

**Discussion**: Commenters are skeptical of the doom scenario, noting that open-weight models like Qwen, Llama, and DeepSeek are close behind frontier models. They also argue that datacenter shortages, not model access, are the real bottleneck, and that only the US and China may have sufficient infrastructure.

**Tags**: `#AI`, `#geopolitics`, `#open-source`, `#datacenters`, `#frontier models`

---

<a id="item-6"></a>
## [UK ditches Palantir for in-house refugee system](https://www.bbc.com/news/articles/c2l2j1lxdk5o) ⭐️ 8.0/10

The UK government has replaced Palantir's Foundry-based refugee case management software with an internally-built system, saving millions of pounds. The new system was developed by the Home Office's own digital team. This move signals a shift away from expensive, controversial vendors like Palantir toward in-house development, potentially influencing other government procurement decisions. It also demonstrates that complex data integration challenges can be solved by internal teams at lower cost. The Palantir system was used for the Homes for Ukraine scheme, matching refugees with accommodation. The new system is open-source and built using standard government digital tools, with the Home Office claiming significant cost savings.

hackernews · cdrnsf · May 14, 22:44 · [Discussion](https://news.ycombinator.com/item?id=48142251)

**Background**: Palantir's Foundry platform is a data integration and analysis tool often used by governments and large enterprises. The UK government had contracted Palantir to manage data for the Homes for Ukraine scheme, which involved matching tens of thousands of visa applications with accommodation offers. Critics have long questioned Palantir's high costs and ethical concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c2l2j1lxdk5o">UK saves 'millions' of pounds by ditching Palantir for refugee system</a></li>
<li><a href="https://blog.palantir.com/ensuring-the-resettling-and-safeguarding-of-refugees-fleeing-the-war-in-ukraine-a5a5fcb306fa">Ensuring the Resettling and Safeguarding of Refugees ... | Palantir Blog</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about Palantir's value, with one noting that the data integration challenges were standard work for government digital teams. Another pointed out that Palantir's high cost stems from its consulting-heavy model, which may not be justified in the long term. Some also questioned whether the Palantir system was actually effective, citing anecdotal evidence that matching happened through Facebook groups instead.

**Tags**: `#government`, `#palantir`, `#software procurement`, `#UK`, `#refugee system`

---

<a id="item-7"></a>
## [RTX 5090 eGPU on M4 MacBook Air: Gaming & LLM Breakthrough](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

A developer successfully connected an RTX 5090 eGPU to an M4 MacBook Air via Thunderbolt, enabling playable gaming and significantly faster LLM inference on macOS. This is one of the first documented instances of a modern Nvidia GPU working with Apple Silicon through a custom driver and VM passthrough. This achievement challenges Apple's official stance that eGPUs are unsupported on Apple Silicon, opening new possibilities for Mac users in gaming and AI workloads. It also highlights the growing demand for GPU acceleration on Macs, especially for local LLM inference where prompt processing speed is a bottleneck. The setup uses a custom driver (TinyGPU) and a Linux VM with GPU passthrough, bypassing macOS's lack of eGPU support. Performance is limited by Thunderbolt bandwidth, but LLM prompt processing speed improved dramatically compared to Apple's unified memory. The author notes that only a 1.5 GB PCIe window is available, complicating the setup.

hackernews · allenleee · May 14, 15:47 · [Discussion](https://news.ycombinator.com/item?id=48137145)

**Background**: Apple Silicon Macs use unified memory, which is great for many tasks but limits GPU performance for gaming and AI. Apple officially dropped eGPU support with the transition to Apple Silicon, leaving users without a straightforward way to add discrete graphics. Thunderbolt-based eGPUs have been possible on Intel Macs, but on Apple Silicon, they require complex workarounds like VM passthrough and custom drivers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.compute-market.com/blog/nvidia-egpu-mac-local-ai-setup-2026">Nvidia eGPU on Mac for Local AI 2026 — TinyGPU Setup</a></li>
<li><a href="https://www.tomshardware.com/pc-components/gpus/copprlink-destroys-every-egpu-standard-in-new-test-achieves-near-native-level-performance-with-an-rtx-5090-setup-requires-usd2-300-worth-of-additional-hardware">'CopprLink' destroys every eGPU standard in new test ...</a></li>
<li><a href="https://egpu.io/setup-guide-external-graphics-card-mac/">The Beginner’s External Graphics Card Setup Guide for Mac | eGPU .io</a></li>

</ul>
</details>

**Discussion**: Commenters praised the technical achievement, with many noting the LLM inference improvements as the most practical benefit. Some expressed frustration with Apple's lack of official support, while others highlighted the complexity of the setup. One commenter suggested that adding Vulkan support via MoltenVK might be easier than the eGPU hack for some games.

**Tags**: `#eGPU`, `#Apple Silicon`, `#gaming`, `#LLM inference`, `#hardware hacking`

---

<a id="item-8"></a>
## [Mullvad VPN Exit IPs Enable User Fingerprinting](https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/) ⭐️ 8.0/10

A security researcher discovered that Mullvad VPN assigns exit IPs deterministically based on a user's WireGuard public key using a seeded random number generator, causing the same relative IP position across different servers and enabling cross-session user tracking. This undermines the anonymity promise of a highly trusted VPN service, as forum moderators or adversaries could link multiple accounts to the same user with high confidence, even when different servers are used. The deterministic assignment reduces the number of unique exit IP combinations from trillions to just 284 observed combinations, making it trivial to correlate users across sessions. Mullvad's co-founder confirmed they are testing a patch for the unintended behavior.

hackernews · RGBCube · May 15, 02:35 · [Discussion](https://news.ycombinator.com/item?id=48143880)

**Background**: VPNs typically assign a random exit IP from a pool to each connection, providing anonymity by mixing users. Mullvad uses a seeded RNG based on the user's WireGuard public key to assign IPs, which was intended to keep the same IP per server for consistency but inadvertently made the assignment predictable across servers.

<details><summary>References</summary>
<ul>
<li><a href="https://app.daily.dev/posts/mullvad-exit-ips-as-a-fingerprinting-vector-qalnhy2qk">Mullvad exit IPs as a fingerprinting vector | daily.dev</a></li>
<li><a href="https://thecodersblog.com/mullvad-exit-ips-a-privacy-paradox/">Mullvad Exit IPs: A Privacy Paradox? - The Coders Blog | Home</a></li>

</ul>
</details>

**Discussion**: Mullvad's co-founder acknowledged the issue and stated they are testing a patch, while some commenters questioned the statistical methodology used to claim >99% confidence in linking users. Others expressed surprise that such a simple oversight occurred in a privacy-focused service.

**Tags**: `#VPN`, `#privacy`, `#fingerprinting`, `#security`, `#Mullvad`

---

<a id="item-9"></a>
## [Critical Nginx RCE Exploit Published with ASLR Bypass Claim](https://github.com/DepthFirstDisclosures/Nginx-Rift) ⭐️ 8.0/10

A proof-of-concept exploit for a critical heap buffer overflow vulnerability in Nginx's rewrite module has been published, enabling unauthenticated remote code execution. The exploit, tracked as CVE-2026-42945, affects Nginx versions since 2008 and assumes ASLR is disabled, but the author claims a reliable ASLR bypass is possible. Nginx serves about 34% of all websites and is a critical component in enterprise Kubernetes environments, making this vulnerability extremely high-impact. If the ASLR bypass claim is validated, the exploit could affect a vast number of production deployments using rewrite rules with unnamed captures. The vulnerability requires a rewrite directive with a question mark in the replacement string and a subsequent set directive referencing a regex capture group (e.g., set $var $1). F5 has patched versions 1.31.0 and 1.30.1, and a mitigation is to use named captures instead of unnamed ones.

hackernews · hetsaraiya · May 14, 17:17 · [Discussion](https://news.ycombinator.com/item?id=48138268)

**Background**: Address Space Layout Randomization (ASLR) is a security technique that randomizes memory addresses to make exploitation harder. The published exploit disables ASLR to demonstrate the vulnerability, but ASLR bypass techniques such as memory disclosure or brute force can be used to overcome this protection. The vulnerability was discovered by an LLM-powered AI agent, highlighting the growing role of AI in security research.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/18-year-old-nginx-rce-vulnerability/">Critical 18-Year-Old NGINX Vulnerability Enables Remote Code ...</a></li>
<li><a href="https://dailysecurityreview.com/cyber-security/18-year-nginx-flaw-cve-2026-42945-enables-unauthenticated-rce/">18-Year NGINX Flaw CVE-2026-42945 Enables Unauthenticated RCE</a></li>
<li><a href="https://www.csoonline.com/article/4171437/ai-agent-finds-18-year-old-remote-code-execution-flaw-in-nginx.html">AI agent finds 18-year-old remote code execution flaw in Nginx</a></li>

</ul>
</details>

**Discussion**: Community comments express concern that the exploit is serious despite the ASLR precondition, with one security professional noting that the ASLR bypass claim is credible and should be taken seriously. Others point out specific preconditions required for exploitation, such as the use of unnamed captures in rewrite rules, and note that F5 has provided patches and mitigations.

**Tags**: `#nginx`, `#security`, `#exploit`, `#vulnerability`, `#aslr`

---

<a id="item-10"></a>
## [World Labs' image-blaster turns single image into 3D world](https://twitter.com/drfeifei/status/tweet-2055022392569905411) ⭐️ 8.0/10

World Labs has released 'image-blaster', a tool that converts a single image into a fully meshed 3D world in minutes, built by a team member and combining multiple generation models. This innovation significantly accelerates 3D reconstruction from a single image, potentially impacting computer vision, graphics, and spatial AI applications by enabling rapid creation of explorable 3D environments. The tool uses World Labs' Marble model (marble-1.1) to generate the explorable environment and a nano-banana model for source cleanup and reference images. It is available on GitHub under the repository 'neilsonnn/image-blaster'.

twitter · Fei-Fei Li · May 14, 20:28

**Background**: Traditional 3D reconstruction from a single image is challenging because depth information is lost during projection. Recent advances like LRM and SAM 3D have improved single-image 3D, but World Labs' approach combines multiple models for a complete meshed world in minutes.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/neilsonnn/image-blaster">GitHub - neilsonnn/ image - blaster : An image-to- world skillset for...</a></li>
<li><a href="https://www.worldlabs.ai/">World Labs</a></li>
<li><a href="https://fastcompany.co.za/impact/2025-11-13-discover-how-fei-fei-lis-world-labs-is-revolutionising-3d-environments-with-ai/">Discover how Fei-Fei Li's World Labs is revolutionising...</a></li>

</ul>
</details>

**Tags**: `#3D reconstruction`, `#computer vision`, `#AI`, `#graphics`

---

<a id="item-11"></a>
## [Codex Now Available in ChatGPT Mobile App](https://openai.com/index/work-with-codex-from-anywhere/) ⭐️ 7.0/10

OpenAI has integrated its Codex AI coding agent into the ChatGPT mobile app, allowing users to perform AI-assisted coding directly from their smartphones. This move extends Codex's availability beyond desktop and CLI to mobile devices. This integration makes AI-powered coding more accessible, enabling developers to work on code while on the go without needing a full desktop setup. It also popularizes the 'vibe coding' trend, where developers use natural language prompts to generate code iteratively. Codex is available for free on the ChatGPT free plan, though interactions may be used for training. The mobile app supports agentic coding with built-in worktrees and cloud environments, allowing parallel work across projects.

hackernews · OpenAI Blog · May 14, 20:06 · [Discussion](https://news.ycombinator.com/item?id=48140529)

**Background**: OpenAI Codex is a large language model that translates natural language prompts into source code. It was originally released as a standalone tool and later integrated into ChatGPT. 'Vibe coding' refers to an AI-assisted development practice where developers describe tasks in plain language and accept AI-generated code with minimal manual intervention.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model ) - Wikipedia</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some users appreciate the free access and convenience, while others report that mobile coding yields lower quality results due to screen size and lack of keyboard. There is also discussion about 'vibe coding' workflows, with some users experimenting with remote agents and voice-to-text setups.

**Tags**: `#AI coding`, `#ChatGPT`, `#Codex`, `#mobile development`, `#vibe coding`

---

<a id="item-12"></a>
## [Coding Agents Reduce Technology Lock-In](https://simonwillison.net/2026/May/14/not-so-locked-in/#atom-everything) ⭐️ 6.0/10

A blog post by Simon Willison reports that a medium-sized company used coding agents to rewrite both their iPhone and Android apps into React Native, and the team noted that if it turns out to be the wrong decision, they could easily port back to native in the future. This anecdote illustrates how AI-powered coding agents are lowering the cost of rewriting software, making technology choices less permanent and reducing vendor or platform lock-in. It signals a shift in software engineering where flexibility and reversibility become more feasible. The company had legacy iPhone and Android apps that were rewritten to React Native using coding agents. The decision was based on React Native's improvements and the ability to revert to native if needed, echoing Mitchell Hashimoto's observation that programming languages are increasingly not lock-in.

rss · Simon Willison · May 14, 22:53

**Background**: Technology lock-in occurs when a company becomes dependent on a specific technology, making switching costly or difficult. Coding agents are AI tools that can autonomously generate, modify, or rewrite code, reducing the effort required for large-scale rewrites. React Native is a cross-platform framework that allows building mobile apps using JavaScript and React, sharing code between iOS and Android.

<details><summary>References</summary>
<ul>
<li><a href="https://www.brilworks.com/blog/agentic-ai-software-development/">AI Coding Agents: Benefits, Risks & Best Practices</a></li>
<li><a href="https://reactnative.dev/blog/2024/10/23/the-new-architecture-is-here">New Architecture is here - React Native</a></li>

</ul>
</details>

**Tags**: `#coding agents`, `#React Native`, `#technology lock-in`, `#software engineering`

---