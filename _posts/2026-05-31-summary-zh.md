---
layout: default
title: "Horizon Summary: 2026-05-31 (ZH)"
date: 2026-05-31
lang: zh
---

> From 21 items, 16 important content pieces were selected

---

1. [斯坦福 AI 实验室发布 GPIC：1 亿图文数据集](#item-1) ⭐️ 8.0/10
2. [联邦研究资助拟需政治批准](#item-2) ⭐️ 7.0/10
3. [微软开源 SkillOpt，革新 AI 智能体学习方式](#item-3) ⭐️ 7.0/10
4. [杜克大学 Argus 机器人：20 条腿，无前后之分](#item-4) ⭐️ 6.0/10
5. [美的集团推出六臂人形机器人 MIRO U](#item-5) ⭐️ 6.0/10
6. [Anthropic 的 31 页提示指南提炼为 9 条规则](#item-6) ⭐️ 6.0/10
7. [机器人手：难造，却不可或缺](#item-7) ⭐️ 5.0/10
8. [SpaceX 用猎鹰 9 号发射 24 颗星链卫星](#item-8) ⭐️ 5.0/10
9. [ESMFold2 基准测试困惑得到澄清](#item-9) ⭐️ 5.0/10
10. [OpenAI Codex 现可通过 Ollama 免费本地运行](#item-10) ⭐️ 5.0/10
11. [Renishaw REVO CMM 实现高速零件检测](#item-11) ⭐️ 4.0/10
12. [SpaceX 发射 29 颗星链卫星](#item-12) ⭐️ 4.0/10
13. [埃克森美孚警告两周内石油末日](#item-13) ⭐️ 2.0/10
14. [杨立昆转发批评 MAGA 言论](#item-14) ⭐️ 2.0/10
15. [推文对比 2024 年与 2026 年美国经济](#item-15) ⭐️ 2.0/10
16. [斯坦福 AI 实验室发布无上下文链接推文](#item-16) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [斯坦福 AI 实验室发布 GPIC：1 亿图文数据集](https://twitter.com/StanfordAILab/status/2060484521129332833) ⭐️ 8.0/10

斯坦福 AI 实验室宣布推出 GPIC（巨型许可图像语料库），包含 1 亿个由最先进视觉语言模型标注的训练图文对，并附带一个视觉生成基准。 GPIC 提供了一个大规模、许可开放的图像数据集，支持视觉生成建模的公平比较和可扩展研究，满足了现代大规模生成模型时代对稳定、可获取资源的需求。 该数据集包含约 28 万亿像素，包括 1 亿训练样本、20 万验证样本和 100 万测试样本，全部经过安全过滤、去重，并集中托管在 Hugging Face 上。

twitter · StanfordAILab · May 29, 22:12

**背景**: 视觉生成建模需要大规模、多样且高质量的图文数据集。以往的 COCO 或 LAION 等数据集在规模、许可或标注质量上存在局限。GPIC 通过使用视觉语言模型为许可开放的互联网图像生成标注，解决了这些问题，确保了一个大规模且干净的语料库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gpic.stanford.edu/">GPIC: A Giant Permissive Image Corpus for Visual Generation</a></li>
<li><a href="https://arxiv.org/abs/2605.30341">GPIC: A Giant Permissive Image Corpus for Visual Generation</a></li>
<li><a href="https://www.machinebrief.com/news/gpic-a-dataset-thats-changing-the-game-for-visual-generative-qpi0">GPIC: A Dataset That's Changing the Game for Visual...</a></li>

</ul>
</details>

**社区讨论**: 社区对此表示兴奋，一位研究者指出，在 GPIC 上训练一个 epoch 的成本相当于在以前数据集上训练 100 个 epoch，凸显了其效率以及成为新标准基准的潜力。

**标签**: `#AI`, `#Computer Vision`, `#Dataset`, `#Visual Generation`, `#Benchmark`

---

<a id="item-2"></a>
## [联邦研究资助拟需政治批准](https://twitter.com/ylecun/status/2060764165778915335) ⭐️ 7.0/10

一项拟议的政策变更将要求每项联邦研究资助在发放前获得政治批准，这可能改变美国科学资助的格局。 这一转变可能将政治考量引入科学资助决策，威胁到作为美国研究卓越基石、基于同行评议的评审体系。 该提案由 Catharine Young 博士强调，并由 Yann LeCun 转发，建议所有联邦研究资助都需要政治批准，但具体实施细节尚不明确。

twitter · ylecun · May 30, 16:43

**背景**: 美国的联邦研究资助通常通过评估科学价值的同行评议过程授予。引入政治批准可能会使科学资助政治化，可能影响研究方向和学术自由。

**社区讨论**: 该推文获得了大量转发（449 次），表明科学界对基于价值的资助可能受到侵蚀表现出强烈兴趣和担忧。

**标签**: `#research policy`, `#science funding`, `#government`, `#academia`

---

<a id="item-3"></a>
## [微软开源 SkillOpt，革新 AI 智能体学习方式](https://twitter.com/RodmanAi/status/2060603132124750283) ⭐️ 7.0/10

微软开源了 SkillOpt 系统，该系统通过训练一个 markdown 文件而非重新训练底层模型来提升 AI 智能体性能。它利用学习率、小批量数据和验证检查等技术来优化自然语言技能文档。 这种方法显著降低了改进 AI 智能体的成本和复杂性，因为它避免了昂贵的模型重新训练。它可能加速开发更强大、更适应性强的 AI 智能体，应用于各种场景。 SkillOpt 将紧凑的自然语言技能文档视为冻结语言智能体的可训练状态，然后通过轨迹执行、反思、有界编辑和保留验证门进行学习。最终输出是一个可部署的 best_skill.md 文件。

twitter · RodmanAi · May 30, 06:04

**背景**: 传统的 AI 智能体改进通常需要微调大型语言模型，计算成本高昂。SkillOpt 转而优化基于文本的技能文档来指导智能体行为，使过程更高效、更易用。Markdown 文件在智能体 AI 中越来越被用于持久化规则、工作流和提示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/SkillOpt">GitHub - microsoft/SkillOpt: SkillOpt is a text-space ...</a></li>
<li><a href="https://arxiv.org/abs/2605.23904">[2605.23904] SkillOpt: Executive Strategy for Self-Evolving ...</a></li>
<li><a href="https://microsoft.github.io/SkillOpt/">SkillOpt | Executive Strategy for Self-Evolving Agent Skills</a></li>

</ul>
</details>

**标签**: `#AI`, `#Microsoft`, `#open-source`, `#machine learning`, `#agents`

---

<a id="item-4"></a>
## [杜克大学 Argus 机器人：20 条腿，无前后之分](https://twitter.com/lukas_m_ziegler/status/2060484890496324028) ⭐️ 6.0/10

杜克大学研究人员推出了 Argus 机器人，它受海胆启发，拥有 20 条可伸缩的腿，每条腿末端配备深度摄像头，能够实现全向移动和感知。 Argus 引入了一种名为“动态对称”的新设计原则，可能催生更坚固、更通用的机器人，用于搜救、探索及其他非结构化环境中的任务。 该机器人没有指定的前后上下之分，20 个摄像头提供近乎 360 度的视野。可伸缩的腿使其能够翻滚、攀爬，并穿越草地、沙地和湿地面等崎岖地形。

twitter · lukas_m_ziegler · May 29, 22:14

**背景**: 传统机器人通常模仿双侧对称（如人类、狗）或使用轮子/履带，这限制了它们在复杂环境中的机动性。Argus 从海胆中汲取灵感，海胆具有径向对称性，可以向任何方向移动。“动态对称”的概念侧重于均匀的动作而非静态形状，使机器人能够根据环境调整运动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pratt.duke.edu/news/argus-robot-design/">Omnidirectional, Sea-Urchin-Like Robot Defies Traditional ...</a></li>
<li><a href="https://apnews.com/article/robot-duke-argus-6ba9651ba6553ebc4405ffc07a26afed">Duke engineers develop robot with 20 legs and eyes | AP News</a></li>
<li><a href="https://www.zmescience.com/science/news-science/20-legged-robot-argus/">This Weird 20- Legged Robot Moves Like Nothing Else on Earth and It...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#research`, `#bio-inspired`, `#Duke University`

---

<a id="item-5"></a>
## [美的集团推出六臂人形机器人 MIRO U](https://twitter.com/lukas_m_ziegler/status/2060350452202365420) ⭐️ 6.0/10

美的集团发布了 MIRO U，这是一款专为工业装配任务设计的六臂人形机器人，能够用下肢搬运重型部件，用上肢进行精细装配。 这款机器人挑战了人形机器人领域传统的 1:1 人类模仿理念，优先考虑工业实用性和效率而非拟人化设计，有望显著提升工厂生产效率。 MIRO U 具备 360 度旋转、稳定垂直升降和快速换刀能力，计划于 2025 年 12 月底在美的无锡洗衣机工厂部署。

twitter · lukas_m_ziegler · May 29, 13:20

**背景**: 人形机器人通常设计为双臂双腿以模仿人类形态。美的 MIRO U 打破了这一惯例，增加了四只手臂，并使用轮子而非腿部进行移动，以最大化工业效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scmp.com/tech/tech-trends/article/3335721/chinese-home-appliance-giant-midea-unveils-six-arm-robot-factory-work">Chinese home appliance giant Midea unveils 6-arm robot for factory work | South China Morning Post</a></li>
<li><a href="https://www.humanoidsdaily.com/news/midea-s-super-humanoid-miro-u-has-six-arms-and-wheels-challenges-1-1-human-mimicry">Midea’s ‘Super Humanoid’ MIRO U Has Six Arms and Wheels, Challenges 1:1 Human Mimicry | Humanoids Daily</a></li>
<li><a href="https://indiandefencereview.com/mideas-super-humanoid-six-arms-zero-rest/">Midea’s Super Humanoid: Six Arms, Zero Rest, and More Factory Output!</a></li>

</ul>
</details>

**标签**: `#robotics`, `#humanoid robot`, `#industrial automation`

---

<a id="item-6"></a>
## [Anthropic 的 31 页提示指南提炼为 9 条规则](https://twitter.com/RodmanAi/status/2060263146103980092) ⭐️ 6.0/10

Twitter 用户 @RodmanAi 将 Anthropic 的 31 页提示指南总结为 9 条实用规则，例如“命名输出而非任务”，以改进提示工程。 这一总结使 Anthropic 的最佳实践更易于广泛受众获取，帮助开发者和 AI 用户为大型语言模型编写更有效的提示。 第一条规则建议指定期望的输出格式（例如线程、表格、电子邮件、JSON），而不是描述任务，从而获得更清晰的结果。

twitter · RodmanAi · May 29, 07:33

**背景**: 提示工程是设计输入以引导 AI 模型产生期望输出的实践。Anthropic 是一家领先的 AI 公司，发布了关于该主题的 31 页综合指南，该 Twitter 帖子将其浓缩为可操作的规则。

**标签**: `#prompt engineering`, `#Anthropic`, `#AI`, `#LLM`, `#best practices`

---

<a id="item-7"></a>
## [机器人手：难造，却不可或缺](https://twitter.com/lukas_m_ziegler/status/2060358895797784770) ⭐️ 5.0/10

Chris Paxton 发布了一篇博客文章，探讨了为什么制造好的机器人手极其困难，以及为什么它们对于先进机器人技术仍然必不可少。 这个话题对机器人领域至关重要，因为灵巧操作仍然是许多实际应用（从制造业到医疗保健）的瓶颈。 这篇博客文章可能涵盖了机械复杂性、传感器集成和控制挑战，以及成本、耐用性和灵巧性之间的权衡。

twitter · lukas_m_ziegler · May 29, 13:53

**背景**: 机器人手因其需要平衡力量、精度和灵敏度，且常需模仿人手的 27 个自由度，而闻名于工程难度。目前大多数机器人夹爪是简单的爪子或吸盘，缺乏完成诸如组装精密电子设备或进行手术等任务的灵巧性。

**标签**: `#robotics`, `#robot hands`, `#engineering`

---

<a id="item-8"></a>
## [SpaceX 用猎鹰 9 号发射 24 颗星链卫星](https://twitter.com/SpaceX/status/2060766975404462459) ⭐️ 5.0/10

SpaceX 成功用猎鹰 9 号火箭从加利福尼亚发射了 24 颗星链卫星，并确认部署成功。 此次发射延续了 SpaceX 快速扩展星链星座的进程，该星座旨在提供全球宽带互联网覆盖。 猎鹰 9 号第一级可能降落在无人船上，但未明确说明；此次任务使已发射的星链卫星总数超过 6000 颗。

twitter · SpaceX · May 30, 16:55

**背景**: 星链是由 SpaceX 运营的卫星互联网星座，为服务不足的地区提供低延迟宽带。猎鹰 9 号是一种可重复使用的两级火箭，已成为 SpaceX 发射的主力。

**标签**: `#SpaceX`, `#Starlink`, `#satellite launch`, `#Falcon 9`

---

<a id="item-9"></a>
## [ESMFold2 基准测试困惑得到澄清](https://twitter.com/ylecun/status/2060622786196918445) ⭐️ 5.0/10

Sylvain Gariel 发推文称，他花了一段时间才理解人们对 ESMFold2 的热情，因为最初的基准测试数据看起来并不出色。Yann LeCun 转发了这一观察。 这凸显了在 AI 蛋白质折叠领域仔细进行基准测试的重要性，因为初步结果可能具有误导性。同时也表明，即使是专家也需要时间来评估像 ESMFold2 这样的新模型。 ESMFold2 是 Meta AI 开发的蛋白质结构预测模型，兼具速度和准确性。该推文暗示，最初的基准测试数据可能未能反映其真实性能。

twitter · ylecun · May 30, 07:22

**背景**: 蛋白质折叠预测是计算生物学中的一个关键挑战。ESMFold2 使用语言模型方法从氨基酸序列预测蛋白质结构，与 AlphaFold2 等模型竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tamarind.bio/tools/esmfold2">ESMFold 2 Online | Next Generation Structure Prediction</a></li>
<li><a href="https://310.ai/blog/benchmarking-machine-learning-methods-for-protein-folding-a-comparative-study-of-esmfold-omegafold-and-alphafold">Benchmarking Machine Learning Methods for Protein Folding ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#protein folding`, `#ESMFold2`

---

<a id="item-10"></a>
## [OpenAI Codex 现可通过 Ollama 免费本地运行](https://twitter.com/RodmanAi/status/2060711654908912065) ⭐️ 5.0/10

OpenAI 的 Codex 此前需要 API 访问，现在可以通过 Ollama 免费本地运行，支持 DeepSeek V4、Gemma 4 和 Qwen 3.6 等开源模型。 这消除了 API 成本和速率限制，为开发者提供私密、离线的 AI 编码辅助，可能加速本地 AI 工具的普及。 设置过程包括使用 Ollama 本地运行开源模型，然后将 Codex CLI 或 Codex App 连接到本地模型。Codex CLI 支持 macOS、Windows 和 Linux。

twitter · RodmanAi · May 30, 13:15

**背景**: Codex 是 OpenAI 的 AI 编码代理，最初需要订阅和云 API。Ollama 是一个在个人电脑上本地运行大语言模型的平台，提供命令行界面和 REST API。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/codex/cli">CLI – Codex | OpenAI Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ollama">Ollama - Wikipedia</a></li>
<li><a href="https://ollama.com/">Ollama</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#Ollama`, `#local AI`, `#open-source`

---

<a id="item-11"></a>
## [Renishaw REVO CMM 实现高速零件检测](https://twitter.com/lukas_m_ziegler/status/2060793388048519278) ⭐️ 4.0/10

@lukas_m_ziegler 的一条推文强调了 Renishaw REVO 五轴 CMM 系统，该系统采用 Renscan5 技术，以比传统 CMM 快得多的速度检测零件。 该技术可显著缩短制造业中的检测周期时间，在不牺牲精度的前提下提高产量，这对航空航天和汽车等行业的质量控制至关重要。 REVO 系统采用五轴测头和测针，可在高速下最大限度地减少动态误差，实现不到传统 CMM 一半的循环时间，同时保持高精度。

twitter · lukas_m_ziegler · May 30, 18:40

**背景**: 坐标测量机 (CMM) 用于测量制造零件的物理几何形状。传统 CMM 移动整个机器结构来捕捉每个测量点，速度较慢。Renishaw REVO 系统则使用快速、轻便的五轴测针独立移动，大幅缩短检测时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=FUgWBlEewyk">Renishaw Revo CMM Demonstration - YouTube</a></li>
<li><a href="https://www.cmmxyz.com/new-cmms/probing-and-accessories/5-axis-systems/renishaw-revo/">Renishaw REVO 5-Axis Measurement System | CMMXYZ</a></li>
<li><a href="https://www.thome-precision.com/Renishaw-Revo.html">THOME Präzision GmbH | Renishaw REVO</a></li>

</ul>
</details>

**标签**: `#manufacturing`, `#CMM`, `#inspection`, `#Renishaw`

---

<a id="item-12"></a>
## [SpaceX 发射 29 颗星链卫星](https://twitter.com/SpaceX/status/2060342610623959109) ⭐️ 4.0/10

SpaceX 在推特上宣布，使用猎鹰 9 号火箭从佛罗里达发射了 29 颗星链卫星进入近地轨道，发射后不久确认卫星已部署。 此次发射继续快速扩展星链星座，该星座旨在提供全球宽带互联网覆盖。每次发射都增加了容量，并改善了服务不足地区用户的服务质量。 猎鹰 9 号第一级是可重复使用的，此次任务可能使用了经过飞行验证的助推器，但未提供具体助推器细节。星链卫星在约 550 公里高度的近地轨道运行。

twitter · SpaceX · May 29, 12:48

**背景**: 猎鹰 9 号是 SpaceX 设计的部分可重复使用两级火箭，是 2020 年代发射次数最多的轨道火箭。星链是由 SpaceX 运营的卫星互联网星座，迄今已发射超过 10,000 颗卫星，为约 150 个国家提供宽带服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falcon_9">Falcon 9 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#satellite`, `#launch`

---

<a id="item-13"></a>
## [埃克森美孚警告两周内石油末日](https://twitter.com/ylecun/status/2060784862483632292) ⭐️ 2.0/10

Yann LeCun 转发了一条消息，强调埃克森美孚警告称，由于一个关键石油咽喉要道的关闭，世界将在两周内面临石油末日。 这条新闻与技术受众无关，因为它涉及石油供应而非软件工程、AI/ML 或系统研究，与社区相关性低。 该推文引用了埃克森美孚关于关闭世界最重要石油咽喉要道的声明，但没有提供具体地点或事件的技术细节或背景。

twitter · ylecun · May 30, 18:06

**标签**: `#off-topic`, `#oil`, `#energy`

---

<a id="item-14"></a>
## [杨立昆转发批评 MAGA 言论](https://twitter.com/ylecun/status/2060718725884699003) ⭐️ 2.0/10

杨立昆转发了一条批评 MAGA 运动扭曲现实和道德的帖子，并提及自己作为科学家在治疗和疫苗方面的工作。 这条推文与 AI/ML 社区无关，技术相关性低，但反映了 LeCun 的个人政治立场。 该推文仅为转发，无额外技术内容，原帖似乎是政治评论。

twitter · ylecun · May 30, 13:43

**标签**: `#politics`, `#twitter`, `#off-topic`

---

<a id="item-15"></a>
## [推文对比 2024 年与 2026 年美国经济](https://twitter.com/ylecun/status/2060615788956991976) ⭐️ 2.0/10

Yann LeCun 转发了一条推文，对比了 2024 年和 2026 年美国经济指标：GDP 增速从 2.8%降至 1.6%，通胀率从 2.9%升至 3.8%，工资增长放缓。 这条推文凸显了经济可能放缓及滞胀风险，可能影响 AI/ML 生态系统的技术投资、招聘和消费支出。 数据点来自 Jared Ryan Sears，似乎源自美国政府统计；推文中未提供来源或方法。

twitter · ylecun · May 30, 06:54

**背景**: GDP 增长、通胀和工资趋势是关键的宏观经济指标。增长放缓与通胀上升并存常被称为滞胀，可能导致失业率上升和企业投资减少。

**标签**: `#economy`, `#politics`, `#twitter`

---

<a id="item-16"></a>
## [斯坦福 AI 实验室发布无上下文链接推文](https://twitter.com/StanfordAILab/status/2060431489544925263) ⭐️ 1.0/10

斯坦福 AI 实验室发布了一条推文，仅包含一个外部文章的链接，没有任何描述或上下文，未提供实质性信息。 这条推文对读者缺乏价值，因为它没有提供任何关于链接内容的见解，降低了其潜在影响力和参与度。 该推文因参与度低且无讨论而获得 1.0/10 的评分，仅包含一个 URL，无附加文字。

twitter · StanfordAILab · May 29, 18:42

**标签**: `#tweet`, `#link`, `#low-value`

---