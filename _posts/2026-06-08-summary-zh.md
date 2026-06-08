---
layout: default
title: "Horizon Summary: 2026-06-08 (ZH)"
date: 2026-06-08
lang: zh
---

> From 20 items, 15 important content pieces were selected

---

1. [代尔夫特理工大学展示端到端神经网络无人机竞速](#item-1) ⭐️ 8.0/10
2. [Yann LeCun 转推称赞一篇“疯狂”的论文](#item-2) ⭐️ 8.0/10
3. [一周内发布 25+个开放权重 AI 模型](#item-3) ⭐️ 8.0/10
4. [NVIDIA 免费提供 120 多个 AI 模型一年访问权限](#item-4) ⭐️ 8.0/10
5. [苏黎世联邦理工的 ViserDex 实现仅用 RGB 的灵巧手控制](#item-5) ⭐️ 7.0/10
6. [Malik 给进入机器人领域的计算机视觉研究者建议](#item-6) ⭐️ 7.0/10
7. [缆绳驱动机器人在硕士论文演示中玩杂耍](#item-7) ⭐️ 6.0/10
8. [SpaceX 发射 21 颗星链和 2 颗星盾卫星](#item-8) ⭐️ 6.0/10
9. [生成模型需要非配对数据翻译以服务科学](#item-9) ⭐️ 6.0/10
10. [人形机器人 vs 专用机器人：现实检验](#item-10) ⭐️ 5.0/10
11. [谷歌 AI 内存压缩说法缺乏证据](#item-11) ⭐️ 3.0/10
12. [10 块 NVIDIA GPU 月入 1.8 万美元：算力租赁轶事](#item-12) ⭐️ 3.0/10
13. [转发批评白宫网页内容](#item-13) ⭐️ 2.0/10
14. [伯克利 AI 转发无上下文的链接](#item-14) ⭐️ 2.0/10
15. [Yann LeCun 转发 David Sarnoff 传记](#item-15) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [代尔夫特理工大学展示端到端神经网络无人机竞速](https://twitter.com/lukas_m_ziegler/status/2063192750850232422) ⭐️ 8.0/10

代尔夫特理工大学展示了一种完全端到端的神经网络无人机竞速方案，该方案直接将摄像头像素映射到电机指令，无需卡尔曼滤波器或传统计算机视觉。 这种方法简化了无人机控制流程，有望实现更快、更自适应的自主飞行，并可能应用于太空任务及其他机器人领域。 该神经网络通过行为克隆从专家示范中训练而成，其工作基于此前神经控制器在无人机竞速中击败人类冠军的研究。

twitter · lukas_m_ziegler · Jun 6, 09:34

**背景**: 传统无人机控制依赖卡尔曼滤波器进行状态估计，并利用计算机视觉提取特征，这些方法计算成本高且需要精细调参。端到端神经网络直接从原始传感器数据学习控制输出，可能提供更高的效率和鲁棒性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.esa.int/Enabling_Support/Space_Engineering_Technology/Drone_racing_prepares_neural-network_AI_for_space">ESA - Drone racing prepares neural-network AI for space</a></li>
<li><a href="https://mavlab.tudelft.nl/end-to-end-neural-network-based-optimal-quadcopter-control-2/">End-to-end Neural Network Based Optimal Quadcopter Control - MAVLab</a></li>

</ul>
</details>

**标签**: `#end-to-end learning`, `#neural networks`, `#drone racing`, `#robotics`, `#computer vision`

---

<a id="item-2"></a>
## [Yann LeCun 转推称赞一篇“疯狂”的论文](https://twitter.com/ylecun/status/2063664356571660716) ⭐️ 8.0/10

Yann LeCun 转发了 Miles Cranmer 对一篇论文的热烈推荐，称其“疯狂”并表示喜爱，但未提供更多细节。 作为 AI 领域的领军人物，LeCun 的推荐表明该论文可能代表一项重大突破或极具创新性的研究，可能影响机器学习的发展方向。 推文中包含论文链接（https://t.co/DP8OR5NJf2）和一张图片（https://t.co/rl4Rmr0FhJ），但未说明具体内容。从该帖子中无法得知论文的确切标题和作者。

twitter · ylecun · Jun 7, 16:48

**背景**: Yann LeCun 是图灵奖得主、Meta 首席 AI 科学家，以深度学习方面的开创性工作闻名。Miles Cranmer 是剑桥大学的研究员，以 AI 驱动的科学发现著称。此类人物的转推通常会放大重要研究的影响力。

**社区讨论**: 该推文没有可用的社区评论。高转发量（1260 次）表明兴趣浓厚，但具体反应未知。

**标签**: `#AI`, `#research`, `#paper`, `#machine learning`

---

<a id="item-3"></a>
## [一周内发布 25+个开放权重 AI 模型](https://twitter.com/ylecun/status/2063611471167144340) ⭐️ 8.0/10

Yann LeCun 转发了一条推文，承认一周内发布了超过 25 个值得关注的开放权重 AI 模型，标志着开放 AI 活动空前激增。 这凸显了开放权重模型发布的加速趋势，使先进 AI 的获取更加民主化，并促进了整个生态系统的快速创新。 开放权重模型提供最终训练好的参数，使研究人员和开发者能够微调和部署它们，但可能不包含完整的训练代码或数据。

twitter · ylecun · Jun 7, 13:18

**背景**: 开放权重模型是指其训练参数（权重和偏置）公开发布的 AI 模型，允许他人运行、微调和在此基础上构建。与完全开源模型不同，开放权重发布可能不包含训练代码或数据集。本周的密集发布包括 OpenAI 的 gpt-oss-120b 以及各种专注于编码的模型，如 GLM-5.1 和 MiniMax M3。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://www.ai21.com/glossary/foundational-llm/open-weights-model/">What is an Open-Weights Model? | AI21</a></li>
<li><a href="https://openai.com/index/introducing-gpt-oss/">Introducing gpt-oss | OpenAI</a></li>

</ul>
</details>

**标签**: `#open-source`, `#AI`, `#machine learning`, `#models`

---

<a id="item-4"></a>
## [NVIDIA 免费提供 120 多个 AI 模型一年访问权限](https://twitter.com/RodmanAi/status/2063653720458731636) ⭐️ 8.0/10

NVIDIA 宣布免费提供超过 120 个 AI 模型的访问权限，速率限制为每分钟 40 次请求，有效期一整年，无需信用卡或付款。 此举大大降低了开发者和创作者尝试最先进 AI 模型的门槛，可能加速整个行业对 AI 的采用和创新。 该优惠包括 120 多个模型、每分钟 40 次请求和一年访问权限，完全免费，无隐藏费用或信用卡要求。

twitter · RodmanAi · Jun 7, 16:06

**背景**: AI 模型通常需要大量计算资源，并常通过付费 API 或订阅服务提供。作为领先的 GPU 制造商，NVIDIA 通过其 NGC 目录等平台提供 AI 模型。此免费套餐允许开发者在无需前期投资的情况下测试和集成 AI 功能。

**标签**: `#NVIDIA`, `#AI models`, `#free access`, `#developer tools`

---

<a id="item-5"></a>
## [苏黎世联邦理工的 ViserDex 实现仅用 RGB 的灵巧手控制](https://twitter.com/lukas_m_ziegler/status/2063678741386342895) ⭐️ 7.0/10

苏黎世联邦理工学院的研究人员开发了 ViserDex，这是一个仅使用单目 RGB 摄像头和 3D 高斯泼溅即可实现手中物体重新定向的仿真到现实框架。 这项工作降低了对灵巧操作的传感器要求，使其在深度传感器可能不可用或不可靠的真实机器人应用中更加实用。 ViserDex 集成了 3D 高斯泼溅以弥合视觉仿真到现实的差距，使得在仿真中训练的策略仅凭 RGB 输入即可迁移到真实机器人上。

twitter · lukas_m_ziegler · Jun 7, 17:45

**背景**: 手中物体重新定向是指在机器人手中旋转或重新定位物体而不掉落的任务。3D 高斯泼溅是一种体积渲染技术，可以从多张图像创建高质量的 3D 表示，实现新视角合成。仿真到现实迁移是机器人学中的一个常见挑战，即在仿真中训练的策略必须适应真实世界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.11138">[2604.11138] ViserDex : Visual Sim - to - Real for Robust Dexterous...</a></li>
<li><a href="https://rffr.leggedrobotics.com/works/viserdex/">ViserDex : Visual Sim - to - Real for Robust Dexterous In-hand...</a></li>
<li><a href="https://en.wikipedia.org/wiki/3D_Gaussian_splatting">3D Gaussian splatting</a></li>

</ul>
</details>

**标签**: `#robotics`, `#sim-to-real`, `#3D Gaussian Splatting`, `#dexterous manipulation`, `#computer vision`

---

<a id="item-6"></a>
## [Malik 给进入机器人领域的计算机视觉研究者建议](https://twitter.com/ylecun/status/2063331709798523343) ⭐️ 7.0/10

Jitendra Malik 在 Twitter 上给进入机器人领域的计算机视觉研究者提出了主动建议，警告不要过度关注某些方面。 这一建议意义重大，因为它指导了计算机视觉与机器人学这一日益交叉的领域，可能影响研究重点并帮助避免常见陷阱。 该推文由 Yann LeCun 转发，表明其认可，但完整内容被截断，具体建议不明确。

twitter · ylecun · Jun 6, 18:46

**背景**: 计算机视觉研究者越来越多地将技能应用于机器人学，但这两个领域的优先级不同。Malik 是计算机视觉领域的顶尖研究者，他的建议可能针对常见的错配问题。

**标签**: `#computer vision`, `#robotics`, `#research advice`, `#AI`

---

<a id="item-7"></a>
## [缆绳驱动机器人在硕士论文演示中玩杂耍](https://twitter.com/lukas_m_ziegler/status/2063612448008032659) ⭐️ 6.0/10

一款名为 CableEndy 的缆绳驱动并联机器人，作为布尔诺理工大学硕士论文的一部分，通过玩杂耍来展示其能力。 这一演示凸显了缆绳驱动并联机器人在执行动态和灵巧任务方面的潜力，可能应用于娱乐、制造或康复等领域。 该机器人是一种缆绳驱动并联机器人（CDPR），通过电机驱动的柔性缆绳来控制末端执行器的运动。该项目在 B&R 工业自动化布尔诺办公室开发。

twitter · lukas_m_ziegler · Jun 7, 13:22

**背景**: 缆绳驱动并联机器人使用缆绳代替刚性连杆来操纵末端执行器，具有工作空间大、有效载荷重量比高等优点。它们是一种并联机构，缆绳缠绕在电机驱动的转子上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cable_robots">Cable robots - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/B&R">B & R - Wikipedia</a></li>

</ul>
</details>

**标签**: `#robotics`, `#cable-driven robot`, `#engineering`, `#master's thesis`

---

<a id="item-8"></a>
## [SpaceX 发射 21 颗星链和 2 颗星盾卫星](https://twitter.com/SpaceX/status/2063502527358816513) ⭐️ 6.0/10

SpaceX 在加州发射了一枚猎鹰 9 号火箭，搭载了 21 颗星链卫星和 2 颗星盾卫星，发射后确认卫星已部署。 此次发射凸显了 SpaceX 在商业宽带和军事太空能力方面的双重角色，因为星盾卫星专为美国政府国防任务设计。同时也展示了星链星座的持续扩展，旨在提供全球互联网覆盖。 猎鹰 9 号火箭从加州发射，共搭载 23 颗卫星：21 颗星链和 2 颗星盾。星盾是 SpaceX 的一个业务部门，为军事目的建造低地球轨道卫星，包括导弹跟踪和侦察。

twitter · SpaceX · Jun 7, 06:05

**背景**: 星链是 SpaceX 的卫星互联网星座，提供全球宽带服务。星盾改编自星链技术，为国家安全客户（如美国太空军和国家侦察局）提供增强能力。截至 2025 年，已发射超过 183 颗星盾卫星。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starshield_(satellite_constellation)">Starshield (satellite constellation)</a></li>
<li><a href="https://www.spacex.com/starshield">SpaceX - Starshield</a></li>
<li><a href="https://www.spacex.com/launches">SpaceX - Launches</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starlink`, `#satellite launch`, `#aerospace`

---

<a id="item-9"></a>
## [生成模型需要非配对数据翻译以服务科学](https://twitter.com/StanfordAILab/status/2063281274605670497) ⭐️ 6.0/10

@shiye_su 的一条推文（被斯坦福 AI 实验室转发）指出，生成模型通常将噪声转换为数据，但许多科学任务需要非配对的数据到数据翻译，例如将未处理细胞映射到干预后状态。 这一观察突显了当前生成 AI 在科学应用中的一个关键缺口，非配对数据翻译对于药物发现和基因组学等任务至关重要，可能推动新的研究方向。 该推文提到了非配对数据翻译，这是一个具有挑战性的问题，输入和输出域之间没有直接的对应关系，不同于配对翻译（例如，具有对齐示例的图像到图像翻译）。

twitter · StanfordAILab · Jun 6, 15:26

**背景**: 像 GAN 和扩散模型这样的生成模型通常学习从随机噪声生成数据，在图像合成等任务中表现出色。然而，许多科学问题需要将一种数据类型转换为另一种，且没有配对示例，这被称为非配对数据翻译。最近的方法，如薛定谔桥流，旨在通过学习分布之间的随机过程来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2409.09347">[2409.09347] Schrödinger Bridge Flow for Unpaired Data Translation</a></li>
<li><a href="https://deep-diver.github.io/neurips2024/spotlight-others/1f32icjffa/">Schrodinger Bridge Flow for Unpaired Data Translation · NeurIPS 2024</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generative_model">Generative model - Wikipedia</a></li>

</ul>
</details>

**标签**: `#generative models`, `#science`, `#data translation`

---

<a id="item-10"></a>
## [人形机器人 vs 专用机器人：现实检验](https://twitter.com/lukas_m_ziegler/status/2063232965618929737) ⭐️ 5.0/10

Lukas Ziegler 的一条推文指出，人形机器人多次尝试后仍难以完成抓杯子等简单任务，而专用机器人自 2008 年以来已可靠地执行特定任务。 这一观察凸显了通用人形机器人的炒作与专用机器人已被验证的效率之间的差距，促使人们对机器人技术的未来进行更现实的讨论。 该推文提及一份机器人通讯并附有加入链接，但未提供所提及机器人的具体技术细节。该比较基于轶事证据而非严谨数据。

twitter · lukas_m_ziegler · Jun 6, 12:14

**背景**: 人形机器人旨在模仿人类形态和动作，以在人类环境中实现多功能性。专用机器人（如工业机械臂）则针对单一任务进行优化，具有高可靠性。通用型与任务专用型机器人之间的争论在机器人研究中持续存在。

**标签**: `#robotics`, `#humanoid robots`, `#specialized robots`

---

<a id="item-11"></a>
## [谷歌 AI 内存压缩说法缺乏证据](https://twitter.com/RodmanAi/status/2063507902963573079) ⭐️ 3.0/10

一条推文声称谷歌使用名为 TurboVec 的工具将 AI 内存从 31GB 减少到 4GB，但该说法模糊且缺乏可靠来源支持。 如果属实，如此显著的内存缩减可能大幅降低硬件成本，并使更大规模的 AI 模型能在消费级设备上运行，但缺乏证据削弱了其可信度。 该推文提及 TurboVec，但网络搜索结果指出 TurboVec 是一个第三方 Rust 库，实现了谷歌的 TurboQuant 算法，并非谷歌官方产品。实际的压缩技术 TurboQuant 实现了 KV 缓存内存约 6 倍缩减，且精度损失近乎为零。

twitter · RodmanAi · Jun 7, 06:26

**背景**: 大型语言模型（LLM）在推理时需要大量内存来存储键值（KV）缓存，这限制了它们在资源受限设备上的部署。谷歌的 TurboQuant 是一种无需训练的压缩算法，可将 KV 缓存内存缩减至每维度约 3 比特，从而实现大幅内存节省。TurboVec 是 TurboQuant 的一个独立开源实现，并非谷歌官方发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techsy.io/en/blog/google-turboquant-ai-memory-compression">TurboQuant: 31 GB AI Memory Down to 4 GB , Explained | TECHSY</a></li>
<li><a href="https://techstartups.com/2026/06/06/google-shrinks-ai-memory-from-31gb-to-4gb-with-turbovec-beating-faiss-on-speed/">Google shrinks AI memory from 31GB to 4GB with TurboVec , beating...</a></li>
<li><a href="https://medevel.com/turbovec/">10M Vectors. 4GB RAM. Zero Training. Meet turbovec</a></li>

</ul>
</details>

**标签**: `#AI`, `#memory`, `#Google`, `#TurboVec`

---

<a id="item-12"></a>
## [10 块 NVIDIA GPU 月入 1.8 万美元：算力租赁轶事](https://twitter.com/RodmanAi/status/2063143996214669359) ⭐️ 3.0/10

一条推文声称，有人花费 12 万美元购买了 10 块 NVIDIA GPU，现在通过向 AI 公司出租算力每月赚取 1.8 万美元，7 个月即可收回成本。 这则轶事凸显了 AI 算力需求的增长以及 GPU 租赁的盈利能力，可能鼓励更多人投资硬件以获取被动收入。 推文未说明 GPU 型号、租赁平台或运营成本，使得该说法难以验证；实际盈利能力因硬件、电力和市场价格而异。

twitter · RodmanAi · Jun 6, 06:20

**背景**: 像 Hivenet、Clore.ai 和 SaladCloud 这样的 GPU 租赁平台允许个人出租闲置的 GPU 算力用于 AI 工作负载。盈利能力取决于 GPU 类型、租赁定价和利用率。随着 AI 需求超过供应，这种模式已获得关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hivenet.com/post/ai-rent-the-complete-guide-to-renting-ai-computing-resources">AI Rent Guide 2026: How to Rent Compute for AI Workloads | Hivenet</a></li>
<li><a href="https://clore.ai/">CLORE. AI - Rent GPUs for AI /ML | Decentralized GPU Cloud</a></li>
<li><a href="https://salad.com/pricing">Salad GPU Cloud Pricing | Rent GPUs from $0.02/hr</a></li>

</ul>
</details>

**标签**: `#GPU`, `#AI compute`, `#hardware investment`

---

<a id="item-13"></a>
## [转发批评白宫网页内容](https://twitter.com/ylecun/status/2063331550247223711) ⭐️ 2.0/10

Yann LeCun 转发了 Paul Graham 的批评，称白宫网页内容像关于第三世界独裁者的宣传。 这凸显了公众对官方政府沟通语气日益增长的不满，但这是一条没有技术意义的政治评论。 推文未指明具体是哪个白宫页面，内容中也没有提供额外背景。

twitter · ylecun · Jun 6, 18:45

**标签**: `#politics`, `#commentary`

---

<a id="item-14"></a>
## [伯克利 AI 转发无上下文的链接](https://twitter.com/berkeley_ai/status/2063363827358634396) ⭐️ 2.0/10

伯克利 AI 的 Twitter 账号转发了@roeiherzig 的一条仅包含链接的推文，没有附加任何评论或上下文。 这条转发缺乏实质内容，不太可能对 AI 社区或公众产生影响。 该推文的参与度评分仅为 2.0/10，且没有讨论，表明其兴趣度或相关性极低。

twitter · berkeley_ai · Jun 6, 20:54

**标签**: `#twitter`, `#retweet`, `#low-value`

---

<a id="item-15"></a>
## [Yann LeCun 转发 David Sarnoff 传记](https://twitter.com/ylecun/status/2063661726818533629) ⭐️ 1.0/10

Yann LeCun 转发了一条关于前 RCA 主席 David Sarnoff 的帖子，强调了他从移民办公室勤杂工成长为媒体大亨的经历。 这条推文是关于历史琐事的，与 AI/ML 或软件工程相关性低，但可能反映了 LeCun 对技术史的兴趣。 David Sarnoff（1891-1971）是一位俄罗斯犹太移民，后来成为 RCA 的总裁兼主席，在无线电和电视广播中发挥了关键作用。

twitter · ylecun · Jun 7, 16:37

**背景**: David Sarnoff 是无线电和电视早期的重要人物。他从 1920 年代到 1950 年代领导 RCA（美国无线电公司），监督了商业广播的发展。他的故事常被引为经典的美国成功故事。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/David_Sarnoff">David Sarnoff - Wikipedia</a></li>
<li><a href="https://www.britannica.com/money/David-Sarnoff">David Sarnoff | Biography & Facts | Britannica Money</a></li>

</ul>
</details>

**标签**: `#history`, `#trivia`

---