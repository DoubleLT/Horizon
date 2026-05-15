---
layout: default
title: "Horizon Summary: 2026-05-15 (ZH)"
date: 2026-05-15
lang: zh
---

> From 5 items, 5 important content pieces were selected

---

1. [Sea Limited 部署 OpenAI Codex 推动 AI 原生开发](#item-1) ⭐️ 7.0/10
2. [World Labs 推出单图转 3D 工具 Image-Blaster](#item-2) ⭐️ 7.0/10
3. [编码代理降低技术锁定风险](#item-3) ⭐️ 6.0/10
4. [Mitchell Hashimoto：编程语言正变得可互换](#item-4) ⭐️ 6.0/10
5. [OpenAI Codex 现已登陆 ChatGPT 移动应用](#item-5) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Sea Limited 部署 OpenAI Codex 推动 AI 原生开发](https://openai.com/index/sea-david-chen) ⭐️ 7.0/10

Sea Limited 的首席产品官 David Chen 宣布，公司正在工程团队中部署 OpenAI 的 Codex，以加速亚洲地区的 AI 原生软件开发。 这标志着一家大型科技公司大规模采用 AI 编码代理的重要行业案例，可能为亚洲及其他地区的企业树立先例。 Codex 是一套 AI 驱动的编码代理，可自动化软件开发任务，如功能开发、重构和代码审查。Sea Limited 运营着 Shopee 和 Garena 等平台，使此次部署极具实用性。

rss · OpenAI Blog · May 14, 20:30

**背景**: AI 原生软件开发是指将 AI 深度集成到开发生命周期中，而不仅仅是作为功能添加。OpenAI Codex 是一个针对编码任务微调的大型语言模型，能够根据自然语言提示生成代码。Sea Limited 是东南亚领先的互联网公司，以电子商务和游戏闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/codex/">Codex</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex">OpenAI Codex - Wikipedia</a></li>
<li><a href="https://www.dootrix.com/ai-native-software-development">AI Native Software Development</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#Codex`, `#software engineering`, `#industry adoption`

---

<a id="item-2"></a>
## [World Labs 推出单图转 3D 工具 Image-Blaster](https://twitter.com/drfeifei/status/tweet-2055022392569905411) ⭐️ 7.0/10

由李飞飞联合创立的 World Labs 发布了 image-blaster 工具，可在五分钟内将单张图片转换为完整的网格化 3D 环境。该工具结合了 Claude 技能、World Labs 技术和 FAL，用于生成 3D 网格、特效和环境。 该工具大幅降低了 3D 内容创作的门槛，使游戏开发者、电影制作人和 VR/AR 创作者能够快速原型设计。它代表了 AI 驱动 3D 重建的实际应用，可能加速计算机图形学和虚拟制作的工作流程。 Image-blaster 由 World Labs 团队成员构建，并在 GitHub 上开源。它使用了 Claude 的技能集，表明与 Anthropic 的 AI 助手集成，并利用 FAL 进行推理。输出的是完整的网格化 3D 环境，而不仅仅是点云或高斯泼溅。

twitter · Fei-Fei Li · May 14, 20:28

**背景**: 单张图片的 3D 重建是计算机视觉领域的长期挑战。最近的方法如 Unique3D 和 InstantMesh 取得了进展，但通常需要大量计算或生成质量较低的网格。由 AI 先驱李飞飞创立的 World Labs 专注于空间智能，从图像生成交互式 3D 世界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/neilsonnn/image-blaster">GitHub - neilsonnn/image-blaster: An image-to-world skillset for Claude. · GitHub</a></li>
<li><a href="https://www.worldlabs.ai/labs">Marble Labs | World Labs</a></li>
<li><a href="https://www.youtube.com/watch?v=9schOFFZtjs">A First Look at World Labs' AI system that Generates 3D Worlds from an Image - YouTube</a></li>

</ul>
</details>

**标签**: `#3D reconstruction`, `#computer vision`, `#AI`, `#graphics`

---

<a id="item-3"></a>
## [编码代理降低技术锁定风险](https://simonwillison.net/2026/May/14/not-so-locked-in/#atom-everything) ⭐️ 6.0/10

一家中型科技公司使用编码代理将其遗留的 iPhone 和 Android 应用重写为 React Native，并指出如果决策有误，他们可以轻松地使用同样的代理移植回原生。 这一轶事表明，AI 辅助编码代理正在降低重写软件的成本，使技术选择不再永久，并减少了整个行业中的供应商或平台锁定。 该公司选择 React Native 是因为它已有显著改进并覆盖了所有应用需求；关键洞察是编码代理使得未来移植回原生同样廉价，逆转了传统的锁定动态。

rss · Simon Willison · May 14, 22:53

**背景**: 编码代理是基于 AI 的工具，能够根据高级指令自主生成、重构或移植代码。历史上，将整个应用从一个框架或语言重写为另一个成本高昂且风险巨大，从而造成强烈的锁定效应。大型语言模型（LLM）的最新进展使这些代理的能力不断增强，正如 Bun 项目使用类似技术从 Zig 迁移到 Rust 所展示的那样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/devops/2026/05/14/anthropics-bun-rust-rewrite-merged-at-speed-of-ai/5240381">Anthropic’s Bun Rust rewrite merged at speed of AI</a></li>
<li><a href="https://ziggit.dev/t/bun-is-being-ported-from-zig-to-rust/15330">Bun is being ported from Zig to Rust - Media - Ziggit</a></li>

</ul>
</details>

**标签**: `#React Native`, `#coding agents`, `#software engineering`, `#portability`

---

<a id="item-4"></a>
## [Mitchell Hashimoto：编程语言正变得可互换](https://simonwillison.net/2026/May/14/mitchell-hashimoto/#atom-everything) ⭐️ 6.0/10

Vagrant 和 Terraform 的创建者 Mitchell Hashimoto 评论说编程语言正变得越来越可互换，并以 Bun 从 Zig 移植到 Rust 为例，说明语言不再是锁定因素。 来自软件工程界受人尊敬人物的这一观察突显了行业的一个转变：项目可以相对容易地切换语言，从而降低了语言选择的长期风险，并鼓励更多实验。 Bun 是一个 JavaScript 运行时，最初用 Zig 编写，但已移植到 Rust。Hashimoto 指出，Bun 展示了他们可以在大约一两周内切换语言，这意味着即使是 Rust 在必要时也可以被替换。

rss · Simon Willison · May 14, 22:31

**背景**: Bun 是一个快速的全能 JavaScript 运行时、打包器和包管理器，旨在作为 Node.js 的直接替代品。Zig 是一种专注于健壮性和最优性的系统编程语言，而 Rust 以内存安全和性能著称。Mitchell Hashimoto 是 DevOps 领域的知名人物，创建了 Vagrant 和 Terraform 等工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/HashiCorp">HashiCorp - Wikipedia</a></li>

</ul>
</details>

**标签**: `#programming languages`, `#Rust`, `#Zig`, `#Bun`, `#software engineering`

---

<a id="item-5"></a>
## [OpenAI Codex 现已登陆 ChatGPT 移动应用](https://openai.com/index/work-with-codex-from-anywhere) ⭐️ 5.0/10

OpenAI 宣布，其 AI 编程代理 Codex 现在可以通过 ChatGPT 移动应用使用，使开发者能够在不同设备和远程环境中实时监控、引导和批准编程任务。 此次集成将 Codex 的使用范围从桌面扩展到移动端，使开发者能够随时随地管理编程任务，有望提升软件开发工作流程中的生产力和协作效率。 移动应用支持包括实时监控和批准编程任务，这是 OpenAI 使 Codex 更具可定制性并跨平台可访问的更广泛努力的一部分。

rss · OpenAI Blog · May 14, 13:00

**背景**: Codex 是 OpenAI 开发的一套 AI 驱动的编程代理，用于自动化软件工程任务。此前它以 CLI 工具和桌面应用程序的形式提供。ChatGPT 移动应用已提供多种 AI 功能，此次更新将 Codex 的能力带给了移动用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/business/media-telecom/openai-brings-codex-coding-tool-chatgpt-mobile-app-2026-05-14/">OpenAI brings Codex coding tool to ChatGPT mobile app - Reuters</a></li>
<li><a href="https://www.engadget.com/2173235/openai-brings-its-codex-coding-app-to-mobile/">OpenAI Brings Its Codex Coding App To Mobile - Engadget</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pjcXUtTUVSSEx2bW8yTG4wMUh5Z0FQAQ?hl=en-NG&gl=NG&ceid=NG:en">Google News - OpenAI adds Codex coding tool to ChatGPT mobile...</a></li>

</ul>
</details>

**标签**: `#Codex`, `#ChatGPT`, `#mobile app`, `#AI coding`

---