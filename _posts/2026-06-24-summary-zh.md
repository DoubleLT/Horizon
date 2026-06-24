---
layout: default
title: "Horizon Summary: 2026-06-24 (ZH)"
date: 2026-06-24
lang: zh
---

> From 34 items, 28 important content pieces were selected

---

1. [逆贝尔曼方程恢复世界模型](#item-1) ⭐️ 8.0/10
2. [NVIDIA Halos：面向机器人的全栈安全系统](#item-2) ⭐️ 8.0/10
3. [SpaceX 演示 Starfall 飞行器，实现微重力访问](#item-3) ⭐️ 8.0/10
4. [Karpathy 推崇 Claude 的新内联范式](#item-4) ⭐️ 8.0/10
5. [斯坦福 AI 实验室提出 Spiral 方法实现测试时计算扩展](#item-5) ⭐️ 8.0/10
6. [GEN-1 机器人展示自适应折箱与螺丝包装](#item-6) ⭐️ 7.0/10
7. [LeCun 转发对 AI 基础设施经济的批评](#item-7) ⭐️ 7.0/10
8. [LLM 评判与人类评估的悖论](#item-8) ⭐️ 7.0/10
9. [M*：多模态模型的通用服务系统](#item-9) ⭐️ 7.0/10
10. [扩散模型避免维度灾难](#item-10) ⭐️ 7.0/10
11. [开发者用 Claude 构建 PS1 游戏开发工具](#item-11) ⭐️ 7.0/10
12. [Lean 的库缺失阻碍研究级数学证明](#item-12) ⭐️ 6.0/10
13. [LLM 的 Map-Reduce：新训练方法](#item-13) ⭐️ 6.0/10
14. [离线自主探索助力机器人技能开发](#item-14) ⭐️ 6.0/10
15. [AI 演示工具：演示品而非产品](#item-15) ⭐️ 6.0/10
16. [用语音将旧电脑改造成家庭 AI 服务器](#item-16) ⭐️ 5.0/10
17. [ZenRobotics 用 AI 机器人将垃圾变成商机](#item-17) ⭐️ 5.0/10
18. [GLP-1 与 CRISPR：来自毒液和酸奶的突破](#item-18) ⭐️ 5.0/10
19. [教程：用 Claude Code 替代 Kimi Code](#item-19) ⭐️ 4.0/10
20. [Schmalz 推出 FDA 认证食品自动化夹爪](#item-20) ⭐️ 4.0/10
21. [SpaceX 用猎鹰 9 号发射星落演示任务](#item-21) ⭐️ 4.0/10
22. [杨立昆转发警告：不要对 AI 恐慌](#item-22) ⭐️ 4.0/10
23. [Claude 社区大使计划扩展至日本](#item-23) ⭐️ 4.0/10
24. [AI 接管小型团队的会议跟进工作](#item-24) ⭐️ 4.0/10
25. [Google DeepMind 祝贺 Project Genie 获得戛纳狮子大奖](#item-25) ⭐️ 3.0/10
26. [IntrinsicAI 在 Automate 展会上展示工业机器人 2.0](#item-26) ⭐️ 3.0/10
27. [AI 短期内不太可能治愈癌症](#item-27) ⭐️ 3.0/10
28. [推文称美国国际开发署削减导致 60 万人死亡](#item-28) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [逆贝尔曼方程恢复世界模型](https://twitter.com/GoogleDeepMind/status/2069433539116912739) ⭐️ 8.0/10

研究人员发现了一种逆贝尔曼方程的方法，可以从智能体的价值函数中恢复其世界模型。该工作引入了 P 学习，作为 Q 学习的逆模拟，通过更新候选世界模型使其与固定价值函数一致。 这一理论突破可能为强化学习带来新方法，使智能体能够直接从价值函数推断环境动态，从而提升模型可解释性和样本效率。它弥合了基于价值的强化学习与基于模型的强化学习之间的鸿沟。 该方法称为 P 学习，通过迭代更新世界模型以匹配观测到的价值函数，从而有效地逆贝尔曼方程。它与 Q 学习类似，但作用于世界模型而非价值函数。

twitter · GoogleDeepMind · Jun 23, 14:52

**背景**: 贝尔曼方程是强化学习中的基本概念，它将状态的价值与期望的未来奖励联系起来。世界模型是智能体用于模拟环境结果的内部表示。传统上，价值函数是从世界模型推导出来的；而这项工作逆转了这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://inverting-bellman.github.io/">Inverting the Bellman Equation: From Q-Values to World Models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bellman_equation">Bellman equation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#Bellman equation`, `#world model`, `#AI research`

---

<a id="item-2"></a>
## [NVIDIA Halos：面向机器人的全栈安全系统](https://twitter.com/lukas_m_ziegler/status/2069084905984712750) ⭐️ 8.0/10

NVIDIA 发布了 Halos for Robotics，这是业界首个面向物理 AI 的全栈安全系统，基于超过 18,600 工程年的自动驾驶安全开发经验构建。 这标志着在现实环境中安全部署人形机器人及其他物理 AI 系统迈出了重要一步，利用了来自自动驾驶领域经过验证的安全方法论。 Halos 将 NVIDIA 的硬件和软件安全解决方案与自动驾驶安全领域的前沿 AI 研究相结合，为机器人提供了全面的安全框架。

twitter · lukas_m_ziegler · Jun 22, 15:47

**背景**: 物理 AI 指能够感知、推理并在物理世界中行动的 AI 系统，例如自动驾驶汽车和机器人。确保这些系统在人类周围运行时的安全性至关重要。NVIDIA 在自动驾驶安全方面的经验为将安全标准扩展到机器人领域奠定了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/halos-safety-system-autonomous-vehicles/">NVIDIA Launches NVIDIA Halos , a Full-Stack, Comprehensive Safety ...</a></li>
<li><a href="https://www.linkedin.com/pulse/ep-42-nvidia-launches-halos-robotics-industrys-first-unified-ziegler-jednf">Ep. 42 nvidia launches halos for robotics, industry's first unified safety ....</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Robotics`, `#Physical AI`, `#Safety`, `#Autonomous Vehicles`

---

<a id="item-3"></a>
## [SpaceX 演示 Starfall 飞行器，实现微重力访问](https://twitter.com/SpaceX/status/2069370979084603672) ⭐️ 8.0/10

SpaceX 在一次任务中演示了名为 Starfall 的新型再入飞行器，旨在为科学研究和太空制造提供经济实惠且常规化的微重力环境访问。 这一进展可能降低研究人员和公司在微重力环境下进行实验和制造产品的门槛，从而加速材料科学、制药等领域的发展。 在展示受控飞行后，Starfall 航天器将溅落在太平洋。SpaceX 秘密开发了 Starfall，并透露了关于该飞行器的少量细节。

twitter · SpaceX · Jun 23, 10:44

**背景**: 微重力环境（如低地球轨道）允许发生独特的现象，例如蛋白质晶体生长和光纤生产，这些在地球上难以或无法实现。太空制造旨在为地球市场生产先进材料和产品。SpaceX 的新飞行器可为这类活动提供专用平台，补充国际空间站等现有设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digg.com/tech/u8aemxf1">SpaceX completes a controlled flight demonstration of a new...</a></li>
<li><a href="https://www.satellitetoday.com/launch/2026/06/23/spacex-launches-new-microgravity-lab-demo-starfall/">SpaceX Launches New Microgravity Lab Demo, Starfall - Via Satellite</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/what-is-starfall-a-look-at-spacexs-mysterious-new-return-capsule">What is Starfall? A look at SpaceX 's mysterious new return... | Space</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#microgravity`, `#space manufacturing`, `#space technology`

---

<a id="item-4"></a>
## [Karpathy 推崇 Claude 的新内联范式](https://twitter.com/karpathy/status/2069547676849557725) ⭐️ 8.0/10

Andrej Karpathy 强调了一种与 Claude 交互的新范式，该范式深度融入组织工作流，需要大量工程工作才能跨工具、集成、计算环境和内存实现无缝体验。 这标志着从简单聊天界面到深度嵌入的 AI 助手的转变，可能改变软件工程团队在整个开发生命周期中与 AI 协作的方式。 该范式需要大量的底层工程工作，以确保 AI 与人类活动内联工作，包括与现有工具、计算环境和内存系统的集成。

twitter · karpathy · Jun 23, 22:26

**背景**: Claude 是 Anthropic 的 AI 助手，近期发展聚焦于使其更深度融入开发环境。内联范式与 Claude Code 等自主代理系统形成对比，在用户现有工作流中提供实时、上下文感知的辅助。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://liora.io/en/claude-ai-interactive-visualization-shift">Anthropic's Claude AI triggers interactive inline visualization shift</a></li>
<li><a href="https://dev.to/shehzan/claude-code-vs-codex-agentic-vs-inline-ai-coding-57ah">Claude Code vs Codex: Agentic vs Inline AI Coding - DEV Community</a></li>

</ul>
</details>

**社区讨论**: 未提供社区讨论内容，但高互动量（1 万+点赞、790 次转发、518 条回复）表明社区对 Karpathy 观点有强烈兴趣和认可。

**标签**: `#AI`, `#Claude`, `#human-AI interaction`, `#paradigm shift`, `#engineering`

---

<a id="item-5"></a>
## [斯坦福 AI 实验室提出 Spiral 方法实现测试时计算扩展](https://twitter.com/StanfordAILab/status/2069562238890074213) ⭐️ 8.0/10

斯坦福 AI 实验室提出了 Spiral，一种新颖的集合强化学习方法，训练 LLM 生成利用测试时计算扩展的响应，包括更长的推理链、并行样本和聚合。 这解决了 LLM 通常只被训练使用单一测试时计算形式的局限性，Spiral 使模型能够以多种方式动态扩展计算，有望提升复杂任务的性能。 Spiral 使用集合强化学习，将响应集合作为状态表示，使模型能够学习在不同脚手架模式间分配测试时计算的最优策略。

twitter · StanfordAILab · Jun 23, 23:24

**背景**: 测试时计算扩展是指在推理时分配更多计算资源以改善 LLM 输出，通常通过更长的推理链或采样多个响应等方法实现。脚手架是用程序逻辑包装 LLM，以编排多次调用来完成复杂任务。集合强化学习是强化学习的一种变体，对元素集合进行操作，能够实现安全约束和鲁棒策略提取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/set-reinforcement-learning-set-rl">Set Reinforcement Learning Overview</a></li>
<li><a href="https://grokipedia.com/page/Test-time_compute_scaling">Test-time compute scaling</a></li>
<li><a href="https://www.lesswrong.com/posts/43C3igfmMrE9Qoyfe/scaffolded-llms-as-natural-language-computers">Scaffolded LLMs as natural language computers</a></li>

</ul>
</details>

**标签**: `#LLM`, `#reinforcement learning`, `#test-time compute`, `#AI research`, `#scaffolding`

---

<a id="item-6"></a>
## [GEN-1 机器人展示自适应折箱与螺丝包装](https://twitter.com/lukas_m_ziegler/status/2069597554975641939) ⭐️ 7.0/10

GeneralistAI 在 AutomateShow 上展示了其 GEN-1 机器人执行自适应折箱和螺丝包装任务，能够处理纸板箱的折痕、变形等真实世界变化。 此次演示凸显了向能适应不可预测条件的通用机器人迈进的进展，这是自动化当前需要人类灵活性的物流和制造任务的关键一步。 机器人在出错时会重试，并适应不同的箱子配置，展示了在真实世界变化下的稳健操作能力。

twitter · lukas_m_ziegler · Jun 24, 01:44

**背景**: 机器人自适应操作是指机器人根据传感器反馈实时调整动作，处理物体和环境变化的能力。GeneralistAI 是一家专注于构建通用机器人的公司，旨在通过创建能够即兴处理多样化任务的系统，实现机器人领域的“ChatGPT 时刻”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://boldstart.vc/news/generalistai-when-robots-start-to-improvise-welcome-to-boldstart/">GeneralistAI — When Robots Start to Improvise — Welcome to boldstart - boldstart ventures</a></li>
<li><a href="https://x.com/generalistai_">Generalist (@GeneralistAI_) / X</a></li>

</ul>
</details>

**标签**: `#robotics`, `#adaptive manipulation`, `#AI`, `#automation`

---

<a id="item-7"></a>
## [LeCun 转发对 AI 基础设施经济的批评](https://twitter.com/ylecun/status/2069041396279845349) ⭐️ 7.0/10

Yann LeCun 转发了 David Linthicum 的批评文章，该文章认为大规模 AI 基础设施投资背后的经济假设存在根本性缺陷，并将此比作“皇帝的新衣”。 来自著名 AI 人物的转发放大了这一批判性观点，挑战了关于 AI 基础设施无限投资的普遍说法，可能影响行业讨论和投资决策。 该批评特别提到了 IBM CEO Arvind Krishna，暗示即使是主要科技领袖也可能夸大了当前 AI 基础设施建设的经济可行性。

twitter · ylecun · Jun 22, 12:54

**背景**: AI 行业在数据中心和计算基础设施上投入巨资，其驱动力是认为扩大模型规模会带来相应的经济回报。像 Linthicum 这样的批评者认为，成本可能超过收益，尤其是在效率改进和替代方法出现的情况下。

**标签**: `#AI infrastructure`, `#economics`, `#critique`, `#industry analysis`

---

<a id="item-8"></a>
## [LLM 评判与人类评估的悖论](https://twitter.com/StanfordAILab/status/2069541541111312658) ⭐️ 7.0/10

Alyssa Unell 的一条推文指出了 LLM 评估中的循环依赖：使用 LLM 评判来扩展昂贵的人工评估，但要信任 LLM 评判本身又需要人工评估。 这一悖论对 AI 社区至关重要，因为它挑战了自动化评估方法的可扩展性和可靠性，而自动化评估对于大规模开发和部署 LLM 至关重要。 推文提到了一项新工作（以'Our ne...'开头），可能提出了解决或进一步分析这一循环依赖的方案。悖论在于，LLM 评判被用来减少对昂贵人工评估的依赖，但验证 LLM 评判本身仍然需要人工评估。

twitter · StanfordAILab · Jun 23, 22:02

**背景**: LLM-as-a-Judge 是一种框架，利用大型语言模型评估其他语言系统的输出，旨在实现评估的自动化和规模化。然而，这些 LLM 评判本身需要通过与人类判断进行对比来验证其准确性和可靠性，从而形成了循环依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LLM-as-a-Judge">LLM-as-a-Judge - Wikipedia</a></li>
<li><a href="https://www.evidentlyai.com/llm-guide/llm-as-a-judge">LLM-as-a-judge: a complete guide to using LLMs for evaluations</a></li>

</ul>
</details>

**标签**: `#LLM`, `#evaluation`, `#AI`, `#NLP`

---

<a id="item-9"></a>
## [M*：多模态模型的通用服务系统](https://twitter.com/StanfordAILab/status/2069158524278685929) ⭐️ 7.0/10

研究人员推出了 M*（M-Star），这是一个多模态模型的通用服务系统，无需为每种新架构构建新的基础设施。 这减少了工程开销并加速了新兴多模态模型的部署，从而在 AI 研究和生产中实现更快的迭代。 M*是模块化和可扩展的，允许模型作者声明其模型结构，并在无需定制引擎的情况下高效提供服务。

twitter · StanfordAILab · Jun 22, 20:40

**背景**: 多模态模型同时处理多种数据类型（如文本、图像、音频）。传统上，每种新模型架构都需要定制的服务系统，导致重复劳动和采用速度变慢。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.12688">M *: A Modular, Extensible, Serving System for Multimodal Models</a></li>
<li><a href="https://www.alphaxiv.org/abs/2606.12688">M*: A Modular, Extensible, Serving System for Multimodal Models | alphaXiv</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#model serving`, `#systems`, `#AI infrastructure`

---

<a id="item-10"></a>
## [扩散模型避免维度灾难](https://twitter.com/berkeley_ai/status/2068954548132016468) ⭐️ 7.0/10

马毅的一条推文强调了一个理论洞见：基于扩散去噪的生成方法即使在数据位于高维空间时也不会遭受维度灾难。 这一洞见意义重大，因为它解释了扩散模型为何能很好地扩展到图像和视频等高维数据，使其成为生成式 AI 中的强大工具。 维度灾难通常会导致传统生成模型在维度增加时失效，但扩散模型通过在学习低维流形上的反向去噪过程来避免这一问题。

twitter · berkeley_ai · Jun 22, 07:09

**背景**: 扩散模型是一类生成模型，学习逆转逐步加噪的过程，从而从随机噪声生成数据。维度灾难是指随着维度增加，体积呈指数增长，使得采样和密度估计变得困难。这条推文表明扩散模型天生规避了这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_model">Diffusion model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Curse_of_dimensionality">Curse of dimensionality - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 该推文被广泛转发，表明社区对扩散模型的理论基础有浓厚兴趣。但内容简短，为具体机制的进一步讨论留下了空间。

**标签**: `#diffusion models`, `#generative AI`, `#curse of dimensionality`, `#machine learning`

---

<a id="item-11"></a>
## [开发者用 Claude 构建 PS1 游戏开发工具](https://twitter.com/RodmanAi/status/2069341369697485152) ⭐️ 7.0/10

一位开发者利用 Anthropic 的 Claude AI 构建了一套完整的 PlayStation 1 游戏开发工具，克服了现有工具陡峭的学习曲线，实现了他 20 年来制作 PS1 游戏的梦想。 这展示了大型语言模型在创建专业软件开发工具方面的新应用，可能降低复古游戏开发的门槛，并激发在其他小众领域出现类似的 AI 辅助工具。 该工具完全使用 Claude 构建，开发者无需掌握复杂的官方 PS1 SDK。该工具的具体功能及其是否公开可用尚未披露。

twitter · RodmanAi · Jun 23, 08:46

**背景**: PlayStation 1（PS1）开发传统上需要掌握该主机的硬件和专有 SDK 的专业知识，这些知识难以学习和使用。Claude 是 Anthropic 开发的大型语言模型，能够生成代码并辅助软件开发，类似于 GPT-4。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(language_model)">Claude ( AI ) - Wikipedia</a></li>
<li><a href="https://claude.com/">Claude</a></li>

</ul>
</details>

**标签**: `#AI`, `#game development`, `#Claude`, `#retro gaming`, `#tooling`

---

<a id="item-12"></a>
## [Lean 的库缺失阻碍研究级数学证明](https://twitter.com/StanfordAILab/status/2069580651322646685) ⭐️ 6.0/10

一条推文指出，像 Lean 这样的形式化证明验证工具在研究级数学中常常无法使用，因为所需的正式库尚不存在。 这一观察突显了形式化验证在前沿数学应用中的关键限制，可能拖累依赖严格证明检查的领域的进展。 该推文特别提到了由微软开发的证明助手 Lean，并指出缺失的库是验证活跃研究领域证明的障碍。

twitter · StanfordAILab · Jun 24, 00:37

**背景**: Lean 是一种证明助手和函数式编程语言，用于形式化数学和验证证明。形式化证明验证涉及用形式语言表达数学陈述，并使用计算机检查逻辑步骤。尽管 Lean 拥有不断增长的形式化数学库，但它仍落后于庞大的研究级数学体系，使得许多当前证明无法实际使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant)</a></li>
<li><a href="https://www.mathlumen.com/articles/formal-proofs-lean-mathematics">The Formal Proof Revolution: How Lean Is Rebuilding... | MathLumen</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#Lean`, `#mathematics`, `#research`

---

<a id="item-13"></a>
## [LLM 的 Map-Reduce：新训练方法](https://twitter.com/StanfordAILab/status/2069564025537810580) ⭐️ 6.0/10

Noah Goodman 的一条推文将一种新颖的 LLM 训练方法比作 map-reduce，该方法使用低方差优势估计器进行端到端训练。 这个类比可能简化对复杂 LLM 训练技术的理解，并激发新的扩展和效率方法。 该方法进行端到端训练，并使用低方差优势估计器，这很可能指的是强化学习中常用的广义优势估计（GAE）。

twitter · StanfordAILab · Jun 23, 23:31

**背景**: Map-reduce 是一种通过将任务拆分为 map 和 reduce 阶段来处理大型数据集的编程模型。在 LLM 中，map-reduce 可用于通过分块处理长文本。低方差优势估计器是一种降低策略梯度方法方差的技术，可提高训练稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://danieltakeshi.github.io/2017/04/02/notes-on-the-generalized-advantage-estimation-paper/">Notes on the Generalized Advantage Estimation Paper</a></li>
<li><a href="https://dev.to/grzegorz_dubiel_db99203fe/turning-entire-blogs-into-short-summaries-map-reduce-for-llms-66j">Turning Entire Blogs into Short Summaries: Map - Reduce for LLMs</a></li>
<li><a href="https://deepwiki.com/thunlp/LLMxMapReduce/2-architecture">Architecture | thunlp/LLMxMapReduce | DeepWiki</a></li>

</ul>
</details>

**社区讨论**: 该推文互动较少（12 次转发），表明社区讨论有限。未提供评论。

**标签**: `#LLM`, `#map-reduce`, `#training`, `#NLP`

---

<a id="item-14"></a>
## [离线自主探索助力机器人技能开发](https://twitter.com/berkeley_ai/status/2068954279998603480) ⭐️ 6.0/10

Ken Goldberg 强调了一种名为“趣味自主机器人学习”的新方法，该方法利用离线自主探索在下游任务到来之前开发机器人技能。 这种范式可能使机器人无需密集奖励或明确任务监督就能获得通用技能，从而加速实际部署。 该方法为具身编码代理提供了一个“玩耍阶段”进行探索，利用离线数据构建可重复使用的技能。

twitter · berkeley_ai · Jun 22, 07:08

**背景**: 离线自主探索是指使用 AI 代理在不进行实时交互的情况下探索环境并收集数据，然后从静态数据集中学习。在机器人学中，这与需要持续环境交互的在线强化学习形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/Ken_Goldberg/status/2068404396061253677">Great work using offline agentic exploration to develop robot skills!</a></li>
<li><a href="https://arxiv.org/html/2601.00555">LLM-Based Agentic Exploration for Robot Navigation & Manipulation...</a></li>
<li><a href="https://ive-robot.github.io/">Imagine, Verify, Execute: Memory-guided Agentic Exploration with...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#reinforcement learning`, `#offline learning`, `#AI`

---

<a id="item-15"></a>
## [AI 演示工具：演示品而非产品](https://twitter.com/RodmanAi/status/2069445623791727020) ⭐️ 6.0/10

推特上的一篇批评指出，许多 AI 演示工具生成的幻灯片在 PowerPoint 等标准软件中打开时会崩溃，字体、布局和标志错位。 这削弱了对 AI 生产力工具的信任，并揭示了演示质量与实际可用性之间的差距，影响了依赖可靠演示软件的专业人士。 该帖子特别提到了从 AI 工具下载后出现的字体替换、布局偏移和标志错位等问题，表明与标准格式的兼容性差。

twitter · RodmanAi · Jun 23, 15:40

**背景**: AI 演示工具使用生成式 AI 根据文本提示创建幻灯片。然而，许多工具导出为依赖精确渲染的 PPTX 等格式，当生成的文件不完全符合目标软件的规范时，就会出现兼容性问题。

**标签**: `#AI`, `#presentation tools`, `#software quality`, `#user experience`

---

<a id="item-16"></a>
## [用语音将旧电脑改造成家庭 AI 服务器](https://twitter.com/tech_shrimp/status/2068969468743868859) ⭐️ 5.0/10

一项 DIY 挑战提出仅通过语音指令将闲置旧电脑改造成家庭 AI 服务器，由@tech_shrimp 在 Twitter 上分享。 该项目展示了如何将过时硬件重新用于现代 AI 工作负载，可能降低爱好者尝试本地 AI 服务的门槛。 推文包含一个教程或视频链接，但内容缺乏具体的技术步骤、工具或性能基准，因此更像是一个高层次概念而非详细指南。

twitter · tech_shrimp · Jun 22, 08:08

**背景**: 家庭 AI 服务器允许用户在本地运行 AI 模型，用于图像生成或自然语言处理等任务，无需依赖云服务。语音控制增加了便利性，实现免提操作。在 DIY 社区中，改造旧硬件是常见做法，有助于减少电子垃圾并节省成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jungley.net/homelab-exploring-infinite-possibilities/">【HomeLab系列0】-HomeLab入门：探索无限可能</a></li>

</ul>
</details>

**标签**: `#DIY`, `#AI`, `#home server`, `#hardware`

---

<a id="item-17"></a>
## [ZenRobotics 用 AI 机器人将垃圾变成商机](https://twitter.com/lukas_m_ziegler/status/2069035694551384210) ⭐️ 5.0/10

ZenRobotics 部署了基于 AI 的机器人系统，利用计算机视觉和传感器对垃圾进行分类，包括大型建筑垃圾和高速传送带上的废弃物，将垃圾转化为可盈利的商业机会。 这项创新显著提高了回收效率，减少了对危险且缓慢的人工分拣的依赖，推动了循环经济，使废物管理更加可持续和有利可图。 ZenRobotics 系统能够分拣超过 500 种垃圾类别，适用于从建筑垃圾到混合可回收物的多种废物类型，利用 AI 实时识别材料。

twitter · lukas_m_ziegler · Jun 22, 12:32

**背景**: 传统的垃圾分拣严重依赖人工，劳动强度大、危险且效率低。像 ZenRobotics 这样的 AI 驱动机器人分拣系统利用计算机视觉和机器学习自动识别和分离不同材料，提高了速度和准确性，同时降低了成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=HxkklR3BNFc">Intelligent Waste Sorting With ZenRobotics Recycler - YouTube</a></li>
<li><a href="https://www.terex.com/zenrobotics">Home | Robotic Waste Sorting | ZenRobotics</a></li>
<li><a href="https://aim2flourish.com/innovations/artificial-intelligence-in-waste-sorting">AIM2Flourish | Artificial Intelligence in Waste Sorting</a></li>

</ul>
</details>

**标签**: `#AI`, `#robotics`, `#waste management`, `#computer vision`

---

<a id="item-18"></a>
## [GLP-1 与 CRISPR：来自毒液和酸奶的突破](https://twitter.com/ylecun/status/2068997113728421992) ⭐️ 5.0/10

Yann LeCun 转发 Eric Topol 的观点，指出两项重大生物医学突破——GLP-1 受体激动剂和 CRISPR 基因编辑——分别源自吉拉毒蜥的毒液和酸奶中的细菌。 这凸显了基础科学中的偶然发现如何催生变革性疗法，例如用于糖尿病和肥胖症的 GLP-1 药物，以及用于精确基因组编辑的 CRISPR。 首个 GLP-1 受体激动剂艾塞那肽于 2005 年获批，其基于吉拉毒蜥唾液中发现的一种化合物。CRISPR-Cas9 基因编辑源自酸奶菌种嗜热链球菌中发现的细菌免疫系统。

twitter · ylecun · Jun 22, 09:58

**背景**: GLP-1 受体激动剂模拟一种刺激胰岛素分泌的天然激素，有助于控制血糖和体重。CRISPR 是一种基因工程工具，允许科学家高精度编辑 DNA，最初在细菌中进化以防御病毒。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nhm.ac.uk/discover/the-monster-whose-bite-saves-lives.html">Gila monster : meet the lizard whose venomous bite is saving lives</a></li>
<li><a href="https://en.wikipedia.org/wiki/CRISPR_gene_editing">CRISPR gene editing - Wikipedia</a></li>
<li><a href="https://www.uniklab.co/research/glp1-triple-agonists-ly3437943/">GLP - 1 Triple Agonists : Mechanism & Pipeline | UNIK LAB</a></li>

</ul>
</details>

**标签**: `#biomedical`, `#GLP-1`, `#CRISPR`

---

<a id="item-19"></a>
## [教程：用 Claude Code 替代 Kimi Code](https://twitter.com/tech_shrimp/status/2069339188311531980) ⭐️ 4.0/10

@tech_shrimp 发布教程，展示如何使用 Claude Code 替代 Kimi Code，涵盖视频理解、数据插件、Goal、Swarm 和 ACP 等高级功能。 该教程帮助开发者探索替代的 AI 编码工具，通过利用 Claude Code 相对于 Kimi Code 的能力，可能提高工作流程效率。 教程涵盖视频理解、数据插件、Goal、Swarm 和 ACP 等高级功能，这些在标准编码助手中并不常见。

twitter · tech_shrimp · Jun 23, 08:38

**背景**: Claude Code 是 Anthropic 开发的智能编码工具，能理解代码库、编辑文件并运行命令。Kimi Code 是 Moonshot AI 开发的开源 AI 代理工具，用于终端软件开发。Swarm 指多代理协调，ACP 可能代表代理通信协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://grokipedia.com/page/Kimi_Code_CLI">Kimi Code CLI</a></li>
<li><a href="https://www.kimi.com/code/en">Kimi Code with K2.7 Code: Next-Gen AI Code Agent & CLI - Kimi AI</a></li>

</ul>
</details>

**标签**: `#tutorial`, `#AI coding tools`, `#Claude Code`, `#Kimi Code`

---

<a id="item-20"></a>
## [Schmalz 推出 FDA 认证食品自动化夹爪](https://twitter.com/lukas_m_ziegler/status/2069209261901582455) ⭐️ 4.0/10

在 AutomateShow 上，Schmalz 展示了一款可配置的 FDA 认证夹爪，专为食品自动化设计，可处理生肉且完全可清洗。 这款夹爪通过提供符合 FDA 标准的卫生、可配置解决方案，使食品自动化更加普及，可能加速机器人在食品加工领域的应用。 该夹爪采用食品级材料制成，可处理生肉且完全可清洗，适用于多种食品应用。它可通过 Schmalz 的模块化系统进行配置。

twitter · lukas_m_ziegler · Jun 23, 00:01

**背景**: 食品自动化需要卫生、易清洁且可直接接触食品的夹爪。FDA 认证确保材料无毒且适合食品处理。Schmalz 是一家为自动化提供真空和夹持解决方案的制造商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.schmalz.com/en-us/digital-assistants/configurators">Customized solutions | Schmalz configurators</a></li>
<li><a href="https://www.linkedin.com/posts/zieglerr_food-automation-made-accessible-during-activity-7474974813766402048-qGbi">Food automation made accessible! During the Automate Show, Schmalz presented their ...</a></li>

</ul>
</details>

**标签**: `#robotics`, `#food automation`, `#gripper`

---

<a id="item-21"></a>
## [SpaceX 用猎鹰 9 号发射星落演示任务](https://twitter.com/SpaceX/status/2069429410965393449) ⭐️ 4.0/10

SpaceX 从佛罗里达州卡纳维拉尔角使用猎鹰 9 号火箭发射了星落演示任务，并确认星落舱成功部署。 该任务测试了一种旨在从轨道返回载荷的新型舱体，可能实现商业太空制造和实验的快速返回地球。 发射窗口为一小时，从 40 号航天发射场进行，任务目标为近地轨道。星落舱是 SpaceX 更广泛的星舰开发计划的一部分。

twitter · SpaceX · Jun 23, 14:36

**背景**: 星落是一种旨在从轨道或近轨道将载荷返回地球的太空舱类别。该演示任务是使用星舰提供商业再入服务的前奏，可能加速基于太空的研究和制造周转。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starfall">SpaceX Starfall - Wikipedia</a></li>
<li><a href="https://www.spacex.com/launches/starfalldemo">Starfall Demo Mission - SpaceX</a></li>
<li><a href="https://www.reddit.com/r/SpaceXLounge/comments/1ude2qs/starfall_demo_mission/">Starfall Demo Mission : r/SpaceXLounge - Reddit</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论指出该任务与星舰的联系，并推测未来的商业应用，一些人对再入舱的潜力表示兴奋。

**标签**: `#space`, `#SpaceX`, `#launch`

---

<a id="item-22"></a>
## [杨立昆转发警告：不要对 AI 恐慌](https://twitter.com/ylecun/status/2069084444070199602) ⭐️ 4.0/10

杨立昆转发了史蒂芬·平克的一条推文，其中引用了诺贝尔奖得主罗伯特·希勒的警告，呼吁不要对 AI 感到恐慌，并将其与历史上的金融恐慌相类比。 这凸显了关于 AI 风险的日益激烈的辩论，知名人士呼吁公众做出更理性的反应，而不是被恐惧驱动的叙事所左右。 这条转发互动量低，缺乏技术深度，更像是一篇观点文章，而非对 AI 安全讨论的实质性贡献。

twitter · ylecun · Jun 22, 15:45

**背景**: 罗伯特·希勒是诺贝尔经济学奖得主，以研究市场波动和非理性繁荣而闻名。史蒂芬·平克是认知心理学家和作家，经常撰写关于理性和进步的文章。杨立昆是顶尖 AI 研究员，Meta 的首席 AI 科学家。

**标签**: `#AI`, `#public opinion`, `#social media`

---

<a id="item-23"></a>
## [Claude 社区大使计划扩展至日本](https://twitter.com/ClaudeDevs/status/2069202892368773468) ⭐️ 4.0/10

ClaudeDevs 宣布启动日本 Claude 社区大使计划，邀请从北海道到冲绳的日本各地人士申请。 此次扩展增强了 Claude 的全球社区影响力，使日本这一关键科技市场能够举办更多本地聚会和协作。 大使们已在 37 个国家的 107 个城市举办了超过 290 场聚会，参与者超过 4 万人。日本计划现已开放申请。

twitter · ClaudeDevs · Jun 22, 23:36

**背景**: Claude 社区大使计划是 ClaudeDevs 发起的一项倡议，旨在支持本地聚会和活动，让开发者和爱好者可以学习并使用 Claude 进行构建。扩展到日本后，该计划将融入充满活力的开发者社区。

**标签**: `#Claude`, `#community`, `#ambassador`, `#Japan`

---

<a id="item-24"></a>
## [AI 接管小型团队的会议跟进工作](https://twitter.com/RodmanAi/status/2069481088838201726) ⭐️ 4.0/10

一位开发者在 Twitter 上分享，几周前他们停止了会议跟进工作，因为 AI 工具现在接手了这项任务，并指出在没有专职 PM 的小型工程团队中，项目管理任务会落到工程师头上。 这一观察突显了一个日益增长的趋势：AI 工具被用来减轻行政负担，可能让工程师专注于核心技术工作。同时，它也揭示了小型团队中 PM 任务的隐性负担，这会影响生产力和工作满意度。 推文没有具体说明使用了哪个 AI 工具，但暗示它自动化了会议摘要、行动项和跟进工作。作者指出，没有 PM 时，PM 工作并不会消失——它只是转移到了工程师身上。

twitter · RodmanAi · Jun 23, 18:01

**背景**: 在小型工程团队中，通常没有专职的产品经理（PM），因此工程师经常承担项目管理任务，如会议跟进，这可能会耗费大量时间。用于会议总结和任务管理的 AI 工具越来越受欢迎，例如 Otter.ai、Fireflies.ai 等产品提供自动转录和行动项提取。这条推文反映了此类工具在现实小型团队中的实际应用场景。

**标签**: `#productivity`, `#engineering management`, `#AI tools`

---

<a id="item-25"></a>
## [Google DeepMind 祝贺 Project Genie 获得戛纳狮子大奖](https://twitter.com/GoogleDeepMind/status/2069542674483261621) ⭐️ 3.0/10

Google DeepMind 在推特上转发祝贺 Project Genie 团队赢得戛纳狮子 AI 工艺大奖。 该奖项凸显了 AI 生成内容和世界模型在创意产业中日益增长的认可度，可能加速此类技术的应用。 Project Genie 是 Google DeepMind 的一个网站，允许订阅者访问 Genie 3，这是一个用于生成和探索 3D 环境的世界模型。该奖项在戛纳国际创意节上颁发。

twitter · GoogleDeepMind · Jun 23, 22:06

**背景**: Project Genie 于 2026 年 1 月发布，是一个早期研究原型，利用文本描述生成可实时探索的逼真世界。它已被用于在 3D 环境中训练 AI 代理和视频游戏设计，但其主要关注点是机器人和模拟。戛纳狮子 AI 工艺大奖旨在表彰在创意工作中对 AI 的杰出运用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Genie_(website)">Project Genie (website)</a></li>
<li><a href="https://labs.google/projectgenie">Project Genie</a></li>
<li><a href="https://deepmind.google/models/genie/">Genie 3 — Google DeepMind</a></li>

</ul>
</details>

**标签**: `#award`, `#AI`, `#GoogleDeepMind`

---

<a id="item-26"></a>
## [IntrinsicAI 在 Automate 展会上展示工业机器人 2.0](https://twitter.com/lukas_m_ziegler/status/2069435308282712202) ⭐️ 3.0/10

IntrinsicAI 在 Automate 展会现场进行工业机器人 2.0 的实时演示，展位采用开放式布局并提供咖啡。 此次活动凸显了 AI 驱动机器人在制造业中的实际应用，标志着工业自动化正朝着更易获取和更具互动性的方向发展。 展位全天进行现场演示，参观者可以直接与团队交流并亲眼目睹技术运作，没有任何隔阂。

twitter · lukas_m_ziegler · Jun 23, 15:00

**背景**: 工业机器人 2.0 指的是将 AI、视觉系统和坚固电子设备集成，使机器人更智能、更适应环境。IntrinsicAI 是一家专注于帮助企业领导者简化 AI 采用的公司，但本条推文未详细说明其具体产品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://roboorion.com/article/industrial-robotics-2.0-ai-&-rugged-electronics-in-manufacturing.html">Industrial Robotics 2 . 0 : AI & Rugged Electronics in... | Robo Orion</a></li>
<li><a href="https://www.automationworld.com/products/data/blog/13310166/robotics-20-using-vision-to-make-robots-smarter">Robotics 2 . 0 : Using Vision to Make Robots Smarter | Automation World</a></li>
<li><a href="https://intrinsicai.co.uk/">IntrinsicAi : Simplifying AI Adoption for Business Leaders</a></li>

</ul>
</details>

**标签**: `#industrial robotics`, `#trade show`, `#promotional`

---

<a id="item-27"></a>
## [AI 短期内不太可能治愈癌症](https://twitter.com/ylecun/status/2069612005791580392) ⭐️ 3.0/10

Yann LeCun 转发了 Eric Topol 的言论，表达了对 AI 短期内治愈癌症的怀疑，并补充说 AI 已在其他方面为医疗保健做出了贡献。 这凸显了关于 AI 在医疗保健领域实际影响的持续辩论，以谨慎的预期缓和了炒作。 该推文是一条转发，参与度低（70 次转发），缺乏技术深度，属于低优先级的观点内容。

twitter · ylecun · Jun 24, 02:42

**标签**: `#AI`, `#healthcare`, `#opinion`

---

<a id="item-28"></a>
## [推文称美国国际开发署削减导致 60 万人死亡](https://twitter.com/ylecun/status/2069082508059136104) ⭐️ 2.0/10

Yann LeCun 转发了一条推文，声称美国国际开发署的解散已导致贫困国家约 60 万人死亡，其中包括 40 万儿童。 如果该说法属实，则凸显了政策变化带来的严重人道主义后果，但该推文缺乏可验证来源，且与技术受众无关。 该推文是转自@AFpost，没有提供任何证据或引用来源。该新闻条目因属于无关的政治内容而得分较低（2.0/10）。

twitter · ylecun · Jun 22, 15:38

**标签**: `#politics`, `#off-topic`

---