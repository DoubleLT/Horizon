---
layout: default
title: "Horizon Summary: 2026-06-05 (ZH)"
date: 2026-06-05
lang: zh
---

> From 34 items, 30 important content pieces were selected

---

1. [Google DeepMind 发布 Gemma 4 12B 无编码器多模态模型](#item-1) ⭐️ 8.0/10
2. [StereoPolicy 为机器人视觉添加几何线索](#item-2) ⭐️ 7.0/10
3. [MicroAGI 推出研究奖学金，提供高达 200 万美元计算和机器人硬件](#item-3) ⭐️ 7.0/10
4. [SpaceX 将于 8 月用猎鹰重型发射罗曼太空望远镜](#item-4) ⭐️ 7.0/10
5. [Yann LeCun 分享关于大脑世界模型的问题](#item-5) ⭐️ 7.0/10
6. [视觉语言模型在比较视觉推理上表现不佳](#item-6) ⭐️ 7.0/10
7. [AI 研究员称静态基准正在消亡](#item-7) ⭐️ 7.0/10
8. [吴恩达推出高效 LLM 服务课程](#item-8) ⭐️ 7.0/10
9. [Robotiq 发布 TSF-85 数字孪生用于 NVIDIA Isaac Sim](#item-9) ⭐️ 6.0/10
10. [噪声优化恢复崩溃的扩散模型](#item-10) ⭐️ 6.0/10
11. [VLM 在图像比较上存在局限](#item-11) ⭐️ 6.0/10
12. [用 Claude 自动化商业分析](#item-12) ⭐️ 6.0/10
13. [Anthropic 工程师：为 Claude 构建自提示系统](#item-13) ⭐️ 6.0/10
14. [Mac Mini + Ollama + Claude Code 大幅降低 AI 成本](#item-14) ⭐️ 6.0/10
15. [SpaceX 宣传月球、火星及更远的创新](#item-15) ⭐️ 5.0/10
16. [Starlink 全球活跃客户突破 1200 万](#item-16) ⭐️ 5.0/10
17. [开发者 8 分钟开箱并设置 NVIDIA DGX Spark](#item-17) ⭐️ 5.0/10
18. [CoRL 2026 主题演讲阵容公布](#item-18) ⭐️ 4.0/10
19. [ICRA 上惊现“兰博基尼”级机械手](#item-19) ⭐️ 4.0/10
20. [SpaceX 发射 29 颗星链卫星](#item-20) ⭐️ 4.0/10
21. [斯坦福 AI 实验室聚焦 CVPR 2026 论文](#item-21) ⭐️ 4.0/10
22. [ClaudeDevs 将触发词改为 'ultracode'](#item-22) ⭐️ 4.0/10
23. [10 个提升 AI Agent 技能的 GitHub 仓库](#item-23) ⭐️ 4.0/10
24. [免费 API 替代付费 Agent 工具指南](#item-24) ⭐️ 3.0/10
25. [SpaceX 从加州发射 24 颗星链卫星](#item-25) ⭐️ 3.0/10
26. [Yann LeCun 转发 Ted Chiang 关于 AI 意识的观点](#item-26) ⭐️ 3.0/10
27. [马斯克关于哈达玛思维的模糊推文](#item-27) ⭐️ 2.0/10
28. [SpaceX 重申跨行星使命，提及星链与 AI](#item-28) ⭐️ 2.0/10
29. [Yann LeCun 转发政治抱怨](#item-29) ⭐️ 1.0/10
30. [政治转发缺乏技术相关性](#item-30) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [Google DeepMind 发布 Gemma 4 12B 无编码器多模态模型](https://twitter.com/GoogleDeepMind/status/2062203391913119894) ⭐️ 8.0/10

Google DeepMind 宣布推出 Gemma 4 12B，这是一个统一的无编码器多模态模型，旨在将高性能 AI 直接带到笔记本电脑上。 此次发布填补了边缘友好型小模型与大型 MoE 模型之间的空白，使消费级硬件也能具备强大的多模态能力。 Gemma 4 12B 用轻量级嵌入模块取代了传统的视觉编码器，并提供密集型和混合专家（MoE）两种架构。

twitter · GoogleDeepMind · Jun 3, 16:02

**背景**: 传统的多模态模型依赖独立的编码器（如视觉编码器）来处理不同类型的数据，这增加了复杂性和资源消耗。Gemma 4 12B 的无编码器设计通过将视觉信息直接集成到模型中，简化了架构，降低了延迟和内存占用，使其适合部署在笔记本电脑和边缘设备上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/">Introducing Gemma 4 12B: a unified, encoder-free multimodal model - Google Blog</a></li>
<li><a href="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4-12b">A Visual Guide to Gemma 4 12B - by Maarten Grootendorst</a></li>
<li><a href="https://huggingface.co/google/gemma-4-12B">google/gemma-4-12B · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: Reddit 和 Hacker News 上的社区对无编码器方法表示兴奋，称其“非常酷”且是长期以来最令人兴奋的模型之一。一些评论者指出，其编码性能可能不如其他小型模型，如 Qwen 3.6 35B A3B 或 Gemma 4 26B A4B。

**标签**: `#AI`, `#multimodal`, `#Google DeepMind`, `#Gemma`, `#machine learning`

---

<a id="item-2"></a>
## [StereoPolicy 为机器人视觉添加几何线索](https://twitter.com/drfeifei/status/2062283541069930791) ⭐️ 7.0/10

研究人员推出了 StereoPolicy，该方法通过从立体视觉中融入几何线索来增强机器人操作策略，无需显式的 3D 重建或校准的深度感知。 该方法将 2D 预训练表示与 3D 几何理解相结合，有望提高机器人操作任务的精度和鲁棒性，这对于桌面操作和双臂移动操作等实际应用至关重要。 StereoPolicy 使用基于交叉注意力的立体变换器融合同步立体图像的左右特征，隐式捕获空间对应关系和视差线索。该方法在桌面操作和双臂移动操作的真实机器人实验中得到了验证。

twitter · drfeifei · Jun 3, 21:21

**背景**: 单目 RGB 图像通常缺乏精确操作所需的深度线索，而 RGB-D 和点云可能噪声大或脆弱。立体视觉通过使用两个摄像头从视差推断深度，提供了一种可扩展且鲁棒的替代方案。StereoPolicy 利用预训练的 2D 视觉编码器并融合立体特征，无需显式 3D 重建即可提供几何感知表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.09989">[2605.09989] StereoPolicy: Improving Robotic Manipulation ... StereoPolicy stereopolicy.github.io/README.md at main · stereopolicy ... Fei-Fei Li Introduces StereoPolicy for Stereo Cues in Robot ... Excited to introduce StereoPolicy, led by @EvansXuHan. ... STEREOTYPES AND POLITICS - National Bureau of Economic Research StereoPolicy: Improving Robotic Manipulation Policies via ...</a></li>
<li><a href="https://stereopolicy.github.io/">StereoPolicy</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#stereo vision`, `#machine learning`, `#robotics`

---

<a id="item-3"></a>
## [MicroAGI 推出研究奖学金，提供高达 200 万美元计算和机器人硬件](https://twitter.com/lukas_m_ziegler/status/2062210959125459348) ⭐️ 7.0/10

专注于具身 AI 和机器人数据基础设施的初创公司 MicroAGI 宣布启动其研究奖学金项目，为入选者提供高达 200 万美元的计算资源和机器人硬件。 该奖学金为 AGI 研究提供了大量资源，可能加速具身 AI 和实际机器人部署的进展。这标志着私营公司直接资助开放研究以推动通用人工智能发展的趋势日益增长。 除了计算和硬件资源外，该奖学金还包括使用 MicroAGI 的评估系统和一对一支持。具体的申请标准和截止日期尚未公布。

twitter · lukas_m_ziegler · Jun 3, 16:33

**背景**: MicroAGI 是一家位于德国慕尼黑的数据研究实验室，致力于端到端物理 AGI，专注于可靠的现实世界部署。该公司专门捕获大规模多模态人类演示数据，用于具身 AI 训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microagi.ai/">microagi</a></li>
<li><a href="https://grokipedia.com/page/MicroAGI">MicroAGI</a></li>

</ul>
</details>

**标签**: `#AGI`, `#research fellowship`, `#compute`, `#robotics`

---

<a id="item-4"></a>
## [SpaceX 将于 8 月用猎鹰重型发射罗曼太空望远镜](https://twitter.com/SpaceX/status/2062604634036851042) ⭐️ 7.0/10

SpaceX 在推特上宣布，猎鹰重型火箭最早将于 2026 年 8 月从佛罗里达州 39A 发射台发射 NASA 的南希·格雷斯·罗曼太空望远镜。 这项任务意义重大，因为罗曼太空望远镜是 NASA 的旗舰级天文台，旨在研究暗能量、系外行星和宇宙结构，而使用猎鹰重型发射它展示了该火箭执行高优先级科学任务的能力。 罗曼太空望远镜配备 2.4 米镜面和两个仪器：一个 300.8 百万像素的广角相机和一个用于系外行星成像的日冕仪。猎鹰重型是一种部分可重复使用的超重型运载火箭，起飞推力超过 500 万磅。

twitter · SpaceX · Jun 4, 18:37

**背景**: 南希·格雷斯·罗曼太空望远镜，原名 WFIRST，是以 NASA 首位天文学主任命名的红外空间天文台。它计划发射到日地 L2 轨道，视场比哈勃大 100 倍。猎鹰重型由 SpaceX 开发，是现役最强大的火箭之一，能将近 64 吨的载荷送入轨道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nancy_Grace_Roman_Space_Telescope">Nancy Grace Roman Space Telescope</a></li>
<li><a href="https://en.wikipedia.org/wiki/Falcon_Heavy">Falcon Heavy</a></li>
<li><a href="https://www.spacex.com/vehicles/falcon-heavy">Falcon Heavy - SpaceX</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Falcon Heavy`, `#Nancy Grace Roman Space Telescope`, `#space mission`

---

<a id="item-5"></a>
## [Yann LeCun 分享关于大脑世界模型的问题](https://twitter.com/ylecun/status/2062541443613270043) ⭐️ 7.0/10

Yann LeCun 转发了 Saining Xie 的一个问题，询问大脑如何从不完整且有噪声的视觉观察中构建和跟踪世界的内部状态。 这个问题对神经科学和人工智能都至关重要，因为理解大脑如何构建内部世界模型可以启发更鲁棒、更高效的 AI 系统，使其能够处理不确定性和不完整信息。 这条推文简短且缺乏详细讨论，但它突显了视觉感知和认知科学中的一个基本挑战，这一挑战在近期关于大脑和机器内部世界模型的跨学科研究中得到了探讨。

twitter · ylecun · Jun 4, 14:26

**背景**: 内部世界模型指的是大脑创建并维持外部环境心理表征的能力，从而实现预测和规划。近期研究，例如 2024 年发表在《Neuron》上的一篇论文，汇集了神经科学家和 AI 研究人员，共同研究生物和人工系统中的这些模型。该问题特别关注大脑如何处理不完整或有噪声的视觉输入以构建连贯的内部状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/39024919/">Internal world models in humans, animals, and AI - PubMed</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0896627324004549">Internal world models in humans, animals, and AI - ScienceDirect</a></li>
<li><a href="https://neurosciencenews.com/ai-internal-world-models-understanding-30581/">How AI "Brain States" Decode Reality - Neuroscience News</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#AI`, `#cognitive science`, `#visual perception`

---

<a id="item-6"></a>
## [视觉语言模型在比较视觉推理上表现不佳](https://twitter.com/berkeley_ai/status/2062653484584030449) ⭐️ 7.0/10

Joey 教授的一条推文指出，视觉语言模型（VLM）在比较视觉推理任务（例如检测图像之间的差异）上表现得出奇地差。 这一局限性意义重大，因为比较推理是许多实际应用（如质量检测、医学影像和科学分析）的基础。它揭示了当前 VLM 能力中的一个关键缺口，研究人员需要加以解决。 该推文特别提到“检测差异类任务”是 VLM 难以应对的例子。虽然没有引用具体的基准或数据集，但这一说法与近期关于 VLM 在视觉比较中局限性的研究一致。

twitter · berkeley_ai · Jun 4, 21:51

**背景**: 视觉语言模型（VLM）结合视觉和语言来执行图像描述和视觉问答等任务。比较视觉推理涉及比较两个或多个图像以识别相似性或差异，这需要细粒度的感知和推理能力。现有的基准通常侧重于识别或描述，而非系统性比较，因此这是一个尚未充分探索的领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2509.22737">CompareBench: A Benchmark for Visual Comparison Reasoning in ...</a></li>
<li><a href="https://arxiv.org/html/2411.00238v1">Understanding the Limits of Vision Language Models Through ...</a></li>

</ul>
</details>

**标签**: `#visual language models`, `#AI limitations`, `#computer vision`, `#reasoning`

---

<a id="item-7"></a>
## [AI 研究员称静态基准正在消亡](https://twitter.com/berkeley_ai/status/2062358478631719262) ⭐️ 7.0/10

AI 研究员杨振发帖称静态基准因快速饱和而正在消亡，并提出评估和训练数据应共同进化。 这一观点揭示了当前 AI 评估实践中的关键缺陷，敦促社区采用能跟上模型改进步伐的动态基准。 基准饱和发生在模型获得接近满分时，使得进一步区分变得不可能；共同进化意味着随着训练数据和模型的进化而更新基准。

twitter · berkeley_ai · Jun 4, 02:19

**背景**: 像 GLUE 或 SuperGLUE 这样的静态基准是用于评估 AI 模型的固定测试集。随着时间的推移，模型变得过于优秀，导致这些基准饱和，无法再衡量进展。共同进化的概念借鉴自生物学，建议评估方法应与其衡量的系统一起适应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mbrenndoerfer.com/writing/benchmark-saturation-ai-evaluation-metrics">Benchmark Saturation : AI Evaluation Metrics and Ceiling Effects...</a></li>
<li><a href="https://kili-technology.com/blog/ai-benchmarks-guide-the-top-evaluations-in-2026-and-why-theyre-not-enough">AI Benchmarks 2026: Top Evaluations and Their Limits</a></li>
<li><a href="https://www.emergentmind.com/topics/benchmark-saturation">Benchmark Saturation Overview</a></li>

</ul>
</details>

**标签**: `#AI benchmarks`, `#machine learning`, `#evaluation`, `#research`

---

<a id="item-8"></a>
## [吴恩达推出高效 LLM 服务课程](https://twitter.com/AndrewYNg/status/2062576164657664469) ⭐️ 7.0/10

吴恩达宣布了一门与 Red Hat 合作、由 Cedric Clyburn 讲授的新短期课程，内容是如何高效地为大量并发用户服务大语言模型。 该课程解决了部署 LLM 时的一个关键实际挑战：在高并发下实现低延迟和合理成本，这对实际应用至关重要。 该课程强调高效内存管理，指出一个 70B 参数的模型需要显著的内存优化。可能涵盖 PagedAttention 和连续批处理等技术。

twitter · AndrewYNg · Jun 4, 16:44

**背景**: 高效服务 LLM 具有挑战性，因为模型庞大且内存密集，尤其是键值缓存。像 PagedAttention（用于 vLLM）这样的技术允许非连续内存存储以提高吞吐量。该课程旨在教授此类优化方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.anyscale.com/llm/serving/intro">What is LLM serving? | Anyscale Docs</a></li>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory -efficient...</a></li>
<li><a href="https://www.rubrik.com/blog/ai/25/guide-how-to-serve-llms-faster-inference">LLM Serving Guide: How to Build Faster Inference for Open-source Models | Rubrik</a></li>

</ul>
</details>

**标签**: `#LLM serving`, `#efficiency`, `#course`, `#Red Hat`, `#deployment`

---

<a id="item-9"></a>
## [Robotiq 发布 TSF-85 数字孪生用于 NVIDIA Isaac Sim](https://twitter.com/lukas_m_ziegler/status/2062173943927095673) ⭐️ 6.0/10

Robotiq 发布了其 TSF-85 触觉传感器的数字孪生，用于 NVIDIA Isaac Sim，从而在机器人仿真中实现了触觉感知。 这一集成使 AI 模型能够在仿真过程中融入触觉反馈，从而提升机器人在现实世界中的抓取和操作能力。 TSF-85 传感器具有触觉单元阵列、1000 Hz 的滑移检测以及用于本体感知的 IMU，现已在 Isaac Sim 中以数字孪生形式提供。

twitter · lukas_m_ziegler · Jun 3, 14:05

**背景**: NVIDIA Isaac Sim 是一个基于 Omniverse 构建的仿真平台，用于开发和测试 AI 驱动的机器人。触觉感知对于灵巧操作至关重要，但大多数机器人仿真仅依赖视觉。数字孪生通过精确建模物理传感器来弥合仿真与现实的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.robotiq.com/robotiq-releases-tsf-85-digital-twin-on-nvidia-isaac-sim">Robotiq releases TSF-85 Digital Twin on NVIDIA Isaac Sim</a></li>
<li><a href="https://developer.nvidia.com/isaac/sim">Isaac Sim - Robotics Simulation and Synthetic Data Generation - NVIDIA Developer</a></li>
<li><a href="https://robotiq.com/tactile-sensor-fingertips">Tactile Sensor Fingertips | Robotiq</a></li>

</ul>
</details>

**标签**: `#robotics`, `#tactile sensing`, `#simulation`, `#NVIDIA Isaac Sim`

---

<a id="item-10"></a>
## [噪声优化恢复崩溃的扩散模型](https://twitter.com/berkeley_ai/status/2062358667077533843) ⭐️ 6.0/10

一篇 CVPR 2026 论文提出在推理时优化初始随机噪声，以恢复已崩溃扩散模型的多样性，这些模型对同一文本提示会生成重复图像。 这项工作解决了文本到图像模型中的模式崩溃关键问题，提供了一种无需重新训练的后训练恢复方法，可提高输出多样性，惠及研究人员和从业者。 该方法称为“崩溃恢复的噪声优化”，仅在推理时通过优化初始噪声潜变量来运作，并在表现出崩溃的已训练扩散模型上进行了演示。

twitter · berkeley_ai · Jun 4, 02:19

**背景**: 扩散模型是一类生成模型，通过逐步去噪随机噪声来生成图像。模式崩溃指模型仅生成有限输出，失去多样性。先前工作已对崩溃进行经验研究，但本文引入了一种新颖的推理时优化方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://akoepke.github.io/divgen/index.html">It's Never Too Late: Noise Optimization for Collapse Recovery</a></li>
<li><a href="https://huggingface.co/papers/2601.00090">It's Never Too Late: Noise Optimization for Collapse Recovery ...</a></li>
<li><a href="https://arxiv.org/pdf/2602.16601">Error Propagation and Model Collapse in Diffusion Models: A ...</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#CVPR`, `#noise optimization`, `#machine learning`

---

<a id="item-11"></a>
## [VLM 在图像比较上存在局限](https://twitter.com/berkeley_ai/status/2062358241238225125) ⭐️ 6.0/10

一条推文指出，人类通过来回观察来比较图像，而许多开源视觉语言模型（VLM）则独立编码每张图像，将比较推迟到后续阶段。 这一观察指出了当前 VLM 在执行细粒度图像比较方面的根本性局限，而该能力对于视觉推理和变化检测等任务至关重要。 该推文特别提到“开源权重 VLM”会独立编码图像，这与人类的视觉比较行为形成对比。

twitter · berkeley_ai · Jun 4, 02:18

**背景**: 视觉语言模型（VLM）结合了视觉和文本理解，通常先对每张图像使用独立的编码器，再进行信息融合。许多开源权重 VLM（如 LLaVA 和 Qwen-VL）独立处理图像，缺乏跨图像注意力机制，这可能阻碍直接比较任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/spaces/opencompass/open_vlm_leaderboard">Open VLM Leaderboard - a Hugging Face Space by opencompass</a></li>
<li><a href="https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models">Multimodal AI: The Best Open-Source Vision Language Models in 2026 - BentoML</a></li>

</ul>
</details>

**标签**: `#VLM`, `#image comparison`, `#AI limitations`

---

<a id="item-12"></a>
## [用 Claude 自动化商业分析](https://twitter.com/ClaudeDevs/status/2062274312363770064) ⭐️ 6.0/10

一篇新博客文章分享了使用 Claude 自动化商业分析的最佳实践，涵盖了构建数据分析代理所需的技能、数据基础和评估方法。 该指南为希望利用 AI 进行商业分析的开发者和分析师提供了实用见解，有望提升组织的效率和决策能力。 博客文章聚焦于三个领域：代理所需的技能、数据基础和评估方法，但并未引入新的技术突破。

twitter · ClaudeDevs · Jun 3, 20:44

**背景**: 商业分析涉及利用数据驱动业务决策。像 Claude 这样的 AI 代理可以自动化数据分析任务，但构建有效的代理需要精心设计技能、数据处理和评估指标。

**标签**: `#AI`, `#business analytics`, `#Claude`, `#automation`, `#best practices`

---

<a id="item-13"></a>
## [Anthropic 工程师：为 Claude 构建自提示系统](https://twitter.com/RodmanAi/status/2062529865749061860) ⭐️ 6.0/10

一位 Anthropic 工程师指出，用户使用 Claude 时最大的错误是手动提示，而不是构建一个能自我提示的系统。 这一见解将范式从手动提示工程转向自动化自提示系统，可能大幅提升 AI 交互的效率和可扩展性。 该工程师指出，大多数用户打开 Claude，输入一个提示，得到一个回答；而 Anthropic 工程师正在运行自动生成提示的系统。

twitter · RodmanAi · Jun 4, 13:40

**背景**: 自提示 AI，也称为自动提示或递归自我改进，允许 AI 系统根据初始输入自主创建和执行提示。这种方法用于 Auto-GPT 等工具，无需人工干预即可完成复杂任务。Anthropic 还发布了针对 Claude 的提示工程教程和最佳实践。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.yeschat.ai/blog-The-Rise-of-SelfPrompting-AI-How-AutoGPT-and-Other-Models-Are-Pioneering-a-New-Era-of-Artificial-Intelligence-2629">The Rise of Self-Prompting AI: How Auto-GPT and Other Models Are Pioneering a New Era of Artificial Intelligence</a></li>
<li><a href="https://github.com/anthropics/prompt-eng-interactive-tutorial">GitHub - anthropics/prompt-eng-interactive-tutorial: Anthropic's Interactive Prompt Engineering Tutorial · GitHub</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices">Prompting best practices - Claude API Docs</a></li>

</ul>
</details>

**标签**: `#prompt engineering`, `#AI`, `#Claude`, `#Anthropic`

---

<a id="item-14"></a>
## [Mac Mini + Ollama + Claude Code 大幅降低 AI 成本](https://twitter.com/RodmanAi/status/2062417722076750095) ⭐️ 6.0/10

开发者发现，通过在 599 美元的 Mac Mini 上运行 Ollama，并将 Claude Code 指向 localhost，他们可以将每月 AI 订阅费用从 459 美元降至仅 23 美元。 这种变通方法通过大幅降低成本，使 AI 编程助手的访问更加民主化，让个人开发者和小型团队无需昂贵的云订阅即可使用强大的 AI 工具。 该方案使用 Ollama 在 Mac Mini 上本地运行开源权重的大语言模型，Claude Code 连接到本地 Ollama API 而非 Anthropic 的云服务，从而消除了按 token 计费的费用。

twitter · RodmanAi · Jun 4, 06:14

**背景**: Ollama 是一个在个人电脑上本地运行大语言模型的平台，提供命令行界面和 REST API。Claude Code 是 Anthropic 的智能编码工具，通常需要云订阅。通过将两者结合，开发者可以使用 Claude Code 的界面配合本地托管的模型，从而绕过订阅费用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ollama">Ollama - Wikipedia</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**社区讨论**: 推文下的 12 条回复普遍对节省成本表示兴奋，一些用户指出与云 GPU 相比，Mac Mini 的硬件性能可能有限。少数评论者质疑这种设置是否违反了 Claude Code 的服务条款。

**标签**: `#AI`, `#cost optimization`, `#local inference`, `#Ollama`, `#Claude Code`

---

<a id="item-15"></a>
## [SpaceX 宣传月球、火星及更远的创新](https://twitter.com/SpaceX/status/2062666108683821373) ⭐️ 5.0/10

SpaceX 发布了一段宣传视频，强调其创新和技术进步，称这些正在重新定义地球上的产业，同时旨在月球、火星及更远的地方创造新产业。 这重申了 SpaceX 实现人类在其他星球定居的长期愿景，可能推动对太空探索的进一步投资和公众兴趣。 该视频在 Twitter 上分享，并附有了解更多信息的链接，但未提供新的技术细节或具体任务时间表。

twitter · SpaceX · Jun 4, 22:41

**背景**: SpaceX 是由埃隆·马斯克创立的私人航空航天制造商，以开发猎鹰 9 号和星舰等可重复使用火箭而闻名。该公司一直积极致力于实现其使生命多行星化的目标，并计划执行载人登月和火星任务。

**标签**: `#SpaceX`, `#space exploration`, `#innovation`

---

<a id="item-16"></a>
## [Starlink 全球活跃客户突破 1200 万](https://twitter.com/SpaceX/status/2062658979507953978) ⭐️ 5.0/10

Starlink 宣布其服务现已覆盖超过 160 个国家和地区，活跃客户数量突破 1200 万。 这一里程碑表明 Starlink 在卫星互联网市场的快速增长和日益增强的主导地位，可能对传统互联网服务提供商形成压力，并扩大欠发达地区的网络覆盖。 1200 万这一数字代表活跃客户而非总订阅用户，服务覆盖超过 160 个国家，包括许多偏远和农村地区。

twitter · SpaceX · Jun 4, 22:13

**背景**: Starlink 是 SpaceX 运营的卫星互联网星座，通过低地球轨道卫星网络提供低延迟宽带互联网服务，旨在覆盖传统互联网基础设施缺乏或不可靠的地区。

**标签**: `#Starlink`, `#satellite internet`, `#SpaceX`, `#milestone`

---

<a id="item-17"></a>
## [开发者 8 分钟开箱并设置 NVIDIA DGX Spark](https://twitter.com/RodmanAi/status/2062262849670639660) ⭐️ 5.0/10

一位中国开发者开箱了一台 NVIDIA DGX Spark，从零开始设置，安装了完整的机器人仿真栈，并在几分钟内让 AI 智能体运行起来，整个过程被记录在一段 8 分钟的视频中。 这一演示表明 NVIDIA 的个人 AI 超级计算机已变得触手可及，无需复杂的基础设施即可快速原型化机器人和 AI 应用。 DGX Spark 采用 NVIDIA Blackwell 架构，可提供高达千万亿次的 AI 性能，适合运行 Isaac Sim 等机器人仿真工具。

twitter · RodmanAi · Jun 3, 19:59

**背景**: NVIDIA DGX Spark 是一款紧凑型个人 AI 超级计算机，旨在让开发者能够在本地创建、测试和验证 AI 模型。它支持完整的 NVIDIA AI 软件栈，包括用于机器人仿真的 Isaac Sim 和用于机器人学习的 Isaac Lab。该设备旨在通过提供桌面级强大算力来普及 AI 开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/">Personal AI Supercomputer Powered by Blackwell | NVIDIA DGX Spark</a></li>
<li><a href="https://developer.nvidia.com/isaac/sim">Isaac Sim - Robotics Simulation and Synthetic Data Generation | NVIDIA Developer</a></li>
<li><a href="https://www.nvidia.com/en-us/use-cases/robotics-simulation/">Robotics Simulation | Use Case</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#DGX Spark`, `#robotics`, `#AI`, `#simulation`

---

<a id="item-18"></a>
## [CoRL 2026 主题演讲阵容公布](https://twitter.com/drfeifei/status/2062402192938832292) ⭐️ 4.0/10

机器人学习大会（CoRL）2026 公布了主题演讲阵容，包括 MIT 的 Russ Tedrake 和斯坦福大学的李飞飞。 这一阵容凸显了机器人学习和空间智能日益增长的重要性，两位演讲者都在该领域领导着有影响力的研究和初创公司。 CoRL 2026 将于 2026 年 11 月 9 日至 12 日在德克萨斯州奥斯汀的 JW 万豪酒店举行，摘要提交截止日期为 2026 年 5 月 26 日，论文提交截止日期为 2026 年 5 月 29 日。

twitter · drfeifei · Jun 4, 05:12

**背景**: 机器人学习大会（CoRL）是一年一度的国际会议，专注于机器人与机器学习的交叉领域。李飞飞是著名的计算机科学家，也是空间智能公司 World Labs 的联合创始人，该公司最近融资 10 亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.corl.org/">CoRL 2026</a></li>
<li><a href="https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf">Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a</a></li>
<li><a href="https://www.reuters.com/business/ai-pioneer-fei-fei-lis-world-labs-raises-1-billion-funding-2026-02-18/">AI pioneer Fei-Fei Li's World Labs raises $1 billion in funding</a></li>

</ul>
</details>

**标签**: `#robotics`, `#conference`, `#keynote`

---

<a id="item-19"></a>
## [ICRA 上惊现“兰博基尼”级机械手](https://twitter.com/lukas_m_ziegler/status/2062136369728602413) ⭐️ 4.0/10

用户@lukas_m_ziegler 发布推文，展示在 ICRA 会议上展出的一款外观引人注目的机械手，并将其比作兰博基尼。 这条推文捕捉了机器人领域中对美学的关注，反映出设计和视觉吸引力正成为机器人硬件的重要方面。 该机械手在顶级机器人会议 ICRA 上被发现，推文中提到了@wuji_global，可能是参展商或设计者。

twitter · lukas_m_ziegler · Jun 3, 11:36

**背景**: ICRA（IEEE 国际机器人与自动化会议）是机器人领域顶级学术会议之一，研究人员和公司在此展示前沿硬件和软件。将机械手比作兰博基尼，暗示其设计流畅高端，令人联想到豪华跑车。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/International_Conference_on_Robotics_and_Automation">International Conference on Robotics and Automation</a></li>
<li><a href="https://2025.ieee-icra.org/">2025 IEEE International Conference on Robotics and Automation ...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#robot hand`, `#ICRA`

---

<a id="item-20"></a>
## [SpaceX 发射 29 颗星链卫星](https://twitter.com/SpaceX/status/2062585343388319851) ⭐️ 4.0/10

SpaceX 在佛罗里达州发射了一枚猎鹰 9 号火箭，搭载 29 颗星链卫星并将其部署到轨道上。 此次发射扩大了星链星座，该星座旨在为全球（尤其是服务不足地区）提供宽带互联网覆盖。 猎鹰 9 号第一级可能尝试在无人船上着陆，但推文未确认成功。星链卫星是批量生产的，通常一次发射 20-60 颗。

twitter · SpaceX · Jun 4, 17:20

**背景**: 猎鹰 9 号是 SpaceX 开发的两级可重复使用火箭，于 2010 年首次发射。星链是 SpaceX 运营的卫星互联网星座，由数千颗低地球轨道小型卫星组成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falcon_9">Falcon 9 - Wikipedia</a></li>
<li><a href="https://spacex-rockets-docs.vercel.app/Rocket/Falcon+9">Falcon 9 | SpaceX</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#satellite`, `#launch`

---

<a id="item-21"></a>
## [斯坦福 AI 实验室聚焦 CVPR 2026 论文](https://twitter.com/StanfordAILab/status/2062226889058726172) ⭐️ 4.0/10

斯坦福 AI 实验室发布了一篇博客文章，展示了他们在 CVPR 2026 上被接收的论文。 这凸显了斯坦福在计算机视觉研究领域的持续贡献，尽管该公告本身缺乏技术细节。 该博客文章是一般性推广，没有具体的论文标题或技术摘要。

twitter · StanfordAILab · Jun 3, 17:36

**背景**: CVPR（计算机视觉与模式识别会议）是计算机视觉领域的顶级年度会议。斯坦福 AI 实验室定期在此发表有影响力的研究。

**标签**: `#CVPR`, `#computer vision`, `#Stanford`, `#academic papers`

---

<a id="item-22"></a>
## [ClaudeDevs 将触发词改为 'ultracode'](https://twitter.com/ClaudeDevs/status/2062257177788858398) ⭐️ 4.0/10

ClaudeDevs 将触发词从 'workflow' 改为 'ultracode'，以避免意外触发动态工作流。用户仍可在自然语言中使用 'workflow'，但只有 'ultracode' 会明确触发该功能。 这一更改通过减少误触来改善用户体验——日常对话中的 'workflow' 不再会意外启动动态工作流。同时，它为用户提供了更清晰、更有意地调用该功能的方式。 此更改在 Claude Code v2.1.160 中生效。'ultracode' 触发词还会启用更高的努力级别（xhigh），并为实质性任务编排动态工作流，且仅适用于当前会话。

twitter · ClaudeDevs · Jun 3, 19:36

**背景**: Claude Code 中的动态工作流允许 Claude 通过执行并行子代理并在返回结果前检查工作来处理复杂任务。原触发词 'workflow' 在日常语言中过于常见，导致频繁的意外触发。将其重命名为 'ultracode' 解决了这一问题，同时保留了该功能的强大能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/layzerzero105/claude-code-v21160-renamed-the-workflow-trigger-to-ultracode-every-scripted-prompt-that-288n">Claude Code v2.1.160 renamed the `workflow` trigger to ` ultracode</a></li>
<li><a href="https://claudefa.st/blog/guide/development/ultracode">Ultracode in Claude Code: Effort Setting Explained</a></li>
<li><a href="https://claude.com/blog/introducing-dynamic-workflows-in-claude-code">Introducing dynamic workflows | Claude</a></li>

</ul>
</details>

**标签**: `#AI tools`, `#UX`, `#Claude`

---

<a id="item-23"></a>
## [10 个提升 AI Agent 技能的 GitHub 仓库](https://twitter.com/RodmanAi/status/2062582654395183209) ⭐️ 4.0/10

@RodmanAi 在 Twitter 上发布了一个帖子，列出了 10 个用于学习 AI Agent 开发的 GitHub 仓库，包括一个完整的大语言模型代码笔记本和一个免费的 11 部分 AI Agent 入门课程。 这个精选列表为开发者提供了易于上手的实践资源，帮助他们快速开始构建 AI Agent，这是 AI 领域一个快速发展的方向。 该帖子重点介绍了两个仓库：包含完整代码笔记本的“Hands-On Large Language Models”和包含 11 部分课程的“AI Agents for Beginners”。该列表旨在作为可收藏的技能提升资源。

twitter · RodmanAi · Jun 4, 17:10

**背景**: AI Agent 是能够执行任务、做出决策并与环境交互的自主程序。GitHub 仓库通常是开源学习材料的中心枢纽，包括代码示例和教程。

**标签**: `#AI agents`, `#GitHub`, `#resources`, `#tutorials`

---

<a id="item-24"></a>
## [免费 API 替代付费 Agent 工具指南](https://twitter.com/tech_shrimp/status/2062327316198703123) ⭐️ 3.0/10

一篇教程介绍了如何用免费 API 替代 Codex 和 Hermes 等付费 Agent 工具，声称可长期稳定免费获得一线模型的 Agent 体验。 这很重要，因为它降低了开发者使用高级 AI Agent 的门槛，无需订阅费用，可能使强大的编码和个人 Agent 工具的获取更加民主化。 该指南专门针对 Codex（OpenAI 的编码 Agent）和 Hermes（Nous Research 的开源 Agent），并提供了完整教程的链接。该推文互动量低，仅有 5 条回复。

twitter · tech_shrimp · Jun 4, 00:15

**背景**: Codex 是 OpenAI 开发的 AI 编码 Agent，用于编写代码和修复 bug 等软件工程任务，于 2025 年 4 月以 Codex CLI 形式发布。Hermes Agent 是 Nous Research 开发的开源 AI Agent，具有持久记忆和自我改进能力。两者通常需要付费或消耗 API 额度，但该指南声称提供免费替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://openai.com/index/introducing-codex/">Introducing Codex - OpenAI</a></li>
<li><a href="https://github.com/nousresearch/hermes-agent">GitHub - NousResearch/hermes-agent: The agent that grows with ...</a></li>

</ul>
</details>

**标签**: `#API`, `#Agent`, `#Free`, `#Tutorial`

---

<a id="item-25"></a>
## [SpaceX 从加州发射 24 颗星链卫星](https://twitter.com/SpaceX/status/2062230253771120936) ⭐️ 3.0/10

SpaceX 使用猎鹰 9 号火箭从加州发射了 24 颗星链卫星，发射后不久即确认部署成功。 此次发射延续了 SpaceX 快速扩建星链星座的步伐，该星座旨在提供全球宽带互联网覆盖。 猎鹰 9 号第一级很可能按惯例在无人船上着陆，但推文未说明着陆细节。

twitter · SpaceX · Jun 3, 17:49

**背景**: 星链是由 SpaceX 运营的卫星互联网星座，由数千颗低地球轨道小型卫星组成。猎鹰 9 号是一种可重复使用的两级火箭，已成为 SpaceX 发射的主力。

**标签**: `#SpaceX`, `#Starlink`, `#satellite launch`

---

<a id="item-26"></a>
## [Yann LeCun 转发 Ted Chiang 关于 AI 意识的观点](https://twitter.com/ylecun/status/2062491219872084049) ⭐️ 3.0/10

Yann LeCun 转发了 @kasratweets 的一条评论，指出 Ted Chiang 新文章中的一个有趣观点：没有人声称 AlphaFold 或 Sora 具有意识，这引发了对 AI 意识归因的质疑。 这一讨论挑战了将 AI 系统拟人化的倾向，促使人们对 AI 中的意识含义进行更细致的理解。它突显了令人印象深刻的 AI 能力与真正感知之间的差距。 该转发引用了 Ted Chiang 的文章，该文章将 AlphaFold（蛋白质结构预测）和 Sora（文本生成视频）作为未归因意识的例子，与 ChatGPT 等对话式 AI 形成对比。

twitter · ylecun · Jun 4, 11:06

**背景**: AlphaFold 是 DeepMind 开发的 AI 系统，能够高精度预测蛋白质三维结构，并因此获得 2024 年诺贝尔化学奖。Sora 是 OpenAI 开发的文本生成视频模型，可根据提示生成短视频，后于 2026 年关闭。Ted Chiang 是著名科幻作家，经常撰写关于 AI 和意识的文章。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaFold">AlphaFold</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sora_AI">Sora AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#consciousness`, `#Ted Chiang`

---

<a id="item-27"></a>
## [马斯克关于哈达玛思维的模糊推文](https://twitter.com/drfeifei/status/2062522924326855101) ⭐️ 2.0/10

埃隆·马斯克发布了一条隐晦的推文，内容为“Hadamard thought in image space”，该推文被李飞飞转发，引发了对其含义的猜测。 这条推文因马斯克的庞大粉丝群和 AI 研究员李飞飞的参与而受到关注，但缺乏技术实质，被认为价值较低。 短语“Hadamard thought”可能指图像处理中使用的哈达玛变换，但马斯克未提供任何背景或解释。

twitter · drfeifei · Jun 4, 13:12

**背景**: 哈达玛变换是一种用于图像压缩和特征提取的数学运算，以其计算效率著称。埃隆·马斯克经常发布关于技术和 AI 的隐晦推文，这些推文有时会引发讨论，但缺乏深度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hadamard_transform">Hadamard transform - Wikipedia</a></li>
<li><a href="https://www.reddit.com/r/LovingAI/comments/1sdvn6m/elon_musk_hadamard_thought_in_image_space_yann/">Elon Musk "Hadamard thought in image space" ➡️ Yann LeCun "Thinking in language has ... - Reddit</a></li>

</ul>
</details>

**社区讨论**: 在 Reddit 上，用户将马斯克的推文与 Yann LeCun 的回应联系起来，LeCun 认为语言思维的应用有限，与马斯克的模糊引用形成对比。讨论大多是猜测性的，没有明确共识。

**标签**: `#twitter`, `#vague`, `#low-value`

---

<a id="item-28"></a>
## [SpaceX 重申跨行星使命，提及星链与 AI](https://twitter.com/SpaceX/status/2062630481087082874) ⭐️ 2.0/10

SpaceX 发布了一条宣传推文，重申其让生命成为多行星物种的创始使命，并简要提及了星链和 AI 解决方案，但未提供任何技术细节或新信息。 这条推文只是对 SpaceX 长期愿景的泛泛提醒，对技术社区没有实质性更新。与软件工程、AI/ML 或系统研究的相关性很低。 推文包含一个指向 SpaceX 网站的链接，但没有具体的技术声明、性能指标或时间表。提到的 AI 解决方案没有定义或详细说明。

twitter · SpaceX · Jun 4, 20:20

**背景**: SpaceX 由埃隆·马斯克于 2002 年创立，目标是降低太空运输成本并实现火星殖民。星链是 SpaceX 正在建设的卫星互联网星座，旨在提供全球宽带覆盖。该公司还探索了 AI 应用，例如自主对接系统。

**标签**: `#spacex`, `#starlink`, `#ai`, `#promotional`

---

<a id="item-29"></a>
## [Yann LeCun 转发政治抱怨](https://twitter.com/ylecun/status/2062541298821660976) ⭐️ 1.0/10

Yann LeCun 转发了参议员 Mark Warner 的一条推文，声称美国共和党和民主党适用不同的规则。 这次转发值得注意，因为 LeCun 是著名的人工智能研究者，但内容纯粹是政治性的，与他的技术专长无关，凸显了社交媒体上个人与职业内容的混合。 Mark Warner 的原始推文包含一个未指明来源的链接，该转发在技术内容策展中的相关性评分仅为 1.0/10。

twitter · ylecun · Jun 4, 14:25

**标签**: `#politics`, `#off-topic`

---

<a id="item-30"></a>
## [政治转发缺乏技术相关性](https://twitter.com/ylecun/status/2062541207851434005) ⭐️ 1.0/10

Yann LeCun 转发了一条声称特朗普预算主任 Russ Vought 很危险的推文，内容不涉及技术或学术。 这条新闻对技术社区毫无意义，因为它纯属政治话题且不相关。 该转发不包含任何技术细节、数据或分析，仅是一种政治观点。

twitter · ylecun · Jun 4, 14:25

**标签**: `#politics`, `#off-topic`

---