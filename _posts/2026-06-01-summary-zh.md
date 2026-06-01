---
layout: default
title: "Horizon Summary: 2026-06-01 (ZH)"
date: 2026-06-01
lang: zh
---

> From 26 items, 21 important content pieces were selected

---

1. [知识库将 754 项网络安全技能映射到主要框架](#item-1) ⭐️ 7.0/10
2. [微软开源 SkillOpt，革新 AI 代理学习方式](#item-2) ⭐️ 7.0/10
3. [80 克大鼠外骨骼用于神经康复研究](#item-3) ⭐️ 6.0/10
4. [Yann LeCun 转发世界模型定义](#item-4) ⭐️ 6.0/10
5. [免费工具可跨 400 多个平台查找用户名](#item-5) ⭐️ 6.0/10
6. [声称通过 Ollama 免费本地运行 OpenAI Codex](#item-6) ⭐️ 6.0/10
7. [10 个颠覆企业 AI 收入的 GitHub 仓库](#item-7) ⭐️ 5.0/10
8. [开源工具包为 Claude Code 增加 30 个智能体](#item-8) ⭐️ 5.0/10
9. [推特上分享伦敦机器人地图](#item-9) ⭐️ 4.0/10
10. [雷尼绍 REVO 三坐标测量机大幅提升检测速度](#item-10) ⭐️ 4.0/10
11. [SpaceX 从加州发射 24 颗星链卫星](#item-11) ⭐️ 4.0/10
12. [哈佛研究员研究 AI 加速主义者、安全主义者和怀疑论者](#item-12) ⭐️ 4.0/10
13. [比尔·格利：Anthropic 追求超级智能是狂妄](#item-13) ⭐️ 4.0/10
14. [可视化日历自动导入应用商店订阅](#item-14) ⭐️ 3.0/10
15. [神秘推文称七大科技股中有一个是冒牌货](#item-15) ⭐️ 2.0/10
16. [石油供应警告推文与技术无关](#item-16) ⭐️ 2.0/10
17. [联邦研究拨款或需政治批准](#item-17) ⭐️ 2.0/10
18. [Yann LeCun 转发对 ESMFold2 基准测试的困惑](#item-18) ⭐️ 2.0/10
19. [转发对比 2024 与 2026 年美国经济](#item-19) ⭐️ 2.0/10
20. [推文称赞 ICRA26 研讨会促进学习](#item-20) ⭐️ 2.0/10
21. [杨立昆在推文中批评 MAGA](#item-21) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [知识库将 754 项网络安全技能映射到主要框架](https://twitter.com/RodmanAi/status/2061031921891901596) ⭐️ 7.0/10

RodmanAI 发布了一个知识库，将 754 项网络安全技能映射到 MITRE ATT&CK、NIST CSF、D3FEND、ATLAS 和 AI RMF，使 AI 代理能够执行结构化的安全工作流程。 这个即插即用的知识库使 Claude、Copilot 等 AI 代理能够提供特定领域的安全响应，而非通用答案，有望加速威胁分析和事件响应。 该知识库兼容 Claude、Copilot、Cursor、Codex 和 Gemini 等多种 AI 代理，并通过公共仓库提供。

twitter · RodmanAi · May 31, 10:27

**背景**: MITRE ATT&CK 是一个全球可访问的对手战术和技术知识库，NIST CSF 提供了改善网络安全态势的框架。D3FEND 是防御性网络安全技术的知识图谱，ATLAS 专注于 AI 特定威胁，AI RMF 是管理 AI 风险的框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://attack.mitre.org/">MITRE ATT & CK</a></li>
<li><a href="https://www.paloaltonetworks.com/cyberpedia/what-is-mitre-attack">What Is MITRE ATT & CK Framework ? - Palo Alto Networks</a></li>
<li><a href="https://en.wikipedia.org/wiki/NIST_Cybersecurity_Framework">NIST Cybersecurity Framework</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI`, `#MITRE ATT&CK`, `#knowledge base`, `#frameworks`

---

<a id="item-2"></a>
## [微软开源 SkillOpt，革新 AI 代理学习方式](https://twitter.com/RodmanAi/status/2060603132124750283) ⭐️ 7.0/10

微软开源了 SkillOpt 系统，该系统通过训练一个 markdown 文件来改进 AI 代理，而无需重新训练底层模型。优化器利用轨迹驱动的编辑和验证门控更新来编辑自然语言技能文档。 这种方法大幅降低了改进 AI 代理的成本和复杂性，因为它避免了重新训练拥有数十亿参数的大模型。它使得代理技能的迭代更快、部署更容易，可能加速 AI 代理在生产中的应用。 SkillOpt 将紧凑的 markdown 文件视为冻结语言代理的可训练状态，使用单独的优化器模型进行有界编辑。仅当编辑严格提高了保留验证分数时才被接受，从而确保技能改进的可靠性。

twitter · RodmanAi · May 30, 06:04

**背景**: 传统的 AI 代理改进需要微调底层大语言模型，计算成本高且风险大。SkillOpt 则优化代理在推理时读取的自然语言技能文档，使过程轻量且可解释。这是使用 markdown 文件定义和协调 AI 代理行为的增长趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/SkillOpt">GitHub - microsoft/SkillOpt: SkillOpt is a text-space optimizer that ...</a></li>
<li><a href="https://microsoft.github.io/SkillOpt/">SkillOpt | Executive Strategy for Self-Evolving Agent Skills</a></li>
<li><a href="https://arxiv.org/abs/2605.23904">SkillOpt: Executive Strategy for Self-Evolving Agent Skills</a></li>

</ul>
</details>

**标签**: `#AI`, `#Microsoft`, `#open-source`, `#machine learning`, `#agents`

---

<a id="item-3"></a>
## [80 克大鼠外骨骼用于神经康复研究](https://twitter.com/lukas_m_ziegler/status/2061127999945073030) ⭐️ 6.0/10

筑波大学和名古屋大学的研究人员开发了首个支持大鼠整个后肢的啮齿动物外骨骼，重量仅 80 克（约大鼠体重的 1/4），并使用 Bowden 线缆进行驱动。 这种轻量级外骨骼为在啮齿动物模型中研究神经康复提供了新的可能性，可能加速人类脊髓损伤和中风恢复疗法的开发。 该外骨骼使用 Bowden 线缆，这是一种通过内线在外壳内滑动来传递力的柔性线缆，可在不增加肢体重量的情况下实现远程驱动。该设备仅重 80 克，最大限度地减少了对自然运动的干扰。

twitter · lukas_m_ziegler · May 31, 16:49

**背景**: 啮齿动物模型广泛用于神经科学研究，以研究运动控制和神经损伤后的康复。人类外骨骼很常见，但由于重量和尺寸限制，将其缩小到啮齿动物身上具有挑战性。Bowden 线缆因其灵活性和低摩擦而常用于自行车刹车和假肢装置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bowden_cable">Bowden cable</a></li>
<li><a href="https://www.academia.edu/82024543/Rehabilitative_Soft_Exoskeleton_for_Rodents">(PDF) Rehabilitative Soft Exoskeleton for Rodents</a></li>

</ul>
</details>

**标签**: `#robotics`, `#neurorehabilitation`, `#exoskeleton`, `#biomedical engineering`

---

<a id="item-4"></a>
## [Yann LeCun 转发世界模型定义](https://twitter.com/ylecun/status/2061179160626610371) ⭐️ 6.0/10

Yann LeCun 转发了 CSProfKGD 的一条推文，该推文定义了什么是世界模型，并附有一个链接。这条推文本身没有提供额外评论。 作为著名 AI 研究者，LeCun 的认可凸显了世界模型在 AI 研究中日益增长的重要性。这一概念对于开发能够理解和预测物理世界的 AI 系统至关重要。 这条转发包含一个资源链接，但推文中未指定该资源的内容。该定义可能符合 LeCun 本人关于世界模型作为环境内部表征的观点。

twitter · ylecun · May 31, 20:13

**背景**: 世界模型是学习环境内部表征的 AI 系统，使其能够模拟和预测结果。它们是实现人类级 AI 的关键，因为允许智能体对世界进行推理。Yann LeCun 一直是世界模型作为通往更智能 AI 路径的积极倡导者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence">Artificial intelligence - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2024/12/14/what-are-ai-world-models-and-why-do-they-matter/">What are AI ' world models ,' and why do they matter? | TechCrunch</a></li>
<li><a href="https://pub.towardsai.net/what-are-world-models-41ff394ed871">What Are World Models ?. World models : the physical... | Towards AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#world model`, `#Yann LeCun`

---

<a id="item-5"></a>
## [免费工具可跨 400 多个平台查找用户名](https://twitter.com/RodmanAi/status/2061295805487788433) ⭐️ 6.0/10

一款免费工具（很可能是 Sherlock）可在数秒内搜索超过 400 个社交网络和网站中的用户名，自动发现匹配的个人资料。 该工具简化了开源情报调查和网络安全研究，使得跨多个平台追踪数字足迹和识别与同一用户名关联的账户变得更加容易。 该工具基于命令行且开源，可扫描 Twitter、GitHub、Reddit 等平台；特别适用于渗透测试人员和数字取证专家。

twitter · RodmanAi · Jun 1, 03:56

**背景**: 开源情报（OSINT）是指收集和分析公开信息以用于调查目的。Sherlock 是一款知名的 OSINT 工具，可自动在数百个网站上搜索用户名，帮助研究人员构建数字档案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sherlockosint.com/">SherlockOSINT - Username Search Tool | Social Media OSINT</a></li>
<li><a href="https://osintpro.net/tools/username-analyzer">Username Analyzer - Search 350+ Social Media Platforms | Sherlock ...</a></li>
<li><a href="https://www.x-cmd.com/install/sherlock/">Username Taken Somewhere? Sherlock Check 400+ Platforms at Once</a></li>

</ul>
</details>

**标签**: `#OSINT`, `#cybersecurity`, `#tool`, `#social media`

---

<a id="item-6"></a>
## [声称通过 Ollama 免费本地运行 OpenAI Codex](https://twitter.com/RodmanAi/status/2060711654908912065) ⭐️ 6.0/10

一条推文声称，现在可以使用 Ollama 和 DeepSeek V4、Gemma 4、Qwen 3.6 等开源模型免费本地运行 OpenAI 的 Codex，无需 API 费用和速率限制。 如果属实，这将使 AI 编程助手的访问民主化，允许开发者离线且私密地使用强大模型。然而，该说法可能具有误导性，因为 Codex 本身并非开源。 该推文指的是使用 Ollama 运行开源模型作为 Codex 的替代品，而非实际运行 Codex 本身。Ollama 是一个管理本地 LLM 的平台，而 Codex CLI 需要订阅。

twitter · RodmanAi · May 30, 13:15

**背景**: Ollama 是一个允许用户在本地硬件上运行大型语言模型的工具。OpenAI 的 Codex 是一个专有的 AI 编程助手，通常需要 API 访问或订阅。该推文将使用 Ollama 运行开源模型与运行 Codex 混为一谈，这是不准确的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ollama">Ollama - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Codex_CLI">Codex CLI</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260424">DeepSeek V4 Preview Release | DeepSeek API Docs</a></li>

</ul>
</details>

**标签**: `#AI`, `#OpenAI`, `#Codex`, `#Ollama`, `#local`

---

<a id="item-7"></a>
## [10 个颠覆企业 AI 收入的 GitHub 仓库](https://twitter.com/RodmanAi/status/2061168617287463189) ⭐️ 5.0/10

Twitter 用户@RodmanAi 发布了一个帖子，列出了 10 个据称威胁 500 亿美元企业收入的 GitHub 仓库，其中 Ollama 因能在笔记本电脑上本地运行 GPT-4 级别 AI 且无需 API 费用而受到关注。 这份列表凸显了本地 AI 的兴起趋势，它减少了对昂贵云 API 的依赖，赋予开发者离线、私密的 AI 能力，可能颠覆主要 AI 提供商商业模式。 Ollama 允许用户通过简单命令本地运行 Llama 3.1 等大型语言模型，消除了每月高达 500 美元的 OpenAI 服务订阅费用。

twitter · RodmanAi · May 31, 19:31

**背景**: 本地 AI 是指在用户自己的硬件上运行 AI 模型，而非在云端，从而确保数据隐私且无需持续 API 费用。Ollama 等工具简化了这一过程，使没有深厚基础设施知识的开发者也能轻松使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Ollama">Ollama</a></li>
<li><a href="https://ollama.com/">Ollama is the easiest way to automate your work using open models...</a></li>
<li><a href="https://atomicmail.io/blog/how-to-run-ai-locally-without-sending-your-data-to-the-cloud">How to Run AI Locally in 2026: Private, Offline, Free</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#AI`, `#open source`, `#Ollama`

---

<a id="item-8"></a>
## [开源工具包为 Claude Code 增加 30 个智能体](https://twitter.com/RodmanAi/status/2060974525970518505) ⭐️ 5.0/10

一个新的开源工具包为 Claude Code 扩展了 30 个智能体、64 项技能、33 条命令和 1,282 项安全测试，支持自动化代码审查、测试驱动开发（TDD）、自动修复和令牌优化。 该工具包将 Claude Code 从单智能体编码助手转变为完整的 AI 工程团队，有望显著提升开发者的生产力和代码质量。 该工具包包含 30 个专门智能体，用于规划、代码审查、TDD、自动修复和令牌优化，以及 64 项技能和 33 条命令。它还提供了 1,282 项安全测试以确保代码安全。

twitter · RodmanAi · May 31, 06:39

**背景**: Claude Code 是 Anthropic 的智能编码工具，运行在终端中，使用 Claude 3.7 Sonnet 来理解代码库、编辑文件和运行命令。TDD（测试驱动开发）是一种先写测试再写代码的软件开发实践，有助于防止使用 AI 智能体时出现回归问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.anthropic.com/claude-code">Claude Code : Deep Coding at Terminal Velocity \ Anthropic</a></li>
<li><a href="https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent">TDD, AI agents and coding with Kent Beck</a></li>

</ul>
</details>

**标签**: `#AI coding tools`, `#open-source`, `#Claude Code`, `#developer productivity`

---

<a id="item-9"></a>
## [推特上分享伦敦机器人地图](https://twitter.com/lukas_m_ziegler/status/2061073451528454368) ⭐️ 4.0/10

Lukas Ziegler 在推特上发布了一张地图，重点标注了伦敦的机器人公司和大学，包括帝国理工学院和伦敦大学学院。 这张地图提供了伦敦机器人生态系统的直观概览，可能有助于研究人员、投资者和学生识别关键参与者和合作机会。 推文包含地图链接，但未明确列出公司或机构的具体数量。该地图聚焦于伦敦，这是英国主要的机器人技术中心。

twitter · lukas_m_ziegler · May 31, 13:12

**背景**: 机器人地图通常用于追踪行业集群和学术优势。伦敦拥有帝国理工学院和伦敦大学学院的领先机器人研究团队，以及众多初创公司。

**标签**: `#robotics`, `#London`, `#map`

---

<a id="item-10"></a>
## [雷尼绍 REVO 三坐标测量机大幅提升检测速度](https://twitter.com/lukas_m_ziegler/status/2060793388048519278) ⭐️ 4.0/10

用户@lukas_m_ziegler 在推文中强调雷尼绍 REVO 三坐标测量机（CMM）系统检测零件速度极快，并指出其采用五轴测头而非移动整机。 该系统可在保持精度的同时将检测周期缩短一半以上，有望通过提高吞吐量来变革制造业的质量控制流程。 REVO 系统采用 Renscan5 测量技术，在超高速下最小化 CMM 运动的动态影响，从而比传统 CMM 更快地检测零件。

twitter · lukas_m_ziegler · May 30, 18:40

**背景**: 三坐标测量机（CMM）通过探测表面点来精确测量物理物体的表面几何形状。传统 CMM 需要移动整机到每个测量点，限制了速度。雷尼绍 REVO 系统采用独立运动的五轴测头，大幅缩短了检测周期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=FUgWBlEewyk">Renishaw Revo CMM Demonstration - YouTube</a></li>
<li><a href="https://www.cmmxyz.com/new-cmms/probing-and-accessories/5-axis-systems/renishaw-revo/">Renishaw REVO 5-Axis Measurement System | CMMXYZ</a></li>
<li><a href="https://www.thome-precision.com/Renishaw-Revo.html">THOME Präzision GmbH | Renishaw REVO</a></li>

</ul>
</details>

**标签**: `#manufacturing`, `#metrology`, `#CMM`

---

<a id="item-11"></a>
## [SpaceX 从加州发射 24 颗星链卫星](https://twitter.com/SpaceX/status/2060741839544594436) ⭐️ 4.0/10

SpaceX 在加州使用猎鹰 9 号火箭发射了 24 颗星链卫星，发射后不久即确认部署成功。 此次发射扩大了星链卫星群，提升了全球宽带覆盖和容量，对 SpaceX 实现全球低延迟互联网的目标至关重要。 猎鹰 9 号第一级可能降落在无人船上，但推文中未确认。星链卫星采用批量生产和大规模部署以降低成本。

twitter · SpaceX · May 30, 15:15

**背景**: 星链是 SpaceX 运营的卫星互联网星座，为服务不足地区提供宽带服务。猎鹰 9 号是一种可重复使用的两级火箭，已成为 SpaceX 发射的主力。

**标签**: `#SpaceX`, `#Starlink`, `#satellite`, `#launch`

---

<a id="item-12"></a>
## [哈佛研究员研究 AI 加速主义者、安全主义者和怀疑论者](https://twitter.com/ylecun/status/2061280839489515882) ⭐️ 4.0/10

哈佛研究员 James Snover 正在研究 AI 加速主义者、安全主义者和怀疑论者的观点，这一信息通过 Yann LeCun 的转发分享出来。 这项研究凸显了 AI 讨论中日益加剧的分歧——一方追求快速进步，一方优先考虑安全，还有一方持怀疑态度——这种分歧影响着政策制定和公众辩论。 该推文本身缺乏技术深度或新颖见解，仅有 75 次转发，表明参与度较低。该研究是 Snover 在哈佛大学奖学金项目的一部分。

twitter · ylecun · Jun 1, 02:57

**背景**: AI 加速主义主张快速推进 AI 发展，常拥抱技术奇点；而 AI 安全主义则侧重于降低高级 AI 带来的风险。怀疑论者则质疑此类 AI 的可行性或可取性。这些观点代表了 AI 社区中的关键意识形态阵营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Accelerationism">Accelerationism</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_Safety_Summit_2023">AI Safety Summit 2023</a></li>

</ul>
</details>

**标签**: `#AI`, `#AI safety`, `#AI accelerationism`

---

<a id="item-13"></a>
## [比尔·格利：Anthropic 追求超级智能是狂妄](https://twitter.com/ylecun/status/2061278918561206302) ⭐️ 4.0/10

著名风险投资人比尔·格利在 All-In 播客中批评 Anthropic，称其构建超级智能 AI 的野心体现了自恋和妄自尊大。 这一观点凸显了人们对 AI 公司宏大宣言日益增长的怀疑，可能影响公众看法和投资者对 Anthropic 及类似公司的态度。 格利的评论出自 All-In 播客，并由 Yann LeCun 转发，但该推文互动量低（258 次转发），且缺乏技术深度。

twitter · ylecun · Jun 1, 02:49

**背景**: Anthropic 是一家成立于 2021 年的 AI 安全公司，以开发 Claude 系列大语言模型而闻名。超级智能是指一种假设的超越人类智能的 AI，一些 AI 实验室追求这一目标，但另一些人批评其不切实际或危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Superintelligence">Superintelligence - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#opinion`

---

<a id="item-14"></a>
## [可视化日历自动导入应用商店订阅](https://twitter.com/RodmanAi/status/2061102058355441903) ⭐️ 3.0/10

一位开发者构建了一个可视化日历，可自动从应用商店导入所有订阅，无需手动输入。 该工具简化了被多个定期付款困扰的用户的订阅跟踪，可能减少遗漏扣费并提高财务意识。 该日历直接从应用商店拉取订阅数据，以可视化格式显示金额和到期日，无需手动输入。

twitter · RodmanAi · May 31, 15:06

**背景**: 许多用户通过应用商店订阅多项服务，但跟踪续费日期和费用可能很繁琐。现有解决方案通常需要手动记录或缺乏可视化概览。

**标签**: `#subscription management`, `#visual calendar`, `#app store`

---

<a id="item-15"></a>
## [神秘推文称七大科技股中有一个是冒牌货](https://twitter.com/ylecun/status/2061310030129799210) ⭐️ 2.0/10

Yann LeCun 转发了 @antibearthesis 的一条推文，该推文神秘地声称七大科技股中有一个是冒牌货，并附上了一个未指明的链接。 该推文缺乏实质性技术内容，未提供任何可操作信息，因此对技术受众毫无意义。 该推文仅为转发，LeCun 未添加任何评论，且所附链接无法访问或未说明内容。

twitter · ylecun · Jun 1, 04:53

**标签**: `#twitter`, `#vague`, `#low-value`

---

<a id="item-16"></a>
## [石油供应警告推文与技术无关](https://twitter.com/ylecun/status/2060784862483632292) ⭐️ 2.0/10

Yann LeCun 转发了一条来自 Exxon 的警告推文，称我们距离汽油末日还有两周。 这条新闻与技术受众无关，与软件工程、AI 或系统研究毫无关联。 该推文是对 Microinteracti1 引用 Exxon 声明的转发，缺乏技术深度或背景。

twitter · ylecun · May 30, 18:06

**标签**: `#off-topic`, `#current-events`

---

<a id="item-17"></a>
## [联邦研究拨款或需政治批准](https://twitter.com/ylecun/status/2060764165778915335) ⭐️ 2.0/10

Yann LeCun 转发了一条消息，指出美国联邦研究拨款可能很快需要政治任命官员的批准。 这一变化可能将政治监督引入科研经费决策，可能影响研究的独立性和方向。 该推文未说明是哪个机构或政府提出这一变化，也未明确受影响拨款的具体范围。

twitter · ylecun · May 30, 16:43

**背景**: 美国联邦研究拨款通常由 NSF 和 NIH 等机构通过同行评审流程分配。引入政治批准可能意味着对基于绩效的资助传统的重大偏离。

**标签**: `#policy`, `#research funding`, `#science`

---

<a id="item-18"></a>
## [Yann LeCun 转发对 ESMFold2 基准测试的困惑](https://twitter.com/ylecun/status/2060622786196918445) ⭐️ 2.0/10

Yann LeCun 转发了 Sylvain Gariel 的评论，该评论表达了对 ESMFold2（一种新的蛋白质结构预测模型）基准测试数据的初步困惑。 这凸显了蛋白质折叠 AI 中清晰基准测试的重要性，即使是专家也可能最初被数据呈现所误导。 ESMFold2 是一种用于蛋白质结构预测和设计的最先进模型，在抗体相互作用方面尤其强大。

twitter · ylecun · May 30, 07:22

**背景**: 像 AlphaFold2 和 ESMFold 这样的蛋白质折叠模型使用 AI 从氨基酸序列预测 3D 蛋白质结构。基准测试评估其准确性，但如果指标或数据集没有清晰传达，结果可能会令人困惑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.latent.space/p/esmfold2">🔬 ESMFold2: The Bitter Lesson is Coming for Proteins - Alex Rives, BioHub</a></li>
<li><a href="https://www.tamarind.bio/tools/esmfold2">ESMFold2 Online | Next Generation Structure Prediction</a></li>

</ul>
</details>

**标签**: `#bioinformatics`, `#protein folding`, `#ESMFold2`

---

<a id="item-19"></a>
## [转发对比 2024 与 2026 年美国经济](https://twitter.com/ylecun/status/2060615788956991976) ⭐️ 2.0/10

Yann LeCun 转发了一条对比 2024 年和 2026 年美国关键经济指标的推文，显示 GDP 增长率从 2.8%降至 1.6%，通胀率从 2.9%升至 3.8%，而 2024 年工资增长更快。 这一对比凸显了潜在的经济下行趋势，可能影响科技行业的招聘、投资和消费支出，但该推文缺乏背景和方法论说明。 这些数据点没有提供来源或定义，不清楚是实际数据还是预测值。该推文是转发自 JaredRyanSears，并非原创分析。

twitter · ylecun · May 30, 06:54

**背景**: GDP 增长率、通胀率和工资增长等经济指标常用于评估经济健康状况。比较两个年份可以揭示趋势，但缺乏更广泛背景的单一快照可能具有误导性。

**标签**: `#economics`, `#twitter`, `#data`

---

<a id="item-20"></a>
## [推文称赞 ICRA26 研讨会促进学习](https://twitter.com/StanfordAILab/status/2061319988808696043) ⭐️ 2.0/10

来自@leto__jean 的一条推文（被斯坦福 AI 实验室转发）称赞 ICRA26 会议的研讨会是了解他人工作的最佳途径。 在 ICRA26 等大型会议上，研讨会对于知识交流和建立联系至关重要，尤其是在机器人和人工智能等快速发展的领域。 该推文内容模糊且不完整，以“我将谈论……”结尾，互动量极低，仅有一个转发。

twitter · StanfordAILab · Jun 1, 05:32

**背景**: ICRA（IEEE 国际机器人与自动化会议）是机器人领域最重要的年度会议。ICRA26 将于 2026 年在奥地利维也纳举行，研讨会定于 2026 年 6 月 1 日和 6 月 5 日举办。研讨会为学习最新研究和建立联系提供了专注的环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://2026.ieee-icra.org/">2026 IEEE International Conference on Robotics and Automation (ICRA)</a></li>
<li><a href="https://2026.ieee-icra.org/workshops-and-tutorials/">Workshops & Tutorials - IEEE ICRA 2026</a></li>

</ul>
</details>

**标签**: `#conference`, `#workshops`, `#robotics`

---

<a id="item-21"></a>
## [杨立昆在推文中批评 MAGA](https://twitter.com/ylecun/status/2060718725884699003) ⭐️ 1.0/10

杨立昆发推文批评 MAGA 的现实感和道德观，并提及他在疫苗方面的工作。 这条推文值得注意，因为杨立昆是著名 AI 科学家，但内容涉及政治，与其技术专长无关。 该推文是对他自己先前推文的转发，参与度低且无实质性讨论。

twitter · ylecun · May 30, 13:43

**标签**: `#politics`, `#twitter`, `#low-value`

---