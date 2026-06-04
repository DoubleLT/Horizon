---
layout: default
title: "Horizon Summary: 2026-06-04 (ZH)"
date: 2026-06-04
lang: zh
---

> From 36 items, 33 important content pieces were selected

---

1. [Google DeepMind 发布 Gemma 4 12B 无编码器多模态模型](#item-1) ⭐️ 8.0/10
2. [NVIDIA 与微软推出 AI 原生本地计算机](#item-2) ⭐️ 8.0/10
3. [MicroAGI 推出提供 200 万美元算力的研究奖学金](#item-3) ⭐️ 7.0/10
4. [NVIDIA Cosmos 3：面向机器人的世界基础模型](#item-4) ⭐️ 7.0/10
5. [静态基准测试正在消亡，需协同进化](#item-5) ⭐️ 7.0/10
6. [Claude Code 的 /fork 命令现在可运行带完整上下文的后台代理](#item-6) ⭐️ 7.0/10
7. [Claude Code 自我验证技巧](#item-7) ⭐️ 7.0/10
8. [开发者用摄像头和笔记本电脑复现 Vision Pro](#item-8) ⭐️ 7.0/10
9. [StereoPolicy 为机器人操作添加几何线索](#item-9) ⭐️ 6.0/10
10. [Robotiq 为 Isaac Sim 发布触觉传感器数字孪生](#item-10) ⭐️ 6.0/10
11. [Helsing AI 发布首款防御四足机器人](#item-11) ⭐️ 6.0/10
12. [Robotiq 推出 IQ AI 平台，实现机器人集成自动化](#item-12) ⭐️ 6.0/10
13. [医学突破：Retatrutide 及其他进展](#item-13) ⭐️ 6.0/10
14. [视频理解瓶颈：运行模型而非设计模型](#item-14) ⭐️ 6.0/10
15. [噪声优化恢复崩溃的扩散模型](#item-15) ⭐️ 6.0/10
16. [用 Claude 自动化商业分析](#item-16) ⭐️ 6.0/10
17. [工作流：Claude Code 的重大升级](#item-17) ⭐️ 6.0/10
18. [Claude 实例像同事一样协作](#item-18) ⭐️ 6.0/10
19. [从第一性原理教授 AI 代理的教程](#item-19) ⭐️ 6.0/10
20. [10 个优秀到不该免费的 GitHub 仓库](#item-20) ⭐️ 6.0/10
21. [CoRL 2026 主题演讲阵容公布](#item-21) ⭐️ 5.0/10
22. [AI 将成为位于操作系统之上的新主要界面](#item-22) ⭐️ 5.0/10
23. [斯坦福 AI 实验室突出展示 CVPR 2026 论文](#item-23) ⭐️ 5.0/10
24. [人类比较图像时来回看，VLM 则不然](#item-24) ⭐️ 5.0/10
25. [开发者开箱 NVIDIA DGX Spark，8 分钟运行机器人 AI](#item-25) ⭐️ 5.0/10
26. [波兰创业生态蓬勃发展，ElevenLabs 处于核心](#item-26) ⭐️ 4.0/10
27. [ClaudeDevs 将触发词改为 'ultracode'](#item-27) ⭐️ 4.0/10
28. [NVIDIA RTX Spark：1 Petaflop AI 笔记本电脑，128GB 内存](#item-28) ⭐️ 4.0/10
29. [免费使用 Codex 和 Hermes Agent 的指南](#item-29) ⭐️ 3.0/10
30. [ICRA 上惊现“机器人手界的兰博基尼”](#item-30) ⭐️ 3.0/10
31. [SpaceX 从加州发射 24 颗星链卫星](#item-31) ⭐️ 3.0/10
32. [Yann LeCun 推广 NYU AI Frontier Lab 活动](#item-32) ⭐️ 3.0/10
33. [Sergey Levine 将在 CVPR 2026 ScaleBot 研讨会发表演讲](#item-33) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [Google DeepMind 发布 Gemma 4 12B 无编码器多模态模型](https://twitter.com/GoogleDeepMind/status/2062203391913119894) ⭐️ 8.0/10

Google DeepMind 宣布推出 Gemma 4 12B，这是一个统一的无编码器多模态模型，无需独立编码器即可直接处理视觉和音频，设计用于在配备 16 GB 内存的消费级笔记本电脑上运行。 此次发布通过支持在本地设备上运行智能体工作流和高级推理，减少对云基础设施的依赖并降低延迟，从而普及了高性能多模态 AI。 这个 120 亿参数的密集模型是 Gemma 4 系列的一部分，该系列包含从 2B 到 31B 参数的变体，并针对推理、编码和多模态理解进行了优化。

twitter · GoogleDeepMind · Jun 3, 16:02

**背景**: 传统的多模态模型依赖独立的编码器处理每种模态（例如视觉、音频），这会增加延迟和内存开销。Gemma 4 12B 通过将原始模态数据直接输入语言模型主干，消除了这些编码器，从而提高了效率。这种方法使得模型能够在资源有限的设备上运行，例如配备 16 GB 内存的笔记本电脑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/">Introducing Gemma 4 12B: a unified, encoder-free multimodal model</a></li>
<li><a href="https://huggingface.co/google/gemma-4-12B">google/ gemma - 4 - 12 B · Hugging Face</a></li>
<li><a href="https://www.marktechpost.com/2026/06/03/google-deepmind-releases-gemma-4-12b-an-encoder-free-multimodal-model-with-native-audio-that-runs-on-a-16-gb-laptop/">Google DeepMind Releases Gemma 4 12B: An Encoder-Free Multimodal Model with Native audio that runs on a 16 GB laptop - MarkTechPost</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的早期社区反馈是积极的，用户注意到较小的 E4B 变体取得了良好效果，并对 12B 版本的无编码器多模态能力表示兴趣。一些人正在等待量化模型以进一步降低资源需求。

**标签**: `#AI`, `#multimodal`, `#Google DeepMind`, `#Gemma`

---

<a id="item-2"></a>
## [NVIDIA 与微软推出 AI 原生本地计算机](https://twitter.com/RodmanAi/status/2062140830207611206) ⭐️ 8.0/10

NVIDIA 与微软宣布推出一款新的 AI 原生计算机，无需云连接或互联网即可本地运行强大的 AI 模型，取代价值 5 万美元的工作站。 这一发展标志着 AI 硬件民主化的重要一步，使个人和小型企业能够在本地运行高级 AI 模型，无需承担持续的云成本或延迟问题。 该设备被描述为一款真正的 AI 原生计算机，能够运行以前需要 5 万美元工作站才能运行的模型，并且完全离线运行，无需订阅。

twitter · RodmanAi · Jun 3, 11:54

**背景**: AI 原生计算机从底层设计用于加速 AI 工作负载，通常集成 GPU 或 NPU 等专用硬件。传统的 AI 推理通常依赖云服务器，这会引入延迟和持续成本。这一公告表明向强大的本地 AI 处理转变，类似于边缘计算趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/laptops/nvidia-and-microsoft-tease-a-new-era-of-pc-ahead-of-computex-2026-coordinated-social-media-posts-could-indicate-that-rumored-n1x-laptops-will-be-windows-on-arm-systems">Nvidia and Microsoft tease "a new era of PC..." | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#NVIDIA`, `#Microsoft`, `#local AI`, `#edge computing`

---

<a id="item-3"></a>
## [MicroAGI 推出提供 200 万美元算力的研究奖学金](https://twitter.com/lukas_m_ziegler/status/2062210959125459348) ⭐️ 7.0/10

MicroAGI 启动了一项为期 6 个月的研究奖学金，为 AI 研究人员提供高达 200 万美元的算力和机器人硬件。该奖学金将在慕尼黑或苏黎世进行，研究员可访问实验室的机器人硬件、数据和算力。 该奖学金为物理 AI 研究提供了大量资源，可能加速具身 AI 和实际部署的进展。它为研究人员提供了难得的机会，无需受制于常规资金限制即可获得大量算力和机器人硬件。 该奖学金是在 MicroAGI 位于慕尼黑或苏黎世的实验室进行为期 6 个月的有偿研究，可访问所有机器人硬件、数据和算力。提供的算力和硬件总价值可达 200 万美元。

twitter · lukas_m_ziegler · Jun 3, 16:33

**背景**: MicroAGI 是一个数据研究实验室，专注于端到端的物理 AGI，强调可靠的现实世界部署。具身 AI 旨在创建能够与物理世界交互的 AI 系统，这需要大量的机器人硬件和算力资源进行训练和评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microagi.ai/">microagi</a></li>
<li><a href="https://www.linkedin.com/posts/zenoh_with-microagi-were-launching-the-microagi-activity-7467866584007704577-6Pll">With microagi we're launching the microagi fellowship to give up to ...</a></li>
<li><a href="https://x.com/0xalain_/status/2062341285944709302">Paid Research Fellowship alert: MicroAGI just launched a paid 6-month ...</a></li>

</ul>
</details>

**社区讨论**: 该公告获得了一定程度的传播，一些用户强调这是物理 AI 领域的绝佳机会。目前未观察到实质性的讨论或批评。

**标签**: `#AI`, `#research fellowship`, `#compute`, `#robotics`

---

<a id="item-4"></a>
## [NVIDIA Cosmos 3：面向机器人的世界基础模型](https://twitter.com/lukas_m_ziegler/status/2061782380784832819) ⭐️ 7.0/10

NVIDIA 在 COMPUTEX 上发布了 Cosmos 3，这是一个世界基础模型，融合了视觉、推理和多模态生成能力，包括关节角度和夹爪位置等机器人动作数据。 这标志着向能够理解并在现实世界中行动的通用物理 AI 模型迈出了重要一步，有望加速机器人开发并实现更强大的自主系统。 Cosmos 3 基于混合 Transformer 架构构建，并且是开源的，在物理 AI 推理和世界模拟排行榜上名列前茅。

twitter · lukas_m_ziegler · Jun 2, 12:10

**背景**: 世界基础模型是旨在理解和模拟物理世界的 AI 模型，超越了传统的语言或图像模型。宇树科技是一家中国公司，以其四足机器人和人形机器人闻名，常用于研究和演示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai">NVIDIA Launches Cosmos 3 , the Open Frontier Foundation Model ...</a></li>
<li><a href="https://huggingface.co/docs/diffusers/main/en/api/pipelines/cosmos3">Cosmos 3 · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unitree_Robotics">Unitree Robotics</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#AI`, `#robotics`, `#foundation model`, `#multimodal`

---

<a id="item-5"></a>
## [静态基准测试正在消亡，需协同进化](https://twitter.com/berkeley_ai/status/2062358478631719262) ⭐️ 7.0/10

伯克利 AI 研究员杨振指出，静态基准测试因快速饱和而逐渐过时，并建议评估与训练数据应与 AI 前沿协同进化。 这揭示了当前 AI 评估实践中的关键缺陷——模型过度拟合静态基准，阻碍了真正进步。呼吁动态评估可能重塑 AI 社区衡量和推动进展的方式。 推文强调 GLUE、SuperGLUE 等基准已被饱和，需要与模型能力同步进化的新基准。这种方法要求持续更新评估数据集以防止过拟合。

twitter · berkeley_ai · Jun 4, 02:19

**背景**: 静态基准是用于评估 AI 模型的固定数据集，但随着模型改进，它们常达到近乎完美的分数，使基准无法区分进展。评估与训练数据协同进化的概念旨在创建一个更能反映现实挑战的动态目标。

**标签**: `#AI`, `#ML`, `#benchmarks`, `#evaluation`

---

<a id="item-6"></a>
## [Claude Code 的 /fork 命令现在可运行带完整上下文的后台代理](https://twitter.com/ClaudeDevs/status/2061947411141169494) ⭐️ 7.0/10

Claude Code 更新了 /fork 命令：现在它会启动一个后台代理，携带完全相同的系统提示、工具、对话历史、模型和提示缓存，并将结果直接返回当前会话。旧的 /fork 行为（将对话记录复制到一个新的交互式会话）已更名为 /branch。 此更新通过允许在不阻塞主会话的情况下并行探索解决方案，显著改善了开发者工作流程，减少了上下文切换开销。它还明确了后台执行 (/fork) 与会话分支 (/branch) 之间的区别，使 Claude Code 在处理复杂编码任务时更加强大。 /fork 中的后台代理保留了包括提示缓存在内的完整上下文，通过避免重复处理相同前缀来降低延迟和成本。/branch 命令保留了原始的分支行为，允许用户从对话记录副本手动驱动新会话。

twitter · ClaudeDevs · Jun 2, 23:05

**背景**: Claude Code 是 Anthropic 推出的基于终端的 AI 编码助手，与 Claude 模型集成。/fork 命令最初用于将对话记录复制到一个新的交互式会话中，类似于版本控制中的分支。提示缓存是一种技术，它存储最近处理过的输入前缀，以加速后续请求并降低 API 成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@richardhightower/mastering-claude-codes-btw-fork-and-rewind-the-context-hygiene-toolkit-5ceefa59623d">Mastering Claude Code ’s /btw, / fork , and /rewind: The... | Medium</a></li>
<li><a href="https://code.claude.com/docs/en/cli-reference">Complete reference for Claude Code command -line interface...</a></li>
<li><a href="https://blog.dailydoseofds.com/p/prompt-caching-in-llms">Prompt Caching in LLMs! - by Avi Chawla</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，许多开发者称赞工作流程效率的提升以及 /fork 和 /branch 之间的清晰区分。一些用户指出，后台代理功能解决了长时间运行任务期间阻塞会话这一长期痛点。

**标签**: `#Claude Code`, `#AI coding tools`, `#developer tools`, `#product update`

---

<a id="item-7"></a>
## [Claude Code 自我验证技巧](https://twitter.com/ClaudeDevs/status/2061900434722496604) ⭐️ 7.0/10

一项技术被分享，展示了如何编码手动检查，使 Claude Code 在返回输出前能自我验证，从而关闭自身的反馈循环。 这提高了 AI 生成代码的可靠性，减少了人工审查的需求，节省了开发者的时间，并在工作流程中更早地捕获错误。 核心原则是预先指定验证标准，使 Claude 能够自我判断是否正确完成任务，而不是被动等待失败和修复。

twitter · ClaudeDevs · Jun 2, 19:59

**背景**: Claude Code 是一种 AI 编码助手，可根据自然语言提示生成代码。通常，开发人员需要手动审查 AI 输出的正确性，这可能很耗时。自我验证技术旨在将这一质量检查自动化到 AI 自身的流程中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://levelup.gitconnected.com/expected-output-self-verification-in-claude-code-d5eb314545d1">Expected Output Self - Verification in Claude Code | Level Up Coding</a></li>

</ul>
</details>

**标签**: `#AI-assisted coding`, `#Claude Code`, `#code quality`, `#feedback loops`

---

<a id="item-8"></a>
## [开发者用摄像头和笔记本电脑复现 Vision Pro](https://twitter.com/RodmanAi/status/2061689842074063211) ⭐️ 7.0/10

一位名为 RodmanAi 的开发者展示了一个纯软件系统，仅用摄像头和笔记本电脑就复现了 Apple Vision Pro 的核心体验，无需头戴设备即可达到 60 FPS。 这突显了一个趋势：软件创新可以大幅降低先进技术的成本，可能使 AR/VR 体验无需昂贵硬件就能惠及更广泛的用户。 该系统以每秒 60 帧实时运行，性能堪比专用硬件。开发者声称无需耗资数十亿美元的实验室或大量工程师，仅靠代码即可实现。

twitter · RodmanAi · Jun 2, 06:02

**背景**: Apple Vision Pro 是一款高端混合现实头戴设备，售价 3500 美元，耗时七年开发。它利用先进传感器和显示器将数字内容与物理世界融合。此次复现表明，其部分核心功能可通过简单摄像头和计算机视觉算法实现。

**标签**: `#AR/VR`, `#innovation`, `#software`, `#cost reduction`

---

<a id="item-9"></a>
## [StereoPolicy 为机器人操作添加几何线索](https://twitter.com/drfeifei/status/2062283541069930791) ⭐️ 6.0/10

研究人员推出了 StereoPolicy，这是一个视觉运动策略学习框架，利用同步立体图像对来增强机器人操作中的几何推理，无需显式的 3D 重建或相机标定。 该方法通过提供几何感知的视觉表示，可能显著提升机器人操作策略的鲁棒性和泛化能力，并减少对昂贵深度传感器的依赖。 StereoPolicy 直接处理立体图像对以增强几何推理，避免了显式 3D 重建的计算开销。该框架专为视觉运动策略学习设计，无需标定深度传感。

twitter · drfeifei · Jun 3, 21:21

**背景**: 计算机立体视觉通过从不同视角拍摄的两幅或多幅图像中提取 3D 信息，模拟人类双眼视觉。传统方法通常需要显式的 3D 重建或标定相机，这在实时机器人应用中可能计算成本高昂或不切实际。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.09989">[2605.09989] StereoPolicy: Improving Robotic Manipulation ... StereoPolicy stereopolicy.github.io/README.md at main · stereopolicy ... [PDF] StereoPolicy: Improving Robotic Manipulation Policies ... Stanford Computer Vision Lab : Publications Stereo Vision and Depth Estimation - GeeksforGeeks Computer stereo vision - Wikipedia</a></li>
<li><a href="https://stereopolicy.github.io/">StereoPolicy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computer_stereo_vision">Computer stereo vision - Wikipedia</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#stereo vision`, `#AI`, `#research`

---

<a id="item-10"></a>
## [Robotiq 为 Isaac Sim 发布触觉传感器数字孪生](https://twitter.com/lukas_m_ziegler/status/2062173943927095673) ⭐️ 6.0/10

Robotiq 为其 TSF-85 触觉传感器发布了适用于 NVIDIA Isaac Sim 的数字孪生，使机器人能够在虚拟环境中模拟触觉。 这一集成将触觉感知引入传统仅依赖视觉的机器人仿真中，可能提升用于操作任务的 AI 模型性能。 该数字孪生可在 NVIDIA Isaac Sim（Omniverse 上的开源仿真平台）中使用，使开发者无需物理硬件即可测试触觉反馈。

twitter · lukas_m_ziegler · Jun 3, 14:05

**背景**: NVIDIA Isaac Sim 是一个机器人仿真平台，用于在逼真的虚拟环境中开发和测试 AI 驱动的机器人。TSF-85 等触觉传感器可测量接触力和纹理，对精确操作至关重要。数字孪生是物理传感器的虚拟副本，可实现基于仿真的开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/isaac/sim">Isaac Sim - Robotics Simulation and Synthetic Data Generation | NVIDIA Developer</a></li>
<li><a href="https://github.com/isaac-sim/IsaacSim">GitHub - isaac-sim/IsaacSim: NVIDIA Isaac Sim™ is an open-source application on NVIDIA Omniverse for developing, simulating, and testing AI-driven robots in realistic virtual environments.</a></li>
<li><a href="https://arxiv.org/html/2509.10063v1">TwinTac: A Wide-Range, Highly Sensitive Tactile Sensor with ...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#tactile sensing`, `#simulation`, `#NVIDIA Isaac Sim`

---

<a id="item-11"></a>
## [Helsing AI 发布首款防御四足机器人](https://twitter.com/lukas_m_ziegler/status/2061920695014035943) ⭐️ 6.0/10

欧洲领先的国防人工智能公司 Helsing AI 发布了其首个先进机器人平台，这是一款专为防御应用设计的四足机器人。 这标志着 Helsing 进入实体机器人领域，从纯软件 AI 解决方案扩展，可能加速欧洲国防领域对自主系统的采用。 该公告通过 Lukas M. Ziegler 的推文发布，但未提供技术规格或部署时间表。该平台被描述为“四足机器人”，类似于波士顿动力的 Spot。

twitter · lukas_m_ziegler · Jun 2, 21:19

**背景**: Helsing AI 是一家专注于国防人工智能的欧洲公司，以开发战斗机和无人机软件而闻名。四足机器人因其能够穿越崎岖地形，越来越多地被用于侦察和后勤等军事任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Helsing_(company)">Helsing (company) - Wikipedia</a></li>
<li><a href="https://helsing.ai/">Helsing | Artificial intelligence to protect our democracies</a></li>

</ul>
</details>

**标签**: `#defense AI`, `#robotics`, `#quadruped`, `#Helsing AI`

---

<a id="item-12"></a>
## [Robotiq 推出 IQ AI 平台，实现机器人集成自动化](https://twitter.com/lukas_m_ziegler/status/2061809221818036248) ⭐️ 6.0/10

Robotiq 推出了 IQ 平台，这是一个由 AI 驱动的平台，能够自动化从初步评估到可部署工作单元的整个机器人工作单元集成流程。 这解决了工业机器人领域长期存在的瓶颈——集成过程复杂、耗时且成本高昂——有望加速中小企业的机器人部署。 IQ 能够捕获项目需求、协调工程工作流并生成经过验证的系统设计，从而减少集成过程中的人工劳动和错误。

twitter · lukas_m_ziegler · Jun 2, 13:56

**背景**: 机器人集成涉及设计、编程和测试机器人工作单元以执行特定任务，通常需要专业的集成商。传统集成过程是手动的、迭代的，并且容易延误。IQ 旨在通过 AI 自动化设计和验证步骤来简化这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://robotiq.com/iq-platform">IQ AI-enabled platform that automates integration | Robotiq</a></li>
<li><a href="https://roboticsandautomationnews.com/2026/06/03/robotiq-launches-ai-platform-to-automate-robotic-workcell-integration/102227/">Robotiq launches AI-powered IQ platform for robotic workcell integration</a></li>

</ul>
</details>

**标签**: `#robotics`, `#AI`, `#industrial automation`

---

<a id="item-13"></a>
## [医学突破：Retatrutide 及其他进展](https://twitter.com/karpathy/status/2061930040003280905) ⭐️ 6.0/10

Andrej Karpathy 转发了一条推文，指出过去五周内出现了一系列医学突破，包括用于肥胖症的三重激动剂 retatrutide 及其他进展。 这些突破可能对肥胖及相关代谢疾病的治疗产生重大影响，为患者带来新希望，并重塑医药行业格局。 Retatrutide 是一种实验性三重激素受体激动剂，靶向 GLP-1、GIP 和胰高血糖素受体，由礼来公司开发。在 2 期试验中，12 mg 剂量组在 48 周后平均体重减轻了 24.2%。

twitter · karpathy · Jun 2, 21:56

**背景**: 肥胖症是一场全球健康危机，与多种疾病相关。像 semaglutide 这样的 GLP-1 受体激动剂已取得成功，但 retatrutide 同时靶向三种受体，可能提供更高的疗效。该推文还提及同期其他未具体说明的医学进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retatrutide">Retatrutide - Wikipedia</a></li>
<li><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2301972">Triple–Hormone-Receptor Agonist Retatrutide for Obesity — A ...</a></li>
<li><a href="https://investor.lilly.com/news-releases/news-release-details/lillys-triple-agonist-retatrutide-delivered-weight-loss-average">Lilly's triple agonist, retatrutide, delivered weight loss of up to an average of 71.2 lbs along with substantial relief from osteoarthritis pain in first successful Phase 3 trial | Eli Lilly and Company</a></li>

</ul>
</details>

**标签**: `#medicine`, `#health`, `#science`

---

<a id="item-14"></a>
## [视频理解瓶颈：运行模型而非设计模型](https://twitter.com/StanfordAILab/status/2061910343170011283) ⭐️ 6.0/10

斯坦福 AI 实验室的一条推文指出，视频理解的最大挑战在于运行现有模型的计算困难，而非模型架构本身。 这一观察突显了模型创新与实际部署之间的关键差距，影响了需要高效推理以应用于实际场景的研究人员和从业者。 该推文是一条参与度较低的转发，但它指出了一个广泛认可的问题：许多最先进的视频理解模型需要过多的计算资源，限制了其使用。

twitter · StanfordAILab · Jun 2, 20:38

**背景**: 视频理解模型，例如基于 CNN 或 Transformer 的模型，通常需要每秒处理大量帧，导致高内存和计算需求。最近像 Mobile-VideoGPT 这样的工作旨在创建高效模型以用于实际部署，但差距仍然显著。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2503.21782v1">Mobile-VideoGPT: Fast and Accurate Video Understanding Language Model</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-57679-9_7">Efficient Video Understanding | SpringerLink</a></li>

</ul>
</details>

**标签**: `#video understanding`, `#AI`, `#computational efficiency`

---

<a id="item-15"></a>
## [噪声优化恢复崩溃的扩散模型](https://twitter.com/berkeley_ai/status/2062358667077533843) ⭐️ 6.0/10

一篇 CVPR2026 论文《为时未晚：训练后扩散模型崩溃恢复的噪声优化》提出使用噪声优化来恢复已崩溃（即生成输出失去多样性）的扩散模型。 这项工作解决了扩散模型中的关键问题——模型崩溃，该问题在模型使用合成数据训练时会导致性能下降。它提供了一种无需重新训练的后训练修复方法，对于维护迭代训练流程中的模型质量具有重要意义。 该论文专门针对已训练扩散模型的“崩溃恢复”，通过优化推理过程中的噪声输入来实现。这种方法不同于传统的通过修改训练过程来预防崩溃的方法。

twitter · berkeley_ai · Jun 4, 02:19

**背景**: 扩散模型通过逐步去噪随机噪声来生成数据。当模型无法产生多样化的输出时，就会出现模式崩溃，这通常是由于使用合成数据训练或其他因素导致。噪声优化技术已被探索用于通过选择或优化推理时的初始噪声来提高生成质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zilliz.com/ai-faq/how-do-you-prevent-mode-collapse-in-diffusion-models">How do you prevent mode collapse in diffusion models? - Zilliz Vector Database</a></li>
<li><a href="https://arxiv.org/abs/2602.16601">[2602.16601] Error Propagation and Model Collapse in Diffusion Models: A Theoretical Study</a></li>
<li><a href="https://arxiv.org/html/2407.14041v1">Not All Noises Are Created Equally: Diffusion Noise Selection and Optimization</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#noise optimization`, `#CVPR`, `#AI research`

---

<a id="item-16"></a>
## [用 Claude 自动化商业分析](https://twitter.com/ClaudeDevs/status/2062274312363770064) ⭐️ 6.0/10

一篇博客文章分享了使用 Claude 自动化商业分析的最佳实践，涵盖了构建数据分析代理所需的技能、数据基础和评估方法。 这为开发者和分析师提供了利用 Claude 进行商业分析的实用指南，有望提高数据驱动洞察的效率和可及性。 该文章聚焦三个领域：技能（提示工程、工具使用）、数据基础（数据清洗、模式设计）和评估（测试准确性、处理边缘情况）。

twitter · ClaudeDevs · Jun 3, 20:44

**背景**: 商业分析涉及分析数据以辅助商业决策。Claude 是一个 AI 助手，可以通过技能和工具进行定制，以自动化该过程的某些部分。

**标签**: `#Claude`, `#business analytics`, `#automation`, `#best practices`

---

<a id="item-17"></a>
## [工作流：Claude Code 的重大升级](https://twitter.com/ClaudeDevs/status/2061907684656599464) ⭐️ 6.0/10

工作流被引入为自技能和子代理以来 Claude Code 能力的最大升级，一位开发者在 Twitter 上强调了这一点。 这一升级显著增强了 Claude Code 处理复杂多步骤开发任务的能力，使其在软件开发工作流中更加强大。 工作流建立在现有技能和子代理之上，允许开发者以结构化序列编排多个 AI 代理，实现生产级开发。

twitter · ClaudeDevs · Jun 2, 20:27

**背景**: Claude Code 是一个 AI 驱动的编码助手，帮助开发者编写、调试和重构代码。技能和子代理是早期的自定义层：技能提供可重用的任务特定指令，而子代理是用于特定任务的专门 AI 代理。工作流现在能够将这些组合成自动化流水线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/shinpr/claude-code-workflows">GitHub - shinpr/ claude - code - workflows : Production-ready...</a></li>
<li><a href="https://code.claude.com/docs/en/skills">Extend Claude with skills - Claude Code Docs</a></li>
<li><a href="https://zencoder.ai/blog/claude-code-skills-vs-subagents">Claude Code Skills vs. Subagents : What Are the Differences?</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI tools`, `#workflows`, `#software development`

---

<a id="item-18"></a>
## [Claude 实例像同事一样协作](https://twitter.com/RodmanAi/status/2061898807332454827) ⭐️ 6.0/10

一位开发者演示了多个 Claude 实例直接相互通信，共同完成一个软件项目，每个实例分别承担后端、前端、调试、研究和代码审查等不同角色。 这展示了一种无需传统 API、代理框架或编排器的多智能体 AI 协作新方法，可能简化 AI 代理在复杂任务中的协同工作方式。 该设置让 Claude 实例直接相互发送消息，像同事一样共享上下文，而非依赖外部编排工具或 API。

twitter · RodmanAi · Jun 2, 19:52

**背景**: 多智能体协作涉及多个 AI 代理共同解决复杂问题。通常，这需要编排框架或 API 来协调代理。该演示通过让 Claude 实例直接通信，绕过了这些中间层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/Anthropic/comments/1rmya79/i_built_an_mcp_server_that_lets_multiple_claude/">I built an MCP server that lets multiple Claude instances talk to each other in real time</a></li>
<li><a href="https://code.claude.com/docs/en/agent-teams">Orchestrate teams of Claude Code sessions</a></li>
<li><a href="https://www.ibm.com/think/topics/multi-agent-collaboration">What is multi-agent collaboration? - IBM</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区讨论了一个相关的开源 MCP 服务器 Cross-Claude MCP，它支持 Claude 实例之间的实时消息传递，被比作 AI 代理的轻量级 Slack。

**标签**: `#AI`, `#multi-agent`, `#Claude`, `#collaboration`

---

<a id="item-19"></a>
## [从第一性原理教授 AI 代理的教程](https://twitter.com/RodmanAi/status/2061868795795505176) ⭐️ 6.0/10

RodmanAi 发布了一个教程系列，从第一性原理教授构建 AI 代理，避免黑盒框架，专注于代理如何思考、规划、使用工具和执行任务。 这种方法帮助开发者深入理解 AI 代理的内部机制，而不仅仅是使用高层抽象，这对于在生产中构建健壮且可定制的代理至关重要。 该教程承诺提供无黑盒框架的实践分解，链接指向的资源可能包含代码示例和逐步解释。

twitter · RodmanAi · Jun 2, 17:53

**背景**: AI 代理是能够感知环境、做出决策并采取行动以实现目标的自主系统。许多现有框架抽象了底层机制，使开发者难以自定义或调试代理。从第一性原理学习意味着理解核心算法和数据流，而不依赖预构建的库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/ai-agents-for-beginners">GitHub - microsoft/ai-agents-for-beginners: 12 Lessons to Get ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/">AI Agents for Beginners | Microsoft Learn</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents ? | IBM</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#tutorial`, `#first principles`, `#software engineering`

---

<a id="item-20"></a>
## [10 个优秀到不该免费的 GitHub 仓库](https://twitter.com/RodmanAi/status/2061798362798768628) ⭐️ 6.0/10

一条推文列出了 10 个令人印象深刻的 GitHub 仓库，首先是 AutoHedge，一个由四个 AI 代理构建的自主对冲基金，负责投资论点、验证、风险管理和订单执行。 这个合集突显了金融领域开源 AI 工具的增长趋势，使之前仅对机构投资者开放的复杂交易策略变得大众化。 AutoHedge 利用群体智能和大语言模型来协调专门的 AI 代理，模仿真实对冲基金的结构，且不收取管理费或业绩报酬。

twitter · RodmanAi · Jun 2, 13:13

**背景**: AI 交易机器人利用机器学习分析市场并自动执行交易。像 AutoHedge 这样的开源项目允许开发者构建和定制自己的交易系统，降低了算法交易的入门门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/The-Swarm-Corporation/AutoHedge">GitHub - The-Swarm-Corporation/AutoHedge: Build your ...</a></li>
<li><a href="https://www.blog.brightcoding.dev/2025/11/26/autohedge-build-your-autonomous-ai-hedge-fund-in-minutes-2025-guide/">AutoHedge: Build Your Autonomous AI Hedge Fund in Minutes ...</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#AI`, `#Python`, `#finance`

---

<a id="item-21"></a>
## [CoRL 2026 主题演讲阵容公布](https://twitter.com/drfeifei/status/2062402192938832292) ⭐️ 5.0/10

机器人学习大会（CoRL）2026 公布了主题演讲阵容，包括来自 MIT 的 Russ Tedrake 以及来自斯坦福大学和 World Labs 的李飞飞。 这一阵容凸显了机器人与人工智能日益交叉的趋势，两位演讲者都是机器人学习和空间智能领域的领军人物。 CoRL 2026 将在德克萨斯州奥斯汀举行，会议聚焦机器人与机器学习的交叉领域。

twitter · drfeifei · Jun 4, 05:12

**背景**: 机器人学习大会（CoRL）是一年一度的国际会议，汇集了机器人和机器学习领域的研究人员。李飞飞是著名的计算机科学家，以计算机视觉和空间智能方面的研究闻名，她的初创公司 World Labs 最近筹集了 10 亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.corl.org/">CoRL 2026</a></li>
<li><a href="https://www.reuters.com/business/ai-pioneer-fei-fei-lis-world-labs-raises-1-billion-funding-2026-02-18/">AI pioneer Fei-Fei Li's World Labs raises $1 billion in funding</a></li>

</ul>
</details>

**标签**: `#robotics`, `#conference`, `#keynote`, `#AI`

---

<a id="item-22"></a>
## [AI 将成为位于操作系统之上的新主要界面](https://twitter.com/ylecun/status/2061837853944848640) ⭐️ 5.0/10

Yann LeCun 转发了一个预测，认为 AI 将成为世界的主要界面，位于操作系统之上，并瓦解当前的 SaaS 层。 这一愿景表明计算架构将发生根本性转变，AI 将中介所有用户交互，可能颠覆现有软件商业模式和用户体验范式。 该推文特别指出 AI 将位于比操作系统更高的堆栈位置，并将瓦解当前的 SaaS 层，意味着多个应用将整合到单一的 AI 驱动界面中。

twitter · ylecun · Jun 2, 15:50

**背景**: 目前，用户通过操作系统和应用程序与计算机交互。像 Siri 或 ChatGPT 这样的 AI 助手是独立的工具。这一预测设想 AI 成为理解用户意图并协调所有软件任务的顶层，使传统应用界面变得不那么重要。

**标签**: `#AI`, `#interface`, `#future`, `#SaaS`

---

<a id="item-23"></a>
## [斯坦福 AI 实验室突出展示 CVPR 2026 论文](https://twitter.com/StanfordAILab/status/2062226889058726172) ⭐️ 5.0/10

斯坦福 AI 实验室发布了一篇博客文章，展示了他们在 CVPR 2026 上被接收的论文。 这凸显了斯坦福大学在计算机视觉研究方面的持续贡献，并提供了其最新工作的集中概述。 该博客文章列出了 SAIL 在 CVPR 2026 上出现的多篇论文，但公告中未提供具体的论文标题或细节。

twitter · StanfordAILab · Jun 3, 17:36

**背景**: CVPR（计算机视觉与模式识别会议）是计算机视觉领域的顶级年度会议。斯坦福 AI 实验室（SAIL）是一个领先的研究团队，经常在此类会议上发表有影响力的工作。

**标签**: `#CVPR`, `#computer vision`, `#academic papers`, `#Stanford`

---

<a id="item-24"></a>
## [人类比较图像时来回看，VLM 则不然](https://twitter.com/berkeley_ai/status/2062358241238225125) ⭐️ 5.0/10

@zwcolin 的一条推文（由 @berkeley_ai 转发）指出，人类比较图像时会来回查看，而许多开放权重的视觉语言模型（VLM）则独立编码每张图像，将比较推迟到后续阶段。 这一观察突显了人类视觉比较与当前 VLM 方法之间的根本差异，可能限制了 VLM 执行细粒度图像比较任务的能力。理解这一差距有助于指导未来 VLM 架构向更接近人类处理方式的方向发展。 该推文特别提到“开放权重 VLM”会独立编码图像，与人类采用来回查看的策略形成对比。该观察属于轶事性质，缺乏实验验证或具体模型名称。

twitter · berkeley_ai · Jun 4, 02:18

**背景**: 视觉语言模型（VLM）是同时处理图像和文本的 AI 模型，常用于图像描述、视觉问答和图像比较等任务。开放权重 VLM 的模型权重公开可用，允许研究人员研究和修改。许多当前 VLM 在跨图像交互之前，会分别将每张输入图像编码为固定表示，这与人类视觉比较中涉及迭代、对比查看的方式不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2601.10611">[2601.10611] Molmo2: Open Weights and Data for Vision ... Best Open-Source Vision Language Models of 2026 Lightweight VLM Open Source Models Collection Multimodal AI: The Best Open-Source Vision Language Models in ... Tiny VLMs Lab - GitHub Molmo and PixMo: Open Weights and Open Data for State-of-the ...</a></li>
<li><a href="https://nipunbatra.github.io/blog/posts/2025-12-27-multi-image-vlm.html">Multi- Image Vision-Language Model: Compare , Reason, and...</a></li>
<li><a href="https://blog.roboflow.com/what-is-a-vision-language-model/">Best Vision-Language Models: Guide to Using VLMs</a></li>

</ul>
</details>

**标签**: `#VLM`, `#computer vision`, `#AI research`

---

<a id="item-25"></a>
## [开发者开箱 NVIDIA DGX Spark，8 分钟运行机器人 AI](https://twitter.com/RodmanAi/status/2062262849670639660) ⭐️ 5.0/10

一位中国开发者开箱了 NVIDIA DGX Spark，从零开始设置，安装了完整的机器人仿真软件栈，并在短短 8 分钟内让 AI 智能体运行起来，整个过程通过未剪辑的视频展示。 这一演示突显了个人 AI 超级计算变得多么易于使用，可能加速个人开发者和小型团队的机器人研究与开发。 NVIDIA DGX Spark 搭载 GB10 Grace Blackwell 超级芯片，提供高达 1 petaFLOP 的 FP4 AI 性能，拥有 128 GB 统一内存，并支持高达 2000 亿参数的模型。

twitter · RodmanAi · Jun 3, 19:59

**背景**: NVIDIA DGX Spark 是一款于 2025 年发布的紧凑型个人 AI 超级计算机，专为 AI 开发和机器人仿真设计。机器人仿真软件栈通常包括 NVIDIA Isaac Sim、Isaac ROS 和 Omniverse，使开发者能够在虚拟环境中模拟和训练机器人，然后再部署到真实硬件上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/">Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark</a></li>
<li><a href="https://www.robosynx.com/learn/nvidia-stack">NVIDIA Robotics Stack Explained — Silicon to Isaac Sim ...</a></li>
<li><a href="https://developer.nvidia.com/isaac/sim">Isaac Sim - Robotics Simulation and Synthetic Data Generation ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#DGX Spark`, `#robotics`, `#AI agents`, `#simulation`

---

<a id="item-26"></a>
## [波兰创业生态蓬勃发展，ElevenLabs 处于核心](https://twitter.com/lukas_m_ziegler/status/2061738832140091703) ⭐️ 4.0/10

Lukas Ziegler 在参加华沙的 ElevenLabs 峰会后发推称，波兰创业生态蓬勃发展，ElevenLabs 处于核心位置。 这凸显了波兰作为欧洲主要科技中心（尤其在 AI 领域）的崛起，并强调了 ElevenLabs 在推动 AI 实际应用中的影响力。 推文指出，波兰已悄然成为最适合创业的地方之一，而峰会则像是 AI 快速融入实体经济的缩影。

twitter · lukas_m_ziegler · Jun 2, 09:16

**背景**: 波兰的创业生态已显著成熟，风投基础设施不断增长，AI 创业公司激增。ElevenLabs 以其逼真的 AI 语音技术闻名，是该领域的关键参与者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://elevenlabs.io/">ElevenLabs</a></li>
<li><a href="https://therecursive.com/poland-startup-ecosystem-investors-startups-scaleups-update-2025/">Poland ’s Startup Ecosystem in 2025 Is No More Early-Stage Hub</a></li>
<li><a href="https://startupuniversal.com/country/poland/">Startup Universal | Poland Startup Ecosystem Country Guide</a></li>

</ul>
</details>

**标签**: `#startup ecosystem`, `#Poland`, `#ElevenLabs`, `#AI`

---

<a id="item-27"></a>
## [ClaudeDevs 将触发词改为 'ultracode'](https://twitter.com/ClaudeDevs/status/2062257177788858398) ⭐️ 4.0/10

ClaudeDevs 将触发词从 'workflow' 改为 'ultracode'，以避免动态工作流被意外激活。 这一微小的用户体验调整减少了 ClaudeDevs 用户的误触发，提高了工具的可靠性和使用体验。 用户仍然可以使用自然语言 'use a workflow for this'，但必须明确说出 'ultracode' 才能触发动态工作流。

twitter · ClaudeDevs · Jun 3, 19:36

**背景**: ClaudeDevs 是 Claude Code 的调试工具，可读取会话日志并重构工具调用。动态工作流允许编排多个子代理，触发词的更改旨在避免意外调用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude-dev.tools/">claude-devtools — Your Claude is coding blind</a></li>
<li><a href="https://blog.laozhang.ai/en/posts/claude-code-ultracode">Claude Code Ultracode : What It Does, When to... | LaoZhang AI Blog</a></li>
<li><a href="https://developertoolkit.ai/en/claude-code/advanced-techniques/dynamic-workflows/">Dynamic Workflows & ultracode | Developer Toolkit</a></li>

</ul>
</details>

**标签**: `#AI tools`, `#UX`, `#ClaudeDevs`

---

<a id="item-28"></a>
## [NVIDIA RTX Spark：1 Petaflop AI 笔记本电脑，128GB 内存](https://twitter.com/RodmanAi/status/2061849768876466210) ⭐️ 4.0/10

@RodmanAi 的一条推文吹捧 NVIDIA 的 RTX Spark 是一款革命性的笔记本电脑，具有 1 Petaflop 的本地 AI 算力、128GB 统一内存和 RTX 5070 级别图形，声称它从根本上改变了笔记本电脑的形态。 如果属实，这将使在笔记本电脑上本地运行大规模 AI 模型（高达 1200 亿参数）成为可能，消除对云连接的需求，并改变移动设备上的 AI 开发和创意工作流程。 RTX Spark 超级芯片将 20 核 Arm 架构的 Grace CPU 与 Blackwell RTX GPU 以及高达 128GB 的 LPDDR5X 统一内存相结合，提供 1 Petaflop 的 FP4 AI 性能。它由 NVIDIA 和微软于 2026 年 5 月 31 日正式发布，用于 Windows on Arm 设备。

twitter · RodmanAi · Jun 2, 16:37

**背景**: 传统笔记本电脑使用独立的 CPU 和 GPU 芯片，共享内存有限，限制了 AI 工作负载。NVIDIA 的 RTX Spark 将 CPU、GPU 和统一内存集成在单个芯片上，类似于 Apple 的 M 系列，但具有 NVIDIA 的 AI 加速和 RTX 图形能力。这使得无需依赖云即可本地运行大型语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_RTX_Spark">Nvidia RTX Spark</a></li>
<li><a href="https://www.nvidia.com/en-us/products/rtx-spark/">NVIDIA RTX Spark — Slim Laptops & Small Desktops</a></li>
<li><a href="https://thors-terminal-briefings.ghost.io/the-2026-06-01-intel/">Nvidia Puts Petaflop AI In Laptops.</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#laptop`, `#AI`, `#hardware`

---

<a id="item-29"></a>
## [免费使用 Codex 和 Hermes Agent 的指南](https://twitter.com/tech_shrimp/status/2062327316198703123) ⭐️ 3.0/10

@tech_shrimp 发布推文，推广一份声称能长期免费使用 Codex 和 Hermes 等 Agent 工具 API 的指南，让用户无需付费即可体验前沿的 Agent 能力。 如果该指南确实有效，它将降低使用强大 AI 编程 Agent（Codex）和自改进个人 Agent（Hermes）的门槛，使开发者和爱好者更容易体验 Agent AI。 推文包含指南链接，但未提供技术细节。Codex 是 OpenAI 的 AI 编程 Agent，Hermes 是 Nous Research 的开源自改进 Agent。

twitter · tech_shrimp · Jun 4, 00:15

**背景**: Codex 是 OpenAI 开发的 AI 编程 Agent，于 2025 年 4 月以 Codex CLI 形式发布，能够编写代码和修复 Bug。Hermes Agent 是 Nous Research 开发的开源自改进 AI Agent，可在自有服务器上运行，能记住历史交互并支持多种 LLM 提供商。这两款工具通常需要付费 API 访问或订阅。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://github.com/nousresearch/hermes-agent">GitHub - NousResearch/hermes-agent: The agent that grows with ...</a></li>

</ul>
</details>

**标签**: `#API`, `#Agent`, `#Free`, `#Guide`

---

<a id="item-30"></a>
## [ICRA 上惊现“机器人手界的兰博基尼”](https://twitter.com/lukas_m_ziegler/status/2062136369728602413) ⭐️ 3.0/10

用户@lukas_m_ziegler 在推特上提到，在 ICRA 机器人会议上发现了一款来自 Wuji Global 的视觉上引人注目的机器人手，并将其比作兰博基尼。 这一观察引起了人们对美观设计和高性能机器人手这一趋势的关注，可能预示着机器人技术正朝着更亲民、更具视觉吸引力的方向发展。 这款机器人手来自中国初创公司 Wuji Global，采用仿生设计，拥有五根手指，每根手指有 4 个自由度，重量低于 600 克，指尖力可达 15N。

twitter · lukas_m_ziegler · Jun 3, 11:36

**背景**: ICRA（IEEE 国际机器人与自动化会议）是展示前沿研究和产品的顶级机器人会议。Wuji Global 的机器人手因其流畅的仿生控制和耐用性而受到关注，有人称其为“特斯拉 Optimus 手部杀手”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/joeyjooste_breaking-a-chinese-startup-just-dropped-activity-7374513025506074624-z8Nz">BREAKING: A Chinese startup just dropped a robot hand that makes...</a></li>
<li><a href="https://2026.ieee-icra.org/">2026 IEEE International Conference on Robotics and Automation...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#robot hand`, `#ICRA`

---

<a id="item-31"></a>
## [SpaceX 从加州发射 24 颗星链卫星](https://twitter.com/SpaceX/status/2062195212026261682) ⭐️ 3.0/10

SpaceX 在加州使用猎鹰 9 号火箭发射了 24 颗星链卫星，并确认部署成功。 此次发射扩大了星链星座，增强了全球宽带覆盖范围，并降低了全球用户的延迟。 猎鹰 9 号第一级可能按惯例在无人船上着陆。未提供更多技术细节。

twitter · SpaceX · Jun 3, 15:30

**背景**: 星链是由 SpaceX 运营的卫星互联网星座，为服务不足的地区提供低延迟宽带互联网。猎鹰 9 号是一种可重复使用的两级火箭，已成为 SpaceX 发射的主力。

**标签**: `#SpaceX`, `#Starlink`, `#satellite launch`

---

<a id="item-32"></a>
## [Yann LeCun 推广 NYU AI Frontier Lab 活动](https://twitter.com/ylecun/status/2061838888935514152) ⭐️ 3.0/10

Yann LeCun 转发了 @kchonyc 的邀请，参加由 @c10labs、纽约大学和纽约市经济发展公司联合主办的 NYU Global AI Frontier Lab 活动，旨在连接学术界与产业界。 该活动凸显了促进人工智能学术研究与产业应用之间合作的持续努力，这对于将突破性成果转化为实际影响至关重要。 该活动由 @c10labs、纽约大学和纽约市经济发展公司组织，计划在下午举行。推文中未提供具体日期、议程或演讲者信息。

twitter · ylecun · Jun 2, 15:54

**标签**: `#AI`, `#event`, `#NYU`

---

<a id="item-33"></a>
## [Sergey Levine 将在 CVPR 2026 ScaleBot 研讨会发表演讲](https://twitter.com/berkeley_ai/status/2062357907413570016) ⭐️ 2.0/10

Sergey Levine 通过 Twitter 宣布，他将于 2026 年 6 月 4 日下午 1:30 在 CVPR 2026 的 ScaleBot 研讨会上发表演讲，地点为 610/612 房间。 此次演讲凸显了计算机视觉与机器人技术日益融合的趋势，特别是在可扩展机器人学习系统方面，这对通用机器人发展至关重要。 该演讲是首届 ScaleBot 研讨会的一部分，该研讨会专注于可扩展机器人学习系统，汇聚了计算机视觉、自然语言处理和机器人领域的研究人员。

twitter · berkeley_ai · Jun 4, 02:16

**背景**: CVPR 是计算机视觉领域的顶级会议。ScaleBot 研讨会于 2026 年首次举办，旨在解决构建可扩展至通用机器人的学习系统所面临的挑战，融合了多个 AI 子领域的见解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scalebot-workshop.github.io/">ScaleBot @ CVPR 2026</a></li>
<li><a href="https://openreview.net/group?id=thecvf.com/CVPR/2026/Workshop/ScaleBot">CVPR 2026 Workshop ScaleBot | OpenReview</a></li>
<li><a href="https://x.com/XihuiLiu/status/2018883157551182164">Trilled to announce our ScaleBot workshop in CVPR 2026!</a></li>

</ul>
</details>

**标签**: `#CVPR`, `#talk`, `#robotics`

---