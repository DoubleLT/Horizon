---
layout: default
title: "Horizon Summary: 2026-06-09 (ZH)"
date: 2026-06-09
lang: zh
---

> From 42 items, 35 important content pieces were selected

---

1. [VLA-JEPA 在 LeRobot 中发布：无监督动作学习](#item-1) ⭐️ 8.0/10
2. [一周内发布 25+个开放权重 AI 模型](#item-2) ⭐️ 8.0/10
3. [独立开发者打造本地私有版 NotebookLM](#item-3) ⭐️ 8.0/10
4. [NVIDIA 免费提供 120 多个 AI 模型一年使用权](#item-4) ⭐️ 8.0/10
5. [ETH Zurich 的 ViserDex：仅用 RGB 相机和 3D 高斯泼溅实现灵巧手控制](#item-5) ⭐️ 7.0/10
6. [斯坦福：本地模型回答 71.3%真实查询](#item-6) ⭐️ 7.0/10
7. [沃顿论文：AI 需将生产率提升 2.7 倍以避免负面影响](#item-7) ⭐️ 7.0/10
8. [Yann LeCun 力挺突破性论文](#item-8) ⭐️ 7.0/10
9. [机器学习模型学习 BCR 亲和力成熟用于变异预测](#item-9) ⭐️ 7.0/10
10. [新论文定义并衡量 AI 政治中立性](#item-10) ⭐️ 7.0/10
11. [Claude Code 团队回顾 GA 一周年](#item-11) ⭐️ 7.0/10
12. [自主挖掘机：建筑领域新兴市场](#item-12) ⭐️ 6.0/10
13. [缆索驱动机器人在硕士论文演示中玩杂耍](#item-13) ⭐️ 6.0/10
14. [Vast 与欧空局签署捷克私人宇航员前往国际空间站协议](#item-14) ⭐️ 6.0/10
15. [SpaceX 猎鹰 9 号第 35 次在无人船着陆](#item-15) ⭐️ 6.0/10
16. [斯坦福 AI 实验室推出 AI 编码输出 CPI](#item-16) ⭐️ 6.0/10
17. [抗体语言模型学到结构，未学到进化](#item-17) ⭐️ 6.0/10
18. [开源 AI 代理聚合智慧对话](#item-18) ⭐️ 6.0/10
19. [AIRSKIN 智能安全垫实现无围栏人机协作](#item-19) ⭐️ 5.0/10
20. [星链为巴拉圭学校提供互联网连接](#item-20) ⭐️ 5.0/10
21. [SpaceX 发射 21 颗星链和 2 颗星盾卫星](#item-21) ⭐️ 5.0/10
22. [意见分歧者也能就优质 AI 回答达成共识](#item-22) ⭐️ 5.0/10
23. [SpaceX 用猎鹰 9 号发射 29 颗星链卫星](#item-23) ⭐️ 4.0/10
24. [纽约大学成立多学科地球系统研究所](#item-24) ⭐️ 4.0/10
25. [Claude AI 宣布东京活动](#item-25) ⭐️ 4.0/10
26. [19 岁少年用 ESP8266 和 Claude AI 打造智能灯开关](#item-26) ⭐️ 4.0/10
27. [Lukas Ziegler 将在伦敦科技周主持机器人小组讨论](#item-27) ⭐️ 3.0/10
28. [星链将为威兹航空提供机上 Wi-Fi](#item-28) ⭐️ 3.0/10
29. [LeRobotHF 转推承诺提供模型技术细节](#item-29) ⭐️ 3.0/10
30. [花旗推广 SpaceX IPO 面向散户投资者](#item-30) ⭐️ 2.0/10
31. [转推反对暂停 AI 开发，缺乏实质内容](#item-31) ⭐️ 2.0/10
32. [关于 NIH 拨款政策变化的转发](#item-32) ⭐️ 2.0/10
33. [转发大卫·萨尔诺夫传记](#item-33) ⭐️ 2.0/10
34. [Google TurboVec 声称将 AI 内存减少 92%](#item-34) ⭐️ 2.0/10
35. [SpaceX 转发的采访缺乏技术深度](#item-35) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [VLA-JEPA 在 LeRobot 中发布：无监督动作学习](https://twitter.com/ylecun/status/2064102718377955693) ⭐️ 8.0/10

VLA-JEPA，一种无需显式监督即可学习动作的新型视觉-语言-动作模型，已在 LeRobot 机器人框架中发布。该模型采用 JEPA 风格的预训练方法，专注于与动作相关的状态转换，而非像素级细节。 此次发布标志着向更高效、更泛化的机器人学习迈出了重要一步，因为 VLA-JEPA 可以利用互联网规模的视频数据，而无需昂贵的动作标注。它可能加速从多样化、非结构化视觉数据中学习的机器人的开发。 VLA-JEPA 基于 JEPA（联合嵌入预测架构）框架构建，该框架避免像素级重建，而是预测未来状态的潜在表示。该模型可在 LeRobot 中获取，LeRobot 是一个基于 PyTorch 的开源机器人研究框架。

twitter · ylecun · Jun 8, 21:50

**背景**: 视觉-语言-动作（VLA）模型结合了视觉、语言和动作模态用于机器人控制。传统的 VLA 预训练通常使用潜在动作目标，这些目标无意中关注像素变化而非有意义的动作相关变化。JEPA 风格的模型通过学习在潜在空间中预测未来状态的抽象表示来解决这一问题，使其对外观偏差和干扰运动更加鲁棒。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.10098">[2602.10098] VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model</a></li>
<li><a href="https://github.com/ginwind/VLA-JEPA">GitHub - ginwind/VLA-JEPA: VLA-JEPA: Enhancing Vision-Language-Action Model with Latent World Model · GitHub</a></li>
<li><a href="https://huggingface.co/lerobot">lerobot ( LeRobot )</a></li>

</ul>
</details>

**标签**: `#robotics`, `#AI`, `#VLA-JEPA`, `#LeRobot`, `#unsupervised learning`

---

<a id="item-2"></a>
## [一周内发布 25+个开放权重 AI 模型](https://twitter.com/ylecun/status/2063611471167144340) ⭐️ 8.0/10

Yann LeCun 转发了一条推文，承认一周内发布了超过 25 个值得关注的开放权重 AI 模型，标志着开放 AI 进展的非凡速度。 开放权重模型的大量发布加速了 AI 领域的创新和可访问性，使全球研究者和开发者能够在没有专有限制的情况下基于最先进的模型进行构建。 开放权重模型提供最终训练参数，允许微调和部署，但不提供训练数据或代码的完全透明。该推文强调了社区对这种快速发布节奏的认可。

twitter · ylecun · Jun 7, 13:18

**背景**: 开放权重模型是指其训练参数（权重和偏置）公开发布的 AI 模型，使他人能够运行、微调和集成这些模型。与完全开源模型不同，开放权重发布可能不包括训练数据或代码，但仍能促进可重复性并降低先进 AI 的门槛。最近的例子包括 OpenAI 的 gpt-oss 系列以及各种编码模型，如 GLM-5.1 和 DeepSeek V4-Pro。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open-Weights Model? | AI21</a></li>
<li><a href="https://openai.com/index/introducing-gpt-oss/">Introducing gpt-oss | OpenAI</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，许多人对开放权重模型的快速发布感到兴奋。一些评论者指出这一趋势使 AI 访问民主化，而另一些人则提醒开放权重模型可能仍缺乏完全透明度。

**标签**: `#open-source`, `#AI`, `#models`, `#open-weight`, `#community`

---

<a id="item-3"></a>
## [独立开发者打造本地私有版 NotebookLM](https://twitter.com/RodmanAi/status/2064025497273852323) ⭐️ 8.0/10

一位独立开发者构建了 Google NotebookLM 的完全本地化、保护隐私的替代品，能够处理 PDF、YouTube 视频、音频、网站和文档，并完全在用户机器上生成 AI 播客。 这表明检索增强生成和播客合成等复杂 AI 功能可以在本地运行，为用户提供完全的数据隐私和离线能力，无需依赖云服务。 该工具支持多种输入类型，包括 PDF、YouTube 视频、音频文件、网站和文档，并能从用户数据生成 AI 播客，全程无需云端处理，无数据泄露风险。

twitter · RodmanAi · Jun 8, 16:43

**背景**: NotebookLM 是 Google 的 AI 驱动研究和笔记工具，利用检索增强生成帮助用户与文档交互，以其生成播客式讨论的音频概述功能而闻名。本地运行此类模型需要大量计算资源，但确保数据永不离开用户设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NotebookLM">NotebookLM</a></li>
<li><a href="https://datanorth.ai/blog/local-llms-privacy-security-and-control">Local LLM: Privacy, Security, and Control - DataNorth AI</a></li>
<li><a href="https://notegpt.io/ai-podcast-generator">AI Podcast Generator – Turn Any Content into a Podcast Free</a></li>

</ul>
</details>

**标签**: `#AI`, `#privacy`, `#local LLM`, `#open source`, `#productivity`

---

<a id="item-4"></a>
## [NVIDIA 免费提供 120 多个 AI 模型一年使用权](https://twitter.com/RodmanAi/status/2063653720458731636) ⭐️ 8.0/10

NVIDIA 宣布免费提供超过 120 个 AI 模型，每分钟 40 次请求，有效期一整年，无需信用卡。 此举大幅降低了开发者和创作者尝试最先进 AI 模型的门槛，可能加速 AI 创新和普及。 该优惠包括 120 多个模型、每分钟 40 次请求和一年免费使用，无需信用卡或付款。

twitter · RodmanAi · Jun 7, 16:06

**背景**: NVIDIA 是 AI 硬件和软件的领先提供商。此免费套餐允许开发者无需前期成本即可测试和集成 NVIDIA 的 AI 模型，与其他云 AI 服务竞争。

**标签**: `#NVIDIA`, `#AI models`, `#free access`, `#developer tools`

---

<a id="item-5"></a>
## [ETH Zurich 的 ViserDex：仅用 RGB 相机和 3D 高斯泼溅实现灵巧手控制](https://twitter.com/lukas_m_ziegler/status/2063678741386342895) ⭐️ 7.0/10

ETH Zurich 的研究人员开发了 ViserDex，这是一个仅使用单目 RGB 相机和 3D 高斯泼溅技术实现手中物体重新定向的仿真到现实框架。 这项工作通过消除对专用深度传感器或触觉反馈的需求，推进了灵巧操作的发展，可能降低机器人手的成本和复杂性。 ViserDex 利用 3D 高斯泼溅从 RGB 图像中表示物体的几何和外观，使得在仿真中精确重新定向，并能迁移到真实机器人上。

twitter · lukas_m_ziegler · Jun 7, 17:45

**背景**: 3D 高斯泼溅是一种体渲染技术，能从稀疏的 2D 图像创建逼真的 3D 场景。仿真到现实框架在仿真中训练策略，并直接部署到真实硬件上，无需额外真实数据，从而弥合现实差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/3D_Gaussian_splatting">3D Gaussian splatting</a></li>
<li><a href="https://arxiv.org/abs/2501.05439">From Simple to Complex Skills: The Case of In-Hand Object Reorientation</a></li>

</ul>
</details>

**标签**: `#robotics`, `#computer vision`, `#3D Gaussian Splatting`, `#sim-to-real`, `#dexterous manipulation`

---

<a id="item-6"></a>
## [斯坦福：本地模型回答 71.3%真实查询](https://twitter.com/ylecun/status/2064082422010925178) ⭐️ 7.0/10

斯坦福大学的研究发现，本地模型能够回答 71.3%的真实聊天和推理问题，挑战了本地模型远不如云端模型的普遍说法。 这一发现表明本地模型可能比通常认为的更强大，可能减少许多应用对云端 API 的依赖，并影响 AI 部署策略。 该研究由斯坦福大学的研究人员进行，专门衡量了在真实聊天和推理任务上的表现，而不仅仅是基准数据集。

twitter · ylecun · Jun 8, 20:29

**背景**: 本地模型是指在用户自己的硬件上运行的人工智能模型，而非在云服务器上。它们通常被认为不如 GPT-4 等大型云端模型强大，但在隐私、延迟和成本方面具有优势。

**社区讨论**: Yann LeCun 的推文强调这是一个“叙事违规”，表明该发现与普遍假设相矛盾。社区讨论有限，但转发量表明人们对挑战主流叙事感兴趣。

**标签**: `#AI`, `#local models`, `#research`, `#Stanford`

---

<a id="item-7"></a>
## [沃顿论文：AI 需将生产率提升 2.7 倍以避免负面影响](https://twitter.com/ylecun/status/2064041550527508785) ⭐️ 7.0/10

沃顿商学院的一篇论文得出结论：AI 必须迅速将生产率提升 2.7 倍，否则科技公司将面临负面经济影响。 这一发现为 AI 投资和发展设定了关键基准，若未能达到这一生产率阈值，可能导致科技公司乃至整个经济遭受重大损失。 该论文专门针对科技公司的影响，指出如果 AI 不能快速带来显著的生产率提升，这些公司可能会面临回报减少或竞争优势丧失。

twitter · ylecun · Jun 8, 17:47

**背景**: 生产率增长是经济繁荣的关键驱动力，而 AI 被广泛预期能提升生产率。然而，量化这种提升所需的幅度和速度对于商业战略和政策制定至关重要。沃顿的论文为 AI 的经济影响提供了一个具体、可操作的目标。

**标签**: `#AI`, `#productivity`, `#economics`, `#research`

---

<a id="item-8"></a>
## [Yann LeCun 力挺突破性论文](https://twitter.com/ylecun/status/2063664356571660716) ⭐️ 7.0/10

Yann LeCun 转发了 Miles Cranmer 对一篇研究论文的热烈推荐，称其“疯狂”并表示强烈认可。 来自顶尖 AI 研究人员的认可表明该论文可能代表了机器学习领域的重大进展，可能影响未来的研究方向。 推文中包含论文链接 (https://t.co/DP8OR5NJf2) 和一张图片 (https://t.co/rl4Rmr0FhJ)，但未说明论文标题和具体内容。

twitter · ylecun · Jun 7, 16:48

**背景**: Yann LeCun 是著名 AI 研究员、Meta 首席 AI 科学家，以深度学习研究闻名。Miles Cranmer 是剑桥大学的研究员，致力于科学领域的 AI 应用。LeCun 的转发通常会给论文带来极大关注。

**标签**: `#machine learning`, `#research`, `#AI`, `#paper`

---

<a id="item-9"></a>
## [机器学习模型学习 BCR 亲和力成熟用于变异预测](https://twitter.com/berkeley_ai/status/2064095006860906542) ⭐️ 7.0/10

研究人员宣布即将在 ICML 发表一篇论文，应用机器学习建模 BCR 亲和力成熟过程，并用于变异效应预测。 这项工作连接了免疫学和机器学习，有望更准确地预测遗传变异如何影响抗体结合，对疫苗设计和治疗性抗体开发至关重要。 该论文专注于学习 BCR 亲和力成熟的动态过程，即 B 细胞通过体细胞超突变和选择优化抗体亲和力的过程。模型的变异效应预测能力有助于解释免疫相关遗传变异。

twitter · berkeley_ai · Jun 8, 21:19

**背景**: BCR 亲和力成熟是一个关键的免疫过程，生发中心中的 B 细胞通过突变其 B 细胞受体并经历选择，产生高亲和力抗体。变异效应预测工具（如 Ensembl VEP）评估遗传变异对蛋白质功能的影响。这项工作利用机器学习将这两个领域结合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-020-2262-4">BCR selection and affinity maturation in Peyer’s patch germinal centres | Nature</a></li>
<li><a href="https://www.sciencedirect.com/topics/immunology-and-microbiology/affinity-maturation">Affinity Maturation - an overview | ScienceDirect Topics</a></li>
<li><a href="https://www.ensembl.org/vep">Ensembl Variant Effect Predictor (VEP)</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#immunology`, `#ICML`, `#variant effect prediction`

---

<a id="item-10"></a>
## [新论文定义并衡量 AI 政治中立性](https://twitter.com/berkeley_ai/status/2064094357003919433) ⭐️ 7.0/10

一篇新论文和数据集提出了 AI 政治中立性的正式定义和测量框架，由 Jonathan Stray 提出并由 Berkeley AI 分享。 这项工作通过提供评估 AI 系统中政治偏见的 concrete 方法，填补了 AI 伦理中的一个关键空白，对于确保 AI 应用的公平性和可信度至关重要。 该论文包含一个用于测试政治中立性的数据集，但可用内容中未提供数据集大小或评估指标等具体技术细节。

twitter · berkeley_ai · Jun 8, 21:16

**背景**: AI 政治中立性指的是 AI 输出中不存在系统性政治偏见。随着 AI 系统越来越多地用于内容审核、新闻推荐和公共讨论，对政治偏见的担忧日益增加。该论文试图将中立性概念操作化，以便进行实证测量。

**标签**: `#AI ethics`, `#political neutrality`, `#AI safety`, `#dataset`

---

<a id="item-11"></a>
## [Claude Code 团队回顾 GA 一周年](https://twitter.com/ClaudeDevs/status/2064032814392352816) ⭐️ 7.0/10

Claude Code 团队（包括 @bcherny 和 @_catwu）在正式发布一周年之际发布回顾，分享了验证最佳实践、自动模式的设计理由以及关于 routines 和 loops 的见解。 这次回顾为使用 AI 辅助编码工具的开发者提供了宝贵指导，展示了如何安全有效地将 Claude Code 集成到工作流中，可能影响整个行业的最佳实践。 自动模式通过将工具调用路由到分类器来阻止破坏性操作，从而允许 Claude Code 无需权限提示即可运行；而 routines 和 loops 则支持自动化、定时或事件驱动的 Claude Code 会话云运行。

twitter · ClaudeDevs · Jun 8, 17:12

**背景**: Claude Code 是 Anthropic 为开发者提供的智能编码工具，能够理解代码库、编辑文件并运行命令。它于一年前正式发布。该工具使用 Anthropic Claude 系列的大语言模型，这些模型通过宪法 AI 训练以提高安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://code.claude.com/docs/en/auto-mode-config">Configure auto mode - Claude Code Docs</a></li>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude</a></li>

</ul>
</details>

**社区讨论**: Twitter 上的 59 条回复表明社区参与度适中，开发者可能正在讨论自动模式和验证实践的实际影响，但未提供具体评论。

**标签**: `#AI-assisted coding`, `#Claude Code`, `#best practices`, `#developer tools`, `#retrospective`

---

<a id="item-12"></a>
## [自主挖掘机：建筑领域新兴市场](https://twitter.com/lukas_m_ziegler/status/2063896051631653291) ⭐️ 6.0/10

Lukas Ziegler 访问了苏黎世的 GravisRobotics，亲身体验了其自主挖掘机技术，并指出自主建筑机械是一个新兴市场。 自主挖掘机可显著提升建筑行业的安全性和生产力——该行业在自主化讨论中常被忽视，有望将事故率降低并提升效率高达 30%。 GravisRobotics 通过加装传感器和平板界面（Gravis Slate）对现有挖掘机进行改造，实现自主操作同时保留手动控制；该公司近期融资 2300 万美元以加速全球部署。

twitter · lukas_m_ziegler · Jun 8, 08:08

**背景**: 自主挖掘机利用传感器、人工智能和机器人技术，无需持续人工干预即可完成挖掘、平整和物料搬运等任务。全球智能建筑挖掘机市场预计到 2033 年将达到 150 亿美元，年复合增长率为 12%。GravisRobotics 的技术旨在增强而非取代人类操作员。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gravisrobotics.com/">Gravis Robotics | Autonomous Earthmoving Technology</a></li>
<li><a href="https://roboticsandautomationnews.com/2025/11/29/gravis-robotics-raises-23-million-and-signs-series-of-landmark-deals/97107/">Gravis Robotics raises $23 million to accelerate global rollout of autonomous earthmoving technology</a></li>
<li><a href="https://www.strategicrevenueinsights.com/industry/intelligent-construction-excavator-market">Intelligent Construction Excavator Market Size , Future Growth and...</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#construction`, `#robotics`

---

<a id="item-13"></a>
## [缆索驱动机器人在硕士论文演示中玩杂耍](https://twitter.com/lukas_m_ziegler/status/2063612448008032659) ⭐️ 6.0/10

一款名为 CableEndy 的缆索驱动并联机器人，作为布尔诺理工大学硕士论文的一部分，展示了抛接球的能力。该项目在 B&R 工业自动化布尔诺办公室进行了展示。 这一演示突显了缆索驱动并联机器人所能达到的精度和控制能力，这类机器人越来越多地用于需要大工作空间和高速度的工业自动化任务。同时，它也展示了学生在实际环境中的工程实践技能。 CableEndy 是一种缆索驱动并联机器人（CDPR），它使用由电机驱动的柔性缆索来控制末端执行器的位置。抛接球任务需要精确协调缆索的张力和长度，以有节奏地接住并抛出球。

twitter · lukas_m_ziegler · Jun 7, 13:22

**背景**: 缆索驱动并联机器人（CDPR）是一种并联机械臂，其中柔性缆索取代了刚性连杆，从而能够实现大工作空间和高负载自重比。它们常用于大型 3D 打印、仓库自动化和摄像系统等应用。B&R 工业自动化是一家奥地利公司，现为 ABB 集团成员，专注于自动化和过程控制技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cable_robots">Cable robots - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/B&R">B & R - Wikipedia</a></li>

</ul>
</details>

**标签**: `#robotics`, `#cable-driven robot`, `#engineering`, `#master's thesis`

---

<a id="item-14"></a>
## [Vast 与欧空局签署捷克私人宇航员前往国际空间站协议](https://twitter.com/SpaceX/status/2064004410305585329) ⭐️ 6.0/10

Vast 公司与欧洲空间局（ESA）代表捷克共和国签署了一项协议，将执行一次前往国际空间站（ISS）的私人宇航员任务。 此次任务标志着商业航天领域的进一步发展，使捷克共和国等较小国家能够通过私人合作伙伴关系进入国际空间站。同时，这也巩固了 Vast 作为私人宇航员任务提供商的地位。 该协议由 Vast 与欧空局签署，捷克共和国作为赞助国。任务预计最早于 2026 年发射，尚需 NASA 批准和日程安排。

twitter · SpaceX · Jun 8, 15:19

**背景**: 前往国际空间站的私人宇航员任务始于 2022 年 4 月的公理一号任务。Vast 是一家总部位于加利福尼亚的航空航天公司，成立于 2021 年，旨在开发商业空间站。捷克共和国是欧空局成员国，此前曾通过俄罗斯联盟号任务将宇航员送入太空。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vast_(company)">Vast (company) - Wikipedia</a></li>
<li><a href="https://www.nasa.gov/humans-in-space/private-astronaut-missions/">Private Astronaut Missions - NASA</a></li>

</ul>
</details>

**标签**: `#space`, `#ISS`, `#private astronaut mission`, `#ESA`

---

<a id="item-15"></a>
## [SpaceX 猎鹰 9 号第 35 次在无人船着陆](https://twitter.com/SpaceX/status/2063932254460494191) ⭐️ 6.0/10

SpaceX 实现了猎鹰 9 号火箭助推器第 35 次在无人船“A Shortfall of Gravitas”上发射并着陆。 这一里程碑凸显了 SpaceX 在重复使用火箭助推器方面的持续成功，降低了发射成本并推动了太空进入。 着陆是在自主无人船“A Shortfall of Gravitas”上完成的，该船具备自主航行能力。

twitter · SpaceX · Jun 8, 10:32

**背景**: SpaceX 的猎鹰 9 号一级助推器是可重复使用的，自 2018 年以来该公司常规回收并重复使用它们。无人船“A Shortfall of Gravitas”是用于海上着陆的多个自主平台之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Autonomous_spaceport_drone_ship">Autonomous spaceport drone ship - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_Falcon_9_first-stage_boosters">List of Falcon 9 first-stage boosters - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Falcon_9">Falcon 9 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#rocket landing`, `#reusable rockets`, `#space technology`

---

<a id="item-16"></a>
## [斯坦福 AI 实验室推出 AI 编码输出 CPI](https://twitter.com/StanfordAILab/status/2064030627343798686) ⭐️ 6.0/10

斯坦福 AI 实验室分享了一个针对 AI 编码输出的消费者价格指数（CPI），该指数基于 Anthropic 的 Opus 4.6 模型在 SWE-chat 中的数据构建，用于衡量 token 价值随时间的变化。 该 CPI 提供了一种追踪 AI 编码 token 经济价值的新方法，帮助开发者和企业了解成本趋势，并就 AI 工具的使用做出明智决策。 该指数覆盖 2026 年 2 月 5 日至 4 月 15 日的数据，并包含针对代码存活率上升的享乐调整，揭示了作者所称的“token 通胀”现象。

twitter · StanfordAILab · Jun 8, 17:03

**背景**: AI 中的 token 化是指将文本转换为更小的单元（token）进行处理。消费者价格指数（CPI）衡量一篮子商品价格随时间的平均变化。将 CPI 应用于 AI 编码输出，可以追踪 token 随时间购买编码能力的变化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digg.com/ai/z7lelgif">AI Code Tools CPI Adds Hedonic Adjustment For Rising Code Survival...</a></li>

</ul>
</details>

**标签**: `#AI`, `#economics`, `#coding`, `#tokenization`

---

<a id="item-17"></a>
## [抗体语言模型学到结构，未学到进化](https://twitter.com/berkeley_ai/status/2064094968365584753) ⭐️ 6.0/10

一位研究人员观察到，抗体语言模型能够识别类似抗体的序列，但无法捕捉进化选择如何将幼稚的种系抗体转化为强结合剂。 这凸显了当前抗体语言模型的一个根本性局限，可能阻碍其设计需要理解亲和力成熟过程的有效治疗性抗体的能力。 该推文特别指出，模型学会了“看起来像抗体的东西”，但没有学会产生强结合剂的选择过程，指出了序列识别与功能优化之间的差距。

twitter · berkeley_ai · Jun 8, 21:19

**背景**: 抗体语言模型是在大量抗体序列数据集上训练的机器学习模型，用于预测特性或生成新抗体。种系抗体是基因组编码的初始未突变版本，通过体细胞超突变和选择成为高亲和力结合剂。该推文表明当前模型忽略了这一进化动力学。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2403.17889">Large scale paired antibody language models</a></li>
<li><a href="https://elifesciences.org/articles/111070">Antibody Language Models : Taking the biology seriously makes...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8178282/">Potent germline -like monoclonal antibodies : rapid identification of...</a></li>

</ul>
</details>

**标签**: `#antibody`, `#language models`, `#machine learning`, `#bioinformatics`

---

<a id="item-18"></a>
## [开源 AI 代理聚合智慧对话](https://twitter.com/RodmanAi/status/2063914193917800579) ⭐️ 6.0/10

一款名为 /last30days 的新型开源 AI 研究代理能够并行搜索 Reddit、X、YouTube、TikTok、Hacker News、GitHub、Polymarket 和网络，以寻找智慧对话，这一工具得到了 Lex Fridman 的关注。 该工具通过聚合多个平台的内容，使高质量讨论的获取更加民主化，可能为研究人员和爱好者节省大量时间。它代表了 AI 驱动内容策展的日益增长趋势。 该代理并行搜索八个来源，包括基于加密货币的预测市场 Polymarket。它是开源的，但推文具有宣传性质，缺乏关于底层模型或架构的技术细节。

twitter · RodmanAi · Jun 8, 09:21

**背景**: Lex Fridman 是一位知名播客主持人，采访 AI、科学和技术领域的知名人物。/last30days 是一款 AI 研究代理，聚合多个在线平台的内容以呈现值得关注的讨论，类似于其他 AI 驱动的新闻聚合器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Polymarket">Polymarket</a></li>
<li><a href="https://grokipedia.com/page/Hacker_News">Hacker News</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#research`, `#aggregator`

---

<a id="item-19"></a>
## [AIRSKIN 智能安全垫实现无围栏人机协作](https://twitter.com/lukas_m_ziegler/status/2064028859394109766) ⭐️ 5.0/10

Lukas Ziegler 展示了一个使用 AIRSKIN 智能安全垫的无围栏人机协作应用，只需轻触即可立即停止机器人。 这项技术有望取代工业环境中的物理安全围栏，在保证生产效率的同时实现更安全、更灵活的人机交互。 AIRSKIN 安全垫是一种柔软、气密的表皮，覆盖在柔性阻尼结构上，并配备智能安全电子元件；它通过压电泵维持内部气压以实现触觉灵敏度。

twitter · lukas_m_ziegler · Jun 8, 16:56

**背景**: 传统工业机器人在安全围栏后运行以防止伤害。协作机器人旨在与人类并肩工作，但安全标准仍要求进行风险评估。AIRSKIN 安全垫提供柔软、压力敏感的表面，能够检测接触并触发立即停止，从而实现无围栏操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://airskin.io/airskin.html">Learn about the AIRSKIN technology, it's functionality and how...</a></li>
<li><a href="https://www.youtube.com/watch?v=-sHcQcFd7-A">AIRSKIN ® product video - YouTube</a></li>
<li><a href="https://tipteh.com/al/machine-safety/collaborative-robot-affordable-with-airskin-equipment/">Airskin safety touch sensor for affordable collaborative robots</a></li>

</ul>
</details>

**标签**: `#robotics`, `#safety`, `#human-robot collaboration`, `#smart pads`

---

<a id="item-20"></a>
## [星链为巴拉圭学校提供互联网连接](https://twitter.com/SpaceX/status/2064022843319369777) ⭐️ 5.0/10

SpaceX 的星链正在巴拉圭提供卫星互联网连接，以支持学校和学生的在线学习，使他们能够访问必要的在线服务和资源。 这一扩展有助于缩小服务不足地区的数字鸿沟，为之前缺乏可靠互联网接入的学生提供教育机会。 星链运营着高度在 500-1200 公里的低地球轨道（LEO）卫星星座，提供低延迟宽带服务。在巴拉圭，每月服务费用约为 450,000 巴拉圭瓜拉尼（约 58 美元）。

twitter · SpaceX · Jun 8, 16:32

**背景**: 星链是 SpaceX 开发的卫星互联网星座，旨在为全球偏远和农村地区提供高速、低延迟的互联网。巴拉圭与许多发展中国家一样，在互联网基础设施方面面临挑战，尤其是在农村学校。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>
<li><a href="https://www.tedic.org/en/starlink-in-paraguay-are-there-risks-or-concerns-about-this-technology/">Starlink in Paraguay : are there risks or concerns about this technology?</a></li>
<li><a href="https://satspeedcheck.com/cost/paraguay/">Starlink Cost in Paraguay 2026: Price, Hardware, and 5-Year TCO</a></li>

</ul>
</details>

**标签**: `#Starlink`, `#connectivity`, `#education`, `#Paraguay`

---

<a id="item-21"></a>
## [SpaceX 发射 21 颗星链和 2 颗星盾卫星](https://twitter.com/SpaceX/status/2063502527358816513) ⭐️ 5.0/10

SpaceX 从加州发射了一枚猎鹰 9 号火箭，搭载了 21 颗星链卫星和 2 颗星盾卫星，部署已确认。 此次发射凸显了 SpaceX 在商业宽带和军事太空能力方面的双重角色，星盾为美国国防提供先进的监视和导弹跟踪能力。 星盾卫星是美国政府一份价值 18 亿美元的机密合同的一部分，用于导弹跟踪和侦察。猎鹰 9 号的第一级可能降落在无人船上，尽管未明确说明。

twitter · SpaceX · Jun 7, 06:05

**背景**: 星链是 SpaceX 的卫星互联网星座，提供全球覆盖。星盾是一个独立的业务部门，将星链技术用于军事用途，包括目标跟踪和早期导弹预警。美国太空发展局和太空军是主要客户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starshield_(satellite_constellation)">Starshield (satellite constellation)</a></li>
<li><a href="https://www.spacex.com/starshield">SpaceX - Starshield</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#satellite launch`, `#space technology`

---

<a id="item-22"></a>
## [意见分歧者也能就优质 AI 回答达成共识](https://twitter.com/berkeley_ai/status/2064094377086173250) ⭐️ 5.0/10

一项研究发现，在某个问题上意见严重分歧的人仍然能就什么是好的 AI 回答达成共识，这表明即使在两极分化的情况下，人们对 AI 质量也存在共同标准。 这很重要，因为它表明即使在有争议的领域，AI 回答的质量也可以被客观评估，这有助于建立对 AI 系统的信任并指导对齐工作。 该研究由包括 Serina Chang 在内的研究人员进行，可能让持有对立观点的参与者评估 AI 生成回答的质量。

twitter · berkeley_ai · Jun 8, 21:17

**背景**: AI 回答的质量通常是主观的，尤其是在有争议的话题上。这项研究探讨了尽管存在个人分歧，人们在评判 AI 输出时是否存在共同点，这对于开发服务多样化用户的 AI 至关重要。

**标签**: `#AI`, `#research`, `#human-computer interaction`

---

<a id="item-23"></a>
## [SpaceX 用猎鹰 9 号发射 29 颗星链卫星](https://twitter.com/SpaceX/status/2063924878944702743) ⭐️ 4.0/10

SpaceX 于 2026 年 6 月 8 日从佛罗里达州用猎鹰 9 号火箭将 29 颗星链卫星送入近地轨道，部署已确认。 此次发射延续了星链星座的快速扩张，目前该星座已拥有超过 10,000 颗卫星，为全球超过 1200 万用户提供服务，进一步推动了全球宽带互联网覆盖。 此次任务使用的猎鹰 9 号助推器很可能是经过飞行验证的，截至 2026 年 6 月，SpaceX 已成功回收助推器 598 次。这 29 颗卫星加入了计划中近 12,000 颗卫星的星座。

twitter · SpaceX · Jun 8, 10:03

**背景**: 星链是由 SpaceX 运营的卫星互联网星座，为约 150 个国家提供宽带服务。猎鹰 9 号是一种部分可重复使用的中型运载火箭，以其高可靠性和高发射频率而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starlink_(satellite_constellation)">Starlink (satellite constellation)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Falcon_9_rocket">Falcon 9 rocket</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#satellite`, `#launch`

---

<a id="item-24"></a>
## [纽约大学成立多学科地球系统研究所](https://twitter.com/ylecun/status/2064048494751408342) ⭐️ 4.0/10

纽约大学宣布成立新的地球系统研究所，这是一个旨在应对复杂环境挑战的多学科研究中心。 该研究所将促进气候科学、生态学和政策等领域的合作，可能加速应对气候变化和可持续性等紧迫全球问题的解决方案。 该研究所设在纽约大学库朗数学科学研究所，将涉及多个院系的研究人员，但具体研究项目或资金细节尚未披露。

twitter · ylecun · Jun 8, 18:14

**背景**: 地球系统科学整合多个学科，将地球作为一个复杂的互联系统进行研究。纽约大学的新研究所旨在利用其在数学、数据科学和环境研究方面的现有优势，解决跨学科问题。

**标签**: `#academia`, `#earth systems`, `#NYU`

---

<a id="item-25"></a>
## [Claude AI 宣布东京活动](https://twitter.com/claudeai/status/2064139073590104402) ⭐️ 4.0/10

Claude AI 宣布在东京举办最后一站活动，参与者可直接听取 Claude 团队成员的分享。 该活动为东京的 AI 社区提供了与 Claude 开发者直接交流的机会，可能促进合作与反馈。 推文中提供了活动注册链接，但未提及具体日期、地点或议程细节。

twitter · claudeai · Jun 9, 00:14

**背景**: Claude 是由 Anthropic 开发的 AI 助手。该公司偶尔会举办活动来展示其技术并与用户互动。

**标签**: `#Claude`, `#event`, `#AI`

---

<a id="item-26"></a>
## [19 岁少年用 ESP8266 和 Claude AI 打造智能灯开关](https://twitter.com/RodmanAi/status/2063966342076899719) ⭐️ 4.0/10

一名 19 岁少年没有工程或编程经验，仅用 ESP8266 开发板、舵机和 Anthropic 的 Claude AI，在 2 小时内打造了一个智能灯开关，包括 AI 生成的固件和移动应用。 这展示了 AI 辅助开发如何大幅降低物联网项目的入门门槛，使非专业人士能够快速、低成本地创建功能性的智能家居设备。 该项目总成本不到 2 美元，使用 ESP8266 Wi-Fi 微控制器和舵机物理拨动灯开关。固件和移动应用完全由 Claude AI 生成。

twitter · RodmanAi · Jun 8, 12:48

**背景**: ESP8266 是一款低成本的 Wi-Fi 系统级芯片，在物联网项目中很受欢迎；Claude 是 Anthropic 开发的大型语言模型，能够生成代码。该项目体现了利用 AI 自动化硬件项目软件开发的增长趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ESP8266">ESP8266</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_AI">Claude AI</a></li>

</ul>
</details>

**标签**: `#smart home`, `#ESP8266`, `#AI-generated code`, `#DIY`

---

<a id="item-27"></a>
## [Lukas Ziegler 将在伦敦科技周主持机器人小组讨论](https://twitter.com/lukas_m_ziegler/status/2063913497902096896) ⭐️ 3.0/10

Lukas Ziegler 在 Twitter 上宣布，他将在伦敦科技周主持一场关于供应链中机器人技术和物理 AI 的小组讨论。 该小组将汇聚顶尖机器人创始人，讨论物理 AI 将如何改变供应链，突显了 AI 与机器人技术在工业中日益融合的趋势。 该小组将重点讨论物理 AI 对供应链的影响，Ziegler 将与机器人创始人共同主持讨论。

twitter · lukas_m_ziegler · Jun 8, 09:18

**背景**: 伦敦科技周是英国一项重要的科技活动，聚焦新兴技术趋势。物理 AI 指的是与物理世界交互的 AI 系统，例如机器人和自动驾驶车辆。

**标签**: `#robotics`, `#event`, `#supply chain`

---

<a id="item-28"></a>
## [星链将为威兹航空提供机上 Wi-Fi](https://twitter.com/SpaceX/status/2063955731305414738) ⭐️ 3.0/10

SpaceX 通过推特宣布，星链将为威兹航空航班提供快速可靠的连接，使乘客能够无缝地流媒体、浏览和上网。 这标志着星链航空连接服务的又一次扩展，有望提升乘客体验，并为低成本航空公司采用卫星互联网树立先例。 威兹航空是一家匈牙利低成本航空公司；此次合作旨在为其机队提供机上 Wi-Fi，但未披露具体技术细节或部署时间表。

twitter · SpaceX · Jun 8, 12:06

**背景**: 星链是由 SpaceX 运营的卫星互联网星座，利用低地球轨道卫星在全球范围内提供高速互联网。传统的机上连接依赖于地球静止卫星或空对地网络，而星链的低轨星座提供更低的延迟和更高的带宽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/guide-how-starlink-internet-works-patrick-mutabazi-rtr2e">A Guide to How Starlink Internet Works</a></li>

</ul>
</details>

**标签**: `#Starlink`, `#satellite internet`, `#aviation`

---

<a id="item-29"></a>
## [LeRobotHF 转推承诺提供模型技术细节](https://twitter.com/ylecun/status/2064169589454278924) ⭐️ 3.0/10

Yann LeCun 转发了 LeRobotHF 的一条推文，该推文宣布将发布一个关于模型技术细节的后续帖子，但未提供实际内容。 这条转推表明了对模型透明度的关注，但由于缺乏实质性信息，其对社区的直接影响有限。 LeRobotHF 的原始推文提到许多人对其技术细节感兴趣，但转推本身不包含链接或进一步解释。

twitter · ylecun · Jun 9, 02:15

**标签**: `#machine learning`, `#twitter`, `#retweet`

---

<a id="item-30"></a>
## [花旗推广 SpaceX IPO 面向散户投资者](https://twitter.com/SpaceX/status/2063981965951332618) ⭐️ 2.0/10

花旗宣布其在 SpaceX IPO 中发挥积极作用，首次向丹麦、法国、德国等特定国家的合格散户投资者开放。 这标志着在让散户投资者更容易参与知名私营公司 IPO 方面迈出了重要一步，可能扩大零售投资者对航天产业的投资参与。 此次 IPO 仅限于特定国家的合格散户投资者，该推文为宣传性质，未提供有关发行或 SpaceX 财务状况的技术细节。

twitter · SpaceX · Jun 8, 13:50

**背景**: SpaceX 是由埃隆·马斯克创立的私人航天公司，其 IPO 备受期待。散户投资者通常难以参与此类高知名度 IPO，这些 IPO 往往只面向机构投资者。

**标签**: `#finance`, `#IPO`, `#SpaceX`

---

<a id="item-31"></a>
## [转推反对暂停 AI 开发，缺乏实质内容](https://twitter.com/ylecun/status/2064046554508349869) ⭐️ 2.0/10

Yann LeCun 转发了 Dan_Jeffries1 的一条推文，该推文将暂停 AI 开发的呼吁斥为‘彻头彻尾的胡说八道’，但未提供任何技术推理或证据。 这条转推反映了对 AI 安全问题的轻视态度，但由于参与度低且缺乏实质性论证，其对更广泛讨论的影响有限。 Dan_Jeffries1 的原帖使用了‘通过不制造飞机来让飞机更安全’的类比，但转推未对此或任何其他观点进行详细说明。该推文仅有 14 次转推，可见度较低。

twitter · ylecun · Jun 8, 18:07

**背景**: AI 暂停辩论指的是部分研究人员和公众人物呼吁暂时停止训练先进 AI 系统（如 GPT-4），以便制定安全措施。这条转推代表了认为此类暂停是错误的反对意见，但缺乏技术深度。

**标签**: `#AI safety`, `#opinion`, `#low-value`

---

<a id="item-32"></a>
## [关于 NIH 拨款政策变化的转发](https://twitter.com/ylecun/status/2063872270083162519) ⭐️ 2.0/10

Yann LeCun 转发了众议员 Auchincloss 的帖子，批评 Russell Vought 的提案，该提案主张用政治标准取代同行评审来决定 NIH 科学拨款。 这凸显了关于科学资助诚信的辩论，但该新闻与 AI/ML 或软件工程等技术领域相关性较低。 该提案将使 NIH 拨款决策政治化，可能破坏基于科学价值的评估。该转发本身未提供新的技术信息。

twitter · ylecun · Jun 8, 06:34

**背景**: NIH（美国国立卫生研究院）的拨款通常通过同行评审授予，由专家评估科学价值。Russell Vought 是一位政治人物，曾提议改变这一流程。

**标签**: `#politics`, `#NIH`, `#science policy`

---

<a id="item-33"></a>
## [转发大卫·萨尔诺夫传记](https://twitter.com/ylecun/status/2063661726818533629) ⭐️ 2.0/10

Yann LeCun 转发了一条关于大卫·萨尔诺夫传记的推文，强调了他从移民到 RCA 总裁的崛起。 这条推文缺乏技术或学术意义，对软件工程或 AI 讨论没有贡献。 大卫·萨尔诺夫（1891-1971）是一位俄罗斯犹太移民，后来成为 RCA 的总裁兼董事长。

twitter · ylecun · Jun 7, 16:37

**标签**: `#history`, `#biography`

---

<a id="item-34"></a>
## [Google TurboVec 声称将 AI 内存减少 92%](https://twitter.com/RodmanAi/status/2063507902963573079) ⭐️ 2.0/10

Google 推出了 TurboVec 工具，可将 AI 内存从 31GB 压缩至 4GB，对高维嵌入实现高达 92% 的内存缩减。 这一突破可能大幅降低运行大规模 AI 应用的硬件要求，使其在普通 Mac 等消费级设备上更易使用。 TurboVec 基于 Google 的 TurboQuant 技术，使用 Rust 编写并带有 Python 绑定，声称搜索速度超过 FAISS，且完全离线运行。

twitter · RodmanAi · Jun 7, 06:26

**背景**: 向量搜索是 AI 系统中从大型数据集检索相似项的关键组件。FAISS 等传统方法需要大量内存，限制了在低资源设备上的部署。TurboVec 使用量化技术将每个维度的向量压缩至 2-4 位，大幅减少内存占用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techstartups.com/2026/06/06/google-shrinks-ai-memory-from-31gb-to-4gb-with-turbovec-beating-faiss-on-speed/">Google shrinks AI memory from 31GB to 4GB with TurboVec, beating FAISS on speed - Tech Startups</a></li>
<li><a href="https://www.explainx.ai/blog/google-turbovec-turboquant-vector-search-rust-2026">Google TurboVec: Compress 10M Vectors from 31GB to | explainx.ai Blog | explainx.ai</a></li>
<li><a href="https://www.reddit.com/r/tech_x/comments/1tz3518/google_just_shrunk_31gb_of_ai_memory_down_to_4gb/">r/tech_x on Reddit: Google just shrunk 31GB of AI memory down to 4GB. The tool is called TurboVec. It uses up to 16x less memory, searches faster than FAISS, runs fully offline, and works on a regular Mac.</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论指出，尽管 TurboVec 的内存节省令人印象深刻，但 FAISS 因其成熟性和精确搜索能力仍是更安全的通用选择。一些用户对缺乏同行评审的基准测试表示怀疑。

**标签**: `#AI`, `#memory`, `#Google`

---

<a id="item-35"></a>
## [SpaceX 转发的采访缺乏技术深度](https://twitter.com/SpaceX/status/2064132519503798712) ⭐️ 1.0/10

SpaceX 转发了一段对任务控制中心 Bret Johnsen 的采访，但内容仅为个人轶事，缺乏技术或学术价值。 该新闻与软件工程、AI/ML 或系统研究的相关性较低，对更广泛的技术社区没有贡献。 该推文是对个人采访轶事的转发，没有技术细节或行业影响，相关性评分为 1.0/10。

twitter · SpaceX · Jun 8, 23:48

**标签**: `#spacex`, `#interview`, `#personal`

---