---
layout: default
title: "Horizon Summary: 2026-05-15 (EN)"
date: 2026-05-15
lang: en
---

> From 5 items, 5 important content pieces were selected

---

1. [Sea Limited Deploys OpenAI Codex for AI-Native Development](#item-1) ⭐️ 7.0/10
2. [World Labs Unveils Image-Blaster for 3D from Single Image](#item-2) ⭐️ 7.0/10
3. [Coding Agents Reduce Technology Lock-In](#item-3) ⭐️ 6.0/10
4. [Mitchell Hashimoto: Languages Becoming Fungible](#item-4) ⭐️ 6.0/10
5. [OpenAI Codex Now Available on ChatGPT Mobile App](#item-5) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Sea Limited Deploys OpenAI Codex for AI-Native Development](https://openai.com/index/sea-david-chen) ⭐️ 7.0/10

Sea Limited's Chief Product Officer David Chen announced the company is deploying OpenAI's Codex across engineering teams to accelerate AI-native software development in Asia. This marks a significant industry adoption of AI coding agents at scale by a major tech company, potentially setting a precedent for other enterprises in Asia and beyond. Codex is a suite of AI-driven coding agents that automate software engineering tasks such as feature development, refactoring, and code reviews. Sea Limited operates platforms like Shopee and Garena, making this deployment highly practical.

rss · OpenAI Blog · May 14, 20:30

**Background**: AI-native software development refers to building applications where AI is deeply integrated into the development lifecycle, not just added as a feature. OpenAI Codex is a large language model fine-tuned for coding tasks, capable of generating code from natural language prompts. Sea Limited is a leading internet company in Southeast Asia, known for e-commerce and gaming.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/codex/">Codex</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex">OpenAI Codex - Wikipedia</a></li>
<li><a href="https://www.dootrix.com/ai-native-software-development">AI Native Software Development</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#Codex`, `#software engineering`, `#industry adoption`

---

<a id="item-2"></a>
## [World Labs Unveils Image-Blaster for 3D from Single Image](https://twitter.com/drfeifei/status/tweet-2055022392569905411) ⭐️ 7.0/10

World Labs, co-founded by Fei-Fei Li, released image-blaster, a tool that converts a single image into a fully meshed 3D environment in under five minutes. The tool combines Claude skills, World Labs technology, and FAL to generate 3D meshes, SFX, and environments. This tool significantly lowers the barrier for creating 3D content, enabling rapid prototyping for game developers, filmmakers, and VR/AR creators. It represents a practical application of AI-driven 3D reconstruction, potentially accelerating workflows in computer graphics and virtual production. Image-blaster is built by a World Labs team member and is available on GitHub. It uses a skillset for Claude, indicating integration with Anthropic's AI assistant, and leverages FAL for inference. The output is a fully meshed 3D environment, not just a point cloud or Gaussian splat.

twitter · Fei-Fei Li · May 14, 20:28

**Background**: Single-image 3D reconstruction is a long-standing challenge in computer vision. Recent methods like Unique3D and InstantMesh have made progress, but often require significant compute or produce lower-quality meshes. World Labs, founded by AI pioneer Fei-Fei Li, focuses on spatial intelligence and generating interactive 3D worlds from images.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/neilsonnn/image-blaster">GitHub - neilsonnn/image-blaster: An image-to-world skillset for Claude. · GitHub</a></li>
<li><a href="https://www.worldlabs.ai/labs">Marble Labs | World Labs</a></li>
<li><a href="https://www.youtube.com/watch?v=9schOFFZtjs">A First Look at World Labs' AI system that Generates 3D Worlds from an Image - YouTube</a></li>

</ul>
</details>

**Tags**: `#3D reconstruction`, `#computer vision`, `#AI`, `#graphics`

---

<a id="item-3"></a>
## [Coding Agents Reduce Technology Lock-In](https://simonwillison.net/2026/May/14/not-so-locked-in/#atom-everything) ⭐️ 6.0/10

A medium-sized tech company used coding agents to rewrite both its legacy iPhone and Android apps into React Native, and noted that if the decision proves wrong, they can easily port back to native using the same agents. This anecdote illustrates how AI-assisted coding agents are lowering the cost of rewriting software, making technology choices less permanent and reducing vendor or platform lock-in across the industry. The company chose React Native because it has improved significantly and covered all their app requirements; the key insight is that coding agents make future porting back to native equally cheap, reversing the traditional lock-in dynamic.

rss · Simon Willison · May 14, 22:53

**Background**: Coding agents are AI-powered tools that can autonomously generate, refactor, or port code based on high-level instructions. Historically, rewriting an entire app from one framework or language to another was expensive and risky, creating strong lock-in. Recent advances in large language models (LLMs) have made these agents increasingly capable, as seen in projects like Bun's Zig-to-Rust migration using similar techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theregister.com/devops/2026/05/14/anthropics-bun-rust-rewrite-merged-at-speed-of-ai/5240381">Anthropic’s Bun Rust rewrite merged at speed of AI</a></li>
<li><a href="https://ziggit.dev/t/bun-is-being-ported-from-zig-to-rust/15330">Bun is being ported from Zig to Rust - Media - Ziggit</a></li>

</ul>
</details>

**Tags**: `#React Native`, `#coding agents`, `#software engineering`, `#portability`

---

<a id="item-4"></a>
## [Mitchell Hashimoto: Languages Becoming Fungible](https://simonwillison.net/2026/May/14/mitchell-hashimoto/#atom-everything) ⭐️ 6.0/10

Mitchell Hashimoto, creator of Vagrant and Terraform, commented on the increasing fungibility of programming languages, citing Bun's port from Zig to Rust as an example that languages are no longer a lock-in. This observation from a respected figure in software engineering highlights a shift in the industry where projects can switch languages relatively easily, reducing the long-term risk of language choice and encouraging more experimentation. Bun, a JavaScript runtime, was originally written in Zig but has been ported to Rust. Hashimoto notes that Bun demonstrated they could switch languages in roughly a week or two, implying that even Rust is expendable if needed.

rss · Simon Willison · May 14, 22:31

**Background**: Bun is a fast all-in-one JavaScript runtime, bundler, and package manager designed as a drop-in replacement for Node.js. Zig is a systems programming language focused on robustness and optimality, while Rust is known for memory safety and performance. Mitchell Hashimoto is a prominent figure in DevOps, having created tools like Vagrant and Terraform.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/HashiCorp">HashiCorp - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#programming languages`, `#Rust`, `#Zig`, `#Bun`, `#software engineering`

---

<a id="item-5"></a>
## [OpenAI Codex Now Available on ChatGPT Mobile App](https://openai.com/index/work-with-codex-from-anywhere) ⭐️ 5.0/10

OpenAI announced that Codex, its AI coding agent, can now be used via the ChatGPT mobile app, allowing developers to monitor, steer, and approve coding tasks in real time across devices and remote environments. This integration expands Codex's accessibility beyond desktop, enabling developers to manage coding tasks on the go, which could improve productivity and collaboration in software development workflows. The mobile app support includes real-time monitoring and approval of coding tasks, and is part of OpenAI's broader effort to make Codex more customizable and accessible across platforms.

rss · OpenAI Blog · May 14, 13:00

**Background**: Codex is a suite of AI-driven coding agents developed by OpenAI to automate software engineering tasks. It was previously available as a CLI tool and desktop application. The ChatGPT mobile app already offers various AI features, and this update brings Codex's capabilities to mobile users.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/business/media-telecom/openai-brings-codex-coding-tool-chatgpt-mobile-app-2026-05-14/">OpenAI brings Codex coding tool to ChatGPT mobile app - Reuters</a></li>
<li><a href="https://www.engadget.com/2173235/openai-brings-its-codex-coding-app-to-mobile/">OpenAI Brings Its Codex Coding App To Mobile - Engadget</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pjcXUtTUVSSEx2bW8yTG4wMUh5Z0FQAQ?hl=en-NG&gl=NG&ceid=NG:en">Google News - OpenAI adds Codex coding tool to ChatGPT mobile...</a></li>

</ul>
</details>

**Tags**: `#Codex`, `#ChatGPT`, `#mobile app`, `#AI coding`

---