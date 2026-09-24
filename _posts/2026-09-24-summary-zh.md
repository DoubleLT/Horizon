---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24
lang: zh
---

> From 37 items, 34 important content pieces were selected

---

1. [2.3B MoE 混合 Mamba-2 模型以不到 1% 算力媲美 Llama-3.2-3B](#item-1) ⭐️ 8.0/10
2. [Cognex 以 5 亿美元收购 RealSense，距其从 Intel 分拆仅 439 天](#item-2) ⭐️ 7.0/10
3. [斯坦福 AI 实验室论文实现无需重训练的机器人基础模型引导](#item-3) ⭐️ 7.0/10
4. [Anthropic 用 Claude 让 claude.ai 在两周内提速 3 倍](#item-4) ⭐️ 7.0/10
5. [Anthropic 的 ClaudeDevs 分享 Opus 5.5 首次使用技巧](#item-5) ⭐️ 7.0/10
6. [研究者质疑 Astra 发布后纯研究型机器人实验室的价值](#item-6) ⭐️ 6.0/10
7. [SpaceX 计划在星舰第 14 次飞行前进行全栈测试](#item-7) ⭐️ 6.0/10
8. [Yann LeCun 转发 NYU 纳维-斯托克斯研究者 Tristan Buckmaster 的讲座消息](#item-8) ⭐️ 6.0/10
9. [MotionJEPA 解决 JEPA 世界模型的慢特征偏差](#item-9) ⭐️ 6.0/10
10. [LeCun 转发每周必读 AI 论文：JEPA-Anything 与 ModAR](#item-10) ⭐️ 6.0/10
11. [斯坦福 AI 实验室转发纳维-斯托克斯突破及其对 AI 智能体的影响](#item-11) ⭐️ 6.0/10
12. [斯坦福 AI 实验室发布 Matryoshka Attribution 模型归因新方法](#item-12) ⭐️ 6.0/10
13. [斯坦福 AI 实验室推出面向 VLA 策略的实时 EXPO-FT](#item-13) ⭐️ 6.0/10
14. [研究发现单个注意力头在五类上下文学习任务中均至关重要](#item-14) ⭐️ 6.0/10
15. [SpaceX 计划最早 10 月 1 日发射猎鹰 9 号执行 Crew-13 任务](#item-15) ⭐️ 5.0/10
16. [Chelsea Finn 提出基于 EXPO-FT 的延迟感知强化学习方法](#item-16) ⭐️ 5.0/10
17. [李飞飞：AI 的目标应是改善人类生活与社会](#item-17) ⭐️ 4.0/10
18. [物理 AI 快速进展引发线下峰会价值讨论](#item-18) ⭐️ 4.0/10
19. [社区维护的 Robotiq 夹爪驱动获赞，支持 ROS 2 与 Isaac Sim](#item-19) ⭐️ 4.0/10
20. [Perplexity 推出面向早期职业人才的研究奖学金](#item-20) ⭐️ 4.0/10
21. [Anthropic 澄清 Claude Code 云会话在 Pro 和 Max 套餐上的计费方式](#item-21) ⭐️ 4.0/10
22. [推特帖子列出 10 个免费 GitHub 仓库，涵盖 Python 与 AI 学习路径](#item-22) ⭐️ 4.0/10
23. [推特热帖盘点 10 个免费开源 GitHub 仓库，含 Archify 与 OpenMAIC](#item-23) ⭐️ 4.0/10
24. [Adam 宣布与 Rhino 3D 直接集成](#item-24) ⭐️ 3.0/10
25. [LeCun 转发 Hugging Face CEO 受邀在联合国安理会发言](#item-25) ⭐️ 3.0/10
26. [Yann LeCun 在 NYU CILVR 研讨会开幕演讲中谈世界模型](#item-26) ⭐️ 3.0/10
27. [LeCun 转发 ICWM 会议单盲评审与开放参与政策](#item-27) ⭐️ 3.0/10
28. [斯坦福 AI 实验室分享从数据中恢复特征的研究项目](#item-28) ⭐️ 3.0/10
29. [加州大学伯克利分校招募计算健康科学博士后](#item-29) ⭐️ 3.0/10
30. [推特帖子列出 12 个 AI 智能体必备 JEV 技能](#item-30) ⭐️ 3.0/10
31. [MecAgent 宣传 Copilot V2.0.0 搭配虚构的 GPT-6 Astra 与 SolidWorks 2026](#item-31) ⭐️ 2.0/10
32. [Yann LeCun 转发 ICWM 研讨会推广，截止日期约两个月后](#item-32) ⭐️ 2.0/10
33. [吴恩达转发马斯克含糊评论「有趣的观点」](#item-33) ⭐️ 2.0/10
34. [幽默推文调侃英格兰足球历史](#item-34) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [2.3B MoE 混合 Mamba-2 模型以不到 1% 算力媲美 Llama-3.2-3B](https://twitter.com/berkeley_ai/status/2102805420461171158) ⭐️ 8.0/10

研究人员预训练了一个 2.3B 参数的混合专家（MoE）模型，仅激活 360M 参数，采用混合 Mamba-2 架构，性能与 Llama-3.2-3B 仅相差几个百分点，而预训练算力消耗不到后者的 1%。 这一结果表明，将 MoE 稀疏性与混合状态空间/注意力架构结合，可以大幅降低预训练成本，有望让构建有竞争力的语言模型变得便宜得多，从而让小型研究团队也能参与其中。 该模型采用混合 Mamba-2 设计，将状态空间模型模块与注意力机制交错堆叠，其 MoE 层每个 token 仅激活 2.3B 总参数中的 360M，这解释了低算力消耗的原因；该结论仅基于预训练算力，不涉及推理或微调成本。

twitter · berkeley_ai · Sep 23, 17:00

**背景**: 混合专家（MoE）模型用多个“专家”子网络和一个路由器替代稠密前馈层，每个输入只激活少数专家，从而在保持总参数量较大的同时降低实际计算量。Mamba-2 是一种以线性时间处理序列的状态空间模型架构，混合设计将 Mamba-2 模块与 Transformer 注意力交错堆叠，兼顾高效长序列建模与强召回能力。Llama-3.2-3B 是 Meta 发布的稠密 30 亿参数开源模型，在此作为性能基线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mamba_(deep_learning_architecture)">Mamba (deep learning architecture) - Wikipedia</a></li>
<li><a href="https://docs.nvidia.com/nemo-framework/user-guide/24.07/llms/mamba/index.html">Mamba2 and Hybrid Models — NVIDIA NeMo Framework User Guide</a></li>

</ul>
</details>

**社区讨论**: 该内容是一条转发，讨论有限，但 77 次转发表明 AI/ML 社区对其效率提升和架构创新有浓厚兴趣。

**标签**: `#MoE`, `#Mamba-2`, `#efficient-training`, `#language-models`, `#AI-research`

---

<a id="item-2"></a>
## [Cognex 以 5 亿美元收购 RealSense，距其从 Intel 分拆仅 439 天](https://twitter.com/lukas_m_ziegler/status/2102473989897503154) ⭐️ 7.0/10

据@lukas_m_ziegler 报道，Cognex 公司将以 5 亿美元收购 RealSense。这笔交易距离 RealSense 从 Intel 分拆成为独立公司仅 439 天，期间 CEO Nadav Orbach 在库比蒂诺、北京和海法设立了办公室。 此次收购整合了机器视觉和深度传感领域的两大重要参与者，可能重塑工业自动化、机器人及物理 AI 的供应链格局。这表明随着人形机器人和自主移动机器人日益普及，深度传感技术正成为工业视觉领导者的核心战略资产。 5 亿美元的收购价对 RealSense 的投资方而言意味着可观回报——一年多前，Intel Capital 和联发科才在分拆时投入了 5000 万美元。RealSense 的立体 3D 摄像头和软件被定位为物理 AI 的感知平台，尤其面向人形机器人和自主移动机器人。

twitter · lukas_m_ziegler · Sep 22, 19:03

**背景**: RealSense 在 Intel 内部孵化了十多年，开发用于机器人、门禁控制、工业自动化和医疗保健的深度摄像头及计算机视觉系统。2025 年，Intel 完成 RealSense 的分拆，使其成为独立公司，并从 Intel Capital 和联发科获得 5000 万美元融资，同时宣布与 NVIDIA 战略合作以加速物理 AI 和机器人技术。Cognex 是全球领先的工业自动化机器视觉解决方案提供商，提供视觉软件、条码扫描器和视觉引导机器人系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RealSense">RealSense - Wikipedia</a></li>
<li><a href="https://www.cognex.com/">Cognex | Machine Vision & Industrial Barcode Solutions</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lRMklYU0RoSDJpcnFNY19hUnhTZ0FQAQ?hl=en-US&gl=US&ceid=US:en">Google News - Intel spins off RealSense , an AI robotics company...</a></li>

</ul>
</details>

**社区讨论**: 该推文获得中等程度的互动，88 个点赞和 10 条回复，表明社区有关注但未形成病毒式讨论。帖子内容简短、缺乏深度分析，但收购本身的速度和估值值得关注。

**标签**: `#acquisition`, `#computer-vision`, `#depth-sensing`, `#Intel`, `#Cognex`

---

<a id="item-3"></a>
## [斯坦福 AI 实验室论文实现无需重训练的机器人基础模型引导](https://twitter.com/StanfordAILab/status/2102627428074209384) ⭐️ 7.0/10

斯坦福 AI 实验室（Stanford AI Lab）发布的一篇新论文（由研究员 Marco Pavone 分享）探讨了能否在不重新训练的情况下引导机器人基础模型，并借鉴了控制理论的思路。该工作提出了一种推理时行为引导方法，通过三阶段流程调整机器人策略，而无需对底层模型进行微调。 重新训练或微调大型机器人基础模型成本高昂且耗时，因此一种能在推理阶段引导行为的方法可以让通用机器人策略更具适应性、部署也更安全。这对基于 OpenVLA、Octo 等模型开展研究的机器人学者和企业尤为重要，因为他们需要快速改变行为，而不必经历昂贵的重训练周期。 该方法被描述为一个三阶段的推理时行为引导流程，无需重新训练，并借鉴控制理论的概念来调节模型输出。该成果来自斯坦福 Marco Pavone 团队，他们近期的研究还包括用于鲁棒策略评估的视频世界模型引导。

twitter · StanfordAILab · Sep 23, 05:13

**背景**: 机器人基础模型是大型预训练神经网络，能够融合视觉、语言及其他传感器输入，从而在多种任务中控制机器人，代表性例子包括 OpenVLA、Octo 和π0。由于这些模型基于海量数据训练，要让它们适应新行为通常需要微调或重训练，成本很高。而控制理论提供了将动力系统引导至期望行为的数学工具，这篇论文将两者结合，用控制启发的思路在推理阶段引导机器人基础模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/drmapavone/status/2102592146478088698">Marco Pavone on X: "Can we steer a robot foundation model without ...</a></li>
<li><a href="https://arxiv.org/html/2606.26588v1">Inference-Time Robot Behavior Steering through Physically-Aware ...</a></li>
<li><a href="https://robotics-fm-survey.github.io/">Towards General-Purpose Robots via Foundation Models: A Survey and Meta-Analysis</a></li>

</ul>
</details>

**标签**: `#robotics`, `#foundation-models`, `#control-theory`, `#AI-research`, `#model-steering`

---

<a id="item-4"></a>
## [Anthropic 用 Claude 让 claude.ai 在两周内提速 3 倍](https://twitter.com/ClaudeDevs/status/2102839691154427983) ⭐️ 7.0/10

Anthropic 的 ClaudeDevs 团队宣布，他们在短短两周内让 claude.ai 的速度提升了 3 倍，整个过程使用 Claude 自身来测量、调试和优化性能，并公开了所用的提示词和方法。 这展示了一个在大型生产级 Web 应用上由 AI 辅助完成性能工程的具体且高价值的案例，公开的提示词也为其他开发者提供了可复用的提速方法。 根据配套的博客文章，团队并行运行了由 Claude 驱动的优化线程，每个线程会生成数十个优化 PR，有时单个线程就有五十到一百个，而不是在第一次修复后就停止。

twitter · ClaudeDevs · Sep 23, 19:17

**背景**: claude.ai 是 Anthropic 面向消费者的 Claude 模型聊天界面，网页性能（页面加载、响应速度）直接影响其使用体验。像 Claude Code 这样的 AI 编程助手可以阅读代码库、提出修改并提交 PR，因此很适合用于迭代式的性能优化。推文篇幅有限，真正的技术方法在链接的博客文章中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.dev/blog/how-we-made-claude-ai-faster/">How we made claude.ai 3x faster in two weeks / claude.dev</a></li>
<li><a href="https://claude.com/blog/optimize-code-performance-quickly">Optimize code performance quickly | Claude by Anthropic</a></li>

</ul>
</details>

**社区讨论**: 该公告获得了很高的互动量（约 6767 个点赞、369 次转发和 165 条回复），说明社区兴趣浓厚并认可这一成果，不过推文本身的技术深度有限。

**标签**: `#performance-optimization`, `#claude`, `#ai-assisted-development`, `#web-performance`, `#anthropic`

---

<a id="item-5"></a>
## [Anthropic 的 ClaudeDevs 分享 Opus 5.5 首次使用技巧](https://twitter.com/ClaudeDevs/status/2102491840612380934) ⭐️ 7.0/10

官方账号 @ClaudeDevs 发布了一条简短的技巧帖，指导用户在首次使用 Claude Opus 5.5 时如何操作：把完整任务交给模型并明确“完成”的标准和检查节点；不要再写“think carefully”，因为模型总会先进行推理；在长时间运行后主动询问模型还需要什么才能继续推进。帖子附带了 Anthropic 的使用手册链接，并迅速获得大量关注，点赞超过 1.4 万、转发 974 次、回复 222 条。 Opus 5.5 是 Anthropic 在公开呼吁“放缓前沿模型发展节奏”之后发布的首个模型，它在大多数任务上达到 Claude Fable 5.1 的水平，而运行成本比 Opus 5 低 40%，因此这些使用技巧能帮助开发者和团队更好地利用这个更便宜、更强大的模型。这些建议也反映出提示词实践的变化：对于默认就会推理的模型，用户应把重点放在任务定义和委派上，而不是反复要求模型“仔细思考”。 这些技巧强调 Opus 5.5 总是会先进行推理，因此无需再明确要求它“仔细思考”；同时，长时间运行的会话适合定期检查模型还需要什么才能继续推进。Anthropic 表示，Opus 5.5 是其自动化行为审计中表现最强的模型，并在发布前由 Frontier Design、METR 等外部评估方测试，在生物和网络安全方面采用了与 Fable 5.1 类似的防护措施。

twitter · ClaudeDevs · Sep 22, 20:14

**背景**: Claude Opus 5.5 是 Anthropic 全新 Claude 5.5 系列的首个模型，被定位为相较 Opus 5 的重大升级，在性能与安全性上都有提升。它可通过 Amazon Bedrock、Azure、Google Vertex、AWS 上的 Claude Platform 以及 Anthropic 自身等多个渠道使用；Anthropic 还在降价的同时提高了 Pro、Max 和 Team 套餐的五小时使用限额。@ClaudeDevs 是 Anthropic 面向开发者的官方账号，用于分享 Claude 模型的使用指导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude-opus-5-5">Introducing Claude Opus 5 . 5 \ Anthropic</a></li>
<li><a href="https://9to5mac.com/2026/09/22/anthropic-upgrades-claude-with-new-opus-5-5-model-details-here/">Anthropic upgrades Claude with new Opus 5 . 5 model ... - 9to5Mac</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5.5">Claude Opus 5 . 5 - API Pricing & Providers | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 该帖互动量很高，点赞超过 1.4 万、转发 974 次、回复 222 条，显示出社区对新模型及其推荐工作流的浓厚兴趣。讨论主要围绕如何针对默认就会推理的模型调整提示习惯，用户们分享了自己首次使用的体验和任务委派策略。

**标签**: `#Claude`, `#Opus 5.5`, `#AI model`, `#usage tips`, `#Anthropic`

---

<a id="item-6"></a>
## [研究者质疑 Astra 发布后纯研究型机器人实验室的价值](https://twitter.com/lukas_m_ziegler/status/2102743118969770077) ⭐️ 6.0/10

研究者 Lukas Ziegler 在 X 上发帖，质疑在 Astra 这一新前沿 AI 模型发布后，纯研究型机器人实验室将如何创造价值。他认为，如果前沿实验室持续提供更好的现成通用智能，那么从零开始训练机器人自己的“大脑”将不再是一种竞争优势。 这为机器人研究界提出了一个战略性问题：如果通用智能变成可以现成获取的商品，那么只专注于自研模型的实验室可能会失去差异化优势。这可能促使实验室转向专攻硬件、数据或细分应用，而非模型训练。 这条推文属于推测性评论，并未提供详细分析，但它是在 Astra 发布后发出的，并获得了中等程度的互动（82 个赞，28 条回复）。其核心论点是，价值将从从零开始的模型训练转向机器人技术栈的其他环节。

twitter · lukas_m_ziegler · Sep 23, 12:53

**背景**: Astra 指的是近期发布的前沿 AI 成果，根据搜索结果，它既包括 Apptronik 的人形机器人原型，也包括 OpenAI 的 GPT-6 Astra 模型。前沿实验室是指处于 AI 开发最前沿的组织，如 OpenAI 和 Google DeepMind，它们会发布强大的通用模型。纯研究型机器人实验室传统上会从零开始训练自己的控制或感知模型，但现成的通用智能可能使这种做法变得不再必要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence - OpenAI</a></li>
<li><a href="https://humanoid.guide/welcome-astra-humanoid-robot-by-apptronik/">Welcome, Astra Humanoid Robot by Apptronik! - Humanoid.guide</a></li>
<li><a href="https://ideas.fin.ai/p/general-intelligence-isnt-the-bottleneck">General intelligence isn’t the bottleneck</a></li>

</ul>
</details>

**社区讨论**: 这条推文获得了 82 个赞和 28 条回复，表明社区有一定兴趣，但所提供的内容并未包含具体的评论线程或情绪细节。

**标签**: `#robotics`, `#AI research`, `#foundation models`, `#research strategy`, `#industry trends`

---

<a id="item-7"></a>
## [SpaceX 计划在星舰第 14 次飞行前进行全栈测试](https://twitter.com/SpaceX/status/2102899767403851945) ⭐️ 6.0/10

SpaceX 宣布计划在星舰第 14 次飞行前于 Starbase 进行机会性全栈测试，发射目标定于 9 月 28 日星期一，尚待监管批准。Ship 41 已被移至发射台，堆叠工作正在进行中。 第 14 次飞行预计将是星舰的首次运营飞行，包括该系统首次运营性 Starlink 部署以及首次尝试进入持续轨道。成功的全栈测试将在此里程碑前验证整合后的飞行器，标志着星舰迈向常规商业运营的重要一步。 此次全栈测试被描述为“机会性”的，意味着它取决于硬件准备情况和时间安排。根据搜索结果，第 14 次飞行中飞船和助推器均不计划被捕获，而是预计执行溅落。

twitter · SpaceX · Sep 23, 23:15

**背景**: 星舰是 SpaceX 正在研发的两级完全可重复使用超重型运载火箭，由 Super Heavy 助推器和星舰上面级组成。位于德克萨斯州博卡奇卡的 Starbase 是 SpaceX 星舰的主要测试、生产和发射设施。“全栈”指飞船安装在助推器顶部的完整飞行器，每次飞行前都会进行整合测试以验证各系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starship_flight_14">Starship flight 14</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Starbase_spacex">Starbase spacex</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starship`, `#aerospace`, `#launch`, `#rocket-testing`

---

<a id="item-8"></a>
## [Yann LeCun 转发 NYU 纳维-斯托克斯研究者 Tristan Buckmaster 的讲座消息](https://twitter.com/ylecun/status/2102936941280821634) ⭐️ 6.0/10

Yann LeCun 转发了 Gautam Kamath 的一条推文，内容提到 NYU Courant 教授 Tristan Buckmaster——因近期纳维-斯托克斯争议而知名——在 NYU 新举办的 Mathematics in the Atmosphere 活动上做了一场讲座。 Buckmaster 是 2026 年 9 月围绕“谁最先解决纳维-斯托克斯存在性与光滑性问题”争议的核心人物，因此他的公开露面会受到数学家和 AI 研究者的共同关注。 这条推文本身只是一次转发，几乎没有提供上下文；讲座是在 NYU 新设立的 Mathematics in the Atmosphere 系列活动中进行的，推文中并未分享讲座的技术内容。

twitter · ylecun · Sep 24, 01:43

**背景**: 纳维-斯托克斯存在性与光滑性问题问的是：描述流体运动的方程在三维空间中是否总有光滑解，它是克莱数学研究所七道千禧年大奖难题之一。2026 年 9 月，OpenAI 声称用约一万个 AI 智能体组成集群解决了该问题的一个版本，但随即爆发了优先权争议，涉及 Anthropic 的数学家 Levent Alpöge 以及此前在欧拉方程上得出密切相关结果的 Tristan Buckmaster。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness">Navier-Stokes existence and smoothness</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_priority_controversy">Navier – Stokes priority controversy - Wikipedia</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/991710/openai-navier-stokes-solution">Drama swirls around OpenAI’s legendary mathematical... | The Verge</a></li>

</ul>
</details>

**标签**: `#Navier-Stokes`, `#mathematics`, `#fluid dynamics`, `#academia`, `#Twitter`

---

<a id="item-9"></a>
## [MotionJEPA 解决 JEPA 世界模型的慢特征偏差](https://twitter.com/ylecun/status/2102935861243625476) ⭐️ 6.0/10

Yann LeCun 转发了 MotionJEPA 的发布，该模型由 Markus Karmann 与 12 位合著者提出，旨在克服 JEPA 风格世界模型偏向学习缓慢、简单特征的倾向。配套的 arXiv 论文（2609.23881）标题为《MotionJEPA: Preventing Temporal Feature Collapse by Capturing Visual Changes in Latent Space》。 JEPA 风格世界模型是从原始像素学习预测性表征的核心研究方向，而偏向缓慢、简单特征的偏差会限制其捕捉运动等快速动态的能力。如果 MotionJEPA 能成功防止这种时序特征坍缩，就可能提升视频理解、机器人学和具身智能中的表征质量；而作为 JEPA 主要倡导者的 LeCun 转发该工作，也使其更受关注。 论文将问题定义为“时序特征坍缩”，即潜在表征收敛到变化缓慢、复杂度低的信号，而忽略快速的视觉变化。该方法明确针对潜在空间中的视觉变化，并发布了 Hugging Face Space（MotionJEPA-representation-view）用于查看学习到的表征。

twitter · ylecun · Sep 24, 01:39

**背景**: JEPA（联合嵌入预测架构）由 Yann LeCun 倡导，是一种自监督方法，它在潜在空间中预测未来观测的表征，而不是重建原始像素。以此构建的世界模型可以学习环境动态，被视为通向规划与具身智能的路径。表征学习中的一个已知问题是，模型会偏向简单、常见或缓慢变化的特征，从而可能抑制关于运动等快速变化事件的信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.23881">[2609.23881] MotionJEPA : Preventing Temporal Feature Collapse by...</a></li>
<li><a href="https://huggingface.co/spaces/HongzeFu/MotionJEPA-representation-view">MotionJEPA Representation View - a Hugging Face Space by...</a></li>
<li><a href="https://arxiv.org/pdf/2405.05847">Learned feature representations are biased by complexity</a></li>

</ul>
</details>

**标签**: `#JEPA`, `#world models`, `#MotionJEPA`, `#representation learning`, `#AI research`

---

<a id="item-10"></a>
## [LeCun 转发每周必读 AI 论文：JEPA-Anything 与 ModAR](https://twitter.com/ylecun/status/2102443742204469550) ⭐️ 6.0/10

Yann LeCun 转发了 The Turing Post 的每周必读 AI 论文汇总，其中重点介绍了 JEPA-Anything 和 Modality-Autoregressive World-Action Models（ModAR），以及一篇关于上下文机器人学习的论文。该推文获得了中等程度的互动（77 次转发），但没有可见的讨论。 LeCun 的背书表明这些论文与他长期倡导的世界模型和非生成式预测架构方向一致，可能引导研究关注转向 JEPA 类方法。ModAR 和上下文机器人学习的入选，说明将世界建模与动作预测统一用于机器人领域正获得越来越多的关注。 JEPA-Anything 通过正交预测分解（Orthogonal Predictive Factorization）扩展了联合嵌入预测架构，构建跨视觉、生物学、临床数据、物理、分子和天气的因子化世界模型。ModAR 被描述为首个在预测动作之前对多种未来模态进行自回归去噪的世界-动作模型，而非将未来预测为 RGB 图像。

twitter · ylecun · Sep 22, 17:03

**背景**: JEPA（联合嵌入预测架构）是一种自监督学习框架，它预测输入的抽象表示（嵌入），而不是重建原始像素或生成 token，这是 Yann LeCun 世界模型愿景中的核心思想。世界-动作模型（WAM）联合建模未来观测和动作，通常将未来帧预测为图像，而 ModAR 旨在通过自回归处理多种模态来改进这一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2609.20800">JEPA - Anything : Learning Predictive Models across... | alphaXiv</a></li>
<li><a href="https://arxiv.org/html/2609.17524v1">Modality-Autoregressive World-Action Models - arXiv</a></li>
<li><a href="https://www.turingpost.com/p/jepa">JEPA : Joint Embedding Predictive Architecture Explained</a></li>

</ul>
</details>

**标签**: `#AI research`, `#paper recommendations`, `#JEPA`, `#world models`, `#Yann LeCun`

---

<a id="item-11"></a>
## [斯坦福 AI 实验室转发纳维-斯托克斯突破及其对 AI 智能体的影响](https://twitter.com/StanfordAILab/status/2102830363563422130) ⭐️ 6.0/10

斯坦福 AI 实验室转发了 Aneesh Pappu 的一条帖子，指出最近纳维-斯托克斯方程的一项突破引发了广泛关注，人们开始探讨 AI 智能体由此涌现的新可能性。该推文本身并未提供技术细节，主要起到指向数学与 AI 交叉领域更广泛讨论的作用。 纳维-斯托克斯方程是数学领域最重要的未解难题之一，任何声称的突破都会受到数学家和 AI 研究者的严格审视。如果 AI 智能体在此类成果中发挥了作用，将进一步证明 AI 系统能够对前沿数学研究做出实质性贡献。 该推文是一条内容极简的转发，没有说明突破的具体性质、所使用的方法或涉及哪些研究者。纳维-斯托克斯方程描述黏性流体运动，与 100 万美元的千禧年大奖难题相关，因此任何声称的进展在被接受前都需要经过严格的同行评审。

twitter · StanfordAILab · Sep 23, 18:40

**背景**: 纳维-斯托克斯方程是由克劳德-路易·纳维和乔治·加布里埃尔·斯托克斯在 1822 年至 1850 年间逐步建立的偏微分方程组，用于描述黏性流体的运动，从机翼上的气流到洋流皆在其列。证明三维情况下光滑解是否始终存在，是七个千禧年大奖难题之一，克雷数学研究所为此悬赏 100 万美元。另一方面，AI 智能体——能够规划并执行多步任务的自主系统——近来被应用于数学问题求解，有时会发现证明检验软件中的漏洞，而非给出真正的证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_equations">Navier – Stokes equations - Wikipedia</a></li>
<li><a href="https://www.lms.ac.uk/news/navier-stokes-equations-breakthrough">Navier - Stokes Equations Breakthrough | London Mathematical Society</a></li>
<li><a href="https://techxplore.com/news/2026-09-ai-agents-math-problems.html">When AI agents cheat on math problems, others blow the whistle</a></li>

</ul>
</details>

**社区讨论**: 该转发获得了约 114 次转发的中等互动量，表明 AI 与数学社区对此有一定兴趣，但现有内容中没有实质性的回复或详细辩论。根据所提供材料，无法总结出明确的共识或反驳观点。

**标签**: `#Navier-Stokes`, `#AI`, `#breakthrough`, `#mathematics`, `#agents`

---

<a id="item-12"></a>
## [斯坦福 AI 实验室发布 Matryoshka Attribution 模型归因新方法](https://twitter.com/StanfordAILab/status/2102830122219008045) ⭐️ 6.0/10

斯坦福 AI 实验室转发了一篇由 Aryaman Arora 撰写的新论文，介绍了 Matryoshka Attribution 方法，该方法利用梯度下降来识别神经网络中哪些部分对输出有贡献。该消息在 X 平台上发布，推文本身的技术细节较为有限。 归因方法是可解释性研究的核心，能帮助研究人员和从业者理解并信任模型行为。来自斯坦福等知名实验室的基于梯度下降的方法，可能为现有的特征归因和数据归因技术提供新视角，但其实际影响仍有待验证。 推文仅提供了简短描述，指出该方法使用梯度下降来找出神经网络中与特定输出相关的部分。'Matryoshka'（套娃）这一名称暗示了嵌套的层次结构，但推文并未说明具体机制、基准测试或局限性。

twitter · StanfordAILab · Sep 23, 18:39

**背景**: 机器学习中的归因指的是评估哪些输入特征、训练数据或内部组件对模型输出负责，这是可解释 AI 的核心关注点。梯度下降是通过迭代最小化损失函数来训练神经网络的标准优化算法。套娃式方法（如 Matryoshka 稀疏自编码器的相关工作中所见）通常涉及嵌套表示，可以逐步蒸馏或选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/aryaman2020/status/2102800933659000846">Aryaman Arora on X: "New paper! We introduce Matryoshka Attribution, a ...</a></li>
<li><a href="https://arxiv.org/html/2512.24975v1">Attribution-Guided Distillation of Matryoshka Sparse Autoencoders</a></li>
<li><a href="https://arxiv.org/abs/2501.18887">Towards Unified Attribution in Explainable AI, Data-Centric AI, and ...</a></li>

</ul>
</details>

**标签**: `#interpretability`, `#attribution`, `#machine-learning`, `#research`, `#gradient-descent`

---

<a id="item-13"></a>
## [斯坦福 AI 实验室推出面向 VLA 策略的实时 EXPO-FT](https://twitter.com/StanfordAILab/status/2102829915334975694) ⭐️ 6.0/10

斯坦福 AI 实验室发布了 Real-Time EXPO-FT，这是一个用于微调实时视觉-语言-动作（VLA）策略的强化学习框架。该方法通过将强化学习的可靠性提升与实时执行的响应性相结合，使π0.5 模型能够应对具有挑战性的任务。 这项工作填补了机器人领域的一个关键空白：大多数强化学习微调方法对于实时控制来说太慢，而快速策略又缺乏可靠性。通过使强化学习适用于实时 VLA 策略，它有望加速通用机器人在动态真实环境中的部署。 Real-Time EXPO-FT 建立在 EXPO-FT 样本高效强化学习微调方法之上，并针对实时执行约束进行了优化。该方法在π0.5 上进行了演示，π0.5 是 Physical Intelligence 开发的面向开放世界泛化的 VLA 模型，不过公告摘要中未包含详细的基准测试结果。

twitter · StanfordAILab · Sep 23, 18:38

**背景**: 视觉-语言-动作（VLA）模型是一类多模态 AI 系统，结合视觉感知、语言理解和运动控制，使机器人能够遵循指令并在物理世界中行动。π0.5 是 Physical Intelligence 开发的 VLA 模型，通过在机器人演示、网络数据和语言上联合训练，能够泛化到新家庭和家务任务。强化学习（RL）微调可以提升策略可靠性，但标准 RL 方法对于实时机器人控制往往太慢，这正是 Real-Time EXPO-FT 试图弥合的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pd-perry.github.io/real-time-expo-ft/">Real - Time EXPO - FT : Reinforcement Learning for Real - Time ...</a></li>
<li><a href="https://arxiv.org/html/2609.18207">Reinforcement Learning for Real - Time Vision-Language-Action...</a></li>
<li><a href="https://www.alphaxiv.org/overview/2504.16054v1">$ π _{ 0 . 5 }$: a Vision - Language - Action Model with... | alphaXiv</a></li>

</ul>
</details>

**标签**: `#reinforcement-learning`, `#vision-language-action`, `#real-time`, `#robotics`, `#AI-research`

---

<a id="item-14"></a>
## [研究发现单个注意力头在五类上下文学习任务中均至关重要](https://twitter.com/berkeley_ai/status/2102805066084384938) ⭐️ 6.0/10

Berkeley AI 转发（原帖来自 @xyVickyHu）了一项机制可解释性发现：单个注意力头可以在五类上下文学习（ICL）任务家族中都很重要。原帖据称对这一跨任务的重要性进行了深入的机制分析。 这一发现表明，某些注意力头承担的是通用的、与具体任务无关的功能，而非只专精于单一任务，这可能简化研究人员识别和调控大语言模型中重要回路的方式。它也对依赖定位关键行为组件的模型编辑、剪枝和安全研究工作具有启示意义。 该结论基于对五类 ICL 任务家族中注意力头的机制可解释性分析，但这条推文本身只是转发，细节有限且互动量中等（14 次转发）。完整证据、方法及可能的注意事项都在原帖中，而非转发摘要里。

twitter · berkeley_ai · Sep 23, 16:59

**背景**: 机制可解释性是可解释 AI 的一个子领域，通过分析神经网络的内部结构、算法和回路来对其进行逆向工程。在 Transformer 模型中，注意力头是多头注意力机制的组成部分，使模型能够权衡 token 之间的关系；研究人员常研究单个注意力头，以理解哪些头驱动了特定行为。上下文学习（ICL）指模型无需更新权重，仅凭提示中给出的示例就能完成一项任务的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://www.datacamp.com/tutorial/multi-head-attention-transformers">Understanding Multi- Head Attention in Transformers | DataCamp</a></li>

</ul>
</details>

**标签**: `#mechanistic-interpretability`, `#attention-heads`, `#in-context-learning`, `#transformers`, `#AI-research`

---

<a id="item-15"></a>
## [SpaceX 计划最早 10 月 1 日发射猎鹰 9 号执行 Crew-13 任务](https://twitter.com/SpaceX/status/2102524630019768625) ⭐️ 5.0/10

SpaceX 宣布，计划最早于 10 月 1 日（星期四）用猎鹰 9 号火箭发射 NASA 的 Crew-13 任务前往国际空间站。该消息通过 X 平台上的一条简短帖子发布，并附有任务详情链接。 Crew-13 将把宇航员送往国际空间站，继续轮换远征队成员并维持空间站的持续载人存在。该任务凸显了 NASA 商业载人计划对 SpaceX 猎鹰 9 号和载人龙飞船的持续依赖，这对维持国际空间站运营和科学研究至关重要。 Crew-13 乘组包括 NASA 宇航员 Jessica Watkins 和 Luke Delaney、加拿大航天局宇航员 Joshua Kutryk 以及俄罗斯航天集团宇航员 Sergey Teteryatnikov。发射将使用猎鹰 9 号火箭，该火箭已获得载人认证且可靠性记录良好，乘组将乘坐载人龙飞船前往空间站。

twitter · SpaceX · Sep 22, 22:25

**背景**: 国际空间站是位于低地球轨道的模块化研究实验室，由 NASA、俄罗斯航天集团、欧洲航天局、日本宇宙航空研究开发机构和加拿大航天局五个机构共同运营。自 2000 年 11 月以来，空间站一直有人类连续驻留，并在微重力环境下开展科学实验。SpaceX 的猎鹰 9 号是一种部分可重复使用的两级火箭，于 2010 年首飞，并在 2020 年成为首个将人类送入轨道的商业火箭。NASA 的商业载人计划委托 SpaceX 使用载人龙飞船往返国际空间站运送宇航员。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falcon_9_rocket">Falcon 9 rocket</a></li>
<li><a href="https://www.asc-csa.gc.ca/eng/missions/crew-13/mission.asp">Crew - 13 mission | Canadian Space Agency</a></li>
<li><a href="https://en.wikipedia.org/wiki/International_Space_Station">International Space Station</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#NASA`, `#spaceflight`, `#Falcon 9`, `#ISS`

---

<a id="item-16"></a>
## [Chelsea Finn 提出基于 EXPO-FT 的延迟感知强化学习方法](https://twitter.com/StanfordAILab/status/2102805898884460545) ⭐️ 5.0/10

斯坦福人工智能实验室转发了 Chelsea Finn 的一条推文，介绍了一种面向动态任务的强化学习方法：让基础 VLA 策略在较旧的图像上运行，同时通过另一机制补偿延迟，该方法建立在 EXPO-FT 框架之上。 延迟是将学习到的策略部署到真实机器人上的根本障碍——当模型处理完观测数据时，现实世界已经发生变化。显式处理过期观测的方法有望让经强化学习训练的 VLA 策略适用于快速、动态的操作任务。 该方法基于 EXPO-FT——一个面向视觉-语言-动作（VLA）模型的样本高效强化学习微调框架，核心思路是让基础 VLA 在较旧的图像上行动，同时由额外组件处理由此产生的延迟；推文内容被截断，未公布量化结果或基准测试。

twitter · StanfordAILab · Sep 23, 17:02

**背景**: 视觉-语言-动作（VLA）模型将视觉输入和语言指令直接映射为机器人动作，而 EXPO-FT 是一个以样本高效方式用强化学习微调此类策略的框架。在动态任务中，从拍摄图像到执行动作之间的延迟意味着策略实际上是在依据过时信息行动，这可能导致失败。Chelsea Finn 是斯坦福大学教授，在元学习和机器人学习领域有重要影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pd-perry.github.io/real-time-expo-ft/">Real-Time EXPO - FT : Reinforcement Learning for Real-Time...</a></li>
<li><a href="https://github.com/pd-perry/expo-ft">GitHub - pd-perry/ expo - ft · GitHub</a></li>
<li><a href="https://medium.com/@anishcp663/vla-models-in-plain-english-from-an-engineer-still-learning-them-46fc8da2919c">VLA Models in Plain English (From an Engineer Still...) | Medium</a></li>

</ul>
</details>

**标签**: `#reinforcement-learning`, `#robotics`, `#latency`, `#VLA`, `#Stanford`

---

<a id="item-17"></a>
## [李飞飞：AI 的目标应是改善人类生活与社会](https://twitter.com/drfeifei/status/2102508817653379411) ⭐️ 4.0/10

常被称为“AI 教母”的斯坦福大学教授李飞飞在 Twitter（X）上发文表示，构建任何技术（包括 AI）的目标都应是改善人类生活与社会。该表态获得了中等程度的关注，约有 976 个点赞、149 次转发和 84 条回复。 随着 AI 系统能力不断增强并被应用于医疗、教育和公共服务等领域，对 AI 目标的界定会影响研究优先级、企业战略和监管方向。像李飞飞这样有影响力的人物重申以人为本的使命，有助于强化许多实验室、政策制定者和资助方被要求采纳的伦理方向。 这条推文是一条宏观原则，而非技术发布，没有给出具体的政策、评测基准或实施方案。它与李飞飞长期倡导的“以人为本的 AI”理念一致，这一理念也体现在她通过斯坦福 HAI 以及早期 ImageNet 工作所推动的方向上。

twitter · drfeifei · Sep 22, 21:22

**背景**: 李飞飞是斯坦福大学计算机科学教授，因创建大规模图像数据集 ImageNet（推动了现代深度学习热潮）以及共同领导斯坦福以人为本人工智能研究院（HAI）而闻名。“以人为本的 AI”是一种围绕人类需求、价值观和福祉来设计机器智能的思路，而不是把能力本身当作唯一目标。她的表态呼应了被广泛讨论的 AI 伦理原则，例如安全、公平和造福社会，这些原则也出现在澳大利亚自愿性 AI 伦理原则等框架中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.klover.ai/fei-fei-li-and-the-human-centered-ai-inside-stanford-hais-policy-impact/">Fei - Fei Li and the Human - Centered AI Inside Stanford... - Klover. ai</a></li>
<li><a href="https://wisdomia.ai/fei-fei-li-world-building-human-centric-ai?trk=article-ssr-frontend-pulse_little-text-block">wisdomia. ai / fei - fei - li -world-building- human - centric - ai ?trk=article-ssr...</a></li>
<li><a href="https://www.industry.gov.au/publications/australias-artificial-intelligence-ethics-principles/australias-ai-ethics-principles">Australia’s AI Ethics Principles | Australia’s Artificial Intelligence...</a></li>

</ul>
</details>

**社区讨论**: 该帖获得了中等程度的互动（976 个点赞、149 次转发、84 条回复），表明总体上认同这一观点，但该条目也被评价为缺乏技术深度或新意。由于未提供详细评论内容，无法进行更深入的舆情分析。

**标签**: `#AI ethics`, `#technology and society`, `#human-centered AI`, `#Fei-Fei Li`, `#Twitter`

---

<a id="item-18"></a>
## [物理 AI 快速进展引发线下峰会价值讨论](https://twitter.com/lukas_m_ziegler/status/2102774998549078329) ⭐️ 4.0/10

Lukas M. Ziegler 在推文中列举了物理 AI 公司近期的多项进展：Skild AI 年化营收突破 1 亿美元并发布了 S1 机器人基础模型，Wayve 通过 Uber 在伦敦启动了有人监督的自动驾驶载客服务，Dyna Robotics 则持续推进通用机器人研发。他认为，正是这种快速迭代让线下峰会的价值不降反升。 这些里程碑表明物理 AI 正从研究演示走向机器人和自动驾驶领域的商业化落地，可能重塑劳动力、物流和城市交通。关于线下峰会的讨论也折射出一个更广泛的问题：当行业进展以周为单位更新时，从业者应如何协调与共享知识。 Skild AI 的 S1 模型可通过单段演示视频进行提示，无需重新训练或微调权重即可执行任务；Wayve 在伦敦的服务仍属有人监督，而非完全无人驾驶。Dyna Robotics 则专注于面向酒店、物流和工厂流程的低成本通用机器人。

twitter · lukas_m_ziegler · Sep 23, 15:00

**背景**: 物理 AI 指在真实世界中感知和行动的 AI 系统，例如机器人和自动驾驶汽车，而非纯数字任务如文本生成。Skild AI 的 S1 等机器人基础模型旨在跨任务泛化，而 Wayve 的端到端 AI Driver 从数据中学习驾驶行为，而非依赖手工编写的规则。线下峰会则是行业参与者面对面交流进展、建立合作的会议活动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://runtimewire.com/article/skild-ai-s1-robot-model-one-video-prompt">Skild AI ships S 1 , a robot model prompted by one video</a></li>
<li><a href="https://wayve.ai/press/wayve-uber-launch-autonomous-rides/">Wayve and Uber Launch First-Ever Autonomous Rides in the UK</a></li>
<li><a href="https://www.dyna.co/">DYNA Robotics</a></li>

</ul>
</details>

**标签**: `#physical-ai`, `#robotics`, `#autonomous-vehicles`, `#industry-news`, `#social-media`

---

<a id="item-19"></a>
## [社区维护的 Robotiq 夹爪驱动获赞，支持 ROS 2 与 Isaac Sim](https://twitter.com/lukas_m_ziegler/status/2102752347000639620) ⭐️ 4.0/10

Lukas M. Ziegler 在 Twitter 上指出，Robotiq 夹爪之所以能在 ROS 2 和 Isaac Sim 中稳定运行多年，靠的是志愿者编写驱动、构建仿真模型并持续维护。这条推文把功劳归于未具名的社区贡献者，而非 Robotiq 公司本身。 这凸显了机器人基础设施对无偿开源劳动的依赖，也提醒企业和用户：若缺乏持续的社区或厂商支持，这类驱动可能停滞。对 ROS 2 用户而言，这也说明 Robotiq 夹爪支持已足够成熟，可视为事实标准。 相关软件包位于 PickNikRobotics/ros2_robotiq_gripper 仓库，包含 robotiq_driver（ros2_control 硬件接口）、robotiq_controllers 以及 robotiq_description（URDF/xacro、网格模型、RViz 配置和启动文件），最初支持 2F-85 夹爪。仿真工作流通过 ROS 2 桥接与 Isaac Sim 配合，社区项目如 ur10e_2f140_topic_based_ros2_control 即为一例。

twitter · lukas_m_ziegler · Sep 23, 13:30

**背景**: ROS 2 是机器人操作系统（Robot Operating System）的第二代，是构建机器人软件广泛使用的开源框架，而 ros2_control 是其标准硬件接口层。Robotiq 是知名的自适应机器人夹爪厂商，其 2F-85 等产品常与协作机械臂搭配使用。Isaac Sim 是 NVIDIA 的机器人仿真平台，要在其中运行夹爪既需要驱动也需要仿真模型，而这些正是社区提供的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/PickNikRobotics/ros2_robotiq_gripper">GitHub - PickNikRobotics/ ros 2 _ robotiq _ gripper · GitHub</a></li>
<li><a href="https://blog.robotiq.com/robotiq-releases-ros-2-packages-for-adaptive-grippers">Robotiq Releases ROS 2 Packages for Adaptive Grippers</a></li>
<li><a href="https://github.com/qdeyna/ur10e_2f140_topic_based_ros2_control">qdeyna/ur10e_2f140_topic_based_ros2_control: UR10e + Robotiq ...</a></li>

</ul>
</details>

**标签**: `#ROS 2`, `#Robotiq`, `#Isaac Sim`, `#community`, `#robotics`

---

<a id="item-20"></a>
## [Perplexity 推出面向早期职业人才的研究奖学金](https://twitter.com/ylecun/status/2102435954019414403) ⭐️ 4.0/10

Perplexity 首席执行官 Aravind Srinivas 宣布推出 Perplexity Research Fellowship（Perplexity 研究奖学金），该项目面向来自任何技术背景的早期职业研究人员、工程师和分析师。Meta 首席 AI 科学家 Yann LeCun 转发了这一公告，将其传播给大量关注者。 该奖学金表明 Perplexity 有意建立内部研究人才管道，而不仅仅依赖第三方基础模型，同时为早期职业 STEM 人才提供了一条进入前沿 AI 工作的带薪途径。LeCun 的转发也为该项目在更广泛的 AI 研究社区中增添了可信度。 根据项目描述，研究员以全职身份加入，表现优异者有机会转为全职研究岗位。该项目被描述为 Perplexity 的旗舰计划，旨在让早期职业 STEM 人才参与塑造前沿智能的未来。

twitter · ylecun · Sep 22, 16:32

**背景**: Perplexity AI 是一家美国私营公司，由 Aravind Srinivas、Denis Yarats、Johnny Ho 和 Andy Konwinski 于 2022 年 8 月创立。它运营一个 AI 驱动的答案引擎，利用大语言模型综合生成带网页来源引用的回答，截至 2025 年 9 月估值约为 200 亿美元。该公司还因版权和抓取指控而面临多家大型媒体机构的法律审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perplexity_(company)">Perplexity (company)</a></li>
<li><a href="https://jobs.ashbyhq.com/perplexity/ab076e26-adf1-414f-a006-7b1bdc9247c8">Perplexity Research Fellowship @ Perplexity</a></li>
<li><a href="https://opportunitydesk.org/2026/09/21/perplexity-research-fellowship-2027/">Perplexity Research Fellowship 2027 (paid) – Opportunity Desk</a></li>

</ul>
</details>

**标签**: `#AI`, `#fellowship`, `#Perplexity`, `#research`, `#announcement`

---

<a id="item-21"></a>
## [Anthropic 澄清 Claude Code 云会话在 Pro 和 Max 套餐上的计费方式](https://twitter.com/ClaudeDevs/status/2102940480736821610) ⭐️ 4.0/10

@ClaudeDevs 账号澄清，Claude Code 的云会话与 Claude Code 的其他功能一样，运行在用户已有的 Pro 或 Max 套餐之上。促销赠送的一次性额度是可选的，云会话会优先消耗该额度，用完后才会回落到正常的套餐用量。 这一澄清解决了用户对云会话是否需要单独付费或消耗独立额度池的困惑，这对正在考虑采用 Claude Code 托管工作流的开发者尤为重要。清晰的计费规则能降低 Pro 和 Max 订阅者在评估云会话与自托管或第三方沙箱方案时的决策阻力。 该促销额度被描述为一次性、可选的赠额，云会话会优先消耗它，之后用量将回落到订阅者正常的 Pro 或 Max 套餐额度。云会话还支持在 Claude Code 启动前运行的安装脚本，用于安装依赖或配置工具。

twitter · ClaudeDevs · Sep 24, 01:57

**背景**: Claude Code 是 Anthropic 推出的智能体编程工具，云会话让它能在托管环境中运行，而不局限于本地机器。Anthropic 通过 Free、Pro、Max、Team 和 Enterprise 等层级销售 Claude 服务，其中 Pro 和 Max 是大多数开发者使用的个人付费套餐。用量额度则是一种独立机制，付费套餐可以启用它来覆盖超出正常套餐限制的用量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/pricing">Plans & Pricing | Claude by Anthropic</a></li>
<li><a href="https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans">Manage usage credits for paid Claude plans | Claude Help Center</a></li>
<li><a href="https://code.claude.com/docs/en/cloud-environments">Configure cloud environments - Claude Code Docs</a></li>

</ul>
</details>

**社区讨论**: 该帖子互动量很高（约 2744 个赞和 139 条回复），讨论集中在用户对促销额度与正常套餐用量如何相互作用的困惑上。整体情绪似乎是既感谢这一澄清，又对额度机制仍存疑问。

**标签**: `#Claude Code`, `#billing`, `#cloud sessions`, `#Anthropic`, `#developer tools`

---

<a id="item-22"></a>
## [推特帖子列出 10 个免费 GitHub 仓库，涵盖 Python 与 AI 学习路径](https://twitter.com/RodmanAi/status/2102742421100519613) ⭐️ 4.0/10

@RodmanAi 在推特上发布了一个帖子，整理了 10 个免费的 GitHub 仓库，帮助学习者从 Python 基础逐步进阶到 LLM、AI 智能体和生产系统。帖子重点推荐了 Python-100-Days 和微软的 Generative AI for Beginners 等资源，涵盖提示工程、RAG、智能体和微调等主题。 精选的学习路径降低了开发者进入 LLM 和 AI 智能体领域的门槛，而这是软件行业中增长最快的方向之一。对于被零散资源淹没的初学者来说，一个指向结构化免费仓库的帖子可以显著加速他们的学习进程。 帖子特别推荐了 Python-100-Days（涵盖 Python、数据分析和 Web 开发）以及 Generative AI for Beginners（涵盖 LLM、提示工程、RAG、智能体和微调）。该帖子属于轻量级资源整理而非原创技术内容，互动量中等，获得 42 个点赞、15 次转发和 10 条回复。

twitter · RodmanAi · Sep 23, 12:50

**背景**: GitHub 仓库是开发者分享开源代码、教程和结构化课程的常见方式。RAG（检索增强生成）是一种让 LLM 引入外部文档来支撑回答的技术，而微调则是让预训练模型适应特定任务的方法。AI 智能体是能够自主追求目标的程序，通常使用 LLM 进行规划并调用工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>
<li><a href="https://www.superannotate.com/blog/llm-fine-tuning">Fine - tuning large language models (LLMs) in 2026</a></li>

</ul>
</details>

**标签**: `#Python`, `#LLM`, `#AI Agents`, `#Learning Resources`, `#GitHub`

---

<a id="item-23"></a>
## [推特热帖盘点 10 个免费开源 GitHub 仓库，含 Archify 与 OpenMAIC](https://twitter.com/RodmanAi/status/2102392223161786775) ⭐️ 4.0/10

@RodmanAi 发布了一条题为“10 个免费到几乎违法的 GitHub 仓库”的推特帖子，盘点了一批开源开发者工具，其中点名了 Archify（用 AI 将代码库转化为架构图、工作流图、时序图和数据流图）和 OpenMAIC（一个多智能体环境）。该帖子带有明显的推广性质，且摘录内容在第二条之后即被截断。 这类精选清单能让鲜为人知的开源 AI 工具迅速触达广大开发者，可能推动 Archify、OpenMAIC 等项目的采用。不过，标题党式的包装和缺乏技术深度的内容意味着读者应自行核实，而不应把该帖子当作权威推荐。 Archify 被描述为一种“智能体技能”，可将想法、问题或计划转化为可交互的 HTML 架构图，并在输出前对图进行校验；OpenMAIC 则是清华大学开源的多智能体互动课堂，可生成幻灯片、测验、交互式模拟和项目式学习活动。现有摘录只展示了前两个仓库，其余八个无法从所给内容中核实。

twitter · RodmanAi · Sep 22, 13:39

**背景**: GitHub 是托管和分享开源代码的主流平台，社交媒体上“awesome list”式的盘点帖是开发者发现新工具的常见途径。Archify 属于新兴的“AI 编程智能体技能”类别，用于生成并校验软件架构图；OpenMAIC 则属于多智能体编排领域，即多个 AI 智能体围绕同一任务（如讲解某个主题）协同工作。两者都体现了 AI 智能体被封装为可复用开源组件的整体趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tt-a1i/archify">GitHub - tt-a1i/archify: Agent skill for beautiful, verifiable architecture ...</a></li>
<li><a href="https://github.com/THU-MAIC/OpenMAIC">GitHub - THU-MAIC/OpenMAIC: Open Multi-Agent Interactive Classroom</a></li>
<li><a href="https://openmaic.chat/">OpenMAIC - Open Multi-Agent Interactive Classroom</a></li>

</ul>
</details>

**社区讨论**: 该帖互动量中等，约有 350 个点赞、71 次转发和 22 条回复，但现有数据中并未捕捉到实质性的讨论或批判性分析。整体情绪更像是对免费开源工具的随意关注，而非技术层面的辩论。

**标签**: `#open-source`, `#github`, `#ai-tools`, `#developer-tools`, `#twitter-thread`

---

<a id="item-24"></a>
## [Adam 宣布与 Rhino 3D 直接集成](https://twitter.com/adamdotnew/status/2102839787808002380) ⭐️ 3.0/10

Adam（@adamdotnew）通过一条简短的推文宣布，Adam 现在可以直接与 Rhino 集成，并附上了一个了解更多信息的链接。该公告没有提供关于集成如何工作或支持哪些版本的技术细节。 Rhino 是建筑、工业设计和珠宝设计领域广泛使用的基于 NURBS 的 3D 建模工具，因此直接集成可能会为同时使用 Adam 和 Rhino 的设计师简化工作流程。不过，鉴于该推文的影响力有限（11 个赞、2 条回复），其直接影响似乎仅限于这两款工具的现有用户。 该推文没有说明支持的 Rhino 版本、安装方式，也没有说明该集成是插件、API 桥接还是云服务。唯一附加信息位于一个缩短的 t.co 链接之后。

twitter · adamdotnew · Sep 23, 19:17

**背景**: Rhino（Rhinoceros）是一款 3D 建模程序，使用 NURBS 几何来描述任意大小或复杂度的形体，并拥有通过 Yak 包管理器管理的大型插件生态系统。设计工具与 Rhino 之间的集成很常见，例如 Rhino.Inside.Revit 以及 Rhino 8 中内置的 SectionTools。Adam 似乎是一款独立的设计或 CAD 相关工具，现在正在添加与 Rhino 的连接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rhino_(software)">Rhino (software)</a></li>
<li><a href="https://www.rhino3d.com/stories/sectiontools-integrated/">Rhino - SectionTools Integrated</a></li>
<li><a href="https://rhinopackages.github.io/">Rhino Packages — Browse & Install Plugins</a></li>

</ul>
</details>

**社区讨论**: 该新闻没有提供社区评论，因此无法总结相关情绪或观点。

**标签**: `#integration`, `#Rhino`, `#Adam`, `#announcement`, `#CAD`

---

<a id="item-25"></a>
## [LeCun 转发 Hugging Face CEO 受邀在联合国安理会发言](https://twitter.com/ylecun/status/2102939109887021330) ⭐️ 3.0/10

Yann LeCun 转发了 Hugging Face CEO Clement Delangue 的一条推文，Delangue 在推文中感谢法国大使 Jean-Noël Barrot 和联合国邀请他向安理会分享经验，并提到他的公司是首家获此邀请的公司。 这表明像 Hugging Face 这样的开源 AI 公司正日益被纳入高层次的国际 AI 治理讨论，这可能会影响全球 AI 政策对开放模型和开源开发的态度。 这条推文是一则简短的致谢与宣传信息，没有技术内容，且原帖内容似乎被截断；该条目互动量较低（约 31 次转发），被聚合平台评为低价值内容。

twitter · ylecun · Sep 24, 01:52

**背景**: 联合国安理会是负责国际和平与安全的主要机构，近年来已就人工智能的风险与治理举行过会议。Hugging Face 是一个知名的开源 AI 平台，以托管模型和数据集著称；Yann LeCun 则是图灵奖得主、Meta 首席 AI 科学家。Delangue 的推文将此次邀请描述为其公司参与政策制定的一项里程碑。

**标签**: `#twitter`, `#promotional`, `#UN`, `#AI policy`, `#low-value`

---

<a id="item-26"></a>
## [Yann LeCun 在 NYU CILVR 研讨会开幕演讲中谈世界模型](https://twitter.com/ylecun/status/2102878714023592161) ⭐️ 3.0/10

纽约大学数据科学中心创始主任 Yann LeCun 以题为“世界模型”的演讲为 CILVR 研讨会秋季系列揭开序幕。该消息由 NYU Data Science 发布，并被 LeCun 本人转发。 LeCun 是深度学习领域最具影响力的人物之一，他持续倡导将世界模型作为通往机器智能的替代路径，这影响着学术界和工业界的研究方向。纽约大学的这一研讨会系列是将这些理念传播给学生和研究者的平台。 该演讲是纽约大学数据科学中心主办的 CILVR（计算、智能、学习、视觉与机器人）研讨会系列的一部分。公告本身并未包含技术细节或幻灯片，仅有标题和演讲者信息。

twitter · ylecun · Sep 23, 21:52

**背景**: 人工智能中的世界模型是指一种学习环境内部表征的系统，使智能体能够预测未来状态并规划行动。LeCun 在 2022 年的一篇立场论文中提出了这一概念，将其作为他提出的自主机器智能架构的关键组成部分，并常与他的 JEPA（联合嵌入预测架构）框架一同讨论。CILVR 研讨会是纽约大学定期举办的活动，邀请研究者展示在计算、智能、学习、视觉和机器人领域的工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cds.nyu.edu/?mc_id=135">CILVR Seminar : Yann LeCun / September 9, 2026 / NYU Center for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://cims.nyu.edu/ai/seminars/cilvr-seminar-series/">Upcoming Seminars | ai @ NYU</a></li>

</ul>
</details>

**标签**: `#Yann LeCun`, `#NYU`, `#seminar`, `#AI research`, `#announcement`

---

<a id="item-27"></a>
## [LeCun 转发 ICWM 会议单盲评审与开放参与政策](https://twitter.com/ylecun/status/2102437238986379353) ⭐️ 3.0/10

Yann LeCun 转发了 @randall_balestr 的一条帖子，称国际世界建模会议（ICWM）采用单盲评审，并且对任何人完全开放，并将其与 ICLR 相类比。该转发互动量很低，仅有约 3 次转发，且没有实质性讨论。 LeCun 的转发表明世界建模正在成为人工智能领域的重要研究方向，而新成立的 ICWM 会议可能成为该方向的重要发表平台。其单盲评审与开放参与的模式也反映了机器学习社区关于让会议更加包容和可及的更广泛讨论，正如 ICLR 所做的那样。 该推文没有提供投稿截止日期、程序委员会或会议地点等进一步细节，搜索结果中也没有出现 ICWM 会议的官方网站。需要注意的是，“ICWM”同时也是“In-Context World Modeling”（上下文世界建模）这一机器人研究框架的缩写，可能造成混淆。

twitter · ylecun · Sep 22, 16:37

**背景**: 同行评审是专家在论文发表前对其进行评估的过程；在单盲评审中，评审人知道作者身份，但作者不知道评审人是谁，这是科学期刊中最常见的形式。ICLR（国际学习表征会议）是机器学习领域的重要会议，以其开放、可及的评审流程著称。世界建模指人工智能系统学习环境如何演变的内部表示，这一方向在机器人和规划领域日益受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Single-blind_peer_review">Single-blind peer review</a></li>
<li><a href="https://en.wikipedia.org/wiki/International_Conference_on_Learning_Representations">International Conference on Learning Representations - Wikipedia</a></li>
<li><a href="https://www.alphaxiv.org/abs/2606.26025">In-Context World Modeling for Robotic Control | alphaXiv</a></li>

</ul>
</details>

**标签**: `#conference`, `#world-modeling`, `#peer-review`, `#twitter`

---

<a id="item-28"></a>
## [斯坦福 AI 实验室分享从数据中恢复特征的研究项目](https://twitter.com/StanfordAILab/status/2102640423554720198) ⭐️ 3.0/10

斯坦福 AI 实验室转发了 Sanmi Koyejo 的一条推文，介绍其与 Nathan Hu 和 Chris Potts 合作的一个项目，并特别提到第 5 节关于从数据中恢复特征的内容。该推文内容被截断，未提供更多技术细节。 从数据中恢复潜在特征这一概念对可解释性和表示学习至关重要，而由斯坦福知名 NLP 研究者参与的项目可能影响模型分析的方式。不过，该公告过于模糊，难以评估其具体影响。 该推文仅指向某篇未指明论文或项目的第 5 节，称在某些条件下特征可以从数据中恢复；没有给出论文标题、数据集或方法。该帖子互动量很低，仅有 2 次转发。

twitter · StanfordAILab · Sep 23, 06:05

**背景**: 可恢复性通常指从观测数据中重建隐藏或潜在信息的能力，这一问题在因果推断、图神经网络和表示学习中被广泛研究。在机器学习中，特征往往指数据或模型中未被直接观测但可能被推断出的潜在属性。斯坦福 AI 实验室以及 Sanmi Koyejo、Chris Potts 等研究者以机器学习、自然语言处理和可信 AI 方面的工作而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/jordan-recoverability">Jordan Recoverability : Theory & Applications</a></li>
<li><a href="https://www.youtube.com/watch?v=5Yw7m9tot84">On Recoverability of Graph Neural Network Representation - YouTube</a></li>

</ul>
</details>

**标签**: `#AI`, `#machine learning`, `#Stanford`, `#tweet`, `#research`

---

<a id="item-29"></a>
## [加州大学伯克利分校招募计算健康科学博士后](https://twitter.com/berkeley_ai/status/2102876538215825856) ⭐️ 3.0/10

加州大学伯克利分校的 Bakar 计算健康科学研究所正在招募多名博士后研究员，该消息通过@berkeley_ai 的转发公布。招募信息由@yun_s_song 分享，并呼吁社区帮助传播。 这一招募反映了对计算健康科学这一融合计算机科学、数据科学与生物医学的跨学科领域日益增长的投资。它为有兴趣将计算方法应用于精准医学和大规模生物医学数据的早期职业研究者提供了机会。 这些职位属于最近成立的 Bakar 计算健康科学研究所，但公告未说明职位数量、申请截止日期或具体研究方向。该推文互动量一般，仅有 34 次转发。

twitter · berkeley_ai · Sep 23, 21:43

**背景**: 计算健康科学是一个跨学科领域，将计算机科学工具和数据科学方法应用于生物医学研究，包括疾病检测、风险预测和精准医学。Bakar 计算健康科学研究所通过计算和数据科学支持这项工作，加州大学伯克利分校也一直在积极发展相关研究计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bakarinstitute.ucsf.edu/">Bakar Computational Health Sciences Institute</a></li>
<li><a href="https://cdss.berkeley.edu/news/researchers-consider-innovative-inclusive-ways-develop-and-scale-computational-health">Researchers consider innovative, inclusive ways to develop and scale ...</a></li>

</ul>
</details>

**标签**: `#academia`, `#recruitment`, `#computational biology`, `#postdoc`, `#berkeley`

---

<a id="item-30"></a>
## [推特帖子列出 12 个 AI 智能体必备 JEV 技能](https://twitter.com/RodmanAi/status/2102774321324437746) ⭐️ 3.0/10

推特用户@RodmanAi 发布帖子，列出 12 个 AI 智能体配置中“必备”的 JEV 技能，并重点展示了四个例子：typesafe-mario（玩超级马里奥的智能体）、jev-ultrafast（浏览器智能体）、fast-jev-compaction（上下文压缩）和 json-render（生成式 JSON 渲染）。 该帖子反映出一种日益增长的趋势：在 AI 智能体中使用 JEV（TypeSafe Jev）作为结构化决策层，让模型从有限选项中做出选择，而不是生成自由文本，从而使智能体工作流更快、更可靠。 该帖子仅提供名称和链接，没有技术解释，互动量一般（61 个赞、22 次转发、15 条回复）；底层项目包括 browser-use/jev-ultrafast，它用结构化选择替代自由形式的 LLM 生成，以及 fhshaik/typesafe-mario，它让 Jev 模型直接选择 NES 手柄输入，而不接收屏幕截图。

twitter · RodmanAi · Sep 23, 14:57

**背景**: JEV（TypeSafe Jev）是一种面向软件和 AI 智能体的决策助手：不是让 AI 写一段文字，而是给它一小组有限选项，让它从中选择一个。这种方法正被应用于浏览器自动化、上下文压缩、技能选择和模型路由等智能体技能。typesafe-mario 项目是一个实验性控制器，让 Jev 模型直接为原版《超级马里奥兄弟》选择 NES 手柄输入；而 jev-ultrafast 是 browser-use 团队开发的浏览器智能体，使用 Jev 来决定下一步操作哪个页面元素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/AI_Agents/comments/1wndjk7/anyone_here_learning_jev/">Anyone here learning JEV? : r/AI_Agents - Reddit</a></li>
<li><a href="https://github.com/fhshaik/typesafe-mario">fhshaik/ typesafe - mario : A TypeSafe/Jev agent that plays Super ...</a></li>
<li><a href="https://github.com/browser-use/jev-ultrafast/">GitHub - browser -use/ jev - ultrafast : Fastest and cheapest web agent</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#LLM tools`, `#browser automation`, `#context compression`, `#Twitter thread`

---

<a id="item-31"></a>
## [MecAgent 宣传 Copilot V2.0.0 搭配虚构的 GPT-6 Astra 与 SolidWorks 2026](https://twitter.com/MecAgent/status/2102754454269305061) ⭐️ 2.0/10

MecAgent 发布了一条宣传推文，展示其 MecAgent Copilot V2.0.0 在 SolidWorks 2026 上搭配虚构的 GPT-6 Astra 模型运行。该推文除了一句简短说明和一个链接外，没有任何技术细节、基准测试或演示内容。 该帖子表明业界对机械 CAD 工作流中的 AI 副驾驶工具兴趣渐浓，但由于其引用了未经证实的未来产品且未提供实质性证据，对工程社区而言信息价值有限。 MecAgent 自称是首个面向机械 CAD 软件的 AI CAD 副驾驶，提供文本转 CAD 操作、零件与特征重命名以及属性更新等功能。该推文提及的 GPT-6 Astra 和 SolidWorks 2026 均为未经证实或未来的产品，且未提供 Copilot V2.0.0 的版本更新日志或功能列表。

twitter · MecAgent · Sep 23, 13:38

**背景**: MecAgent 是一款 AI 副驾驶工具，旨在自动化 SolidWorks 等机械 CAD 软件中的任务，让工程师通过自然语言提示执行操作。SolidWorks 是达索系统旗下广泛使用的三维 CAD 软件，而 GPT-6 Astra 则指称 OpenAI 未来的一款大语言模型。该推文将这些名称组合在一起，暗示一种由 AI 驱动的集成 CAD 工作流，但所引用的未来产品均未得到独立证实。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mecagent.com/">MecAgent - AI CAD Copilot</a></li>
<li><a href="https://mecagent.com/features">MecAgent - AI CAD Copilot</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>

</ul>
</details>

**标签**: `#AI`, `#CAD`, `#SolidWorks`, `#promotional`, `#low-content`

---

<a id="item-32"></a>
## [Yann LeCun 转发 ICWM 研讨会推广，截止日期约两个月后](https://twitter.com/ylecun/status/2102440488120766622) ⭐️ 2.0/10

Yann LeCun 转发了 @randall_balestr 的一条推文，推广 ICWM 研讨会，该研讨会的提交截止日期大约在两个月后。原推文提到组织者仍在调整细节，并附上了研讨会网站的链接。 LeCun 的转发让该研讨会在其庞大的 AI 研究关注者中获得曝光，可能吸引更多投稿和参会者。不过，这条推文本身没有技术内容或实质性讨论，因此其直接影响仅限于推广。 推文提到截止日期大约在两个月后，并表示组织者仍在调整相关事宜，说明征稿或日程可能仍在变动中。链接是 t.co 短网址，推文正文未提供具体的研讨会日期、地点或主题细节。

twitter · ylecun · Sep 22, 16:50

**背景**: ICWM 是推文中提到的研讨会缩写，但搜索结果未能明确指向具体是哪一个 ICWM 活动，因为多个不相关的会议和研讨会都使用这一缩写。Yann LeCun 是著名的 AI 研究者、图灵奖得主，以卷积神经网络和自监督学习方面的工作闻名。转发研讨会公告是资深研究者表达对社区活动支持的常见方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Iowa_Workshop">Iowa Workshop</a></li>
<li><a href="https://conferenceindex.org/event/international-conference-on-waste-management-icwm-2027-march-algiers-dz">International Conference on Waste Management ICWM on March...</a></li>

</ul>
</details>

**标签**: `#twitter`, `#workshop`, `#promotion`, `#low-engagement`

---

<a id="item-33"></a>
## [吴恩达转发马斯克含糊评论「有趣的观点」](https://twitter.com/AndrewYNg/status/2102452386698817972) ⭐️ 2.0/10

吴恩达（Andrew Ng）转发了埃隆·马斯克的一条推文，内容仅为「有趣的观点」，没有附上链接、上下文，也没有说明所指的是什么观点。吴恩达本人在转发时也没有添加任何额外评论。 这条内容几乎没有信息价值，其曝光度完全来自两位人物的知名度，而非任何技术或行业实质内容。它反映出社交平台上的互动指标在知名人物发布内容时，会放大空洞信息这一现象。 这条推文仅有四个英文单词，没有任何支撑材料，因此没有可核实、可分析或可付诸行动的内容。该新闻条目评分仅为 2.0/10，并被标记为无实质内容的转发。

twitter · AndrewYNg · Sep 22, 17:38

**背景**: 吴恩达是知名人工智能研究者，也是 Google Brain 和 Coursera 的联合创始人；埃隆·马斯克则是特斯拉和 SpaceX 的 CEO，以及 xAI 的创始人。两人在 X（原 Twitter）上都拥有大量粉丝，因此即便是极简短的帖子也能引发大量互动。在 X 上，转发只是把其他用户的帖子重新展示给自己的关注者，并不会添加新的文字内容。

**标签**: `#twitter`, `#retweet`, `#no-content`, `#social-media`

---

<a id="item-34"></a>
## [幽默推文调侃英格兰足球历史](https://twitter.com/lukas_m_ziegler/status/2102811228716589382) ⭐️ 1.0/10

一位推特用户发布了一条幽默推文，写道“兄弟还记得足球真正回家的时候”，并配上了哭泣表情和英格兰旗帜。该推文引用了英格兰足球的长期口号，没有任何实质性新闻内容。 这条推文没有技术或学术意义，对于关注科技的读者来说是离题的。它仅作为一条低分、互动极少的社交媒体帖子被收录。 该推文仅包含一个短句、一个表情符号和英格兰旗帜，没有链接、数据或可验证的说法。由于缺乏相关性和互动，它仅获得 1.0/10 的评分。

twitter · lukas_m_ziegler · Sep 23, 17:23

**背景**: “足球回家”是 1996 年英格兰足球歌曲《三狮》中的著名歌词，表达了对英格兰赢得重大赛事冠军的期望。英格兰男足自 1966 年以来再未赢得过世界杯，因此球迷常以幽默或讽刺的方式使用这句话。

**标签**: `#football`, `#social media`, `#off-topic`, `#humor`

---