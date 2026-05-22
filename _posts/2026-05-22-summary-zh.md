---
layout: default
title: "Horizon Summary: 2026-05-22 (ZH)"
date: 2026-05-22
lang: zh
---

> From 63 items, 36 important content pieces were selected

---

1. [Python 3.14 将允许禁用 GIL](#item-1) ⭐️ 9.0/10
2. [Hugging Face 发布 2500 美元开源人形机器人](#item-2) ⭐️ 8.0/10
3. [SpaceX 第 12 次飞行将首次亮相新一代星舰和猛禽发动机](#item-3) ⭐️ 8.0/10
4. [AI 代理能否自主利用安全漏洞？](#item-4) ⭐️ 8.0/10
5. [Crys-JEPA：用于晶体设计的 AI 方法](#item-5) ⭐️ 7.0/10
6. [斯坦福 AI 实验室提出通用偏好强化学习](#item-6) ⭐️ 7.0/10
7. [算力与数据质量的意外发现](#item-7) ⭐️ 7.0/10
8. [SimpleTES：为 AI 驱动科学扩展评估](#item-8) ⭐️ 7.0/10
9. [斯坦福 AI 实验室发布 Terminal-Bench Science 基准测试](#item-9) ⭐️ 7.0/10
10. [斯坦福 AI 实验室发布 GPU 复制工具 Hawkeye](#item-10) ⭐️ 7.0/10
11. [“优化一切”论文被 CAIS 2026 接收](#item-11) ⭐️ 7.0/10
12. [RAPTOR：四旋翼微型基础策略](#item-12) ⭐️ 7.0/10
13. [ClaudeDevs 扩大与 SpaceX 合作，在 Colossus 2 中扩展 GB200 容量](#item-13) ⭐️ 7.0/10
14. [Anthropic 发布免费 Claude 提示工程研讨会](#item-14) ⭐️ 7.0/10
15. [吴恩达推出 AI 智能体图像视频生成课程](#item-15) ⭐️ 7.0/10
16. [C-Ray 机器人利用双曲鳍实现多种运动模式](#item-16) ⭐️ 6.0/10
17. [星链探索将连接扩展到地球之外](#item-17) ⭐️ 6.0/10
18. [Hermes Agent 获 14 万 GitHub 星标，登顶 OpenRouter](#item-18) ⭐️ 6.0/10
19. [SpaceX：星舰对 NASA 阿尔忒弥斯登月任务至关重要](#item-19) ⭐️ 5.0/10
20. [Anthropic 发布 Claude Code Setup 插件，优化开发流程](#item-20) ⭐️ 5.0/10
21. [2026 年世界创作马拉松获奖者揭晓](#item-21) ⭐️ 4.0/10
22. [通过转发推广 Daedalus 期刊新刊](#item-22) ⭐️ 4.0/10
23. [CHI-Bench：医疗 AI 代理新基准](#item-23) ⭐️ 4.0/10
24. [AI：机械设计的下一场变革](#item-24) ⭐️ 3.0/10
25. [推文表达对太空机器人的兴奋](#item-25) ⭐️ 3.0/10
26. [推特帖子列出学习技术技能的 YouTube 频道](#item-26) ⭐️ 3.0/10
27. [20 个支付美元的远程工作网站](#item-27) ⭐️ 3.0/10
28. [谷歌云合作伙伴验证 Gemini 3.5](#item-28) ⭐️ 2.0/10
29. [Yann LeCun 转发 1 月 6 日贿赂基金文章](#item-29) ⭐️ 2.0/10
30. [Yann LeCun 转发政治类纽约时报文章](#item-30) ⭐️ 2.0/10
31. [转发赞扬法国主权与核威慑](#item-31) ⭐️ 2.0/10
32. [Yann LeCun 转发纽约时报关于支出的观点](#item-32) ⭐️ 2.0/10
33. [低质量推文：'历史的错误一方'引用](#item-33) ⭐️ 2.0/10
34. [特朗普审查指控与美国新闻自由排名](#item-34) ⭐️ 2.0/10
35. [低质量推文重复“vibe cad”](#item-35) ⭐️ 1.0/10
36. [与科技无关的政治推文](#item-36) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [Python 3.14 将允许禁用 GIL](https://twitter.com/RodmanAi/status/2057108613693673957) ⭐️ 9.0/10

Python 3.14 将引入一个可选的无 GIL 模式，首次实现真正的多核并行。 这一改变解决了 CPython 中长达 30 年的瓶颈，使 CPU 密集型多线程程序能够同时利用所有 CPU 核心，显著提升并行工作负载的性能。 GIL 可以在构建时通过 --disable-gil 标志禁用，运行时可通过 PYTHONGIL 环境变量控制。该功能基于 PEP 703。

twitter · RodmanAi · May 20, 14:38

**背景**: 全局解释器锁（GIL）是 CPython 中的一个互斥锁，防止多个原生线程同时执行 Python 字节码。它简化了内存管理，但限制了并行性，尤其是对于 CPU 密集型任务。移除 GIL 一直是 Python 社区长期以来的愿望。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Global_Interpreter_Lock">Global interpreter lock - Wikipedia</a></li>
<li><a href="https://peps.python.org/pep-0703/">PEP 703 – Making the Global Interpreter Lock Optional in CPython | peps.python.org</a></li>
<li><a href="https://towardsdatascience.com/python-3-14-and-the-end-of-the-gil/">Python 3.14 and the End of the GIL | Towards Data Science</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论指出，虽然移除 GIL 有助于并行，但并未解决 Python 本身速度慢的问题，只是分散了工作负载。一些评论者持谨慎乐观态度，认为单线程性能保持不变。

**标签**: `#Python`, `#GIL`, `#Parallelism`, `#CPython`, `#Performance`

---

<a id="item-2"></a>
## [Hugging Face 发布 2500 美元开源人形机器人](https://twitter.com/lukas_m_ziegler/status/2057515219946205399) ⭐️ 8.0/10

Hugging Face 的 LeRobot 项目发布了 LeRobot Humanoid，这是一款完全开源的双足机器人，使用 3D 打印部件和现成组件即可建造，成本约 2500 美元。 这大幅降低了机器人研究和教育的入门门槛，使更多个人和小型实验室能够实验人形机器人，推动具身人工智能的发展。 该机器人属于全栈生态系统的一部分，包括 3D 可打印硬件文件、运行时软件、仿真工具和训练环境，使其成为机器人学习的完整平台。

twitter · lukas_m_ziegler · May 21, 17:33

**背景**: 开源机器人旨在使先进机器人平台的获取民主化，这些平台通常价格昂贵且专有。Hugging Face 以其在人工智能和机器学习方面的工作而闻名，通过其 LeRobot 项目扩展到机器人领域，此前发布了软件工具，现在又推出了硬件平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.humanoidsdaily.com/news/hugging-face-drops-a-2-500-3d-printed-humanoid-for-open-robot-learning">Hugging Face Drops a $2,500 3D-Printed Humanoid for Open ...</a></li>
<li><a href="https://techcrunch.com/2025/05/29/hugging-face-unveils-two-new-humanoid-robots/">Hugging Face unveils two new humanoid robots | TechCrunch</a></li>
<li><a href="https://arstechnica.com/ai/2025/05/hugging-face-hopes-to-bring-a-humanoid-robot-to-market-for-just-3000/">Want a humanoid, open source robot for just $3,000? Hugging Face is on it. - Ars Technica</a></li>

</ul>
</details>

**社区讨论**: 该公告在社交媒体上受到热烈欢迎，许多人称赞其低成本与开源特性。一些评论者对教育和研究潜力表示兴奋，而另一些人则指出组装和维护此类机器人的挑战。

**标签**: `#open-source`, `#robotics`, `#humanoid robot`, `#Hugging Face`

---

<a id="item-3"></a>
## [SpaceX 第 12 次飞行将首次亮相新一代星舰和猛禽发动机](https://twitter.com/SpaceX/status/2057596793299333595) ⭐️ 8.0/10

SpaceX 宣布第 12 次飞行将首次亮相新一代星舰和超重型火箭，两者均由升级版猛禽发动机提供动力。发射将从星基地新建的 2 号发射台进行，该发射台旨在实现全面快速复用。 这标志着航空航天工程的一个重要里程碑，新一代星舰和猛禽发动机旨在提升性能、可靠性和复用性。成功可能加速 SpaceX 的月球任务、火星殖民以及重型卫星部署计划。 升级版猛禽发动机代表了 SpaceX 全流量分级燃烧甲烷液氧发动机的下一代进化，在推力和可靠性方面有所改进。星基地的 2 号发射台是首个从头设计以实现快速复用的发射台，配备了先进的地面支持系统。

twitter · SpaceX · May 21, 22:57

**背景**: SpaceX 的星舰是一种完全可复用的超重型运载火箭，由星舰飞船和超重型助推器组成。猛禽发动机采用甲烷和液氧的全流量分级燃烧循环，以高效率和可复用性著称。2 号发射台是星基地的第二个轨道发射台，旨在支持更高的发射频率和快速周转。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Raptor">SpaceX Raptor - Wikipedia</a></li>
<li><a href="https://www.nasaspaceflight.com/2025/08/starbase-pad-2-advancements-pad-1/">Starbase Pad 2 : Design Advancements from... - NASASpaceFlight.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starship`, `#Raptor engine`, `#aerospace`

---

<a id="item-4"></a>
## [AI 代理能否自主利用安全漏洞？](https://twitter.com/berkeley_ai/status/2057567247783399688) ⭐️ 8.0/10

Dawn Song 发起的一项讨论强调了衡量 AI 代理能否自主将安全漏洞转化为实际攻击的关键任务，这是 AI 安全面临的一个核心挑战。 这个问题对 AI 安全和网络安全至关重要，因为自主利用可能导致大规模自动化攻击，需要强大的评估框架和防御措施。 最近的研究表明，威胁行为者已经在利用 AI 进行漏洞利用，并且自主多代理系统已被证明能够通过链式利用攻击云环境。

twitter · berkeley_ai · May 21, 21:00

**背景**: AI 代理是能够自主执行任务的系统，包括与软件和网络交互。漏洞利用涉及发现并利用安全漏洞以获得未授权访问或造成损害。衡量 AI 代理自主执行此操作的能力对于理解和减轻风险至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access">Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access | Google Cloud Blog</a></li>
<li><a href="https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/">Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#cybersecurity`, `#AI agents`, `#vulnerability exploitation`

---

<a id="item-5"></a>
## [Crys-JEPA：用于晶体设计的 AI 方法](https://twitter.com/ylecun/status/2057474214693834963) ⭐️ 7.0/10

研究人员推出了 Crys-JEPA，这是一种利用联合嵌入预测架构（JEPA）设计新型晶体材料的新型生成式 AI 方法。 Crys-JEPA 在 MP-20 和 Alex-MP-20 数据集上，与基线相比，在 V.S.U.N 指标上分别实现了高达 81.4%和 82.6%的提升。

twitter · ylecun · May 21, 14:50

**背景**: 晶体生成旨在发现真实、稳定且新颖的新材料。传统的生成模型通常最大化观测晶体的似然，这可能与发现目标不一致。JEPA 是一种自监督学习范式，通过在嵌入空间中进行预测来学习抽象表示，由 Yann LeCun 提出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.14759">[2605.14759] Crys-JEPA: Accelerating Crystal Discovery via ...</a></li>
<li><a href="https://www.linkedin.com/posts/xavier-bresson-738585b_how-do-we-design-materials-with-ai-excited-activity-7462301163732783104-74zb">How do we design materials with AI? Excited to introduce Crys ...</a></li>
<li><a href="https://rohitbandaru.github.io/blog/JEPA-Deep-Dive/">Deep Dive into Yann LeCun’s JEPA | Rohit Bandaru</a></li>

</ul>
</details>

**标签**: `#AI`, `#materials science`, `#generative models`, `#research`

---

<a id="item-6"></a>
## [斯坦福 AI 实验室提出通用偏好强化学习](https://twitter.com/StanfordAILab/status/2057531797945397379) ⭐️ 7.0/10

斯坦福 AI 实验室分享了一篇题为《通用偏好强化学习》（GPRL）的新论文，提出将通用偏好模型作为多维奖励源用于在线强化学习的方法。 这项工作可能推动基于人类反馈的强化学习（RLHF）的发展，通过实现更结构化、可扩展的偏好训练，有望改善大语言模型及其他 AI 系统的对齐效果。 GPRL 计算每个维度的组相对优势并对其进行归一化，以防止任何单一轴主导，然后在 GRPO 风格的在线强化学习框架中聚合它们以更新策略。

twitter · StanfordAILab · May 21, 18:39

**背景**: 基于人类反馈的强化学习（RLHF）通常从人类偏好中训练奖励模型，然后优化策略。GPRL 通过使用提供多维反馈的通用偏好模型扩展了这一方法，从而能够提供更细致的训练信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.18721">[2605.18721] General Preference Reinforcement Learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback">Reinforcement learning from human feedback - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#AI research`, `#Stanford`

---

<a id="item-7"></a>
## [算力与数据质量的意外发现](https://twitter.com/StanfordAILab/status/2057531127326453869) ⭐️ 7.0/10

斯坦福 AI 实验室研究员 Tatsu Hashimoto 发推文称，新研究发现，在充足算力下，最优数据会产生令人意外的结果。 这一发现挑战了关于算力、数据质量与模型性能关系的传统认知，可能重塑 AI 研究重点。 推文未提供细节，但“意外”暗示存在非线性或阈值效应，即算力以意想不到的方式放大了数据质量的优势。

twitter · StanfordAILab · May 21, 18:37

**背景**: 在 AI 开发中，算力指训练模型所用的处理能力，而数据质量涵盖训练数据的准确性、完整性和相关性。普遍认为两者都很重要，但它们的相互作用尚未被完全理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/ai-and-compute/">AI and compute - OpenAI</a></li>
<li><a href="https://www.pickl.ai/blog/data-quality-in-machine-learning/">Data Quality in Machine Learning - Pickl.AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#machine learning`, `#research`, `#compute`, `#data`

---

<a id="item-8"></a>
## [SimpleTES：为 AI 驱动科学扩展评估](https://twitter.com/StanfordAILab/status/2057202545991581903) ⭐️ 7.0/10

James Y. Zou 和斯坦福 AI 实验室指出，扩展评估（而非仅仅扩展计算）对 AI 驱动科学至关重要，并介绍了 SimpleTES 框架，用于扩展评估驱动的发现。 这一转变强调，更好的评估方法可以释放 AI 在科学发现中的潜力，尤其对于长推理不足以解决的开放性问题。 SimpleTES 是一个 C++后端、Python 驱动的框架，它将测试时计算分配给迭代评估循环，而不仅仅是生成更长的输出。

twitter · StanfordAILab · May 20, 20:51

**背景**: AI 驱动科学通常依赖于扩展计算（更大的模型或更多训练数据）。然而，对于科学发现等开放性问题，解决方案的路径依赖于迭代评估和搜索。SimpleTES 通过提供一个无需训练的搜索系统来解决这一问题，该系统策略性地扩展评估驱动循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wq-will/SimpleTES">GitHub - wq-will/ SimpleTES : A general framework for strategically...</a></li>
<li><a href="https://www.emergentmind.com/topics/simple-test-time-evaluation-driven-scaling-simpletes">SimpleTES : Evaluation-Driven Scaling</a></li>
<li><a href="https://imtaqin.id/simpletes-a-general-framework-for-strategically-scaling-evaluation-driven-di">SimpleTES : Evaluation-Driven Scaling Framework | AI Research</a></li>

</ul>
</details>

**标签**: `#AI`, `#evaluation`, `#science`, `#framework`

---

<a id="item-9"></a>
## [斯坦福 AI 实验室发布 Terminal-Bench Science 基准测试](https://twitter.com/StanfordAILab/status/2057202472842903664) ⭐️ 7.0/10

斯坦福 AI 实验室宣布推出 Terminal-Bench Science，这是一个用于评估 AI 智能体在真实科学工作流上表现的新基准，现已开放社区任务贡献。 该基准通过测试 AI 智能体在实践科学任务上的表现，而非教科书知识，填补了关键空白，有望加速 AI 在研发领域的应用。 Terminal-Bench Science 基于 Terminal-Bench 构建，后者已被 Anthropic、OpenAI 和 Google DeepMind 等前沿实验室用于软件工程任务。新基准将这一方法扩展到自然科学领域。

twitter · StanfordAILab · May 20, 20:51

**背景**: AI 智能体越来越多地被用于自动化复杂工作流，但现有基准通常只测试理论知识。Terminal-Bench Science 旨在评估智能体在源自实际科学研究的真实命令行任务上的表现，提供更有意义的能力衡量标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tbench.ai/news/tb-science-announcement">Terminal-Bench Science: Contribute your scientific workflows as tasks for AI Agents</a></li>
<li><a href="https://arxiv.org/abs/2601.11868">[2601.11868] Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#benchmarking`, `#scientific workflows`, `#AI research`

---

<a id="item-10"></a>
## [斯坦福 AI 实验室发布 GPU 复制工具 Hawkeye](https://twitter.com/StanfordAILab/status/2057202147494965392) ⭐️ 7.0/10

斯坦福 AI 实验室在 MLSys 2026 上展示了 Hawkeye，该工具能够精确地在 CPU 上复制 GPU 级别的运算（如 FP16 矩阵乘法），确保结果逐位一致。 Hawkeye 解决了机器学习中一个关键的可重复性挑战，使研究人员无需专用硬件即可审计和验证 GPU 计算，这对科学严谨性和问责制至关重要。 Hawkeye 在 CPU 上重新执行精确的矩阵乘法运算，无精度损失，支持 NVIDIA GPU。该工具在 MLSys 2026 上以海报形式展示。

twitter · StanfordAILab · May 20, 20:49

**背景**: 由于并行执行和浮点优化，GPU 计算通常具有非确定性，导致结果难以精确复现。先前的可验证机器学习方法需要大量开销或硬件改动。Hawkeye 通过在 CPU 上复制 GPU 算术运算提供了一种轻量级解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.20421">Hawkeye: Reproducing GPU-Level Non-Determinism</a></li>
<li><a href="https://www.machinebrief.com/news/hawkeye-a-new-era-of-gpu-level-reproducibility-ix8t">Hawkeye: A New Era of GPU-Level Reproducibility</a></li>
<li><a href="https://mlsys.org/virtual/2026/poster/3606">MLSys Poster Hawkeye: Reproducing GPU-Level Non-Determinism</a></li>

</ul>
</details>

**标签**: `#MLSys`, `#GPU`, `#reproducibility`, `#machine learning`, `#systems`

---

<a id="item-11"></a>
## [“优化一切”论文被 CAIS 2026 接收](https://twitter.com/berkeley_ai/status/2057567604987105501) ⭐️ 7.0/10

论文《optimize_anything: 一个用于优化任意文本参数的通用 API》已被 ACM 人工智能与智能体系统会议（CAIS 2026）接收，并在 arXiv 上发布了包含扩展实验和细节的版本。 该工作提供了一个通用 API，用于优化任何可表示为文本的工件（如代码、提示词、智能体架构），这可以显著简化众多 AI 应用中的优化任务，并减少对定制解决方案的需求。 该 API 是声明式的，可优化代码、提示词、智能体架构、矢量图形和配置等工件。与初始版本相比，论文包含了扩展的实验，展示了其多功能性。

twitter · berkeley_ai · May 21, 21:01

**背景**: CAIS 2026 是研究复合 AI 架构、优化和部署的顶级会议。“优化一切”方法基于将优化视为文本级问题的思路，利用大型语言模型来寻找最优配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.caisconf.org/">ACM Conference on AI and Agentic Systems — ACM CAIS 2026</a></li>
<li><a href="https://arxiv.org/abs/2605.19633">[2605.19633] optimize_anything: A Universal API for ...</a></li>
<li><a href="https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/">optimize_anything: A Universal API for Optimizing any Text ...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#optimization`, `#research`, `#arxiv`

---

<a id="item-12"></a>
## [RAPTOR：四旋翼微型基础策略](https://twitter.com/berkeley_ai/status/2057119576299839669) ⭐️ 7.0/10

研究人员开发了 RAPTOR，这是一种单一紧凑的四旋翼基础策略，能够适应各种条件，相关成果发表在《科学机器人》上。 这项工作表明，单一的神经网络策略可以控制多种四旋翼，可能减少针对特定平台的调优需求，加速实际应用中的部署。 RAPTOR 是一种端到端的神经网络策略，经过训练可控制多种四旋翼，详细内容见 2026 年 5 月 13 日发表在《科学机器人》上的论文。

twitter · berkeley_ai · May 20, 15:21

**背景**: 机器人领域的基础模型旨在创建跨不同机器人和任务的通用控制策略，类似于 AI 中的大型语言模型。传统的四旋翼控制通常需要为每个平台手动调整参数，限制了可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.science.org/doi/10.1126/scirobotics.aec1481">RAPTOR: A foundation policy for quadrotor control - Science</a></li>
<li><a href="https://arxiv.org/abs/2509.11481">RAPTOR: A Foundation Policy for Quadrotor Control</a></li>

</ul>
</details>

**标签**: `#robotics`, `#quadrotors`, `#foundation model`, `#AI`

---

<a id="item-13"></a>
## [ClaudeDevs 扩大与 SpaceX 合作，在 Colossus 2 中扩展 GB200 容量](https://twitter.com/ClaudeDevs/status/2057199398573220092) ⭐️ 7.0/10

ClaudeDevs 宣布扩大与 SpaceX 的合作，并计划在整个六月提升 Colossus 2 中的 GB200 容量。 这标志着 AI 计算基础设施的重大增长，利用 SpaceX 的能力和 NVIDIA 最新的 GB200 硬件，可能加速 AI 模型的训练和推理。 GB200 是 NVIDIA 的高性能 GPU 卡，拥有 192 GB 内存；Colossus 2 是 xAI 的下一代超级计算机集群，预计将成为世界上第一个吉瓦级数据中心。

twitter · ClaudeDevs · May 20, 20:38

**背景**: Colossus 是 xAI 现有的 AI 超级计算机，目前是世界上最大的，用于训练 Grok。Colossus 2 是其继任者，旨在实现更大规模。GB200 NVL72 机架功耗约为 120-132 kW，专为大规模 AI 工作负载设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/gb200-nvl72/">GB200 NVL72 | NVIDIA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://newsletter.semianalysis.com/p/xais-colossus-2-first-gigawatt-datacenter">xAI's Colossus 2 - First Gigawatt Datacenter In The World ...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#partnership`, `#SpaceX`, `#GB200`, `#Colossus`

---

<a id="item-14"></a>
## [Anthropic 发布免费 Claude 提示工程研讨会](https://twitter.com/RodmanAi/status/2057143286163542441) ⭐️ 7.0/10

Anthropic 发布了一个免费的 27 分钟提示工程研讨会，由 Claude 的创建者亲自授课，无需注册或付费。 该研讨会为 Claude 提供了权威、高质量的提示工程指导，与付费课程相比可能为用户节省数百美元，并帮助用户充分利用 AI 模型。 该研讨会时长 27 分钟，免费，无需注册或付费。它涵盖的提示工程技术据称超过了 300 美元课程所教授的内容。

twitter · RodmanAi · May 20, 16:55

**背景**: 提示工程是设计 AI 模型输入以获得所需输出的实践。Claude 是 Anthropic 的 AI 助手，有效的提示是发挥其能力的关键。该研讨会提供了来自模型创建者的官方培训。

**标签**: `#Anthropic`, `#Claude`, `#prompt engineering`, `#AI workshop`

---

<a id="item-15"></a>
## [吴恩达推出 AI 智能体图像视频生成课程](https://twitter.com/AndrewYNg/status/2057146565500998024) ⭐️ 7.0/10

吴恩达宣布推出一门新短期课程，教授构建能生成图像和视频的 AI 智能体，该课程与 Google Cloud 合作开发，由 Katie Nguyen 讲授，强调自我评估和迭代改进是提升性能的关键。 该课程涉足 AI 智能体中一个尚未充分探索的前沿领域，将生成式 AI 与智能体自我评估相结合，有望显著提升输出质量。它为希望构建更自主、更高效的生成系统的开发者和研究人员提供了实用指导。 该课程是与 Google Cloud 合作开发的短期课程，由 Katie Nguyen 讲授，重点在于让智能体自我评估输出并通过迭代提升质量。它针对图像和视频生成的 AI 智能体这一新颖领域，相比基于文本的智能体，该领域探索较少。

twitter · AndrewYNg · May 20, 17:08

**背景**: AI 智能体是能够感知环境、做出决策并采取行动以实现目标的自主系统。自我评估和迭代改进是指智能体评估自身输出并通过多轮循环进行优化的技术，从而减少对人类监督的需求。随着 AI 系统扩展到复杂任务，这种方法变得越来越重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/day-12-self-evaluation-feedback-loops-building-agents-ramanujam-ng3jc">Day 12: Self - Evaluation & Feedback Loops: Building Adaptive Agents</a></li>
<li><a href="https://www.emergentmind.com/topics/self-evaluation-module">Self - Evaluation Module in AI Systems</a></li>
<li><a href="https://cloud.google.com/ai/generative-ai">Generative AI | Google Cloud</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#image generation`, `#video generation`, `#education`, `#Google Cloud`

---

<a id="item-16"></a>
## [C-Ray 机器人利用双曲鳍实现多种运动模式](https://twitter.com/lukas_m_ziegler/status/2057035258130808902) ⭐️ 6.0/10

Pliant Energy Systems 展示了 C-Ray 机器人，它使用一对独特的柔性双曲鳍，能够像鳐鱼一样游泳、像千足虫一样爬行、像鱿鱼一样喷射推进、像蛇一样滑行。 这项创新展示了一种高度通用的两栖运动系统，使机器人无需单独的推进机构即可在陆地、水域和冰面等多种环境中运行，有望推动环境监测、搜救和水下勘探等领域的发展。 这些鳍被描述为具有双曲几何的四维物体，使机器人能够以多种模式高效运动。C-Ray 平台由海军研究办公室资助，设计用于在冰面、陆地、水面和水下自主运行。

twitter · lukas_m_ziegler · May 20, 09:46

**背景**: 传统两栖机器人通常依赖独立的陆地和水中运动系统，增加了复杂性和重量。像 C-Ray 这样的仿生设计旨在模仿海洋动物的效率和适应性。双曲鳍利用波动运动产生推力，类似于鳐鱼和乌贼的运动方式，从而实现环境间的平滑过渡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pliantenergy.com/robotics">Robotics — Pliant Energy Systems</a></li>
<li><a href="https://oceanai.mit.edu/pavlab/pdfs/robot_cray.pdf">C-Ray - An autonomous amphibious vehicle with ice, land ...</a></li>
<li><a href="https://www.youtube.com/watch?v=7T-wYJ_bFcI">Meet c-ray - a robot build to monitor protect marine life Pliant Energy's C-Ray Robot and Greensea IQ's Crawlers Enable ... Undulating Fins Enable Robot to Swim, Crawl, Recharge Meet C-Ray, developed by Pliant Energy Systems Inc. This ... Autonomous Robots Could Mine the Deep Seafloor - IEEE Spectrum</a></li>

</ul>
</details>

**标签**: `#robotics`, `#biomimicry`, `#locomotion`, `#innovation`

---

<a id="item-17"></a>
## [星链探索将连接扩展到地球之外](https://twitter.com/SpaceX/status/2057598013565014112) ⭐️ 6.0/10

SpaceX 转发了 Starlink 的帖子，称团队正在探索将连接扩展到地球之外的方法，暗示可能为地球轨道以外的任务提供基于太空的互联网服务。 这表明 SpaceX 有意利用其星链星座进行深空通信，这可能彻底改变月球、火星及其他星际任务的数据传输方式，减少对传统地面网络的依赖。 该公告简短且缺乏技术细节，但与 SpaceX 将星链用作星际互联网骨干的更大愿景一致，可能利用激光星间链路进行远距离通信。

twitter · SpaceX · May 21, 23:02

**背景**: 星链是由 SpaceX 运营的卫星互联网星座，由数千颗低地球轨道（LEO）卫星组成，为偏远地区提供高速互联网。SpaceX 此前曾讨论过将星链用于火星殖民，其星舰飞船专为深空任务设计。将连接扩展到地球之外需要调整星链技术以适应更远的距离和不同的轨道环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>
<li><a href="https://starlink.com/technology">Starlink | Technology</a></li>
<li><a href="https://www.space.com/spacex-starlink-satellites.html">Starlink satellites : Facts, tracking and impact on astronomy | Space</a></li>

</ul>
</details>

**标签**: `#Starlink`, `#SpaceX`, `#satellite internet`, `#space connectivity`

---

<a id="item-18"></a>
## [Hermes Agent 获 14 万 GitHub 星标，登顶 OpenRouter](https://twitter.com/RodmanAi/status/2057451490164592804) ⭐️ 6.0/10

Nous Research 开发的开源自主 AI 代理 Hermes Agent 已获得超过 14 万 GitHub 星标，并在 OpenRouter 上排名第一，RodmanAi 的推广推文强调了这一点。 这种快速采用表明市场对持久化、自我进化的 AI 代理需求日益增长，这类代理可自动化复杂工作流，可能改变开发者和企业部署 AI 助手的方式。 Hermes Agent 具有一键安装、持久化多层记忆、自适应学习和技能构建能力，使其能随时间进化并与消息平台集成。

twitter · RodmanAi · May 21, 13:20

**背景**: Hermes Agent 是 Nous Research 开发的开源自主 AI 代理，设计运行在用户服务器上，通过持久化记忆和自适应学习与用户共同成长。OpenRouter 是一个统一 API 网关，提供对 300 多个 AI 模型的访问，使开发者能通过单一接口比较和使用各种大语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Hermes_Agent">Hermes Agent</a></li>
<li><a href="https://hermes-agent.nousresearch.com/">Hermes Agent — The Agent That Grows With You | Nous Research</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**标签**: `#AI agent`, `#open source`, `#GitHub`, `#OpenRouter`

---

<a id="item-19"></a>
## [SpaceX：星舰对 NASA 阿尔忒弥斯登月任务至关重要](https://twitter.com/SpaceX/status/2057602167423320137) ⭐️ 5.0/10

SpaceX 宣布，星舰将在 NASA 的阿尔忒弥斯计划中发挥关键作用，负责将宇航员和货物运送到月球表面。 这再次确认了 SpaceX 在 NASA 重返月球计划中的核心地位，并凸显了星舰作为重型着陆器对未来月球探索的重要性。 星舰 HLS（载人着陆系统）是专门设计的变体，用于在月球轨道和月面之间运送宇航员，该合同于 2021 年由 NASA 授予。

twitter · SpaceX · May 21, 23:19

**背景**: 阿尔忒弥斯计划旨在自阿波罗计划以来首次将人类送回月球，并建立永久性月球基地。星舰 HLS 是其中的关键组成部分，被 NASA 选中用于将下一批宇航员送上月球。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artemis_program">Artemis program - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Starship_HLS">Starship HLS - Wikipedia</a></li>
<li><a href="https://www.spacex.com/humanspaceflight/moon">SpaceX - Mission: Moon</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starship`, `#Artemis`, `#NASA`, `#space exploration`

---

<a id="item-20"></a>
## [Anthropic 发布 Claude Code Setup 插件，优化开发流程](https://twitter.com/RodmanAi/status/2057175898466734519) ⭐️ 5.0/10

Anthropic 悄然发布了名为 claude-code-setup 的官方插件，它能扫描项目代码库并推荐定制化的自动化配置，包括 hooks、技能、MCP 服务器和子代理。 该插件将 Claude Code 从基础编码助手转变为更智能的 AI 开发环境，通过自动化重复性设置任务，有望提升开发者的生产力。 该插件是开源的，可在 GitHub 的 anthropics/claude-plugins-official 仓库中找到，并可直接从 Claude 插件页面安装。

twitter · RodmanAi · May 20, 19:05

**背景**: Claude Code 是 Anthropic 推出的 AI 编码助手，帮助开发者编写、调试和重构代码。Hooks 是可定制的脚本，在 Claude Code 工作流的特定节点运行，可实现自动格式化、安全检查等功能。MCP 服务器则为 Claude Code 提供额外的上下文和工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/plugins/claude-code-setup">Claude Code Setup – Claude Plugin | Anthropic</a></li>
<li><a href="https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup">claude-plugins-official/plugins/claude-code-setup at main ...</a></li>
<li><a href="https://code.claude.com/docs/en/hooks">Hooks reference - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#AI`, `#developer tools`, `#Claude Code`, `#plugin`

---

<a id="item-21"></a>
## [2026 年世界创作马拉松获奖者揭晓](https://twitter.com/drfeifei/status/2057138100258890235) ⭐️ 4.0/10

李飞飞转发了首届 World Jam（世界创作马拉松）获奖者的公告，该活动是由 The World Labs 组织的互动存档活动。 该活动凸显了人工智能、创意与文化保护之间日益紧密的联系，展示了互动存档如何能够表彰创新项目。 World Jam 的获奖作品在一个在线博物馆中展出，该博物馆存档了在氛围、玩法和互动世界方面突破边界的项目。

twitter · drfeifei · May 20, 16:35

**背景**: World Jam 是一种类似游戏创作马拉松的活动，参与者在限定时间内创作互动项目。该活动由专注于人工智能与创意的组织 The World Labs 举办。李飞飞是著名的人工智能研究员，以计算机视觉方面的贡献和倡导以人为本的 AI 而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jam.worldlabs.ai/">2026 World Jam</a></li>
<li><a href="https://en.wikipedia.org/wiki/Global_Game_Jam">Global Game Jam - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#creative`, `#event`

---

<a id="item-22"></a>
## [通过转发推广 Daedalus 期刊新刊](https://twitter.com/ylecun/status/2057520681214951916) ⭐️ 4.0/10

Yann LeCun 转发了 Eric Topol 关于 Daedalus 期刊新刊的公告，该期刊是美国艺术与科学院的开放获取期刊。 这次转发突显了一期可能包含 AI 和科学界相关内容的跨学科期刊，但缺乏具体细节限制了其直接影响。 该推文未提供新刊文章或主题的任何细节，因此是一条信息量较低的公告。

twitter · ylecun · May 21, 17:55

**背景**: Daedalus 是美国艺术与科学院出版的知名期刊，涵盖广泛主题。开放获取意味着文章可免费向公众提供。

**标签**: `#academic`, `#journal`, `#general`

---

<a id="item-23"></a>
## [CHI-Bench：医疗 AI 代理新基准](https://twitter.com/StanfordAILab/status/2057202379121197160) ⭐️ 4.0/10

斯坦福 AI 实验室与 20 多家机构联合发布了 CHI-Bench，这是一个用于评估 AI 代理在长期医疗工作流中表现的基准。 该基准满足了在复杂、政策密集的医疗环境中评估 AI 代理的关键需求，可能加速 AI 在临床和行政工作流中的应用。 CHI-Bench 包含 75 个工作流，涵盖三个领域：提供者事先授权、支付方利用管理和护理管理，使用一个模拟 21 个医疗应用的模拟器和一本 1279 页的手册。

twitter · StanfordAILab · May 20, 20:50

**背景**: AI 代理越来越多地被用于自动化复杂任务，但在医疗等现实环境中评估其性能仍然具有挑战性。像 CHI-Bench 这样的基准提供了标准化的任务和指标来比较不同的 AI 系统。该基准专注于需要多步骤推理和文档处理的长期、政策驱动的工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.16679">[2605.16679] CHI-Bench: Can AI Agents Automate End-to-End ...</a></li>
<li><a href="https://actava.ai/benchmarks/docs">Docs · Introduction | actAVA Benchmarks</a></li>
<li><a href="https://www.youtube.com/watch?v=Zyq2tMnBaIA">CHI-Bench: New Benchmark for Healthcare Agents - YouTube (PDF) ChiBench: a Benchmark Suite for Testing Electronic ... actava-ai/chi-bench - GitHub Claude, GPT, Gemini Agents Fail 72% of U.S. Healthcare ...</a></li>

</ul>
</details>

**标签**: `#benchmark`, `#health systems`, `#research collaboration`

---

<a id="item-24"></a>
## [AI：机械设计的下一场变革](https://twitter.com/MecAgent/status/2057149726672208016) ⭐️ 3.0/10

@MecAgent 的一条推文指出，正如 CAD 取代了手工绘图，AI 现在也将通过加速工作流程和自动化重复性任务来改变机械设计。 这一观察突显了工程领域可能发生的范式转变，AI 有望大幅提升生产力并实现更复杂的设计，影响全球的 CAD 设计师和工程师。 该推文提到了从手工绘图到 CAD 的历史转变，并指出 AI 将帮助工程师更快地工作、自动化繁琐任务并设计得更远，但没有提供具体的技术细节或示例。

twitter · MecAgent · May 20, 17:21

**背景**: 在 CAD 出现之前，工程师使用绘图板、铅笔和尺子手工绘制技术图纸。CAD（计算机辅助设计）通过实现数字化的创建、编辑和仿真，彻底改变了这一过程。如今，AI 正被集成到 CAD 工具中，用于自动化常规任务、优化设计并生成替代方案，这代表了下一个进化步骤。

**标签**: `#CAD`, `#AI`, `#mechanical design`

---

<a id="item-25"></a>
## [推文表达对太空机器人的兴奋](https://twitter.com/lukas_m_ziegler/status/2057089652834590839) ⭐️ 3.0/10

一位 Twitter 用户发布了一条简短、非技术性的推文，表达了对太空机器人的兴奋，没有提供具体细节或背景。 这条推文参与度低且缺乏实质性内容，因此不代表机器人或太空技术的重大进展。 这条推文含糊不清，没有提及任何具体任务、机器人或技术；仅仅是一种随意的兴趣表达。

twitter · lukas_m_ziegler · May 20, 13:22

**标签**: `#robotics`, `#space`

---

<a id="item-26"></a>
## [推特帖子列出学习技术技能的 YouTube 频道](https://twitter.com/RodmanAi/status/2057324846535901388) ⭐️ 3.0/10

一位推特用户分享了一份 YouTube 频道列表，涵盖 SQL、Excel、统计学、数学、Python、数据分析和机器学习。 这为寻求免费高质量资源以构建数据和 AI 领域技术技能的学习者提供了快速参考。 该帖子包含七个类别，每个类别一个频道，但未透露具体频道名称，仅提供了缩短的 URL。

twitter · RodmanAi · May 21, 04:57

**背景**: YouTube 是一个流行的自学平台，许多频道提供编程、数据分析和机器学习教程。这类精选列表有助于初学者发现信誉良好的教育者。

**标签**: `#YouTube`, `#tech skills`, `#learning resources`

---

<a id="item-27"></a>
## [20 个支付美元的远程工作网站](https://twitter.com/RodmanAi/status/2057025456482947547) ⭐️ 3.0/10

@RodmanAi 在推特上发布了一个帖子，列出了 20 个提供美元支付远程工作的网站，但没有给出任何描述或分析。 这份列表可能帮助求职者找到以美元支付的远程工作机会，但缺乏背景信息降低了其实用价值。 该帖子仅包含网址，没有网站名称或描述，因此难以评估每个平台的质量或合法性。

twitter · RodmanAi · May 20, 09:07

**背景**: 以美元支付的远程工作对货币较弱国家的工人具有吸引力，因为它们提供更高的购买力。许多平台如 Upwork、Toptal 和 Remote OK 专门提供此类机会，但这份列表并未具体说明包含哪些网站。

**标签**: `#remote jobs`, `#job search`, `#career`

---

<a id="item-28"></a>
## [谷歌云合作伙伴验证 Gemini 3.5](https://twitter.com/GoogleDeepMind/status/2057137688353071491) ⭐️ 2.0/10

谷歌云宣布与领先组织合作，在其自身环境中验证 Gemini 3.5 系列，GoogleDeepMind 转发了此消息。 此次验证表明 Gemini 3.5 已具备企业级就绪状态，该模型结合了前沿智能与代理能力，可能加速其在生产环境中的采用。 该公告未提及具体合作伙伴名称或验证结果，且推文互动量低（32 次转发），表明即时影响有限。

twitter · GoogleDeepMind · May 20, 16:33

**背景**: Gemini 3.5 是谷歌在 2026 年 Google I/O 大会上发布的最新模型系列，具有增强的代理和编码能力。谷歌云的验证计划有助于确保模型在广泛部署前满足企业需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3.5: frontier intelligence with action - The Keyword</a></li>
<li><a href="https://llm-stats.com/models/gemini-3.5-flash">Gemini 3.5 Flash Benchmarks, Pricing & Context Window</a></li>
<li><a href="https://noqta.tn/en/news/google-io-2026-gemini-35-agent-tools">Google I/O 2026: Gemini 3.5 Series and Antigravity 2.0 Usher ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google`, `#Gemini`, `#partnership`

---

<a id="item-29"></a>
## [Yann LeCun 转发 1 月 6 日贿赂基金文章](https://twitter.com/ylecun/status/2057579660976746761) ⭐️ 2.0/10

Yann LeCun 转发了 Mike Levin 的一条推文，该推文链接到《纽约时报》一篇关于 1 月 6 日贿赂基金的文章，该基金指特朗普总统设立的 17.76 亿美元纳税人资助基金，用于支持 1 月 6 日暴乱者及其盟友。 这条转发引起了对一项涉及涉嫌滥用纳税人资金的有争议政治问题的关注，尽管这与 LeCun 主要关注的软件工程或 AI 研究并不直接相关。 该贿赂基金源于特朗普与 IRS 之间的和解，一项名为 SLUSH 基金法案的法案已被提出以对其征税。1 月 6 日事件的警察已提起诉讼，指控总统腐败。

twitter · ylecun · May 21, 21:49

**背景**: 1 月 6 日贿赂基金指特朗普总统通过 IRS 和解设立的 17.76 亿美元基金，旨在支持参与 1 月 6 日国会山袭击的个人及其他政治盟友。批评者认为这是对纳税人资金的腐败使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.thebulwark.com/p/of-slush-funds-and-suckups-trump-irs-settlement-weaponization-january-6-cornyn-paxton-massie-republicans-gop">Of Slush Funds and Suckups</a></li>
<li><a href="https://mikethompson.house.gov/newsroom/press-releases/thompson-ways-means-democrats-introduce-bill-tax-presidents-corrupt-slush">THOMPSON, WAYS & MEANS DEMOCRATS INTRODUCE BILL TO TAX PRESIDENT’S CORRUPT SLUSH FUND FOR JANUARY 6 RIOTERS | Representative Mike Thompson</a></li>
<li><a href="https://www.theguardian.com/us-news/2026/may/20/jan-6-police-sue-trump-anti-weaponization-fund">January 6 officers sue Trump over $1.8bn fund, alleging ‘presidential corruption’ | US politics | The Guardian</a></li>

</ul>
</details>

**标签**: `#politics`, `#news`

---

<a id="item-30"></a>
## [Yann LeCun 转发政治类纽约时报文章](https://twitter.com/ylecun/status/2057474779779834226) ⭐️ 2.0/10

Yann LeCun 转发了 Mike Levin 的一条推文，该推文推荐了一篇关于政治事件的纽约时报文章，但推文本身不包含任何技术或学术内容。 这条推文与技术社区的相关性很低，对学术或技术讨论没有贡献。 该推文是一条转发，由于政治性质且缺乏技术深度，评分仅为 2.0/10。

twitter · ylecun · May 21, 14:53

**标签**: `#politics`, `#news`, `#twitter`

---

<a id="item-31"></a>
## [转发赞扬法国主权与核威慑](https://twitter.com/ylecun/status/2057363332210868325) ⭐️ 2.0/10

Yann LeCun 转发了一条来自 @marcosagusstinn 的推文，称法国是少数真正理解主权的欧洲国家之一，因为它建立了自己的核威慑力量。 这条转发突出了关于国家主权和国防的政治观点，但对于关注软件工程、AI/ML 或系统研究的技术受众来说，这并不相关。 原推文强调法国独立的核能力是主权的象征。Yann LeCun 作为知名 AI 研究者的转发可能会让一些期待技术内容的关注者感到意外。

twitter · ylecun · May 21, 07:30

**标签**: `#politics`, `#sovereignty`, `#nuclear`

---

<a id="item-32"></a>
## [Yann LeCun 转发纽约时报关于支出的观点](https://twitter.com/ylecun/status/2057361496737272304) ⭐️ 2.0/10

Yann LeCun 转发了一篇《纽约时报》观点文章，批评总统的支出政策，称美国人应该清醒地看到总统正在拿走他们的钱并大肆挥霍。 该转发与技术和学术内容策展无关，因为它关注的是美国政治，而非软件工程、AI/ML 或系统研究。 该推文是转发，LeCun 未添加任何评论，原始观点文章需付费阅读。由于相关性低，评分为 2.0/10。

twitter · ylecun · May 21, 07:22

**标签**: `#politics`, `#news`, `#off-topic`

---

<a id="item-33"></a>
## [低质量推文：'历史的错误一方'引用](https://twitter.com/ylecun/status/2057357559468593655) ⭐️ 2.0/10

Yann LeCun 转发了@Microinteracti1 的一条引用，内容为'历史的错误一方有一种非常特定的气味'，没有附加任何背景或技术内容。 这条推文没有技术或学术价值，对 AI 或技术领域的有意义讨论没有贡献。 该推文被截断，看起来像是一句引用或梗图，缺乏任何实质性信息或讨论。

twitter · ylecun · May 21, 07:07

**标签**: `#low-quality`, `#off-topic`, `#twitter`

---

<a id="item-34"></a>
## [特朗普审查指控与美国新闻自由排名](https://twitter.com/ylecun/status/2057355497498357921) ⭐️ 2.0/10

Yann LeCun 转发 Anders Aslund 的推文，声称特朗普成功审查了大多数美国主流媒体，并引用美国在世界新闻自由指数中排名第 64 位。 这一说法凸显了关于美国新闻自由的持续辩论，以及政治领导层对媒体独立性的影响，这与民主制度和信息完整性的讨论相关。 世界新闻自由指数由无国界记者组织发布，根据多元化、媒体独立性、自我审查等标准对 180 个国家进行排名。近年来美国排名有所波动，批评者指出特朗普和拜登政府的行动均影响了新闻自由。

twitter · ylecun · May 21, 06:59

**背景**: 世界新闻自由指数（WPFI）是无国界记者组织发布的年度排名，根据多元化、媒体独立性和自我审查等标准评估各国的新闻自由水平。近年来美国排名下降，一些人将其归因于对媒体的政治压力和对记者的法律行动。该推文引用了关于特朗普审查的具体说法，这是关于政府对媒体影响的更广泛辩论的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_Press_Freedom_Index">World Press Freedom Index - Wikipedia</a></li>
<li><a href="https://rsf.org/en/index">Index | RSF</a></li>
<li><a href="https://thehill.com/policy/technology/5801022-doj-settlement-social-media/">Trump administration settles social media censorship case have any of trumps media censorships stuck or have the... Top Stories USA: 8 ways Trump is shrinking the space for press freedom ... Trump's moves against media outlets mirror authoritarian ... Trump ramps up bullying and censorship efforts against media</a></li>

</ul>
</details>

**标签**: `#politics`, `#media`, `#press freedom`

---

<a id="item-35"></a>
## [低质量推文重复“vibe cad”](https://twitter.com/adamdotnew/status/2057266306907525394) ⭐️ 1.0/10

@adamdotnew 发布了一条推文，仅重复了三次“vibe cad”，没有任何额外背景或技术内容。 这条推文毫无意义，属于低质量的噪音帖子，互动极少，没有实质性讨论。 该推文因重复性强且缺乏技术深度或新颖性，评分仅为 1.0/10。

twitter · adamdotnew · May 21, 01:04

**标签**: `#low-quality`, `#noise`, `#twitter`

---

<a id="item-36"></a>
## [与科技无关的政治推文](https://twitter.com/ylecun/status/2057584047170175083) ⭐️ 1.0/10

Yann LeCun 转发了加州州长的一条推文，指责共和党人从事犯罪活动，这是一条与科技无关的政治声明。 这条推文与技术社区无关，对 AI、机器学习或软件工程的讨论没有贡献。 该推文是对政治指控的转发，与技术主题的相关性评分为 1.0/10。

twitter · ylecun · May 21, 22:07

**标签**: `#politics`, `#off-topic`

---