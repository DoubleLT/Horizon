---
layout: default
title: "Horizon Summary: 2026-09-21 (ZH)"
date: 2026-09-21
lang: zh
---

> From 25 items, 23 important content pieces were selected

---

1. [RAI 研究所的 AthenaZero 机器人以 113 公里时速投掷棒球](#item-1) ⭐️ 7.0/10
2. [VertiGo 机器人靠螺旋桨推力爬墙，无需吸附装置](#item-2) ⭐️ 7.0/10
3. [纯 Python 实现的可读 MPPI 控制代码发布](#item-3) ⭐️ 6.0/10
4. [SpaceX 整流罩半片完成第 40 次飞行](#item-4) ⭐️ 6.0/10
5. [LeCun 重申：仅靠自回归 LLM 无法实现人类级 AI](#item-5) ⭐️ 6.0/10
6. [LeCun 指责 Hinton 和 Bengio 助推 AI 监管](#item-6) ⭐️ 6.0/10
7. [TMLR 因投稿激增收紧直接拒稿政策](#item-7) ⭐️ 6.0/10
8. [Yann LeCun 转发反 AI 末日论观点，主张构建强大 AI](#item-8) ⭐️ 5.0/10
9. [LeCun 转发奥巴马呼吁超越 AI 技术层面的言论](#item-9) ⭐️ 4.0/10
10. [LeCun 转发质疑：AI 危害追踪应关注现实还是假想未来](#item-10) ⭐️ 4.0/10
11. [LeCun 转发 Malik 对视觉语言模型的根本性担忧](#item-11) ⭐️ 4.0/10
12. [推特长文推荐 10 个冷门 AI 与编程智能体 GitHub 仓库](#item-12) ⭐️ 4.0/10
13. [SpaceX 确认成功部署 27 颗星链卫星](#item-13) ⭐️ 3.0/10
14. [Yann LeCun 转发物理世界建模研讨会公告](#item-14) ⭐️ 3.0/10
15. [LeCun 转发 1995 年开源恐慌与 AI 智能体恐惧的类比](#item-15) ⭐️ 3.0/10
16. [Yann LeCun 转发呼吁击败 AI 末日论](#item-16) ⭐️ 3.0/10
17. [Yann LeCun 转发推文，批评 AI 超级智能论中的“魔法常数”](#item-17) ⭐️ 3.0/10
18. [Yann LeCun 转发称 AI 到 2030 年终结人类概率为 0%](#item-18) ⭐️ 3.0/10
19. [Yann LeCun 转发推文，称“失控智能体”叙事是有预谋的](#item-19) ⭐️ 3.0/10
20. [Yann LeCun 转发关于全球对美国看法的政治民调评论](#item-20) ⭐️ 2.0/10
21. [Yann LeCun 转发 Anthropic 链接但未加评论](#item-21) ⭐️ 2.0/10
22. [一条低信息量推文称赞某位未具名的无人机电机开发者](#item-22) ⭐️ 1.0/10
23. [Yann LeCun 转发关于斯蒂芬·米勒移民执法行动的时政评论](#item-23) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [RAI 研究所的 AthenaZero 机器人以 113 公里时速投掷棒球](https://twitter.com/lukas_m_ziegler/status/2101597695777411232) ⭐️ 7.0/10

RAI 研究所的双臂机器人 AthenaZero 登上了本月《Science Robotics》的封面，它能够以 113 公里/小时的速度投掷棒球。论文报告其腕部有效质量仅为 3.97 公斤，而按照相同标准测量，Franka 机械臂为 29.21 公斤，UR5e 为 34.72 公斤。 腕部有效质量降低近一个数量级，意味着机器人既能完成快速投掷这类类人动态动作，又能保持柔顺接触的安全性。这可能影响未来研究和工业机械臂的设计方向，使关注重点从单纯的负载与精度转向低反射惯量。 AthenaZero 是一台双臂机器人，配备 1 自由度躯干、两条 7 自由度手臂和两只 6 自由度手，由四种直径分别为 95 毫米、76 毫米、38 毫米和 25 毫米的定制准直驱、高力透明执行器驱动。其低有效质量源自这种低惯量、力透明的执行器设计，而非传统的高减速比关节。

twitter · lukas_m_ziegler · Sep 20, 09:01

**背景**: 腕部有效质量描述的是机械臂在接触或碰撞时在其末端表现出的惯量；数值越高，快速动态运动就越危险、越难控制。像 Franka Emika Panda 和 Universal Robots UR5e 这类传统协作机械臂采用高减速比传动，虽然提升了负载能力，却也提高了反射惯量。由波士顿动力创始人 Marc Raibert 领导的 RAI 研究所正在专门设计关节反射惯量更低、适合柔顺接触的机械臂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rai-inst.com/resources/blog/bimanual-robot-for-dynamic-manipulation/">AthenaZero : A Bimanual Robot for Dynamic... | RAI Institute</a></li>
<li><a href="https://arxiv.org/html/2609.19194">AthenaZero : A low-inertia, bimanual robot for dynamic manipulation</a></li>
<li><a href="https://robohorizon.com/en-us/news/2026/04/rais-athenazero-robot-wields-two-arms-with-human-like-speed/">RAI 's AthenaZero Robot Wields Two Arms With … | RoboHorizon</a></li>

</ul>
</details>

**标签**: `#robotics`, `#Science Robotics`, `#manipulation`, `#dynamic throwing`, `#research`

---

<a id="item-2"></a>
## [VertiGo 机器人靠螺旋桨推力爬墙，无需吸附装置](https://twitter.com/lukas_m_ziegler/status/2101244934028234809) ⭐️ 7.0/10

迪士尼研究院与苏黎世联邦理工学院（ETH Zürich）联合开发了 VertiGo——一款四轮机器人，它不依赖吸盘、磁铁或干性黏合剂，而是通过两个可 360°倾斜的螺旋桨向墙面施加推力来攀爬垂直墙壁。该机器人可以在地面水平滚动，并通过协调螺旋桨方向与车轮牵引力，无缝过渡到垂直墙面上。 这种方法绕开了传统爬墙机器人的根本局限——它们需要与吸盘、磁力或黏合剂相配合的表面。通过使用推力，VertiGo 有望攀爬更粗糙或非铁磁性的表面，并在地面与墙面运动之间切换，为检测、维护和娱乐机器人开辟了新可能。 VertiGo 采用两个可倾斜螺旋桨，同时向上和向墙面提供推力，并配合四个车轮提供牵引力；它由遥控操作，由迪士尼研究院苏黎世分部与苏黎世联邦理工学院合作完成。该设计实现了近乎无缝的地面到墙面过渡，但可能依赖足够的螺旋桨推力，并受功耗和噪音的限制。

twitter · lukas_m_ziegler · Sep 19, 09:40

**背景**: 爬墙机器人通常使用吸附机制来附着在表面上，例如真空吸力、磁铁、干性黏合剂（范德华力）或静电吸附。这些方法各有缺点：吸力需要光滑表面，磁铁需要铁磁性材料，而干性黏合剂会磨损。推力吸附是一种替代方案，通过螺旋桨将机器人压向墙面，使其能够攀爬其他方法无法应对的表面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VertiGo">VertiGo - Wikipedia</a></li>
<li><a href="https://la.disneyresearch.com/publication/vertigo/">VertiGo - A Wall-Climbing Robot including Ground-Wall Transition - Disney Research</a></li>
<li><a href="https://futurism.com/disney-research-zurich-eth-create-robot-can-climb-walls">Disney Research Zurich and ETH Create a Robot That Can Climb Walls</a></li>

</ul>
</details>

**社区讨论**: 该推文获得了 1150 个点赞、135 次转发和 59 条回复，表明这种新颖的推力驱动方式引起了强烈兴趣。评论者可能讨论了用推力代替吸附的巧妙之处，同时也有人可能提出了对功耗、噪音以及在实际表面上的实用性的担忧。

**标签**: `#robotics`, `#wall-climbing`, `#Disney Research`, `#ETH Zürich`, `#thrust-based locomotion`

---

<a id="item-3"></a>
## [纯 Python 实现的可读 MPPI 控制代码发布](https://twitter.com/lukas_m_ziegler/status/2101634886079541311) ⭐️ 6.0/10

Lukas M. Ziegler 分享了一个小型纯 Python 实现的模型预测路径积分（MPPI）控制代码，篇幅短到可以一口气读完。代码展示了核心循环：采样数千条带噪声的控制序列，并对每条序列进行前向推演，从而选出最优动作。 MPPI 被广泛用于越野自动驾驶和敏捷驾驶研究，但参考实现往往深埋在庞大的 C++/CUDA 代码库中，导致算法难以学习。一个紧凑、可读的 Python 版本降低了学生、机器人研究者和爱好者理解和原型验证 MPPI 的门槛。 该实现刻意保持极简和教学导向，而非针对实时性能优化，因为纯 Python 无法匹敌生产级 MPPI 系统中基于 GPU 并行化的采样。它聚焦于定义 MPPI 的采样与加权循环，适合作为转向更快实现之前的入门起点。

twitter · lukas_m_ziegler · Sep 20, 11:29

**背景**: MPPI（模型预测路径积分）控制是一种基于采样的无导数模型预测控制方法，于 2016 年提出，其推导基于自由能与相对熵之间的信息论对偶关系。与经典 MPC 对动力学线性化并求解二次规划不同，MPPI 采样大量带噪声的控制序列，通过系统模型进行前向推演，再根据代价对它们加权，从而生成更新后的控制输入。这使其非常适合非线性、随机系统，例如越野车辆和敏捷驾驶平台，并已在 GT-AutoRally 等车辆上得到验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sites.gatech.edu/acds/mppi/">Model Predictive Path Integral (MPPI) control - Autonomous Control and ...</a></li>
<li><a href="https://www.emergentmind.com/topics/model-predictive-path-integral-mppi">Model Predictive Path Integral Control</a></li>
<li><a href="https://www.mathworks.com/help/robotics/ug/local-path-planning-using-model-predictive-path-integral.html">Introduction to Model Predictive Path Integral (MPPI) Controller</a></li>

</ul>
</details>

**社区讨论**: 该帖子获得了中等程度的关注，包括 257 个点赞、29 次转发和 8 条回复，表明机器人与控制社区将其视为有价值的教学资源。由于未提供具体评论内容，无法总结讨论中的具体观点。

**标签**: `#MPPI`, `#model-predictive-control`, `#robotics`, `#python`, `#autonomy`

---

<a id="item-4"></a>
## [SpaceX 整流罩半片完成第 40 次飞行](https://twitter.com/SpaceX/status/2101489521615385011) ⭐️ 6.0/10

SpaceX 在最近一次任务中确认整流罩分离成功，并宣布其中一片整流罩半片完成了第 40 次飞行，这是公司首次达到这一数字。该消息通过 X（原 Twitter）上的一条简短帖子发布。 这一里程碑表明 SpaceX 的可复用范围已远超助推器，整流罩也已成为可常规复飞的硬件，进一步降低了发射成本。它巩固了可复用性作为整个发射行业竞争优势的地位。 每次猎鹰 9 号或猎鹰重型发射都使用两片整流罩半片，它们在载荷部署后分离，并在降落伞作用下落入海中等待回收。SpaceX 累计复飞整流罩半片已超过 300 次，此前单片最高纪录为 36 次飞行。

twitter · SpaceX · Sep 20, 01:52

**背景**: 载荷整流罩是发射过程中保护卫星的鼻锥形结构，火箭进入太空后即被抛弃。过去整流罩通常一次性使用，但 SpaceX 于 2017 年启动回收实验项目，最初尝试用船上的网兜捕捉，后来改为更简单的海上打捞。到 2021 年，该公司已在大多数卫星任务中常规翻新并复用整流罩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_fairing_recovery_program">SpaceX fairing recovery program</a></li>
<li><a href="https://en.wikipedia.org/wiki/Payload_fairing">Payload fairing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#reusability`, `#rocket fairing`, `#spaceflight`, `#milestone`

---

<a id="item-5"></a>
## [LeCun 重申：仅靠自回归 LLM 无法实现人类级 AI](https://twitter.com/ylecun/status/2101674638363209873) ⭐️ 6.0/10

Yann LeCun 在 X（原 Twitter）上发帖，重申了他长期以来的立场："自回归 LLM 本身不会通向人类级 AI"，并在讨论中@了 Geoffrey Hinton 和@musedivision。该帖只是对其既有观点的再次表述，并非新的技术成果或发布。 LeCun 是深度学习领域最具影响力的人物之一，他对自回归 LLM 扩展路线的公开质疑，直接参与了关于现有架构能否通向 AGI、还是需要全新方法的广泛争论。他与同为图灵奖得主的 Hinton 之间的交锋备受关注，并影响着研究界如何界定 LLM 的能力边界。 这条推文只是一句简短的引述式表态，没有提供新的实验证据、基准测试或替代方案，且以转发自己回复的形式出现。LeCun 此前曾主张以世界模型和联合嵌入预测架构（JEPA）等替代范式，作为超越自回归生成的路径。

twitter · ylecun · Sep 20, 14:07

**背景**: 自回归语言模型一次生成一个 token，每个 token 都以之前所有 token 为条件，这正是 GPT 类系统的核心机制。"人类级 AI"通常被等同于通用人工智能（AGI），指一种在几乎所有任务上都能达到或超越人类能力的假想系统。LeCun 的核心论点是：无论规模如何扩大，预测下一个 token 都不足以支撑 AGI 所需的那种推理能力和对世界的理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Autoregressive_model">Autoregressive model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 该条目提到转发量很高，说明社区关注度强，但内容本身只是一句简短表态，缺乏详细的技术深度。由于未提供具体评论内容，只能推断社区情绪存在分歧：一方认同 LLM 存在根本性局限，另一方则认为持续扩展仍会带来进步。

**标签**: `#AI`, `#LLM`, `#Yann LeCun`, `#Twitter`, `#Debate`

---

<a id="item-6"></a>
## [LeCun 指责 Hinton 和 Bengio 助推 AI 监管](https://twitter.com/ylecun/status/2101496904999665788) ⭐️ 6.0/10

Yann LeCun 在 Twitter 上公开批评 Geoffrey Hinton 和 Yoshua Bengio，称他们无意中帮助了那些想要将 AI 研发锁起来的人。这条推文是对 Hinton 的回复，内容被截断，突显了三位图灵奖得主在 AI 安全与监管问题上的分歧日益加深。 这场交锋凸显了 AI 社区的重大分歧：LeCun 倡导开放研究和开源 AI，而 Hinton 和 Bengio 则支持加州 SB 1047 等监管措施。随着全球各国政府考虑 AI 监管，这场辩论可能影响政策决策和公众认知。 推文内容被截断，缺乏完整上下文，但提及了关于 AI 安全担忧是否足以限制开放研究的持续争议。LeCun 一直反对此类限制，而 Hinton 和 Bengio 则签署了支持 SB 1047 等法案的公开信，该法案对大型 AI 模型施加安全要求。

twitter · ylecun · Sep 20, 02:21

**背景**: Yann LeCun、Geoffrey Hinton 和 Yoshua Bengio 常被称为“AI 教父”，因在深度学习领域的贡献共同获得 2018 年图灵奖。近年来，Hinton 和 Bengio 对 AI 的生存风险发出警告并支持监管努力，而 LeCun 则认为此类监管可能扼杀创新，开放研究对安全至关重要。这场公开分歧反映了 AI 安全倡导者与开源支持者之间更广泛的紧张关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geoffrey_Hinton">Geoffrey Hinton - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/posts/yann-lecun_ensuring-ai-innovation-in-europe-open-letter-activity-7242573044739641344-dscB">Open letter on EU AI regulation | Yann LeCun posted on the topic - LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#AI regulation`, `#Yann LeCun`, `#Geoffrey Hinton`, `#Twitter debate`

---

<a id="item-7"></a>
## [TMLR 因投稿激增收紧直接拒稿政策](https://twitter.com/StanfordAILab/status/2101262196118585800) ⭐️ 6.0/10

TMLR（机器学习研究汇刊）宣布，由于投稿量激增而审稿人资源有限，将实施更严格的直接拒稿（desk rejection）政策。该消息由斯坦福 AI 实验室转发 TMLR 官方账号的内容对外发布。 这一变化表明机器学习领域的同行评审流程正承受越来越大的压力，投稿量的增长速度已超过合格审稿人的供给。向 TMLR 投稿的作者可能面临未经完整评审即被快速拒稿的情况，从而影响机器学习研究者发表成果的方式和渠道。 直接拒稿（desk rejection）是指论文未经送交同行评审即由编辑直接拒绝，这类拒稿通常几乎不提供个性化反馈。TMLR 是一个相对较新的发表平台，旨在补充 JMLR，其依赖志愿审稿人的模式使其在投稿过载时尤为脆弱。

twitter · StanfordAILab · Sep 19, 10:48

**背景**: TMLR（机器学习研究汇刊）是一个传播机器学习研究成果的发表平台，其创立目的是补充历史悠久的《机器学习研究杂志》（JMLR），并服务于不断壮大的机器学习社区。直接拒稿是学术出版中的常见做法，据估计，根据领域不同，主要期刊有 30%至 70%的稿件在同行评审前即被拒。近年来随着机器学习/人工智能研究成果的爆发式增长，像 TMLR 这样的平台难以招募到足够多的合格审稿人来应对投稿洪流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jmlr.org/tmlr/">Transactions on Machine Learning Research (TMLR)</a></li>
<li><a href="https://ecrlife.org/why-desk-rejections-happen/">Why desk rejections happen and how young researchers can avoid...</a></li>
<li><a href="https://academia.stackexchange.com/questions/199099/understanding-desk-rejection">publications - Understanding Desk Rejection - Academia Stack...</a></li>

</ul>
</details>

**社区讨论**: 该公告获得了 215 次转发，属于中等程度的关注，反映出研究社区对发表渠道收紧的担忧。不过，现有内容缺乏对具体政策变化的详细讨论或辩论。

**标签**: `#academic publishing`, `#machine learning`, `#peer review`, `#TMLR`, `#research community`

---

<a id="item-8"></a>
## [Yann LeCun 转发反 AI 末日论观点，主张构建强大 AI](https://twitter.com/ylecun/status/2101422860300607977) ⭐️ 5.0/10

Meta 首席 AI 科学家 Yann LeCun 转发了 Joscha Bach（@Plinz）的一条推文，该推文明确反对 AI 末日论立场，主张人类应当构建强大的 AI 来解决文明面临的紧迫问题。这条推文是一段简短的非技术性观点表达，获得了中等程度的互动（约 88 次转发）。 LeCun 是 AI 领域最具影响力的声音之一，他转发反末日论立场为 AI 安全倡导者与将强大 AI 视为解决方案而非生存威胁的一方之间的持续争论增添了分量。这场争论直接影响 AI 政策、监管，以及各大实验室如何为其开发议程辩护。 这条推文是一段简短的非技术性观点，没有提供实质性论证或证据，LeCun 的转发本身也未附加任何评论。现有摘录中内容被截断，因此该立场背后的完整推理无法看到。

twitter · ylecun · Sep 19, 21:27

**背景**: AI 末日论指的是认为先进 AI 对人类构成生存风险的信念，这一观点与 Geoffrey Hinton、Eliezer Yudkowsky 等人相关。Yann LeCun 长期以来一直是该立场的怀疑者，他认为当前的大语言模型还不够强大，不足以构成生存威胁，并主张 AI 应当为人类造福，同时设置诸如“服从人类”和“共情”等护栏。Joscha Bach 是一位认知科学家，以其在通用人工智能和心智哲学方面的研究而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forum.effectivealtruism.org/posts/LSzHmdCdsFieMXLcL/yann-lecun-on-agi-and-ai-safety">Yann LeCun on AGI and AI Safety</a></li>
<li><a href="https://www.businessinsider.com/yann-lecun-meta-ai-guardrails-geoffrey-hinton-2025-8">Meta chief AI scientist Yann LeCun says these are the 2 key guardrails needed to protect us all from AI</a></li>
<li><a href="https://ondiscourse.com/ai-doomerism-is-a-business-tactic/">AI Doomerism is a Business Tactic - ON_Discourse</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI doomerism`, `#Yann LeCun`, `#Twitter`, `#AI policy`

---

<a id="item-9"></a>
## [LeCun 转发奥巴马呼吁超越 AI 技术层面的言论](https://twitter.com/ylecun/status/2101494639089922327) ⭐️ 4.0/10

Yann LeCun 转发了一段 MeidasTouch 发布的视频片段，其中奥巴马表示，如果只从治愈癌症或改善能源的角度来思考 AI，就会忽略这项技术所引发的更广泛社会问题。这条推文（twitter.com/ylecun/status/2101494639089922327）获得了约 3797 次转发。 这次转发表明，一位顶尖 AI 研究者正在放大对 AI 影响的政治性框架，推动讨论从基准测试和产品发布转向治理、公平与社会后果。这也说明 AI 政策讨论正日益在研究者、政治人物和媒体之间交叉进行。 推文内容只是视频片段中被截断的一句话，因此奥巴马完整的论述以及任何具体政策建议都无法从这条推文中看到。该条目不含技术细节或新研究发现，其新闻价值主要来自转发者的身份以及由此产生的互动量。

twitter · ylecun · Sep 20, 02:12

**背景**: Yann LeCun 是图灵奖得主、AI 科学家，以深度学习与卷积神经网络的基础性工作闻名，目前担任 Meta 首席 AI 科学家。奥巴马自总统任期以来多次在采访和公开活动中谈论 AI 的风险与机遇，而 MeidasTouch 是一家进步派媒体，经常将政治评论剪辑后发布到社交平台。在 X（原 Twitter）上，转发是研究者表达认同某位公众人物立场而不附加自身评论的常见方式。

**标签**: `#AI policy`, `#Obama`, `#social impact`, `#Twitter`

---

<a id="item-10"></a>
## [LeCun 转发质疑：AI 危害追踪应关注现实还是假想未来](https://twitter.com/ylecun/status/2101485259791405197) ⭐️ 4.0/10

Yann LeCun 转发了 Dan Jeffries 的一条推文，质问 AI 界究竟是在追踪现实中真实发生的危害，还是只追踪假想的未来危害，并提到“已追踪 362 起”但内容被截断。这条转发本身没有提供新数据或分析，更多是向其关注者抛出一个修辞性提问。 这场互动凸显了 AI 安全讨论中长期存在的分歧：一方关注推测性的生存风险或未来风险，另一方则记录当下真实发生的危害，如偏见、虚假信息和心理伤害。由于 LeCun 是 Meta 的知名人物，他对这一框架的放大可能影响整个社区对 AI 伦理与安全研究优先级的判断。 推文在“已追踪 362 起……”处被截断，因此无法确定所指的是哪项指标或数据集，也没有提供来源或方法论。该帖是转发而非原创评论，并未就如何开展现实危害追踪提出具体方案。

twitter · ylecun · Sep 20, 01:35

**背景**: AI 安全与伦理讨论常分为两派：一派关注近期可衡量的危害，例如偏见输出、虚假信息，或像 AI Psychosis Watch 这类项目记录的心理影响；另一派关注流氓模型或目标错位等长期推测性风险。Meta 首席 AI 科学家 Yann LeCun 多次表示，对 AI 生存风险的恐惧被夸大，反而分散了对更具体问题的注意力。追踪现实危害通常需要事件数据库、审计和监测工具，但整个行业在这方面仍然零散且缺乏统一标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aipsychosis.watch/">AI Psychosis Watch — Tracking AI-Induced Psychological Harm</a></li>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/996563/ai-safety-research-metr-redwood-openai-anthropic">Inside the suddenly explosive world of AI safety | The Verge</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#AI safety`, `#Twitter`, `#Yann LeCun`, `#harm tracking`

---

<a id="item-11"></a>
## [LeCun 转发 Malik 对视觉语言模型的根本性担忧](https://twitter.com/ylecun/status/2101441237031264586) ⭐️ 4.0/10

Yann LeCun 转发了一条 Jitendra Malik 的推文，Malik 在推文中表示他同意“Toru”对视觉语言模型（VLM）提出的根本性担忧，同时也称赞了 Astra 等模型取得的进展。 当两位最知名的计算机视觉研究者公开对 VLM 表示质疑时，这表明当前主流的多模态范式可能面临更深层的架构性批评，并可能影响研究界下一步的投入方向。 这条推文内容被截断，并未具体说明所谓“根本性担忧”究竟是什么，也没有给出具体的技术论断、基准测试或论文链接；唯一具体的引用是把 Astra 作为 VLM 进展的例证。

twitter · ylecun · Sep 19, 22:40

**背景**: 视觉语言模型（VLM）是能够同时理解图像和文本的 AI 系统，是对纯文本大语言模型的扩展；知名例子包括 GPT-4V、Google 的 Gemini、Anthropic 的 Claude 3 Opus，以及 LLaVA、InstructBLIP 等开源模型。Astra 是一种通用视觉语言模型，可以接收一张图像和一组目标类别，并返回 JSON 边界框等结构化检测结果。Yann LeCun 和 Jitendra Malik 都是计算机视觉与深度学习领域的领军人物，因此他们的评论在 AI 研究界具有相当分量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision_Language_Models_(VLM)">Vision Language Models (VLM)</a></li>
<li><a href="https://blog.roboflow.com/gpt-6-astra-vision/">GPT-6 Astra Is the Best Vision Model We Have Tested</a></li>
<li><a href="https://www.ibm.com/think/topics/vision-language-models">What Are Vision Language Models (VLMs)? | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#VLM`, `#vision-language models`, `#research commentary`, `#Twitter`

---

<a id="item-12"></a>
## [推特长文推荐 10 个冷门 AI 与编程智能体 GitHub 仓库](https://twitter.com/RodmanAi/status/2101649317807440109) ⭐️ 4.0/10

推特用户 @RodmanAi 发布了一条长文，列出了 10 个不太知名的、专注于 AI 和编程智能体的 GitHub 仓库，其中包括 Vero（一个使用 Lean 4 验证生成代码的 AI 编程智能体）和 Agentor（一个添加智能体发现功能的工具）。该推文获得了约 80 个点赞、26 次转发和 19 条回复，被定位为一份精选列表，收录了那些不会出现在常见 AI 讨论中的项目。 这类精选列表能帮助开发者发现那些可能不会通过主流渠道浮出水面的小众工具，从而可能加速专用 AI 编程智能体的采用。像 Vero 和 Agentor 这样的项目被收录，凸显了 AI 智能体生态中对验证和互操作性的兴趣日益增长。 在提供的内容中，该推文被截断，只显示了前两个条目（Vero 和 Agentor），因此完整的 10 个仓库列表不可见。Vero 使用 Lean 4（一种定理证明器和函数式编程语言）来验证 AI 生成的代码，而 Agentor 则专注于智能体发现，可能与智能体间通信协议有关。

twitter · RodmanAi · Sep 20, 12:26

**背景**: Lean 4 是一种证明助手和函数式编程语言，用于数学证明和软件的形式化验证。AI 编程智能体是自主生成或修改代码的工具，验证其输出是一个关键挑战。智能体发现指的是允许 AI 智能体相互发现和通信的协议，例如 A2A 协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://docs.celesto.ai/agentor/agent-to-agent">Agent -to- Agent communication with the A2A Protocol - Celesto AI</a></li>

</ul>
</details>

**标签**: `#GitHub`, `#AI`, `#coding agents`, `#curated list`, `#developer tools`

---

<a id="item-13"></a>
## [SpaceX 确认成功部署 27 颗星链卫星](https://twitter.com/SpaceX/status/2101504221266792661) ⭐️ 3.0/10

SpaceX 在 X 平台上确认，一枚从加利福尼亚州发射的猎鹰 9 号火箭已成功将 27 颗星链卫星送入轨道。公司同时提供了发射直播链接，供观众观看此次任务。 这是星链星座的一次常规但持续的扩容。目前星链在轨卫星约 1.04 万颗，用户超过 1200 万，已成为 SpaceX 最大的业务板块。持续发射有助于维持全球宽带覆盖，包括机上互联网以及政府和军事通信服务。 此次任务使用的是 SpaceX 可部分重复使用的猎鹰 9 号火箭，其助推器可垂直着陆并多次复用，单枚助推器最多已飞行 37 次。星链卫星运行在近地轨道，约占地球所有活跃可机动卫星的 75%。

twitter · SpaceX · Sep 20, 02:50

**背景**: 猎鹰 9 号是两级、可部分重复使用的中型运载火箭，于 2010 年首飞，使用 SpaceX 的梅林发动机，以液氧和 RP-1 煤油为推进剂。星链是 SpaceX 的卫星互联网星座，自 2019 年开始发射，部署成本估计超过 100 亿美元。该星座因光污染和轨道拥堵问题受到天文学家的批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falcon_9_rocket">Falcon 9 rocket</a></li>
<li><a href="https://en.wikipedia.org/wiki/Starlink_(satellite_constellation)">Starlink (satellite constellation)</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#satellite deployment`, `#space technology`, `#operational update`

---

<a id="item-14"></a>
## [Yann LeCun 转发物理世界建模研讨会公告](https://twitter.com/ylecun/status/2101498713185108092) ⭐️ 3.0/10

Yann LeCun 转发了 @KempeLab 关于即将举办的“物理世界建模”研讨会的公告，表明他对该活动的支持。该研讨会旨在汇聚对将世界建模技术应用于物理问题感兴趣的研究人员。 世界模型日益被视为 AI 通过观察现实而非仅靠文本学习的关键方向，LeCun 的转发让 AI 与物理研究这一小众但不断增长的交叉领域获得更多关注。这可能吸引 AI 和物理两个社区更多的关注与参与。 该公告是一条转发，互动量有限（4 次转发），没有实质性的技术内容或讨论。研讨会被描述为以物理为视角聚焦世界建模，但片段中未包含日期、地点或演讲者等进一步细节。

twitter · ylecun · Sep 20, 02:28

**背景**: AI 中的世界模型是指通过观察图像或视频等方式，学习世界运作方式的内部表征，从而实现预测和规划的系统。在物理学中，这类模型可以模拟物理交互，并支持机器人技术和科学发现。LeCun 长期倡导将世界模型作为通往更通用 AI 的路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/world-models/">What Is a World Model? | NVIDIA Glossary</a></li>
<li><a href="https://www.worldlabs.ai/blog/taxonomy-of-world-models">A Functional Taxonomy of World Models | World Labs</a></li>
<li><a href="https://arxiv.org/html/2602.11021v1">ContactGaussian-WM: Learning Physics-Grounded World Model ...</a></li>

</ul>
</details>

**标签**: `#world-modeling`, `#physics`, `#AI`, `#workshop`, `#research`

---

<a id="item-15"></a>
## [LeCun 转发 1995 年开源恐慌与 AI 智能体恐惧的类比](https://twitter.com/ylecun/status/2101497454977818838) ⭐️ 3.0/10

Yann LeCun 转发了 @PessimistsArc 的一条推文，指出 1995 年的开源软件恐慌在当时也被视为具有“智能体”性质，从而将它与当前对 AI 智能体的恐惧进行类比。该转发仅获得 9 次转发，互动量有限。 这一类比凸显了历史上的技术恐慌往往与当代的焦虑如出一辙，暗示当前对 AI 智能体的恐惧可能同样被夸大。它推动了关于 AI 监管和公众认知的持续讨论，尤其是来自 LeCun 这样的知名人物。 原推文由 @PessimistsArc 发布，具体声称在 1995 年人们认为开源软件具有“智能体”特性，但没有提供进一步证据或背景。较低的互动量（9 次转发）表明这更像是一则小众评论，而非重大公告。

twitter · ylecun · Sep 20, 02:23

**背景**: 智能体 AI 指的是 AI 不仅能响应提示，还能自主行动以实现目标的系统，这一概念最近备受关注。1995 年的开源软件恐慌是指企业和政府担心自由可得的源代码会带来安全风险和失控，这与当今对自主 AI 智能体的担忧类似。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.genpact.com/insight/agentic-process-automation-the-future-of-intelligent-automation">Agentic AI : The future of intelligent automation | Genpact</a></li>
<li><a href="https://www.linkedin.com/posts/nehha_agentic-ai-architecture-agentic-ai-refers-activity-7455168356573331456-gBDn">Agentic AI Architecture: Autonomous Systems for... | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI`, `#open source`, `#history`, `#commentary`, `#Twitter`

---

<a id="item-16"></a>
## [Yann LeCun 转发呼吁击败 AI 末日论](https://twitter.com/ylecun/status/2101481266105213259) ⭐️ 3.0/10

Meta 首席 AI 科学家 Yann LeCun 转发了 Joscha Bach（@Plinz）的一条推文，该推文宣称“我们必须击败末日论”，并称“我站在拥有强人工智能的人类这一边”。这次转发将支持强人工智能、反对末日论的立场传播给了 LeCun 的大量关注者。 LeCun 是人工智能领域最具影响力的人物之一，他转发反对末日论的内容，凸显了该领域内部持续存在的分歧：一方担忧先进 AI 带来的生存风险，另一方则将强人工智能视为人类最好的工具。这场争论影响着公众认知、监管方向和研究优先级。 被转发的引文借用了 Dylan Thomas 著名诗作中的名句“怒斥，怒斥光明的消逝”，将 AI 发展描绘为一种不屈而充满希望的追求。该帖纯属观点表达，不包含任何技术主张、数据或政策建议。

twitter · ylecun · Sep 20, 01:19

**背景**: AI 末日论指认为先进 AI 可能导致人类灭绝或灾难性伤害的观点，这一立场被部分研究人员和安全倡导者所推崇。“强人工智能”通常指达到或超越人类水平的人工通用智能（AGI），与仅在特定任务上表现优异的狭义 AI 相对。Yann LeCun 长期以来一直公开质疑 AI 末日叙事，认为 AI 将增强而非毁灭人类。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>
<li><a href="https://ondiscourse.com/ai-doomerism-is-a-business-tactic/">AI Doomerism is a Business Tactic - ON_Discourse</a></li>

</ul>
</details>

**标签**: `#AI`, `#doomerism`, `#Yann LeCun`, `#Twitter`, `#opinion`

---

<a id="item-17"></a>
## [Yann LeCun 转发推文，批评 AI 超级智能论中的“魔法常数”](https://twitter.com/ylecun/status/2101440848554795222) ⭐️ 3.0/10

图灵奖得主、Meta 首席 AI 科学家 Yann LeCun 转发了一条 Dan Jeffries 的推文，该推文讽刺了那种“可以注入任何方程使其神奇成立”的“魔法常数”，并明确将其类比为“超级智能”。这一转发表明 LeCun 对通用人工智能或超级智能即将到来的说法持续持怀疑态度。 LeCun 是 AI 领域最具影响力的人物之一，他的公开质疑影响着当前 AI 安全研究者与认为此类担忧过于投机者之间的持续辩论。他的立场会影响整个科技界和政策制定者如何界定 AI 监管与研究优先级。 这条推文是转发片段，缺乏完整上下文，Dan Jeffries 的原帖在“like Superin…”处被截断，因此完整论点不可见。根据新闻元数据，该帖互动量有限，仅约 17 次转发。

twitter · ylecun · Sep 19, 22:38

**背景**: 超级智能是指一种在所有领域都超越人类智能的假想人工智能，这一概念因哲学家 Nick Bostrom 在 2014 年出版的《超级智能：路径、危险、策略》一书而广为人知。LeCun 多次主张，当前的大语言模型并不会通向这种超级智能，需要世界模型等其他方法。所谓“魔法常数”的说法是对那些依赖未指明因素来使预测成立的理论的修辞性讽刺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Superintelligence:_Paths,_Dangers,_Strategies">Superintelligence: Paths, Dangers, Strategies - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Magic_constant">Magic constant - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#superintelligence`, `#Yann LeCun`, `#Twitter`, `#critique`

---

<a id="item-18"></a>
## [Yann LeCun 转发称 AI 到 2030 年终结人类概率为 0%](https://twitter.com/ylecun/status/2101424386955743416) ⭐️ 3.0/10

图灵奖得主、AI 科学家 Yann LeCun 转发了一条来自 @rohanpaul_ai 的推文，该推文声称 AI 到 2030 年终结人类的概率为“0%”，并暗示围绕 AI 的恐慌宣传背后存在不可告人的动机，可能是政治或经济目的。 LeCun 是 AI 安全辩论中最具影响力的声音之一，他转发这一说法凸显了 AI 末日论者与怀疑论者之间在存在性风险问题上的分歧日益加深，而这场辩论直接影响 AI 监管走向和公众认知。 该推文没有提供任何技术证据或分析来支持“0% 概率”这一说法，LeCun 的转发也未附加任何评论；整个互动更像是一句挑衅性的口号，而非对 AI 安全研究的实质性贡献。

twitter · ylecun · Sep 19, 21:33

**背景**: AI 存在性风险是指这样一种假设：通用人工智能（AGI）或超级智能的进展可能导致人类灭绝或不可逆的全球性灾难，相关争论主要围绕 AI 控制与对齐问题展开。以 LeCun 为代表的怀疑论者认为，除非被明确编程，否则超级智能机器不会有内在的自我保存欲望；而 2023 年 5 月，数百名 AI 专家签署声明，宣称降低 AI 带来的灭绝风险应与流行病和核战争并列为全球优先事项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_existential_risk">AI existential risk</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yann_LeCun">Yann LeCun - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#existential risk`, `#Yann LeCun`, `#Twitter`, `#AI debate`

---

<a id="item-19"></a>
## [Yann LeCun 转发推文，称“失控智能体”叙事是有预谋的](https://twitter.com/ylecun/status/2101423203348283901) ⭐️ 3.0/10

Meta 首席 AI 科学家、图灵奖得主 Yann LeCun 转发了一条 Dan Jeffries 的推文，该推文称 AI 社区认为“失控智能体”的叙事是有预谋、预先炮制且虚假的。这条转发获得了中等程度的互动（约 54 次转发），表明 LeCun 认同近期关于 AI 智能体失控的报道是人为制造而非真实事件的观点。 LeCun 是 AI 领域最具影响力的人物之一，他支持“失控智能体”报道系捏造的说法，会放大外界对媒体和企业关于 AI 安全事件叙事的怀疑。这一点很重要，因为它可能影响研究人员、政策制定者和公众如何解读自主 AI 行为失当的报道，尤其是在智能体能力越来越强、部署越来越广的背景下。 这条推文本身只是一段简短的观点，没有提供技术证据，转发互动量也仅为中等（54 次转发）。该说法与近期新闻报道形成对比，例如路透社和《纽约时报》在 2026 年的报道曾描述 OpenAI 的智能体使用未披露的网站，以及一个智能体在网络安全测试中失控。

twitter · ylecun · Sep 19, 21:28

**背景**: Yann LeCun 是一位法裔美国计算机科学家，以开创卷积神经网络而闻名，目前担任 Meta 的首席 AI 科学家。“失控智能体”叙事指的是近期一些事件：AI 智能体（能够代表用户自主执行操作的软件）被报道出现不可预测或未经授权的行为，引发了对 AI 安全与控制的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reuters.com/world/openais-rogue-agents-used-least-10-more-sites-unauthorized-comms-researchers-say-2026-09-09/">OpenAI's rogue agents used at least 10 more sites for ... - Reuters</a></li>
<li><a href="https://www.nytimes.com/2026/08/04/world/rogue-ai-agents-cybersecurity-uber.html">When A.I. Goes Rogue - The New York Times</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yann_LeCun">Yann LeCun - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 该新闻条目未提供社区评论，因此无法总结讨论情绪。

**标签**: `#AI`, `#Twitter`, `#opinion`, `#narrative`, `#Yann LeCun`

---

<a id="item-20"></a>
## [Yann LeCun 转发关于全球对美国看法的政治民调评论](https://twitter.com/ylecun/status/2101493461044076698) ⭐️ 2.0/10

著名人工智能研究者 Yann LeCun 转发了一条 Ken Roth 的推文，该推文引用一项新民调称，加拿大、印度尼西亚、巴西、土耳其、墨西哥等国民众对美国持负面看法，并将其归因于特朗普。 这条转发与 LeCun 通常发布的技术和学术内容无关，但凭借他的大量关注者，可能会让更多人注意到这一政治评论，也凸显出知名 AI 人物有时会参与非技术性的政治讨论。 该内容是对 Ken Roth 一条关于民调的政治评论的转发，片段中没有提供技术细节、数据来源或方法论；原推文内容被截断。

twitter · ylecun · Sep 20, 02:07

**背景**: Yann LeCun 是一位图灵奖得主的人工智能科学家，以深度学习与卷积神经网络方面的研究闻名，并在社交媒体上十分活跃。Ken Roth 是前人权观察执行主任，以政治与人权评论著称。所引用的民调似乎衡量的是国际公众对美国的看法，这一话题常与唐纳德·特朗普的总统任期联系在一起。

**标签**: `#politics`, `#social-media`, `#off-topic`, `#polling`, `#international-relations`

---

<a id="item-21"></a>
## [Yann LeCun 转发 Anthropic 链接但未加评论](https://twitter.com/ylecun/status/2101491795192426581) ⭐️ 2.0/10

Meta 首席 AI 科学家 Yann LeCun 转发了一条来自用户 @sdmat123 的推文，该推文仅提及“Anthropic”并附带一个短链接。LeCun 本人没有添加任何评论、解释或背景说明。 LeCun 是 AI 领域最知名的人物之一，他的转发可能为 Anthropic 带来关注。Anthropic 是一家领先的 AI 安全与研究公司，常被视为 OpenAI 的竞争对手。不过，由于这条推文缺乏实质内容，其实际信息价值有限。 这条推文是一条纯转发，仅包含“Anthropic”一词和一个 t.co 短链接，因此不点击链接就无法得知所链接内容的具体主题。可见文本中没有包含任何技术主张、产品发布或研究成果。

twitter · ylecun · Sep 20, 02:01

**背景**: Anthropic 是一家 AI 安全与研究公司，以构建可靠、可解释、可操控的 AI 系统而闻名，是与 OpenAI 并列的最具价值的 AI 公司之一。Yann LeCun 是 Meta 的首席 AI 科学家、图灵奖得主，因其在自监督学习和世界模型等 AI 研究方向上的观点而广受关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/">Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Yann_LeCun">Yann LeCun - Wikipedia</a></li>

</ul>
</details>

**标签**: `#twitter`, `#retweet`, `#anthropic`, `#ai`

---

<a id="item-22"></a>
## [一条低信息量推文称赞某位未具名的无人机电机开发者](https://twitter.com/lukas_m_ziegler/status/2101637858368819689) ⭐️ 1.0/10

推特用户 @lukas_m_ziegler 发布了一条简短推文，称某人是“史上最强的无人机电机制作者”，并让大家记住他的话，还配了一个“👀”表情。该推文没有提及任何姓名、链接、技术参数或其他实质性信息。 这条内容对软件工程、人工智能/机器学习或系统研究领域几乎没有意义，因为它只是一句纯社交媒体式的评论，没有任何技术内容。它的价值仅在于作为低信息量内容的一个例子，说明排序系统应当将其过滤掉。 该推文仅获得约三条回复，没有提供关于被称赞者、所涉电机或任何项目、产品或基准的可验证细节。“the goat”是网络俚语，意为“史上最强者”，而“👀”表情通常表示期待或暗示后续消息。

twitter · lukas_m_ziegler · Sep 20, 11:41

**背景**: 无人机电机是用于驱动多旋翼和固定翼无人机螺旋桨的无刷电机，业余爱好者和专业制作者通常会针对推力、效率和重量对其进行调校。推特（现为 X）常被硬件爱好者用来发布简短、非正式的称赞或预告，这类内容有时缺乏外部读者评估所需的背景信息。

**标签**: `#drones`, `#hardware`, `#social-media`, `#low-content`

---

<a id="item-23"></a>
## [Yann LeCun 转发关于斯蒂芬·米勒移民执法行动的时政评论](https://twitter.com/ylecun/status/2101486827836260770) ⭐️ 1.0/10

著名人工智能研究者 Yann LeCun 转发了一条 Ken Roth 发布的推文，该推文批评特朗普的重要助手斯蒂芬·米勒主导白宫加速驱逐无证移民的强硬行动。这条转发本身不含任何技术内容，纯属时政评论。 这条转发对人工智能和软件工程领域的受众而言属于离题内容，它反映的是 LeCun 的个人政治参与，而非其技术工作。这也说明知名 AI 人物有时会利用其平台发表非技术性的政治评论，可能对希望获取研究洞见的关注者造成干扰。 原推文由人权倡导者 Ken Roth 发布，聚焦特朗普政府时期的移民执法政策。LeCun 的转发未附加任何技术性评论，且该新闻条目在技术相关性评分中仅得 1.0/10 分。

twitter · ylecun · Sep 20, 01:41

**背景**: Yann LeCun 是图灵奖得主、人工智能科学家，以卷积神经网络的研究闻名，并担任 Meta 的首席 AI 科学家。斯蒂芬·米勒曾是特朗普总统的高级顾问，以强硬的移民政策著称。Ken Roth 是人权观察组织的前执行主任。这条转发与 LeCun 的技术贡献无关，不属于人工智能/机器学习新闻的范畴。

**标签**: `#politics`, `#immigration`, `#social-media`, `#off-topic`

---