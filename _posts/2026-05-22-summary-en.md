---
layout: default
title: "Horizon Summary: 2026-05-22 (EN)"
date: 2026-05-22
lang: en
---

> From 63 items, 36 important content pieces were selected

---

1. [Python 3.14 to Allow Disabling the GIL](#item-1) ⭐️ 9.0/10
2. [Hugging Face Releases Open-Source Humanoid Robot for $2,500](#item-2) ⭐️ 8.0/10
3. [SpaceX Flight 12 to Debut Next-Gen Starship and Raptor Engines](#item-3) ⭐️ 8.0/10
4. [Can AI Agents Autonomously Exploit Security Vulnerabilities?](#item-4) ⭐️ 8.0/10
5. [Crys-JEPA: AI for Crystal Design](#item-5) ⭐️ 7.0/10
6. [Stanford AI Lab Introduces General Preference RL](#item-6) ⭐️ 7.0/10
7. [Compute and Data Quality Surprise](#item-7) ⭐️ 7.0/10
8. [SimpleTES: Scaling Evaluations for AI-Driven Science](#item-8) ⭐️ 7.0/10
9. [Stanford AI Lab Launches Terminal-Bench Science for Scientific Workflows](#item-9) ⭐️ 7.0/10
10. [Stanford AI Lab Unveils Hawkeye for GPU Replication](#item-10) ⭐️ 7.0/10
11. [Optimize Anything Paper Accepted at CAIS 2026](#item-11) ⭐️ 7.0/10
12. [RAPTOR: Tiny Foundation Policy for Quadrotors](#item-12) ⭐️ 7.0/10
13. [ClaudeDevs Expands SpaceX Partnership, Scales GB200 in Colossus 2](#item-13) ⭐️ 7.0/10
14. [Anthropic Releases Free Claude Prompt Engineering Workshop](#item-14) ⭐️ 7.0/10
15. [Andrew Ng Launches Course on AI Agents for Image/Video Generation](#item-15) ⭐️ 7.0/10
16. [C-Ray Robot Uses Hyperbolic Fins for Multiple Locomotion Modes](#item-16) ⭐️ 6.0/10
17. [Starlink Explores Extending Connectivity Beyond Earth](#item-17) ⭐️ 6.0/10
18. [Hermes Agent Gains 140k+ GitHub Stars, Tops OpenRouter](#item-18) ⭐️ 6.0/10
19. [SpaceX: Starship Critical for NASA's Artemis Moon Missions](#item-19) ⭐️ 5.0/10
20. [Anthropic's Claude Code Setup Plugin Enhances Dev Workflow](#item-20) ⭐️ 5.0/10
21. [World Jam 2026 Winners Announced](#item-21) ⭐️ 4.0/10
22. [Daedalus Journal Issue Promoted via Retweet](#item-22) ⭐️ 4.0/10
23. [CHI-Bench: New Benchmark for Healthcare AI Agents](#item-23) ⭐️ 4.0/10
24. [AI as the Next Shift in Mechanical Design](#item-24) ⭐️ 3.0/10
25. [Tweet Expresses Excitement About Space Robots](#item-25) ⭐️ 3.0/10
26. [Twitter Post Lists YouTube Channels for Tech Skills](#item-26) ⭐️ 3.0/10
27. [20 Remote Job Sites Paying in USD](#item-27) ⭐️ 3.0/10
28. [Google Cloud Partners Validate Gemini 3.5](#item-28) ⭐️ 2.0/10
29. [Yann LeCun Retweets January 6 Slush Fund Article](#item-29) ⭐️ 2.0/10
30. [Yann LeCun Retweets Political NYT Piece](#item-30) ⭐️ 2.0/10
31. [Retweet Praises France's Sovereignty and Nuclear Deterrent](#item-31) ⭐️ 2.0/10
32. [Yann LeCun Retweets NYT Opinion on Spending](#item-32) ⭐️ 2.0/10
33. [Low-Quality Tweet: 'Wrong Side of History' Quote](#item-33) ⭐️ 2.0/10
34. [Trump Censorship Claim and US Press Freedom Ranking](#item-34) ⭐️ 2.0/10
35. [Low-Effort Tweet Repeating 'vibe cad'](#item-35) ⭐️ 1.0/10
36. [Political Tweet Unrelated to Tech](#item-36) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [Python 3.14 to Allow Disabling the GIL](https://twitter.com/RodmanAi/status/2057108613693673957) ⭐️ 9.0/10

Python 3.14 will introduce an optional free-threaded mode that disables the Global Interpreter Lock (GIL), enabling true multi-core parallelism for the first time. This change addresses a 30-year-old bottleneck in CPython, allowing CPU-bound multi-threaded programs to utilize all CPU cores simultaneously, significantly improving performance for parallel workloads. The GIL can be disabled at build time via the --disable-gil flag, and runtime control is available via the PYTHONGIL environment variable. This feature is based on PEP 703.

twitter · RodmanAi · May 20, 14:38

**Background**: The Global Interpreter Lock (GIL) is a mutex in CPython that prevents multiple native threads from executing Python bytecode simultaneously. It simplifies memory management but limits parallelism, especially for CPU-bound tasks. Removing the GIL has been a long-desired goal in the Python community.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Global_Interpreter_Lock">Global interpreter lock - Wikipedia</a></li>
<li><a href="https://peps.python.org/pep-0703/">PEP 703 – Making the Global Interpreter Lock Optional in CPython | peps.python.org</a></li>
<li><a href="https://towardsdatascience.com/python-3-14-and-the-end-of-the-gil/">Python 3.14 and the End of the GIL | Towards Data Science</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion highlights that while removing the GIL helps parallelism, it does not solve Python's inherent slowness; it merely distributes the work. Some commenters express cautious optimism, noting that single-threaded performance remains unchanged.

**Tags**: `#Python`, `#GIL`, `#Parallelism`, `#CPython`, `#Performance`

---

<a id="item-2"></a>
## [Hugging Face Releases Open-Source Humanoid Robot for $2,500](https://twitter.com/lukas_m_ziegler/status/2057515219946205399) ⭐️ 8.0/10

Hugging Face's LeRobot project has released LeRobot Humanoid, a fully open-source bipedal robot that can be built for approximately $2,500 using 3D-printed parts and off-the-shelf components. This drastically lowers the entry barrier for robotics research and education, enabling more individuals and small labs to experiment with humanoid robots and advance embodied AI. The robot is part of a full-stack ecosystem including 3D-printable hardware files, runtime software, simulation tools, and training environments, making it a complete platform for robot learning.

twitter · lukas_m_ziegler · May 21, 17:33

**Background**: Open-source robotics aims to democratize access to advanced robotic platforms, which are typically expensive and proprietary. Hugging Face, known for its work in AI and machine learning, has been expanding into robotics through its LeRobot initiative, previously releasing software tools and now a hardware platform.

<details><summary>References</summary>
<ul>
<li><a href="https://www.humanoidsdaily.com/news/hugging-face-drops-a-2-500-3d-printed-humanoid-for-open-robot-learning">Hugging Face Drops a $2,500 3D-Printed Humanoid for Open ...</a></li>
<li><a href="https://techcrunch.com/2025/05/29/hugging-face-unveils-two-new-humanoid-robots/">Hugging Face unveils two new humanoid robots | TechCrunch</a></li>
<li><a href="https://arstechnica.com/ai/2025/05/hugging-face-hopes-to-bring-a-humanoid-robot-to-market-for-just-3000/">Want a humanoid, open source robot for just $3,000? Hugging Face is on it. - Ars Technica</a></li>

</ul>
</details>

**Discussion**: The announcement has been met with enthusiasm on social media, with many praising the low cost and open-source nature. Some commenters express excitement about the potential for education and research, while others note the challenge of assembling and maintaining such a robot.

**Tags**: `#open-source`, `#robotics`, `#humanoid robot`, `#Hugging Face`

---

<a id="item-3"></a>
## [SpaceX Flight 12 to Debut Next-Gen Starship and Raptor Engines](https://twitter.com/SpaceX/status/2057596793299333595) ⭐️ 8.0/10

SpaceX announced that Flight 12 will debut the next generation Starship and Super Heavy vehicles, both powered by upgraded Raptor engines. The launch is scheduled from the new Pad 2 at Starbase, designed for full and rapid reusability. This marks a significant milestone in aerospace engineering, as the next-generation Starship and Raptor engines aim to improve performance, reliability, and reusability. Success could accelerate SpaceX's plans for lunar missions, Mars colonization, and heavy-lift satellite deployment. The upgraded Raptor engines represent the next evolution of SpaceX's full-flow staged combustion methalox engine, with improvements in thrust and reliability. Pad 2 at Starbase is the first launch pad designed from the ground up for rapid reusability, featuring advanced ground support systems.

twitter · SpaceX · May 21, 22:57

**Background**: SpaceX's Starship is a fully reusable super heavy-lift launch vehicle consisting of the Starship spacecraft and Super Heavy booster. The Raptor engine uses methane and liquid oxygen in a full-flow staged combustion cycle, known for high efficiency and reusability. Pad 2 is the second orbital launch pad at Starbase, designed to support higher launch cadence and rapid turnaround.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Raptor">SpaceX Raptor - Wikipedia</a></li>
<li><a href="https://www.nasaspaceflight.com/2025/08/starbase-pad-2-advancements-pad-1/">Starbase Pad 2 : Design Advancements from... - NASASpaceFlight.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starship`, `#Raptor engine`, `#aerospace`

---

<a id="item-4"></a>
## [Can AI Agents Autonomously Exploit Security Vulnerabilities?](https://twitter.com/berkeley_ai/status/2057567247783399688) ⭐️ 8.0/10

A discussion initiated by Dawn Song highlights the critical task of measuring whether AI agents can autonomously turn security vulnerabilities into real attacks, a key challenge for AI safety. This question is central to AI safety and cybersecurity, as autonomous exploitation could lead to large-scale automated attacks, necessitating robust evaluation frameworks and defenses. Recent research shows threat actors are already leveraging AI for vulnerability exploitation, and autonomous multi-agent systems have been demonstrated to attack cloud environments by chaining exploits.

twitter · berkeley_ai · May 21, 21:00

**Background**: AI agents are systems that can autonomously perform tasks, including interacting with software and networks. Vulnerability exploitation involves finding and using security flaws to gain unauthorized access or cause damage. Measuring AI agents' ability to do this autonomously is important for understanding and mitigating risks.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access">Adversaries Leverage AI for Vulnerability Exploitation, Augmented Operations, and Initial Access | Google Cloud Blog</a></li>
<li><a href="https://unit42.paloaltonetworks.com/autonomous-ai-cloud-attacks/">Can AI Attack the Cloud? Lessons From Building an Autonomous Cloud Offensive Multi-Agent System</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#cybersecurity`, `#AI agents`, `#vulnerability exploitation`

---

<a id="item-5"></a>
## [Crys-JEPA: AI for Crystal Design](https://twitter.com/ylecun/status/2057474214693834963) ⭐️ 7.0/10

Researchers introduced Crys-JEPA, a novel generative AI method for designing new crystal materials, leveraging the Joint Embedding Predictive Architecture (JEPA). 这项工作可能加速发现用于电子、能源和制药领域的稳定且新颖的晶体，解决材料科学中的一个关键瓶颈。 Crys-JEPA achieves up to 81.4% and 82.6% improvements on the V.S.U.N metric on the MP-20 and Alex-MP-20 datasets, respectively, compared to baselines.

twitter · ylecun · May 21, 14:50

**Background**: Crystal generation aims to discover new materials that are realistic, stable, and novel. Traditional generative models often maximize likelihood of observed crystals, which may not align with discovery goals. JEPA is a self-supervised learning paradigm that learns abstract representations by predicting in embedding space, introduced by Yann LeCun.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.14759">[2605.14759] Crys-JEPA: Accelerating Crystal Discovery via ...</a></li>
<li><a href="https://www.linkedin.com/posts/xavier-bresson-738585b_how-do-we-design-materials-with-ai-excited-activity-7462301163732783104-74zb">How do we design materials with AI? Excited to introduce Crys ...</a></li>
<li><a href="https://rohitbandaru.github.io/blog/JEPA-Deep-Dive/">Deep Dive into Yann LeCun’s JEPA | Rohit Bandaru</a></li>

</ul>
</details>

**Tags**: `#AI`, `#materials science`, `#generative models`, `#research`

---

<a id="item-6"></a>
## [Stanford AI Lab Introduces General Preference RL](https://twitter.com/StanfordAILab/status/2057531797945397379) ⭐️ 7.0/10

Stanford AI Lab shared a new paper titled 'General Preference Reinforcement Learning' (GPRL), which proposes a method to treat general preference models as multi-dimensional reward sources for online RL. This work could advance reinforcement learning from human feedback (RLHF) by enabling more structured and scalable preference-based training, potentially improving alignment in large language models and other AI systems. GPRL computes per-dimension group-relative advantages and normalizes them to prevent any single axis from dominating, then aggregates them for policy updates in a GRPO-style online RL framework.

twitter · StanfordAILab · May 21, 18:39

**Background**: Reinforcement learning from human feedback (RLHF) typically trains a reward model from human preferences and then optimizes a policy. GPRL extends this by using a general preference model that provides multi-dimensional feedback, enabling more nuanced training signals.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.18721">[2605.18721] General Preference Reinforcement Learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback">Reinforcement learning from human feedback - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#AI research`, `#Stanford`

---

<a id="item-7"></a>
## [Compute and Data Quality Surprise](https://twitter.com/StanfordAILab/status/2057531127326453869) ⭐️ 7.0/10

Stanford AI Lab researcher Tatsu Hashimoto tweeted surprising new results showing that with enough compute, the best data yields unexpected outcomes. This challenges conventional wisdom about the relationship between compute, data quality, and model performance, potentially reshaping AI research priorities. The tweet lacks specifics, but the surprise suggests a non-linear or threshold effect where compute amplifies data quality benefits in unexpected ways.

twitter · StanfordAILab · May 21, 18:37

**Background**: In AI development, compute refers to the processing power used for training models, while data quality encompasses accuracy, completeness, and relevance of training data. It is widely believed that both factors are important, but their interaction is not fully understood.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/ai-and-compute/">AI and compute - OpenAI</a></li>
<li><a href="https://www.pickl.ai/blog/data-quality-in-machine-learning/">Data Quality in Machine Learning - Pickl.AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#machine learning`, `#research`, `#compute`, `#data`

---

<a id="item-8"></a>
## [SimpleTES: Scaling Evaluations for AI-Driven Science](https://twitter.com/StanfordAILab/status/2057202545991581903) ⭐️ 7.0/10

James Y. Zou and Stanford AI Lab highlight that scaling evaluations, not just compute, is critical for AI-driven science, and introduce SimpleTES, a framework for scaling evaluation-driven discovery. This shift emphasizes that better evaluation methods can unlock AI's potential in scientific discovery, especially for open-ended problems where longer reasoning isn't enough. SimpleTES is a C++-backed, Python-driven framework that allocates test-time compute to iterative evaluation loops rather than just generating longer outputs.

twitter · StanfordAILab · May 20, 20:51

**Background**: AI-driven science often relies on scaling compute (larger models or more training data). However, for open-ended problems like scientific discovery, the path to a solution depends on iterative evaluation and search. SimpleTES addresses this by providing a training-free search system that strategically scales evaluation-driven loops.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/wq-will/SimpleTES">GitHub - wq-will/ SimpleTES : A general framework for strategically...</a></li>
<li><a href="https://www.emergentmind.com/topics/simple-test-time-evaluation-driven-scaling-simpletes">SimpleTES : Evaluation-Driven Scaling</a></li>
<li><a href="https://imtaqin.id/simpletes-a-general-framework-for-strategically-scaling-evaluation-driven-di">SimpleTES : Evaluation-Driven Scaling Framework | AI Research</a></li>

</ul>
</details>

**Tags**: `#AI`, `#evaluation`, `#science`, `#framework`

---

<a id="item-9"></a>
## [Stanford AI Lab Launches Terminal-Bench Science for Scientific Workflows](https://twitter.com/StanfordAILab/status/2057202472842903664) ⭐️ 7.0/10

Stanford AI Lab announced Terminal-Bench Science, a new benchmark for evaluating AI agents on real scientific workflows, and opened it for community task contributions. This benchmark addresses a critical gap by testing AI agents on practical scientific tasks rather than textbook knowledge, potentially accelerating AI adoption in research and development. Terminal-Bench Science builds on Terminal-Bench, which has been adopted by frontier labs like Anthropic, OpenAI, and Google DeepMind for software engineering tasks. The new benchmark extends this approach to natural sciences.

twitter · StanfordAILab · May 20, 20:51

**Background**: AI agents are increasingly used to automate complex workflows, but existing benchmarks often test only theoretical knowledge. Terminal-Bench Science aims to evaluate agents on realistic command-line tasks derived from actual scientific research, providing a more meaningful measure of capability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tbench.ai/news/tb-science-announcement">Terminal-Bench Science: Contribute your scientific workflows as tasks for AI Agents</a></li>
<li><a href="https://arxiv.org/abs/2601.11868">[2601.11868] Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#benchmarking`, `#scientific workflows`, `#AI research`

---

<a id="item-10"></a>
## [Stanford AI Lab Unveils Hawkeye for GPU Replication](https://twitter.com/StanfordAILab/status/2057202147494965392) ⭐️ 7.0/10

Stanford AI Lab presented Hawkeye at MLSys 2026, a tool that enables exact CPU replication of GPU-level operations such as FP16 matrix multiplication, ensuring bit-for-bit identical results. Hawkeye addresses a critical reproducibility challenge in machine learning, allowing researchers to audit and verify GPU computations without needing specialized hardware, which is essential for scientific rigor and accountability. Hawkeye re-executes exact matrix multiplication operations on a CPU without any precision loss, supporting NVIDIA GPUs. It was presented as a poster at MLSys 2026.

twitter · StanfordAILab · May 20, 20:49

**Background**: GPU computations are often non-deterministic due to parallel execution and floating-point optimizations, making it difficult to reproduce results exactly. Prior approaches to verifiable machine learning required significant overhead or hardware changes. Hawkeye provides a lightweight solution by replicating GPU arithmetic on CPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.20421">Hawkeye: Reproducing GPU-Level Non-Determinism</a></li>
<li><a href="https://www.machinebrief.com/news/hawkeye-a-new-era-of-gpu-level-reproducibility-ix8t">Hawkeye: A New Era of GPU-Level Reproducibility</a></li>
<li><a href="https://mlsys.org/virtual/2026/poster/3606">MLSys Poster Hawkeye: Reproducing GPU-Level Non-Determinism</a></li>

</ul>
</details>

**Tags**: `#MLSys`, `#GPU`, `#reproducibility`, `#machine learning`, `#systems`

---

<a id="item-11"></a>
## [Optimize Anything Paper Accepted at CAIS 2026](https://twitter.com/berkeley_ai/status/2057567604987105501) ⭐️ 7.0/10

The paper 'optimize_anything: A Universal API for Optimizing any Text Parameter' has been accepted to the ACM Conference on AI and Agentic Systems (CAIS) 2026 and released on arXiv with expanded experiments and details. This work provides a universal API for optimizing any text-representable artifact (e.g., code, prompts, agent architectures), which could significantly streamline optimization tasks across many AI applications and reduce the need for custom solutions. The API is declarative and optimizes artifacts like code, prompts, agent architectures, vector graphics, and configurations. The paper includes expanded experiments compared to the initial release, demonstrating its versatility.

twitter · berkeley_ai · May 21, 21:01

**Background**: CAIS 2026 is a premier venue for research on compound AI architectures, optimization, and deployment. The 'optimize_anything' approach builds on the idea of treating optimization as a text-level problem, leveraging large language models to find optimal configurations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.caisconf.org/">ACM Conference on AI and Agentic Systems — ACM CAIS 2026</a></li>
<li><a href="https://arxiv.org/abs/2605.19633">[2605.19633] optimize_anything: A Universal API for ...</a></li>
<li><a href="https://gepa-ai.github.io/gepa/blog/2026/02/18/introducing-optimize-anything/">optimize_anything: A Universal API for Optimizing any Text ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#optimization`, `#research`, `#arxiv`

---

<a id="item-12"></a>
## [RAPTOR: Tiny Foundation Policy for Quadrotors](https://twitter.com/berkeley_ai/status/2057119576299839669) ⭐️ 7.0/10

Researchers have developed RAPTOR, a single compact foundation policy for quadrotors that adapts to various conditions, published in Science Robotics. This work demonstrates that a single neural network policy can control diverse quadrotors, potentially reducing the need for platform-specific tuning and accelerating deployment in real-world applications. RAPTOR is an end-to-end neural network policy trained to control a wide variety of quadrotors, as detailed in the Science Robotics paper published on May 13, 2026.

twitter · berkeley_ai · May 20, 15:21

**Background**: Foundation models in robotics aim to create general-purpose control policies that work across different robots and tasks, similar to large language models in AI. Traditional quadrotor control often requires hand-tuned parameters for each platform, limiting scalability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.science.org/doi/10.1126/scirobotics.aec1481">RAPTOR: A foundation policy for quadrotor control - Science</a></li>
<li><a href="https://arxiv.org/abs/2509.11481">RAPTOR: A Foundation Policy for Quadrotor Control</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#quadrotors`, `#foundation model`, `#AI`

---

<a id="item-13"></a>
## [ClaudeDevs Expands SpaceX Partnership, Scales GB200 in Colossus 2](https://twitter.com/ClaudeDevs/status/2057199398573220092) ⭐️ 7.0/10

ClaudeDevs announced an expanded partnership with SpaceX and plans to scale up GB200 capacity in Colossus 2 throughout June. This signals significant infrastructure growth for AI compute, leveraging SpaceX's capabilities and NVIDIA's latest GB200 hardware, which could accelerate AI model training and inference. GB200 is NVIDIA's high-performance GPU card with 192 GB memory, and Colossus 2 is xAI's next-generation supercomputer cluster, expected to be the world's first gigawatt datacenter.

twitter · ClaudeDevs · May 20, 20:38

**Background**: Colossus is xAI's existing AI supercomputer, currently the world's largest, used to train Grok. Colossus 2 is its successor, aiming for even greater scale. GB200 NVL72 racks draw around 120-132 kW and are designed for large-scale AI workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/gb200-nvl72/">GB200 NVL72 | NVIDIA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Colossus_(supercomputer)">Colossus (supercomputer) - Wikipedia</a></li>
<li><a href="https://newsletter.semianalysis.com/p/xais-colossus-2-first-gigawatt-datacenter">xAI's Colossus 2 - First Gigawatt Datacenter In The World ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#partnership`, `#SpaceX`, `#GB200`, `#Colossus`

---

<a id="item-14"></a>
## [Anthropic Releases Free Claude Prompt Engineering Workshop](https://twitter.com/RodmanAi/status/2057143286163542441) ⭐️ 7.0/10

Anthropic released a free 27-minute workshop on prompt engineering for Claude, taught by the people who built it, with no registration or paywall. This workshop provides authoritative, high-quality guidance on prompt engineering for Claude, potentially saving users hundreds of dollars compared to paid courses, and helps users get the most out of the AI model. The workshop is 27 minutes long, free, and requires no registration or paywall. It covers prompt engineering techniques that the poster claims surpass what is taught in $300 courses.

twitter · RodmanAi · May 20, 16:55

**Background**: Prompt engineering is the practice of crafting inputs to AI models to get desired outputs. Claude is Anthropic's AI assistant, and effective prompting is key to leveraging its capabilities. This workshop offers official training from the model's creators.

**Tags**: `#Anthropic`, `#Claude`, `#prompt engineering`, `#AI workshop`

---

<a id="item-15"></a>
## [Andrew Ng Launches Course on AI Agents for Image/Video Generation](https://twitter.com/AndrewYNg/status/2057146565500998024) ⭐️ 7.0/10

Andrew Ng announced a new short course on building AI agents that generate images and videos, co-created with Google Cloud and taught by Katie Nguyen. The course emphasizes self-evaluation and iterative improvement as key to performance. This course addresses an under-explored frontier in AI agents, combining generative AI with agentic self-evaluation, which could significantly improve output quality. It provides practical guidance for developers and researchers looking to build more autonomous and effective generative systems. The course is a short course built with Google Cloud, taught by Katie Nguyen, and focuses on having the agent evaluate its own output and iterate to improve quality. It targets the novel area of AI agents for image and video generation, which is less explored compared to text-based agents.

twitter · AndrewYNg · May 20, 17:08

**Background**: AI agents are autonomous systems that can perceive their environment, make decisions, and take actions to achieve goals. Self-evaluation and iterative improvement are techniques where the agent assesses its own outputs and refines them through multiple cycles, reducing the need for human oversight. This approach is increasingly important as AI systems scale to complex tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/day-12-self-evaluation-feedback-loops-building-agents-ramanujam-ng3jc">Day 12: Self - Evaluation & Feedback Loops: Building Adaptive Agents</a></li>
<li><a href="https://www.emergentmind.com/topics/self-evaluation-module">Self - Evaluation Module in AI Systems</a></li>
<li><a href="https://cloud.google.com/ai/generative-ai">Generative AI | Google Cloud</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#image generation`, `#video generation`, `#education`, `#Google Cloud`

---

<a id="item-16"></a>
## [C-Ray Robot Uses Hyperbolic Fins for Multiple Locomotion Modes](https://twitter.com/lukas_m_ziegler/status/2057035258130808902) ⭐️ 6.0/10

Pliant Energy Systems has showcased the C-Ray robot, which uses a unique pair of flexible hyperbolic fins to swim like a ray, crawl like a millipede, jet like a squid, and slide like a snake. This innovation demonstrates a highly versatile amphibious locomotion system that could enable robots to operate in diverse environments—land, water, and ice—without needing separate propulsion mechanisms, potentially advancing environmental monitoring, search-and-rescue, and underwater exploration. The fins are described as four-dimensional objects with hyperbolic geometry, allowing the robot to move efficiently in multiple modes. The C-Ray platform is funded by the Office of Naval Research and is designed for autonomous operation across ice, land, surface, and underwater.

twitter · lukas_m_ziegler · May 20, 09:46

**Background**: Traditional amphibious robots often rely on separate systems for land and water movement, which adds complexity and weight. Bio-inspired designs like C-Ray aim to mimic the efficiency and adaptability of marine animals. Hyperbolic fins use undulating motion to generate thrust, similar to how rays and cuttlefish move, enabling smooth transitions between environments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pliantenergy.com/robotics">Robotics — Pliant Energy Systems</a></li>
<li><a href="https://oceanai.mit.edu/pavlab/pdfs/robot_cray.pdf">C-Ray - An autonomous amphibious vehicle with ice, land ...</a></li>
<li><a href="https://www.youtube.com/watch?v=7T-wYJ_bFcI">Meet c-ray - a robot build to monitor protect marine life Pliant Energy's C-Ray Robot and Greensea IQ's Crawlers Enable ... Undulating Fins Enable Robot to Swim, Crawl, Recharge Meet C-Ray, developed by Pliant Energy Systems Inc. This ... Autonomous Robots Could Mine the Deep Seafloor - IEEE Spectrum</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#biomimicry`, `#locomotion`, `#innovation`

---

<a id="item-17"></a>
## [Starlink Explores Extending Connectivity Beyond Earth](https://twitter.com/SpaceX/status/2057598013565014112) ⭐️ 6.0/10

SpaceX shared a post from Starlink stating that the team is exploring ways to extend connectivity beyond our planet, hinting at potential space-based internet services for missions beyond Earth orbit. This signals SpaceX's ambition to leverage its Starlink constellation for deep-space communications, which could revolutionize data transmission for lunar, Martian, and other interplanetary missions, reducing reliance on traditional ground-based networks. The announcement is brief and lacks technical specifics, but it aligns with SpaceX's broader vision of using Starlink as a backbone for interplanetary internet, potentially utilizing laser inter-satellite links for long-distance communication.

twitter · SpaceX · May 21, 23:02

**Background**: Starlink is a satellite internet constellation operated by SpaceX, consisting of thousands of satellites in low Earth orbit (LEO) providing high-speed internet to remote areas. SpaceX has previously discussed using Starlink for Mars colonization, and the company's Starship vehicle is designed for deep-space missions. Extending connectivity beyond Earth would require adapting Starlink's technology for longer distances and different orbital environments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>
<li><a href="https://starlink.com/technology">Starlink | Technology</a></li>
<li><a href="https://www.space.com/spacex-starlink-satellites.html">Starlink satellites : Facts, tracking and impact on astronomy | Space</a></li>

</ul>
</details>

**Tags**: `#Starlink`, `#SpaceX`, `#satellite internet`, `#space connectivity`

---

<a id="item-18"></a>
## [Hermes Agent Gains 140k+ GitHub Stars, Tops OpenRouter](https://twitter.com/RodmanAi/status/2057451490164592804) ⭐️ 6.0/10

Hermes Agent, an open-source autonomous AI agent from Nous Research, has surpassed 140,000 GitHub stars and become the top-ranked model on OpenRouter, as highlighted in a promotional tweet by RodmanAi. This rapid adoption signals growing demand for persistent, self-improving AI agents that can automate complex workflows, potentially shifting how developers and businesses deploy AI assistants. Hermes Agent features one-command setup, persistent multi-level memory, adaptive learning, and skill-building capabilities, allowing it to evolve over time and integrate with messaging platforms.

twitter · RodmanAi · May 21, 13:20

**Background**: Hermes Agent is an open-source autonomous AI agent developed by Nous Research, designed to live on the user's server and grow with them through persistent memory and adaptive learning. OpenRouter is a unified API gateway that provides access to over 300 AI models, allowing developers to compare and use various LLMs through a single interface.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Hermes_Agent">Hermes Agent</a></li>
<li><a href="https://hermes-agent.nousresearch.com/">Hermes Agent — The Agent That Grows With You | Nous Research</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**Tags**: `#AI agent`, `#open source`, `#GitHub`, `#OpenRouter`

---

<a id="item-19"></a>
## [SpaceX: Starship Critical for NASA's Artemis Moon Missions](https://twitter.com/SpaceX/status/2057602167423320137) ⭐️ 5.0/10

SpaceX announced that Starship will play a critical role in transporting crew and cargo to the lunar surface under NASA's Artemis program. This reaffirms SpaceX's central role in NASA's return to the Moon and highlights Starship's importance as a heavy-lift lander for future lunar exploration. Starship HLS (Human Landing System) is a specialized variant designed to transfer astronauts from lunar orbit to the surface and back, under a NASA contract awarded in 2021.

twitter · SpaceX · May 21, 23:19

**Background**: The Artemis program aims to return humans to the Moon for the first time since Apollo and establish a permanent lunar base. Starship HLS is one of the key elements, selected by NASA to land the next astronauts on the Moon.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artemis_program">Artemis program - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Starship_HLS">Starship HLS - Wikipedia</a></li>
<li><a href="https://www.spacex.com/humanspaceflight/moon">SpaceX - Mission: Moon</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starship`, `#Artemis`, `#NASA`, `#space exploration`

---

<a id="item-20"></a>
## [Anthropic's Claude Code Setup Plugin Enhances Dev Workflow](https://twitter.com/RodmanAi/status/2057175898466734519) ⭐️ 5.0/10

Anthropic quietly released an official plugin called claude-code-setup that scans a project's codebase and recommends tailored automations such as hooks, skills, MCP servers, and subagents. This plugin transforms Claude Code from a basic coding assistant into a more intelligent AI development environment, potentially boosting developer productivity by automating repetitive setup tasks. The plugin is open-source and available on GitHub under the anthropics/claude-plugins-official repository, and it can be installed directly from the Claude plugins page.

twitter · RodmanAi · May 20, 19:05

**Background**: Claude Code is an AI-powered coding assistant from Anthropic that helps developers write, debug, and refactor code. Hooks are customizable scripts that run at specific points in the Claude Code workflow, enabling automated formatting, security checks, and more. MCP servers provide additional context and tools to Claude Code.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/plugins/claude-code-setup">Claude Code Setup – Claude Plugin | Anthropic</a></li>
<li><a href="https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup">claude-plugins-official/plugins/claude-code-setup at main ...</a></li>
<li><a href="https://code.claude.com/docs/en/hooks">Hooks reference - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#AI`, `#developer tools`, `#Claude Code`, `#plugin`

---

<a id="item-21"></a>
## [World Jam 2026 Winners Announced](https://twitter.com/drfeifei/status/2057138100258890235) ⭐️ 4.0/10

Fei-Fei Li retweeted the announcement of the winners of the first World Jam, an interactive archive event organized by The World Labs. This event highlights the growing intersection of AI, creativity, and cultural preservation, showcasing how interactive archives can celebrate innovative projects. The World Jam winners are featured in an online museum that archives projects pushing boundaries in atmosphere, gameplay, and interactive worlds.

twitter · drfeifei · May 20, 16:35

**Background**: World Jam is a game jam-style event where participants create interactive projects within a limited time. The event is organized by The World Labs, a group focused on AI and creativity. Fei-Fei Li is a renowned AI researcher known for her work in computer vision and her advocacy for human-centered AI.

<details><summary>References</summary>
<ul>
<li><a href="https://jam.worldlabs.ai/">2026 World Jam</a></li>
<li><a href="https://en.wikipedia.org/wiki/Global_Game_Jam">Global Game Jam - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#creative`, `#event`

---

<a id="item-22"></a>
## [Daedalus Journal Issue Promoted via Retweet](https://twitter.com/ylecun/status/2057520681214951916) ⭐️ 4.0/10

Yann LeCun retweeted Eric Topol's announcement of a new issue of Daedalus, the open-access journal of the American Academy of Arts and Sciences. This retweet highlights a multidisciplinary journal issue that may contain relevant content for the AI and science communities, but the lack of specifics limits its immediate impact. The tweet provides no details on the articles or topics covered in the new issue, making it a low-information announcement.

twitter · ylecun · May 21, 17:55

**Background**: Daedalus is a prestigious journal published by the American Academy of Arts and Sciences, covering a wide range of topics. Open-access means the articles are freely available to the public.

**Tags**: `#academic`, `#journal`, `#general`

---

<a id="item-23"></a>
## [CHI-Bench: New Benchmark for Healthcare AI Agents](https://twitter.com/StanfordAILab/status/2057202379121197160) ⭐️ 4.0/10

Stanford AI Lab and over 20 institutions announced CHI-Bench, a benchmark for evaluating AI agents on long-horizon healthcare workflows. This benchmark addresses the critical need for evaluating AI agents in complex, policy-rich healthcare environments, potentially accelerating the adoption of AI in clinical and administrative workflows. CHI-Bench includes 75 workflows across three domains: provider prior authorization, payer utilization management, and care management, using a simulator of 21 healthcare apps and a 1,279-document handbook.

twitter · StanfordAILab · May 20, 20:50

**Background**: AI agents are increasingly used to automate complex tasks, but evaluating their performance in real-world settings like healthcare remains challenging. Benchmarks like CHI-Bench provide standardized tasks and metrics to compare different AI systems. This benchmark focuses on long-horizon, policy-driven workflows that require reasoning over multiple steps and documents.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.16679">[2605.16679] CHI-Bench: Can AI Agents Automate End-to-End ...</a></li>
<li><a href="https://actava.ai/benchmarks/docs">Docs · Introduction | actAVA Benchmarks</a></li>
<li><a href="https://www.youtube.com/watch?v=Zyq2tMnBaIA">CHI-Bench: New Benchmark for Healthcare Agents - YouTube (PDF) ChiBench: a Benchmark Suite for Testing Electronic ... actava-ai/chi-bench - GitHub Claude, GPT, Gemini Agents Fail 72% of U.S. Healthcare ...</a></li>

</ul>
</details>

**Tags**: `#benchmark`, `#health systems`, `#research collaboration`

---

<a id="item-24"></a>
## [AI as the Next Shift in Mechanical Design](https://twitter.com/MecAgent/status/2057149726672208016) ⭐️ 3.0/10

A tweet from @MecAgent highlights that just as CAD replaced hand drafting, AI is now poised to transform mechanical design by accelerating workflows and automating repetitive tasks. This observation underscores a potential paradigm shift in engineering, where AI could significantly boost productivity and enable more complex designs, affecting CAD designers and engineers worldwide. The tweet references the historical transition from hand drafting to CAD and suggests AI will help engineers go faster, automate tedious work, and design further, but provides no specific technical details or examples.

twitter · MecAgent · May 20, 17:21

**Background**: Before CAD, engineers used drawing boards, pencils, and rulers to create technical drawings by hand. CAD (Computer-Aided Design) revolutionized this process by enabling digital creation, editing, and simulation. AI is now being integrated into CAD tools to automate routine tasks, optimize designs, and generate alternatives, representing the next evolutionary step.

**Tags**: `#CAD`, `#AI`, `#mechanical design`

---

<a id="item-25"></a>
## [Tweet Expresses Excitement About Space Robots](https://twitter.com/lukas_m_ziegler/status/2057089652834590839) ⭐️ 3.0/10

A Twitter user posted a brief, non-technical tweet expressing excitement about robots in space, with no specific details or context. This tweet has low engagement and lacks substantive content, so it does not represent a significant development in robotics or space technology. The tweet is vague and does not reference any specific mission, robot, or technology; it is merely a casual expression of interest.

twitter · lukas_m_ziegler · May 20, 13:22

**Tags**: `#robotics`, `#space`

---

<a id="item-26"></a>
## [Twitter Post Lists YouTube Channels for Tech Skills](https://twitter.com/RodmanAi/status/2057324846535901388) ⭐️ 3.0/10

A Twitter user shared a list of YouTube channels covering SQL, Excel, Statistics, Math, Python, Data Analysis, and Machine Learning. This provides a quick reference for learners seeking free, high-quality resources to build technical skills in data and AI fields. The post includes seven categories with one channel each, but the specific channel names are not disclosed; only shortened URLs are provided.

twitter · RodmanAi · May 21, 04:57

**Background**: YouTube is a popular platform for self-paced learning, with many channels offering tutorials on programming, data analysis, and machine learning. Such curated lists help beginners discover reputable educators.

**Tags**: `#YouTube`, `#tech skills`, `#learning resources`

---

<a id="item-27"></a>
## [20 Remote Job Sites Paying in USD](https://twitter.com/RodmanAi/status/2057025456482947547) ⭐️ 3.0/10

A Twitter thread by @RodmanAi lists 20 websites for finding remote jobs that pay in US dollars, but provides no descriptions or analysis of the sites. This list may help job seekers find remote work opportunities with USD compensation, but the lack of context reduces its practical value. The thread includes only URLs, with no site names or descriptions, making it difficult to evaluate the quality or legitimacy of each platform.

twitter · RodmanAi · May 20, 09:07

**Background**: Remote jobs paying in USD are attractive to workers in countries with weaker currencies, as they offer higher purchasing power. Many platforms like Upwork, Toptal, and Remote OK specialize in such opportunities, but this list does not specify which sites are included.

**Tags**: `#remote jobs`, `#job search`, `#career`

---

<a id="item-28"></a>
## [Google Cloud Partners Validate Gemini 3.5](https://twitter.com/GoogleDeepMind/status/2057137688353071491) ⭐️ 2.0/10

Google Cloud announced partnerships with leading organizations to validate the Gemini 3.5 series within their own environments, as retweeted by GoogleDeepMind. This validation signals enterprise readiness for Gemini 3.5, which combines frontier intelligence with agentic capabilities, potentially accelerating adoption in production environments. The announcement lacks specific partner names or validation results, and the tweet has low engagement (32 retweets), indicating limited immediate impact.

twitter · GoogleDeepMind · May 20, 16:33

**Background**: Gemini 3.5 is Google's latest model series unveiled at Google I/O 2026, featuring enhanced agentic and coding capabilities. Google Cloud's validation program helps ensure models meet enterprise requirements before widespread deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3.5: frontier intelligence with action - The Keyword</a></li>
<li><a href="https://llm-stats.com/models/gemini-3.5-flash">Gemini 3.5 Flash Benchmarks, Pricing & Context Window</a></li>
<li><a href="https://noqta.tn/en/news/google-io-2026-gemini-35-agent-tools">Google I/O 2026: Gemini 3.5 Series and Antigravity 2.0 Usher ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Google`, `#Gemini`, `#partnership`

---

<a id="item-29"></a>
## [Yann LeCun Retweets January 6 Slush Fund Article](https://twitter.com/ylecun/status/2057579660976746761) ⭐️ 2.0/10

Yann LeCun retweeted a post by Mike Levin linking to a New York Times article about a January 6th slush fund, which refers to a $1.776 billion taxpayer-funded fund created by President Trump to support January 6 rioters and allies. This retweet brings attention to a controversial political issue involving alleged misuse of taxpayer funds, though it is not directly relevant to software engineering or AI research, which are LeCun's primary areas. The slush fund stems from a settlement between Trump and the IRS, and a bill called the SLUSH Fund Act has been introduced to tax it. Lawsuits have been filed by January 6 police officers alleging presidential corruption.

twitter · ylecun · May 21, 21:49

**Background**: The January 6th slush fund refers to a $1.776 billion fund created by President Trump from an IRS settlement, intended to support individuals involved in the January 6 Capitol attack and other political allies. Critics argue it is a corrupt use of taxpayer money.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thebulwark.com/p/of-slush-funds-and-suckups-trump-irs-settlement-weaponization-january-6-cornyn-paxton-massie-republicans-gop">Of Slush Funds and Suckups</a></li>
<li><a href="https://mikethompson.house.gov/newsroom/press-releases/thompson-ways-means-democrats-introduce-bill-tax-presidents-corrupt-slush">THOMPSON, WAYS & MEANS DEMOCRATS INTRODUCE BILL TO TAX PRESIDENT’S CORRUPT SLUSH FUND FOR JANUARY 6 RIOTERS | Representative Mike Thompson</a></li>
<li><a href="https://www.theguardian.com/us-news/2026/may/20/jan-6-police-sue-trump-anti-weaponization-fund">January 6 officers sue Trump over $1.8bn fund, alleging ‘presidential corruption’ | US politics | The Guardian</a></li>

</ul>
</details>

**Tags**: `#politics`, `#news`

---

<a id="item-30"></a>
## [Yann LeCun Retweets Political NYT Piece](https://twitter.com/ylecun/status/2057474779779834226) ⭐️ 2.0/10

Yann LeCun retweeted a post by Mike Levin that recommends a New York Times article about political events, but the tweet itself contains no technical or academic content. This tweet has low relevance to the technical community and does not contribute to academic or technological discourse. The tweet is a retweet with a score of 2.0/10 due to its political nature and lack of technical depth.

twitter · ylecun · May 21, 14:53

**Tags**: `#politics`, `#news`, `#twitter`

---

<a id="item-31"></a>
## [Retweet Praises France's Sovereignty and Nuclear Deterrent](https://twitter.com/ylecun/status/2057363332210868325) ⭐️ 2.0/10

Yann LeCun retweeted a post by @marcosagusstinn stating that France is one of the few European countries that truly understood sovereignty by building its own nuclear deterrent. This retweet highlights a political perspective on national sovereignty and defense, but it is off-topic for a technical audience focused on software engineering, AI/ML, or systems research. The original tweet emphasizes France's independent nuclear capability as a symbol of sovereignty. The retweet by Yann LeCun, a prominent AI researcher, may surprise some followers expecting technical content.

twitter · ylecun · May 21, 07:30

**Tags**: `#politics`, `#sovereignty`, `#nuclear`

---

<a id="item-32"></a>
## [Yann LeCun Retweets NYT Opinion on Spending](https://twitter.com/ylecun/status/2057361496737272304) ⭐️ 2.0/10

Yann LeCun retweeted a New York Times opinion piece criticizing the president's spending policies, stating that Americans should be clear-eyed about the president taking their money and showering it on unspecified recipients. This retweet is off-topic for technical and academic content curation, as it focuses on US politics rather than software engineering, AI/ML, or systems research. The tweet is a retweet with no additional commentary from LeCun, and the original opinion piece is behind a paywall. The score is 2.0/10 due to low relevance.

twitter · ylecun · May 21, 07:22

**Tags**: `#politics`, `#news`, `#off-topic`

---

<a id="item-33"></a>
## [Low-Quality Tweet: 'Wrong Side of History' Quote](https://twitter.com/ylecun/status/2057357559468593655) ⭐️ 2.0/10

Yann LeCun retweeted a quote from @Microinteracti1 stating 'The Wrong Side of History Has a Very Specific Smell,' with no additional context or technical substance. This tweet has no technical or academic value and does not contribute to meaningful discourse in AI or technology. The tweet is truncated and appears to be a quote or meme, lacking any substantive information or discussion.

twitter · ylecun · May 21, 07:07

**Tags**: `#low-quality`, `#off-topic`, `#twitter`

---

<a id="item-34"></a>
## [Trump Censorship Claim and US Press Freedom Ranking](https://twitter.com/ylecun/status/2057355497498357921) ⭐️ 2.0/10

A tweet by Yann LeCun retweeting Anders Aslund claims that Trump has successfully censored most major US media, citing the US ranking #64 on the World Press Freedom Index. This claim highlights ongoing debates about press freedom in the US and the impact of political leadership on media independence, which is relevant to discussions on democratic institutions and information integrity. The World Press Freedom Index, published by Reporters Without Borders, ranks 180 countries based on pluralism, media independence, self-censorship, and other criteria. The US ranking has fluctuated in recent years, with critics pointing to actions by both Trump and Biden administrations affecting press freedom.

twitter · ylecun · May 21, 06:59

**Background**: The World Press Freedom Index (WPFI) is an annual ranking by Reporters Without Borders that assesses the level of press freedom in countries based on criteria such as pluralism, media independence, and self-censorship. The US has seen its ranking decline in recent years, with some attributing this to political pressure on media and legal actions against journalists. The tweet references a specific claim about Trump's censorship, which is part of a broader debate about government influence on media.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_Press_Freedom_Index">World Press Freedom Index - Wikipedia</a></li>
<li><a href="https://rsf.org/en/index">Index | RSF</a></li>
<li><a href="https://thehill.com/policy/technology/5801022-doj-settlement-social-media/">Trump administration settles social media censorship case have any of trumps media censorships stuck or have the... Top Stories USA: 8 ways Trump is shrinking the space for press freedom ... Trump's moves against media outlets mirror authoritarian ... Trump ramps up bullying and censorship efforts against media</a></li>

</ul>
</details>

**Tags**: `#politics`, `#media`, `#press freedom`

---

<a id="item-35"></a>
## [Low-Effort Tweet Repeating 'vibe cad'](https://twitter.com/adamdotnew/status/2057266306907525394) ⭐️ 1.0/10

A tweet by @adamdotnew simply repeats the phrase 'vibe cad' three times with no additional context or technical content. This tweet has no significance; it is a low-effort, noise-level post with minimal engagement and no substantive discussion. The tweet received a score of 1.0/10 due to its repetitive nature and lack of technical depth or novelty.

twitter · adamdotnew · May 21, 01:04

**Tags**: `#low-quality`, `#noise`, `#twitter`

---

<a id="item-36"></a>
## [Political Tweet Unrelated to Tech](https://twitter.com/ylecun/status/2057584047170175083) ⭐️ 1.0/10

Yann LeCun retweeted a post from the California governor accusing Republicans of running a criminal enterprise, which is a political statement with no technical content. This tweet is irrelevant to the technical community and does not contribute to discussions in AI, ML, or software engineering. The tweet is a retweet of a political accusation and has a relevance score of 1.0/10 for technical topics.

twitter · ylecun · May 21, 22:07

**Tags**: `#politics`, `#off-topic`

---