---
layout: default
title: "Horizon Summary: 2026-07-19 (ZH)"
date: 2026-07-19
lang: zh
---

> From 27 items, 17 important content pieces were selected

---

1. [LightTact：无需形变即可检测触摸的触觉传感器](#item-1) ⭐️ 8.0/10
2. [LingBot-Map：单摄像头实时 3D 重建](#item-2) ⭐️ 8.0/10
3. [Google DeepMind 更新 Weather Lab，推出 AI 天气模型](#item-3) ⭐️ 7.0/10
4. [Kimi K3：2.8 万亿参数中国模型声称超越 Anthropic](#item-4) ⭐️ 7.0/10
5. [Pipecat 开源框架颠覆语音 AI](#item-5) ⭐️ 7.0/10
6. [Tripteron 并联轴机械臂展示](#item-6) ⭐️ 6.0/10
7. [用摄像头和 YOLO 自制液位传感器](#item-7) ⭐️ 6.0/10
8. [LeCun 反驳称开源权重模型是减速主义者的说法](#item-8) ⭐️ 6.0/10
9. [吴恩达联合 Cerebras 推出 LLM 课程](#item-9) ⭐️ 6.0/10
10. [Claude Code 每周限额提升 50%延长至 8 月 19 日](#item-10) ⭐️ 5.0/10
11. [关于 Anthropic 收购 Physical Intelligence 的猜测](#item-11) ⭐️ 4.0/10
12. [AI 安全预测被批评为不准确](#item-12) ⭐️ 3.0/10
13. [关于圈出 Transformer 部分的玩笑](#item-13) ⭐️ 3.0/10
14. [转发批评特朗普在选举安全上的言行](#item-14) ⭐️ 2.0/10
15. [Yann LeCun 转发模糊政治声明](#item-15) ⭐️ 2.0/10
16. [Yann LeCun 无上下文转发 IntuitMachine 链接](#item-16) ⭐️ 2.0/10
17. [斯坦福 AI 实验室转发祝贺 ProgramBench 成果](#item-17) ⭐️ 2.0/10

---

<a id="item-1"></a>
## [LightTact：无需形变即可检测触摸的触觉传感器](https://twitter.com/lukas_m_ziegler/status/2078500834787185051) ⭐️ 8.0/10

研究人员推出了 LightTact，一种基于光学原理的视觉-触觉指尖传感器，通过环境光阻断光学配置，无需物理形变即可检测轻微接触。 这一突破克服了传统触觉传感器依赖形变的根本限制，使机器人能够感知轻触、水、奶油或软膜，扩展了机器人、触觉和人机交互的能力。 LightTact 实现了像素级接触分割，对材料属性、接触力、表面外观和环境光照具有鲁棒性，并提供自然对齐的视觉-触觉多模态信号，适用于机器人学习。

twitter · lukas_m_ziegler · Jul 18, 15:23

**背景**: 传统触觉传感器（如压阻式或电容式）通过软表面形变来测量接触，这限制了它们检测轻触或非形变接触（如触摸水或软膜）的能力。LightTact 采用光学方法，使接触直接可见，无需形变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.20591">[2512.20591] LightTact: A Visual-Tactile Fingertip Sensor for Deformation-Independent Contact Sensing</a></li>
<li><a href="https://arxiv.org/html/2512.20591v1">LightTact: A Visual–Tactile Fingertip Sensor for Deformation-Independent Contact Sensing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tactile_sensor">Tactile sensor - Wikipedia</a></li>

</ul>
</details>

**标签**: `#tactile sensing`, `#robotics`, `#haptics`, `#sensor technology`

---

<a id="item-2"></a>
## [LingBot-Map：单摄像头实时 3D 重建](https://twitter.com/lukas_m_ziegler/status/2078054148231069793) ⭐️ 8.0/10

Robbyant 团队开源了 LingBot-Map，这是一个前馈式 3D 基础模型，能够通过单个普通摄像头以接近 20 FPS 的速度实时重建场景。 这一突破使得单摄像头实时 3D 建图成为可能，对机器人、AR/VR 和自主导航至关重要，而开源发布则加速了研究和实际应用。 LingBot-Map 采用几何上下文 Transformer，在流式框架中统一了坐标定位、密集几何线索和长程漂移校正，从视频流中恢复相机姿态和场景结构。

twitter · lukas_m_ziegler · Jul 17, 09:48

**背景**: 传统的单摄像头 3D 重建通常需要离线处理或多个视角，限制了实时应用。LingBot-Map 是一种前馈模型，顺序处理流式视频帧，随着相机移动更新地图，无需后处理即可实现实时性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Robbyant/lingbot-map">GitHub - Robbyant/ lingbot - map : A feed-forward 3 D foundation model ...</a></li>
<li><a href="https://www.progressiverobot.com/2026/04/25/lingbot-map/">LingBot - Map : Streaming 3 D Reconstruction for Robotics — Explained</a></li>
<li><a href="https://news.aibase.com/news/27181">AntGroup Lingbo Technology Opensources LingBot-Map: Real - Time ...</a></li>

</ul>
</details>

**标签**: `#3D reconstruction`, `#computer vision`, `#open source`, `#real-time mapping`, `#robotics`

---

<a id="item-3"></a>
## [Google DeepMind 更新 Weather Lab，推出 AI 天气模型](https://twitter.com/GoogleDeepMind/status/2078150319016382762) ⭐️ 7.0/10

Google DeepMind 宣布对 Weather Lab 进行重大更新，这是一个用于分享其 AI 天气模型（包括最先进的 WeatherNext 2 系列）的交互式网站。 此次更新推动了 AI 驱动的天气预报，其性能可超越传统方法，并改善对热带气旋等极端事件的预测，有望挽救生命并减少经济损失。 WeatherNext 2 是一系列能够高精度预测风速、降水和气压等变量的模型。Weather Lab 平台允许用户交互式地探索这些 AI 模型。

twitter · GoogleDeepMind · Jul 17, 16:10

**背景**: AI 天气模型利用机器学习，比传统数值天气预报更快、更准确地分析海量数据。Google DeepMind 的 WeatherNext 2 在真实世界测试中表现出卓越的准确性，例如对飓风艾琳的预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/science/weathernext/">WeatherNext 2 is our most accurate AI weather forecasting technology.</a></li>
<li><a href="https://theoutpost.ai/news-story/google-s-ai-weather-model-outperforms-traditional-forecasts-for-hurricane-erin-19539/">Google 's AI Weather Model Outperforms Traditional Forecasts in...</a></li>

</ul>
</details>

**标签**: `#AI`, `#weather modeling`, `#Google DeepMind`

---

<a id="item-4"></a>
## [Kimi K3：2.8 万亿参数中国模型声称超越 Anthropic](https://twitter.com/ylecun/status/2078577113460826312) ⭐️ 7.0/10

一条推文声称，来自 Moonshot AI 的 2.8 万亿参数开源权重中国模型 Kimi K3，在基于人类偏好的评估中，于网页开发任务上超越了 Anthropic 的模型。 如果得到验证，这将标志着中国开源 AI 模型的一个重要里程碑，挑战 Anthropic 等美国前沿实验室的主导地位，并可能重塑大型语言模型的竞争格局。 Kimi K3 采用混合专家架构，拥有 896 个专家，每个 token 仅激活 16 个，因此尽管总参数达 2.8 万亿，活跃参数仅约 500 亿。它支持 100 万 token 的上下文窗口和原生视觉理解。

twitter · ylecun · Jul 18, 20:26

**背景**: Kimi 是中国公司 Moonshot AI 开发的一系列大型语言模型。首个版本于 2023 年发布，支持 128K 上下文窗口。Kimi K2 于 2025 年 7 月以开源权重发布，Kimi K3 是最新的旗舰模型。关于超越 Anthropic 模型的声明尚未得到独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>
<li><a href="https://artificialanalysis.ai/models/kimi-k3">Kimi K3 - Intelligence, Performance & Price Analysis</a></li>

</ul>
</details>

**标签**: `#AI`, `#large language models`, `#Anthropic`, `#Chinese AI`

---

<a id="item-5"></a>
## [Pipecat 开源框架颠覆语音 AI](https://twitter.com/RodmanAi/status/2078335163705291253) ⭐️ 7.0/10

Pipecat 是一个用于构建实时语音和多模态对话智能体的开源 Python 框架，它提供了完整的语音技术栈，包括语音识别、AI 处理、语音响应、流式对话以及 WebRTC/WebSockets 支持，据称此举消除了语音 AI 领域的竞争壁垒。 这使语音 AI 开发民主化，个人开发者和小团队无需依赖专有平台即可构建复杂的实时语音智能体，有望加速行业创新并降低成本。 Pipecat 使用 Python 构建，支持与多种 AI 模型和服务集成，处理实时音频流和多模态交互的复杂管道。它在 GitHub 上的 pipecat-ai 组织下开源。

twitter · RodmanAi · Jul 18, 04:24

**背景**: 构建实时语音 AI 智能体传统上需要大量工程工作来集成语音转文本、AI 推理、文本转语音以及 WebRTC 等低延迟流式协议。Pipecat 将这种复杂性抽象到一个框架中，类似于 Web 框架简化了 Web 开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pipecat-ai/pipecat">GitHub - pipecat -ai/ pipecat : Open Source framework for voice and...</a></li>
<li><a href="https://docs.pipecat.ai/">Build voice and multimodal AI agents with the Pipecat ecosystem.</a></li>
<li><a href="https://medium.com/@yanivbohbot5/beyond-the-chatbot-mastering-real-time-voice-ai-with-pipecat-bd0b2bf0bbc4">Beyond the Chatbot: Mastering Real-Time Voice AI with Pipecat</a></li>

</ul>
</details>

**标签**: `#voice AI`, `#open-source`, `#framework`, `#real-time`

---

<a id="item-6"></a>
## [Tripteron 并联轴机械臂展示](https://twitter.com/lukas_m_ziegler/status/2078108597628682524) ⭐️ 6.0/10

Lukas Ziegler 在视频中展示了一种 tripteron 并联轴机械臂，它利用线性平台实现精确的 XYZ 运动，其设计基于拉瓦尔大学的运动学概念。 该演示突显了一种优雅的机械设计，以简洁的方式实现了高精度和高稳定性，可能为 3D 打印或拾放机器人等应用带来低成本、高性能的 XYZ 平台。 Tripteron 是一种三自由度线性机械臂，其三个输入执行器朝向同一方向，从而在该轴上实现几乎无限的行程。它使用并联运动链来移动平台在 X、Y 和 Z 方向运动。

twitter · lukas_m_ziegler · Jul 17, 13:24

**背景**: 并联机械臂使用多个支链将动平台连接到基座，具有高刚度和高精度。Tripteron 是一种笛卡尔并联机械臂，其支链与笛卡尔坐标轴对齐，简化了控制以及执行器位置到末端执行器坐标的映射。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cartesian_parallel_manipulators">Cartesian parallel manipulators - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/posts/zieglerr_this-is-not-a-mechanical-frog-its-a-activity-7399011769077186560-CBB6">This is not a mechanical frog! It's a tripteron , a parallel - axis ...</a></li>
<li><a href="https://grabcad.com/library/parallel-axis-tripteron-1">Parallel Axis Tripteron | 3D CAD Model Library | GrabCAD</a></li>

</ul>
</details>

**社区讨论**: LinkedIn 上的评论称赞该设计的优雅和稳定性，有用户询问其在刚度和精度上与 Delta 机器人相比如何。没有进一步的讨论。

**标签**: `#robotics`, `#mechanical engineering`, `#kinematics`, `#parallel manipulator`

---

<a id="item-7"></a>
## [用摄像头和 YOLO 自制液位传感器](https://twitter.com/lukas_m_ziegler/status/2078025565907345869) ⭐️ 6.0/10

一个 DIY 液位传感器利用摄像头和 Python 构建，采用 YOLO 进行实时瓶子检测，并通过 HSV 颜色分析测量液位高度，同时具备倾斜校正功能。 该项目展示了如何用廉价的计算机视觉技术替代昂贵的工业传感器来完成液位监测等实际任务，使自动化对爱好者和小型企业更加可及。 该系统使用 YOLO 实时检测瓶子，然后应用 HSV 颜色空间分析，通过区分液体颜色与瓶子背景来确定液位高度。倾斜校正功能补偿传送带上瓶子的倾斜。

twitter · lukas_m_ziegler · Jul 17, 07:54

**背景**: YOLO（You Only Look Once）是一种实时目标检测系统，只需一次神经网络前向传播即可识别物体。HSV（色调、饱和度、明度）是一种颜色空间，它将颜色信息与亮度分离，便于在不同光照条件下分析颜色。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/YOLO_(object_detection)">YOLO (object detection)</a></li>
<li><a href="https://en.wikipedia.org/wiki/HSL_and_HSV">HSL and HSV - Wikipedia</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#YOLO`, `#DIY`, `#Python`, `#sensor`

---

<a id="item-8"></a>
## [LeCun 反驳称开源权重模型是减速主义者的说法](https://twitter.com/ylecun/status/2078584184524705987) ⭐️ 6.0/10

Yann LeCun 转发了 Martin Casado 的一条推文，该推文声称“开源权重模型本质上是减速主义者”，LeCun 称这是一个严重错误的说法，且没有任何支持论据。 这一交锋凸显了 AI 领域关于开源权重模型在加速或减缓 AI 进展方面作用的持续辩论，知名人物各持己见。 Martin Casado 的原始说法将开源权重模型标记为“减速主义者”，该术语源自有效加速主义运动，反对谨慎的 AI 发展。LeCun 的反驳简短，缺乏详细的反对论据。

twitter · ylecun · Jul 18, 20:54

**背景**: 开源权重模型是指其训练参数（权重）公开发布的 AI 模型，允许任何人下载、使用和修改。“减速主义者”（或“decels”）一词被加速主义者用来批评那些主张更慢、更谨慎的 AI 发展（通常带有护栏）的人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Effective_accelerationism">Effective accelerationism - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#open-weight models`, `#debate`

---

<a id="item-9"></a>
## [吴恩达联合 Cerebras 推出 LLM 课程](https://twitter.com/AndrewYNg/status/2078144569594761591) ⭐️ 6.0/10

吴恩达宣布推出一门新短期课程，教授如何使用专为快速推理设计的 Cerebras 硬件构建 LLM 应用，由 Zhenny Zheng、Sebastian Duerr 和 MilksandMatcha 授课。 该课程满足了 LLM 推理速度的关键需求，这对于需要低延迟和高吞吐量的实时应用（如智能体工作流）至关重要。 该课程在 DeepLearning.AI 上托管，专注于推理优化硬件，通过减少数据移动，实现比典型 GPU 设置快数倍的 token 生成速度。

twitter · AndrewYNg · Jul 17, 15:47

**背景**: 大型语言模型（LLM）逐 token 生成文本，推理速度常受内存带宽限制。Cerebras 使用晶圆级芯片将数据保留在片上，大幅降低延迟。本课程教授开发者如何利用此类硬件构建响应迅速的 LLM 应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.deeplearning.ai/courses/fast-llm-inference-with-cerebras/lesson/a4u81f/introduction">Fast LLM Inference with Cerebras - DeepLearning.AI</a></li>
<li><a href="https://www.cerebras.ai/">Cerebras is the go-to platform for fast and effortless AI training.</a></li>

</ul>
</details>

**标签**: `#LLM`, `#inference`, `#course`, `#hardware`

---

<a id="item-10"></a>
## [Claude Code 每周限额提升 50%延长至 8 月 19 日](https://twitter.com/ClaudeDevs/status/2078511173759324328) ⭐️ 5.0/10

Anthropic 宣布，Claude Code 的每周使用限额将保持提升 50%，有效期延长至 2026 年 8 月 19 日，适用于所有 Pro、Max、Team 和基于座位的 Enterprise 用户。 此次延期为付费用户提供了更多 AI 辅助编程任务的容量，可能在促销期间提升生产力和用户满意度。 50%的提升适用于每周上限，而非 5 小时滚动速率限制，未使用的容量不会结转到下一周。

twitter · ClaudeDevs · Jul 18, 16:04

**背景**: Claude Code 是 Anthropic 推出的 AI 编程助手，适用于付费计划。它采用两级速率系统：短期滚动限制（例如 5 小时）和每周上限。50%的提升最初于 2026 年 7 月宣布，现已延长至 8 月中旬。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.morphllm.com/claude-code-usage-limits">Claude Code Usage Limits (2026): 5-Hour Caps Doubled May...</a></li>
<li><a href="https://apidog.com/blog/claude-code-weekly-limits-50-percent-increase-july-2026/">Claude Code Weekly Limits Just Jumped 50% Through July 13: What...</a></li>
<li><a href="https://www.frankx.ai/blog/claude-code-pricing-explained-2026">Claude Code Pricing Explained 2026: Pro vs Max 5x vs Max... | FrankX</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI tools`, `#pricing`, `#announcement`

---

<a id="item-11"></a>
## [关于 Anthropic 收购 Physical Intelligence 的猜测](https://twitter.com/lukas_m_ziegler/status/2078610235321639286) ⭐️ 4.0/10

一条推文猜测，如果关于 Anthropic 收购 Physical Intelligence 的传言属实，那么 OpenAI 可能会收购哪家公司作为回应。 这一猜测凸显了 AI 行业的竞争动态，像 Anthropic 和 OpenAI 这样的主要参与者可能通过收购来增强自身能力，尤其是在物理 AI 和机器人等领域。 Anthropic 是一家专注于 AI 安全的公司，以其 Claude 模型闻名，而 Physical Intelligence 是一家旨在将通用 AI 引入物理世界的初创公司。该推文纯属猜测，没有确认的消息来源。

twitter · lukas_m_ziegler · Jul 18, 22:37

**背景**: Anthropic 由前 OpenAI 员工创立，是一家专注于安全和大型语言模型的领先 AI 公司。Physical Intelligence 是一家致力于通用物理 AI 的机器人和 AI 公司。AI 领域的收购很常见，因为公司寻求扩大技术优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic</a></li>
<li><a href="https://www.pi.website/">Physical Intelligence (π)</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#acquisitions`, `#speculation`

---

<a id="item-12"></a>
## [AI 安全预测被批评为不准确](https://twitter.com/ylecun/status/2078573589826039837) ⭐️ 3.0/10

Yann LeCun 转发了一条帖子，声称 AI 安全社区的预测没有一个正确，而实际问题更加平凡。 这一批评挑战了 AI 安全预测的可信度，可能影响公众和研究焦点转向更直接、实际的问题。 该转发缺乏具体例子或证据来支持这一说法，使其成为模糊的观点而非实质性的分析。

twitter · ylecun · Jul 18, 20:12

**背景**: AI 安全是一个关注确保 AI 系统安全开发和部署的领域，通常侧重于长期风险。批评者认为一些预测过于推测性，分散了对当前问题的注意力。

**标签**: `#AI safety`, `#critique`, `#Twitter`

---

<a id="item-13"></a>
## [关于圈出 Transformer 部分的玩笑](https://twitter.com/ylecun/status/2078362408930705903) ⭐️ 3.0/10

Yann LeCun 转发了 Sasha Rush 的一条推文，开玩笑说圈出了'k3'的所有 Transformer 部分，并自称是个输不起的人。 这是一条缺乏技术内容的个人评论，不太可能对 AI 社区产生影响。 推文提到了'k3'并包含一个链接，但上下文不明确，内容是关于输不起的玩笑。

twitter · ylecun · Jul 18, 06:13

**标签**: `#transformer`, `#twitter`, `#low-value`

---

<a id="item-14"></a>
## [转发批评特朗普在选举安全上的言行](https://twitter.com/ylecun/status/2078584303735164985) ⭐️ 2.0/10

Yann LeCun 转发了 Ken Roth 的批评，指出特朗普曾呼吁修复电子投票系统的漏洞，但在其第二任期内却一直在削弱选举安全。 这凸显了特朗普在选举安全立场上的明显矛盾，虽然这是一个政治敏感话题，但与人工智能或软件工程等技术领域关联度很低。 该推文仅为转发，没有附加技术分析或数据，原始来源是人权倡导者 Ken Roth。

twitter · ylecun · Jul 18, 20:54

**背景**: 选举安全涉及保护投票系统免受篡改和网络攻击。争论的焦点通常在于电子投票机是否安全，以及相关政策是加强还是削弱了防护措施。

**标签**: `#politics`, `#election security`

---

<a id="item-15"></a>
## [Yann LeCun 转发模糊政治声明](https://twitter.com/ylecun/status/2078583891820937621) ⭐️ 2.0/10

Yann LeCun 转发了 Dan_Jeffries1 的一条推文，该推文提出在权力集中与权力扩散之间做出二元选择，未作进一步阐述。 这条推文缺乏技术深度，属于泛泛的政治表态，因此对 AI 或科技界影响极小。 该推文仅获得 14 次转发，且内容被截断，表明参与度低且缺乏实质性讨论。

twitter · ylecun · Jul 18, 20:53

**标签**: `#politics`, `#centralization`, `#power`

---

<a id="item-16"></a>
## [Yann LeCun 无上下文转发 IntuitMachine 链接](https://twitter.com/ylecun/status/2078579853939421297) ⭐️ 2.0/10

Yann LeCun 转发了一条来自 IntuitMachine 的帖子，该帖子仅包含一个链接，未添加任何评论或上下文。 这条转发信息价值低，未能提供关于 LeCun 观点或当前研究的任何见解。 该推文的参与度评分仅为 2.0/10，且链接无法访问，因此无法评估其内容的相关性。

twitter · ylecun · Jul 18, 20:37

**标签**: `#retweet`, `#low-value`, `#twitter`

---

<a id="item-17"></a>
## [斯坦福 AI 实验室转发祝贺 ProgramBench 成果](https://twitter.com/StanfordAILab/status/2078645380930249075) ⭐️ 2.0/10

斯坦福 AI 实验室转发了@KLieret 的一条推文，祝贺在 ProgramBench 上取得优异成绩，但未提供具体细节。 ProgramBench 是一个评估语言模型从二进制文件重建命令行程序能力的基准，对逆向工程和代码理解意义重大。此次转发表明该领域进展获得了认可。 该转发未包含额外背景或数据，仅是一句简短的祝贺。ProgramBench 的任务涵盖从小型到超大型代码仓库，测试模型的程序重建能力。

twitter · StanfordAILab · Jul 19, 00:57

**背景**: ProgramBench 是一个基准测试，评估语言模型在给定可执行二进制文件和行为规范的情况下重建命令行程序的能力。它包含从小型到大型代码库的不同难度任务。该基准托管在 valis.ai 和 programbench.com 上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vals.ai/benchmarks/programbench">ProgramBench</a></li>
<li><a href="https://programbench.com/?ref=boostedlaunch.com">ProgramBench evaluates whether language models can rebuild...</a></li>

</ul>
</details>

**标签**: `#retweet`, `#congratulations`, `#ProgramBench`

---