---
layout: default
title: "Horizon Summary: 2026-09-25 (EN)"
date: 2026-09-25
lang: en
---

> From 45 items, 41 important content pieces were selected

---

1. [Anthropic to Resume Charging for Safeguard-Blocked Claude Requests](#item-1) ⭐️ 8.0/10
2. [Duke's Cartesian Hand Uses Seven Prismatic Joints, No Rotation](#item-2) ⭐️ 7.0/10
3. [SpaceX Completes Launch Rehearsal Ahead of Starship Flight 14](#item-3) ⭐️ 7.0/10
4. [MotionJEPA Targets Slow-Feature Bias in JEPA World Models](#item-4) ⭐️ 7.0/10
5. [Stanford AI Lab Introduces PhilosophyBench for AI Philosophical Reasoning](#item-5) ⭐️ 7.0/10
6. [Stanford AI Lab Introduces Matryoshka Attribution Method](#item-6) ⭐️ 7.0/10
7. [Stanford AI Lab Introduces Real-Time EXPO-FT for Real-Time VLA Policies](#item-7) ⭐️ 7.0/10
8. [TANGO: Whole-Body VLA Model for 29-DoF Humanoid Navigation at CoRL 2026](#item-8) ⭐️ 7.0/10
9. [2.3B MoE Hybrid Mamba Matches Llama-3.2-3B with <1% Compute](#item-9) ⭐️ 7.0/10
10. [Anthropic says claude.ai got 3x faster in two weeks](#item-10) ⭐️ 7.0/10
11. [Gemini 3.8 Live with Live Avatar reaches general availability in Gemini Enterprise](#item-11) ⭐️ 6.0/10
12. [TJ-FlyingFish: China's drone that flies and swims](#item-12) ⭐️ 6.0/10
13. [Researcher asks where value shifts for robotics labs after Astra](#item-13) ⭐️ 6.0/10
14. [Stanford AI Lab Highlights CLM-8B, an Ultra-Fast System One Model](#item-14) ⭐️ 6.0/10
15. [Stanford AI Lab Amplifies Navier-Stokes Breakthrough and AI Agent Implications](#item-15) ⭐️ 6.0/10
16. [Chelsea Finn shares latency-handling trick for RL on dynamic tasks](#item-16) ⭐️ 6.0/10
17. [Single attention head found important across five in-context learning task families](#item-17) ⭐️ 6.0/10
18. [Yann LeCun Retweets Scientist's Critique of AI Hype](#item-18) ⭐️ 5.0/10
19. [Yann LeCun boosts talk by Navier-Stokes mathematician Tristan Buckmaster](#item-19) ⭐️ 5.0/10
20. [Adam Makes Opus 5.5 Its Default Model, Claiming Cheaper CAD Generation](#item-20) ⭐️ 4.0/10
21. [In-person summits still matter as physical AI accelerates](#item-21) ⭐️ 4.0/10
22. [Robotiq ROS 2 and Isaac Sim drivers built by community volunteers](#item-22) ⭐️ 4.0/10
23. [SpaceX Moves Ship 41 to Starbase Launch Pad](#item-23) ⭐️ 4.0/10
24. [Yann LeCun Amplifies Story of Ex-Anthropic Researcher's AI Fears](#item-24) ⭐️ 4.0/10
25. [Stanford AI Lab retweets teaser about System 1 models and Jev](#item-25) ⭐️ 4.0/10
26. [Twitter Thread Lists 10 Open-Source Repos for AI Inference Stacks](#item-26) ⭐️ 4.0/10
27. [Twitter Thread Lists 10 Free GitHub Repos for Python and AI Learning](#item-27) ⭐️ 4.0/10
28. [Adam AI CAD Copilot Adds Direct Rhino Integration](#item-28) ⭐️ 3.0/10
29. [SpaceX Dragon arrives at Pad 40 for Crew-13 ISS mission](#item-29) ⭐️ 3.0/10
30. [Yann LeCun Retweets Truncated AI Safety Commentary](#item-30) ⭐️ 3.0/10
31. [Yann LeCun Retweets Paris Hiring Call for ML PhD Students and Post-Docs](#item-31) ⭐️ 3.0/10
32. [Hugging Face CEO Briefs UN Security Council on AI](#item-32) ⭐️ 3.0/10
33. [Yann LeCun Opens NYU CILVR Seminar with Talk on World Models](#item-33) ⭐️ 3.0/10
34. [Stanford AI Lab retweets project on recovering traits from data](#item-34) ⭐️ 3.0/10
35. [UC Berkeley Recruits Postdocs for Bakar Computational Program](#item-35) ⭐️ 3.0/10
36. [Anthropic clarifies Claude Code cloud session billing and one-time credits](#item-36) ⭐️ 3.0/10
37. [Twitter Thread Lists 20 Projects Built on TypeSafe's Jev Model](#item-37) ⭐️ 3.0/10
38. [Promotional Thread Lists 12 JEV Skills for AI Agent Setups](#item-38) ⭐️ 3.0/10
39. [MecAgent Promotes Copilot V2.0.0 for SolidWorks 2026 Using GPT-6 Astra](#item-39) ⭐️ 2.0/10
40. [Link-only tweet with no context offers no technical value](#item-40) ⭐️ 1.0/10
41. [Humorous Tweet Mocks England's 'Football's Coming Home' Slogan](#item-41) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [Anthropic to Resume Charging for Safeguard-Blocked Claude Requests](https://twitter.com/ClaudeDevs/status/2103170368794185758) ⭐️ 8.0/10

Anthropic announced via its @ClaudeDevs account that it will resume charging for requests that its safeguards block before Claude responds, but only in three categories with low false positive rates: biology, distillation attacks, and frontier LLM development. The company said it has observed coordinated attacks on its systems in recent weeks. This policy change shifts the cost of blocked requests back onto developers, which could deter abuse such as model distillation while also raising concerns about billing for requests that never receive a response. It signals that Anthropic is treating distillation and frontier-model development as security threats rather than ordinary usage. Charging applies only to requests blocked before Claude responds, and only in the three named low-false-positive categories; Anthropic cited coordinated attacks as part of the rationale. The announcement did not specify exact pricing, detection thresholds, or how developers can appeal a blocked-and-charged request.

twitter · ClaudeDevs · Sep 24, 17:11

**Background**: Distillation attacks are systematic efforts to extract capabilities from a frontier AI model by querying it at scale, so a competitor can train a similar model at lower cost; Anthropic has previously published research on detecting and preventing them. Frontier LLM development refers to building the most advanced, cutting-edge models, which typically requires enormous compute and data. AI safeguards are automated filters that block potentially harmful or policy-violating requests, and their false positive rate measures how often they wrongly block legitimate use.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://www.iiss.org/online-analysis/cyber-power-matrix/2026/05/ai-distillation-attacks-in-the-uschina-contest/">AI distillation attacks in the US–China contest</a></li>
<li><a href="https://www.datacamp.com/blog/frontier-models">Frontier Models Explained: What Defines the Cutting Edge of AI | DataCamp</a></li>

</ul>
</details>

**Discussion**: The announcement drew substantial engagement, with 2,331 likes and 341 replies, indicating strong developer interest. Discussion likely centers on the fairness of charging for blocked requests and on the security implications of the disclosed coordinated attacks.

**Tags**: `#Anthropic`, `#Claude`, `#AI safety`, `#API pricing`, `#security`

---

<a id="item-2"></a>
## [Duke's Cartesian Hand Uses Seven Prismatic Joints, No Rotation](https://twitter.com/lukas_m_ziegler/status/2103135650673295592) ⭐️ 7.0/10

The General Robotics Lab at Duke University has introduced the Cartesian Hand, a 7-DoF end-effector in which every joint is prismatic, meaning all motion is purely linear with no rotary articulation anywhere in the hand. It uses two independently actuated parallel grippers that can hold one part of an object while moving another. This design is a counterintuitive departure from conventional dexterous hands, which typically rely on revolute joints to mimic human finger articulation. If it proves capable of in-hand manipulation, it could offer a simpler, more robust mechanical architecture for robotic grasping and assembly tasks. The hand has seven joints total, combining two stacked parallel grippers with four sliding fingertips, and its two grippers are independently actuated so they can grasp and reposition different parts of an object simultaneously. The trade-off is that purely linear joints may limit the range of orientations and dexterous poses achievable compared with revolute-joint designs.

twitter · lukas_m_ziegler · Sep 24, 14:53

**Background**: A prismatic joint is a one-degree-of-freedom kinematic pair that constrains two bodies to slide along a common axis without rotating, often called a slider or sliding pair. Most robot arms and hands use revolute joints, which rotate, because they mimic human joints and offer wide ranges of motion. Parallel grippers, which keep their fingers parallel throughout opening and closing, are a common industrial end-effector for pick-and-place tasks. The Cartesian Hand combines these ideas in an unusual way, building an entire hand from linear joints only.

<details><summary>References</summary>
<ul>
<li><a href="https://generalroboticslab.com/cartesian_handv1">The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers</a></li>
<li><a href="https://generalroboticslab.com/robots">Duke University | Discovery Robotics Research - General Robotics Lab</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prismatic_joint">Prismatic joint - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#mechanical-design`, `#grippers`, `#prismatic-joints`, `#duke-university`

---

<a id="item-3"></a>
## [SpaceX Completes Launch Rehearsal Ahead of Starship Flight 14](https://twitter.com/SpaceX/status/2103230238390173995) ⭐️ 7.0/10

SpaceX announced on X that it has completed the launch rehearsal for Starship Flight 14, with the full stack now assembled at Starbase. The flight is on track for Monday, September 28, pending regulatory approval, with a 75-minute launch window opening at 7:15 a.m. local time. Flight 14 is planned as the first operational flight of the Starship system, including its first operational Starlink deployment and first attempt at a sustained orbital trajectory. Success would mark a major step toward commercializing the world's most powerful rocket and expanding SpaceX's satellite internet constellation. The launch will use a Starship-Super Heavy v3 rocket from Pad 2 at Starbase, Texas, and the ship (Ship 41) has already completed single-engine and six-engine static fire tests. The mission remains contingent on regulatory approval, and the launch window opens at 7:15 a.m. for 75 minutes.

twitter · SpaceX · Sep 24, 21:08

**Background**: Starship is SpaceX's fully reusable super-heavy-lift launch system, consisting of the Super Heavy booster and the Starship upper stage, designed to carry crew and cargo to Earth orbit, the Moon, and Mars. A launch rehearsal, or wet dress rehearsal, involves loading propellant and running through countdown procedures to validate the vehicle and ground systems before an actual launch. Flight 14 follows a series of test flights that have progressively demonstrated booster recovery, ship reentry, and in-space maneuvers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starship_flight_14">Starship flight 14</a></li>
<li><a href="https://www.spacex.com/launches/starship-flight-14">Starship Flight 14 - SpaceX</a></li>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacexs-starship-megarocket-aces-launch-rehearsal-ahead-of-1st-orbital-test-flight-video">SpaceX's Starship megarocket aces launch rehearsal ahead of 1st orbital ...</a></li>

</ul>
</details>

**Discussion**: The announcement generated strong engagement with nearly 13,000 likes and over 1,400 retweets, reflecting high community interest in the upcoming flight. However, the brief update lacked technical depth, and replies largely consisted of excitement and questions about the launch date and regulatory approval.

**Tags**: `#SpaceX`, `#Starship`, `#spaceflight`, `#rocket launch`, `#aerospace`

---

<a id="item-4"></a>
## [MotionJEPA Targets Slow-Feature Bias in JEPA World Models](https://twitter.com/ylecun/status/2102935861243625476) ⭐️ 7.0/10

A team led by Markus Karmann released MotionJEPA, a new model designed to fix the tendency of JEPA-style world models to learn slow, simple features. Yann LeCun amplified the release by retweeting it, signaling its relevance to the self-supervised learning community. JEPA-style world models are central to Yann LeCun's vision for self-supervised learning and robotics, so fixing their bias toward slow features could improve how these models capture motion and temporal dynamics. This matters for researchers working on video understanding, planning, and embodied AI. The paper is titled "MotionJEPA: Preventing Temporal Feature Collapse by Capturing Visual Changes in Latent Space" and is credited to Markus Karmann and 12 other authors. A Hugging Face Space for viewing MotionJEPA representations has also been shared.

twitter · ylecun · Sep 24, 01:39

**Background**: JEPA (Joint-Embedding Predictive Architecture) is a self-supervised approach that learns by predicting missing or future parts of an input in a latent representation space rather than reconstructing raw pixels. Meta's V-JEPA 2 demonstrated that such world models can support video understanding, prediction, and zero-shot robot planning. A known limitation is that these models tend to favor slow, invariant features, which can cause them to miss fast visual changes and temporal dynamics.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.23881">[2609.23881] MotionJEPA : Preventing Temporal Feature Collapse by...</a></li>
<li><a href="https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/">Introducing the V-JEPA 2 world model and new benchmarks for physical reasoning</a></li>
<li><a href="https://huggingface.co/spaces/HongzeFu/MotionJEPA-representation-view">MotionJEPA Representation View - a Hugging Face Space by...</a></li>

</ul>
</details>

**Tags**: `#JEPA`, `#world models`, `#self-supervised learning`, `#MotionJEPA`, `#Yann LeCun`

---

<a id="item-5"></a>
## [Stanford AI Lab Introduces PhilosophyBench for AI Philosophical Reasoning](https://twitter.com/StanfordAILab/status/2103236663317295515) ⭐️ 7.0/10

Stanford AI Lab and Stanford HCI announced PhilosophyBench, described as the first independent, large-scale benchmark for evaluating AI models on philosophical reasoning tasks. The announcement was shared by Sebastian Thrun via a retweet from the @StanfordAILab account. Philosophical reasoning is a relatively underexplored area in AI evaluation, so a dedicated large-scale benchmark could push models beyond standard logical deduction and multi-step inference tests. It may influence how researchers and developers measure higher-order reasoning abilities in future AI systems. The benchmark is positioned as independent and large-scale, and it comes from Stanford AI Lab together with Stanford HCI, though specific task counts, scoring methodology, and model results were not included in the available announcement text.

twitter · StanfordAILab · Sep 24, 21:34

**Background**: AI benchmarks are standardized tests used to compare how well models perform on specific capabilities such as reasoning, language understanding, coding, and tool use. Existing reasoning leaderboards tend to focus on logical deduction and multi-step inference, while philosophical reasoning—covering areas like ethics, epistemology, and argument analysis—has received less systematic evaluation. PhilosophyBench aims to fill that gap with an independent, large-scale evaluation suite from Stanford.

<details><summary>References</summary>
<ul>
<li><a href="https://hai.stanford.edu/">Stanford HAI: Home</a></li>
<li><a href="https://www.evidentlyai.com/blog/ai-benchmarks">25 AI benchmarks: examples of AI models evaluation</a></li>

</ul>
</details>

**Tags**: `#AI benchmark`, `#philosophy`, `#AI evaluation`, `#Stanford`, `#reasoning`

---

<a id="item-6"></a>
## [Stanford AI Lab Introduces Matryoshka Attribution Method](https://twitter.com/StanfordAILab/status/2102830122219008045) ⭐️ 7.0/10

Stanford AI Lab researchers introduced Matryoshka Attribution (MAttr), a new attribution method that uses gradient descent to identify which parts of a neural network's input are most important for its predictions. The method parametrizes a mask with a differentiable sigmoid function and learns it through mask learning, as described in a newly released paper. Attribution methods are central to interpretability research, helping researchers and practitioners understand and debug neural network decisions. A gradient descent-based approach from a prominent lab like Stanford AI Lab could offer a more flexible or accurate alternative to existing gradient-based attribution techniques, potentially influencing how explainability is done in deep learning. The method, called Matryoshka Attribution (MAttr), is a mask learning approach that parametrizes the mask with a simple differentiable sigmoid top, allowing gradient descent to optimize which input parts are selected. The tweet announcing the paper is truncated and lacks detailed discussion, so full technical specifics and limitations are not yet available from the announcement alone.

twitter · StanfordAILab · Sep 23, 18:39

**Background**: Attribution methods in neural networks aim to identify which subset of an input is relevant to a particular decision, a core problem in explainable AI (XAI). Gradient-based attribution techniques use gradients—partial derivatives of the model's prediction with respect to its inputs—to assign influence to input features, and they are widely used because of their efficiency and axiomatic grounding. Matryoshka-style approaches typically involve nested or hierarchical representations, though the exact meaning in this new method is not fully detailed in the truncated announcement.

<details><summary>References</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2609.25518">Matryoshka attribution : Learning to attribute language... | alphaXiv</a></li>
<li><a href="https://arxiv.org/abs/2107.11400">[2107.11400] Robust Explainability: A Tutorial on Gradient-Based Attribution Methods for Deep Neural Networks</a></li>

</ul>
</details>

**Tags**: `#interpretability`, `#attribution`, `#machine learning`, `#research`, `#gradient descent`

---

<a id="item-7"></a>
## [Stanford AI Lab Introduces Real-Time EXPO-FT for Real-Time VLA Policies](https://twitter.com/StanfordAILab/status/2102829915334975694) ⭐️ 7.0/10

Stanford AI Lab announced Real-Time EXPO-FT, a reinforcement learning framework for finetuning real-time vision-language-action (VLA) policies, as described in a tweet by @perryadong. The method unlocks the π0.5 model on challenging tasks and, on the Kinetix benchmark, enables a delayed policy to achieve the best performance among delayed and non-delayed methods in 10 out of 10 environments. Real-time control is a major bottleneck for deploying large VLA models on physical robots, since inference latency can make policies too slow for high-frequency control. By making RL finetuning fast and reliable for delayed policies, Real-Time EXPO-FT could help bridge the gap between powerful pretrained robot foundation models and practical, responsive robotic manipulation in the real world. Real-Time EXPO-FT builds on the earlier EXPO-FT system for stable, sample-efficient RL finetuning of pretrained VLA policies, and is specifically designed for high-frequency control where the forward pass does not fit inside the control step. The project's GitHub guidance suggests using EXPO-FT when the forward pass time fits within the control step or the environment is static, and Real-Time EXPO-FT otherwise.

twitter · StanfordAILab · Sep 23, 18:38

**Background**: Vision-language-action (VLA) models are multimodal foundation models that combine visual perception, language understanding, and action generation to let robots follow instructions. π0.5, developed by Physical Intelligence, is a VLA built on π0 that uses co-training on heterogeneous data sources to generalize robotic manipulation to entirely new environments. Reinforcement learning finetuning adapts such pretrained policies to specific tasks, but real-time deployment requires the policy to produce actions within tight control-loop deadlines.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.18207">[2609.18207] Reinforcement Learning for Real-Time Vision ...</a></li>
<li><a href="https://github.com/pd-perry/expo-ft">GitHub - pd-perry/expo-ft</a></li>
<li><a href="https://arxiv.org/abs/2504.16054">[2504.16054] ||pi;_ {0.5}$: a Vision-Language-Action Model with ... A VLA with Open-World Generalization π 0.5 : a Vision-Language-Action Model with Open-World ... π₀.₅ (Pi05) Policy · Hugging Face Physical Intelligence (π) π0.5: a Vision-Language-Action Model with Open-World ... Physical Intelligence π₀: The Robot Foundation Model ...</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#robotics`, `#vision-language-action`, `#real-time-systems`, `#embodied-ai`

---

<a id="item-8"></a>
## [TANGO: Whole-Body VLA Model for 29-DoF Humanoid Navigation at CoRL 2026](https://twitter.com/berkeley_ai/status/2103082120243823065) ⭐️ 7.0/10

Researchers introduced TANGO, a whole-body vision-language-action (VLA) model that maps RGB camera inputs directly to 29-DoF humanoid navigation control, presented as a CoRL 2026 work by Thomas Yuxin Chen and collaborators and amplified by Berkeley AI's account. It pushes VLA models beyond tabletop manipulation toward whole-body locomotion and navigation on high-DoF humanoids, a harder control problem that could accelerate general-purpose embodied agents that follow natural-language commands in real environments. TANGO's end-to-end design skips separate perception, planning, and low-level control modules by regressing 29-DoF commands straight from RGB, though the announcement gives no benchmark numbers, training data scale, or sim-to-real evaluation details.

twitter · berkeley_ai · Sep 24, 11:20

**Background**: Vision-language-action (VLA) models are multimodal foundation models that take an image or video plus a text instruction and directly output low-level robot actions, an approach pioneered by Google DeepMind's RT-2 in 2023. They are typically built by fine-tuning a vision-language model on datasets pairing visual observations and language with robot trajectories. Humanoids like the 29-DoF Unitree G1 have many joints to coordinate, making whole-body control a substantially harder problem than arm-only manipulation. CoRL (Conference on Robot Learning) is a leading annual venue for robotics and machine learning research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision-language-action_model">Vision-language-action model</a></li>
<li><a href="https://arxiv.org/html/2507.07356v3">Learning Universal Whole-Body Motion Tracker for Humanoid Robots</a></li>
<li><a href="https://www.corl.org/">CoRL 2026</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#humanoid`, `#vision-language-action`, `#embodied-ai`, `#CoRL`

---

<a id="item-9"></a>
## [2.3B MoE Hybrid Mamba Matches Llama-3.2-3B with <1% Compute](https://twitter.com/berkeley_ai/status/2102805481664487490) ⭐️ 7.0/10

Researchers announced they trained a 2.3B-parameter Mixture-of-Experts Hybrid Mamba-2 model with 360M active parameters that lands within a few points of Llama-3.2-3B on benchmarks while using less than 1% of its pre-training compute. If the claim holds, this suggests that combining MoE sparsity with Mamba-2 state-space layers can dramatically cut the compute cost of training capable small language models, which could reshape how efficiently future models are built and make strong models cheaper to produce. The model uses 2.3B total parameters but only 360M active per token, and the comparison target is the dense Llama-3.2-3B; the claim is based on landing 'within a few points' on benchmarks rather than fully matching or exceeding it, and the announcement is a brief retweet with limited detail.

twitter · berkeley_ai · Sep 23, 17:01

**Background**: Mixture-of-Experts (MoE) architectures use multiple specialized sub-networks ('experts') and route each token to only a few of them, so a model can have many parameters while activating only a fraction per token. Mamba-2 is a state-space model (SSM) that offers an efficient alternative to transformer attention, and hybrid models combine Mamba layers with a small amount of attention to balance efficiency and quality. Llama-3.2-3B is Meta's dense 3-billion-parameter model, commonly used as a baseline for small-model comparisons.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/mamba-model">What Is A Mamba Model? - IBM</a></li>
<li><a href="https://huggingface.co/docs/transformers/en/model_doc/mamba2">Mamba 2 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#MoE`, `#Mamba`, `#LLM`, `#efficient-training`, `#model-architecture`

---

<a id="item-10"></a>
## [Anthropic says claude.ai got 3x faster in two weeks](https://twitter.com/ClaudeDevs/status/2102839691154427983) ⭐️ 7.0/10

Anthropic's Claude Devs announced that claude.ai and the Claude desktop app were made roughly 3x faster during a two-week performance sprint in August. The team shared the prompts and methods they used to measure, debug, and improve performance. Latency is a major factor in user retention for AI chat products, so a 3x speedup on a flagship assistant like Claude could meaningfully improve everyday user experience and competitive positioning against rivals such as ChatGPT and Gemini. The published methodology may also help developers optimize their own AI applications. The headline 3x figure is a geometric mean across 13 measurements, so it does not mean every action became exactly three times faster. The announcement is brief and links out to external content containing the actual prompts and methods.

twitter · ClaudeDevs · Sep 23, 19:17

**Background**: Claude is Anthropic's family of large language models, and claude.ai is the company's consumer-facing chat interface. Performance work on such products typically involves reducing network round trips, optimizing rendering, and profiling slow endpoints. Measuring improvements across many different user actions requires aggregating multiple benchmarks rather than relying on a single number.

<details><summary>References</summary>
<ul>
<li><a href="https://digg.com/tech/003a7dd0-bc65-4c25-8eed-8107e26f6833">Claude ’s web and desktop apps reportedly got faster through...</a></li>
<li><a href="https://claude.ai/">Sign in to Claude , Anthropic's AI assistant for problem solvers.</a></li>

</ul>
</details>

**Discussion**: The tweet drew high engagement with over 9,000 likes and 229 replies, indicating strong community interest in the performance gains and the shared methodology. Commenters appeared eager to learn the specific prompts and techniques used.

**Tags**: `#performance`, `#claude`, `#ai`, `#optimization`, `#anthropic`

---

<a id="item-11"></a>
## [Gemini 3.8 Live with Live Avatar reaches general availability in Gemini Enterprise](https://twitter.com/GoogleDeepMind/status/2103176711479402748) ⭐️ 6.0/10

Google DeepMind retweeted Google Cloud Tech's announcement that Gemini 3.8 Live with Live Avatar is now generally available in Gemini Enterprise. The feature brings near real-time visual presence — a talking, lip-synced avatar — to Gemini's conversational AI for enterprise users. This marks Google's push to give enterprise AI agents a human-like visual interface, moving beyond text and voice into real-time video presence. It could differentiate Gemini Enterprise from competing agentic platforms as businesses deploy customer-facing and internal AI agents at scale. According to Google's documentation, Live Avatar generates real-time video of a talking avatar synchronized with synthesized speech from the gemini-3.8-live model, and it reportedly supports 97 languages. Gemini 3.8 Live is positioned as the default option for low-latency voice agent experiences without reasoning-induced delays.

twitter · GoogleDeepMind · Sep 24, 17:36

**Background**: Gemini 3.8 Live is Google's most advanced live dialogue model, launched about a week before the Live Avatar update, and is designed for natural real-time conversation. Gemini Enterprise is Google Cloud's agentic AI platform for businesses, launched on October 9, 2025, serving as an intranet search tool, conversational assistant, and platform for deploying AI agents. Live Avatar builds on the Gemini 3.8 Live launch by adding a synchronized visual presence to these conversational experiences.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/">Introducing Gemini 3.8 Live with Live Avatar</a></li>
<li><a href="https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api/configure-live-avatars">Configure live avatars | Gemini Enterprise Agent Platform</a></li>
<li><a href="https://grokipedia.com/page/Gemini_Enterprise">Gemini Enterprise</a></li>

</ul>
</details>

**Tags**: `#Google DeepMind`, `#Gemini`, `#AI agents`, `#Enterprise AI`, `#Product announcement`

---

<a id="item-12"></a>
## [TJ-FlyingFish: China's drone that flies and swims](https://twitter.com/lukas_m_ziegler/status/2103022744765968658) ⭐️ 6.0/10

Scientists in China have developed TJ-FlyingFish, a lightweight 1.6-kilogram drone that can both fly in the air and dive underwater using four rotor arms that work efficiently in both environments. Aerial-aquatic drones like TJ-FlyingFish could enable combined aerial and underwater missions such as search-and-rescue, remote sensing, and aquatic surveys, expanding what a single robotic platform can do across two very different environments. The drone uses a quadcopter-style layout with a central domed body and four arms, each carrying a motor or propeller module, and it can autonomously navigate underwater as an uncrewed underwater vehicle (UUV) as well as fly as a quadcopter.

twitter · lukas_m_ziegler · Sep 24, 07:24

**Background**: Aerial-aquatic vehicles are designed to move in both air and water, which is challenging because the two fluids have very different properties such as density and viscosity. TJ-FlyingFish was developed by researchers in China and presented in a paper (arXiv:2301.12344) and at ICRA 2023, with coverage by outlets like New Atlas.

<details><summary>References</summary>
<ul>
<li><a href="https://newatlas.com/drones/tj-flyingfish-aerial-underwater-drone">TJ-FlyingFish drone flies through the air and "swims" underwater</a></li>
<li><a href="https://arxiv.org/abs/2301.12344">[2301.12344] TJ-FlyingFish: Design and Implementation of an ... CUHK announces the invention of an aerial-aquatic hybrid ... TJ-FlyingFish Drone Autonomously Swims Underwater and Flies ... TJ-FlyingFish: An Unmanned Morphable Aerial–Aquatic Vehicle ... TJ-FlyingFish flying/aquatic drone - YouTube TJ-FlyingFish: Design and Implementation of an Aerial-Aquatic ...</a></li>
<li><a href="https://www.rotordronepro.com/tj-flyingfish-drone-autonomously-swims-underwater-flies/">TJ-FlyingFish Drone Autonomously Swims Underwater and Flies ...</a></li>

</ul>
</details>

**Discussion**: The tweet received moderate engagement (254 likes, 39 retweets, 15 replies), suggesting general interest in the novel dual-environment drone, though the discussion was not deeply technical.

**Tags**: `#robotics`, `#drone`, `#bio-inspired`, `#China`, `#aerial-aquatic`

---

<a id="item-13"></a>
## [Researcher asks where value shifts for robotics labs after Astra](https://twitter.com/lukas_m_ziegler/status/2102743118969770077) ⭐️ 6.0/10

Researcher Lukas M. Ziegler posed a question on X about how the release of the frontier model GPT-6 Astra could erode the value proposition of research-only robotics labs that train their own models from scratch. The tweet, which drew 98 likes and 29 replies, asks where value will move if frontier labs keep shipping better general intelligence off the shelf. If off-the-shelf general intelligence keeps improving, robotics labs may no longer gain an edge by training their own foundation models, forcing them to compete on hardware, data, embodiment, or niche applications instead. This could reshape funding, talent, and research priorities across the AI and robotics ecosystem. The discussion is speculative and lacks concrete evidence, but it is grounded in the real release of GPT-6 Astra, which OpenAI is rolling out to a limited set of organizations and soon to ChatGPT Plus, Pro, Business, and Enterprise users via API, Azure, and AWS Bedrock. Astra reportedly uses a 'recurrent depth' or 'looped transformers' reasoning technique that obscures its chain of thought, raising monitorability concerns.

twitter · lukas_m_ziegler · Sep 23, 12:53

**Background**: GPT-6 Astra is OpenAI's latest frontier model, released in multiple variants with different intelligence, performance, and pricing tiers. Research-only robotics labs traditionally differentiate themselves by developing custom perception, planning, and control models from scratch. The rise of powerful off-the-shelf general models raises the question of whether that in-house model training still provides a durable competitive advantage.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6">GPT-6 - Wikipedia</a></li>
<li><a href="https://artificialanalysis.ai/models/releases/gpt-6-astra">GPT-6 Astra: Release Intelligence, Performance & Price</a></li>

</ul>
</details>

**Discussion**: The tweet generated moderate engagement with 98 likes and 29 replies, indicating community interest in the strategic implications of frontier models for robotics research. Sentiment appears thoughtful and speculative, with participants debating where value might shift rather than reaching firm conclusions.

**Tags**: `#AI`, `#robotics`, `#research strategy`, `#frontier models`, `#industry impact`

---

<a id="item-14"></a>
## [Stanford AI Lab Highlights CLM-8B, an Ultra-Fast System One Model](https://twitter.com/StanfordAILab/status/2103359830383808573) ⭐️ 6.0/10

Stanford AI Lab retweeted an introduction to Contrastive Language Model (CLM), specifically CLM-8B, an open Apache 2.0 System One model trained with a contrastive learning objective that connects states and actions. CLM-8B places a state head and an action head on top of a frozen Qwen3-8B encoder trained with a bidirectional InfoNCE loss, and is reported to run about 9x faster than Jev while performing on par with it on computer-use tasks. This matters because it offers an open, Apache 2.0 alternative to proprietary System One models like TypeSafe AI's Jev, potentially lowering the barrier for developers building fast, structured decision-making agents. If the claimed speed and parity hold up, it could shift how agentic systems balance latency and accuracy in real-world computer-use workflows. CLM-8B is pre-trained on 60M Nemotron Q&A pairs, mid-trained on 30M synthetic hard negatives, and post-trained on 1M agentic trajectories, and it is served behind a TypeSafe-compatible API. The reported zero-shot comparisons against Jev come with small-sample caveats, so the results should be treated as preliminary.

twitter · StanfordAILab · Sep 25, 05:43

**Background**: System One models are a class of AI models designed to make fast, intuitive, structured decisions, analogous to the fast-thinking System 1 in dual-process psychology, and they typically return typed answers and probabilities rather than free-form text. Contrastive learning is a training technique that pulls similar (positive) pairs closer in embedding space while pushing dissimilar (negative) pairs apart, often using an InfoNCE loss. CLM combines these ideas by learning a shared embedding space that links environment states to possible actions, rather than generating text token by token.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Contrastive-LM/CLM-v0.1-8B">Contrastive-LM/CLM-v0.1-8B · Hugging Face</a></li>
<li><a href="https://github.com/Contrastive-LM/CLM">GitHub - Contrastive-LM/CLM</a></li>
<li><a href="https://www.explainx.ai/blog/contrastive-language-model-clm-8b-system-one-9x-faster-than-jev-2026">Contrastive Language Model (CLM-8B): An Open System One Model ...</a></li>

</ul>
</details>

**Tags**: `#contrastive learning`, `#language models`, `#AI research`, `#Stanford AI Lab`, `#System One Model`

---

<a id="item-15"></a>
## [Stanford AI Lab Amplifies Navier-Stokes Breakthrough and AI Agent Implications](https://twitter.com/StanfordAILab/status/2102830363563422130) ⭐️ 6.0/10

Stanford AI Lab retweeted a post by Aneesh Pappu discussing a recent breakthrough in the Navier-Stokes equations and the new possibilities it opens for AI agents. The original tweet was truncated, but it points to growing excitement about how AI-driven mathematical discoveries could reshape autonomous agent capabilities. This matters because the Navier-Stokes problem is one of the Millennium Prize Problems, and an AI-assisted solution would mark a major milestone in both mathematics and AI. If AI agents can contribute to such fundamental breakthroughs, it could accelerate scientific discovery and change how researchers approach complex unsolved problems. The tweet itself is truncated and lacks technical specifics, but web search results indicate that OpenAI claimed a solution to the Navier-Stokes existence and smoothness problem on September 8, 2026, including a writeup and a formal proof in Lean. The claim has sparked controversy, with an 88-hour effort by roughly 10,000 AI agents reportedly involved.

twitter · StanfordAILab · Sep 23, 18:40

**Background**: The Navier-Stokes equations describe how fluids flow and are central to fields like weather forecasting, aerodynamics, and oceanography. The existence and smoothness problem asks whether solutions always exist without singularities in three dimensions, and it is one of the seven Millennium Prize Problems. AI agents are autonomous systems that can plan and execute tasks; recent work like AI CFD Scientist and HydroGym shows AI increasingly being applied to fluid dynamics research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_priority_controversy">Navier–Stokes priority controversy - Wikipedia</a></li>
<li><a href="https://openai.com/index/navier-stokes-solution/">On the Navier–Stokes Millennium Prize Problem - OpenAI</a></li>
<li><a href="https://www.science.org/content/article/how-ai-math-breakthrough-ignited-controversy">How an AI math breakthrough ignited a controversy | Science | AAAS</a></li>

</ul>
</details>

**Tags**: `#Navier-Stokes`, `#AI agents`, `#fluid dynamics`, `#breakthrough`, `#Stanford AI Lab`

---

<a id="item-16"></a>
## [Chelsea Finn shares latency-handling trick for RL on dynamic tasks](https://twitter.com/StanfordAILab/status/2102805898884460545) ⭐️ 6.0/10

Chelsea Finn, retweeted by Stanford AI Lab, described a technique for handling latency in reinforcement learning for dynamic tasks: building on EXPO-FT, the base vision-language-action (VLA) model is allowed to operate on older images while a separate component handles the delay. Latency is a fundamental obstacle to deploying RL-trained robot policies in the real world, since slow inference or communication delays cause actions to be based on stale observations; this approach could make VLA policies more reliable for high-frequency, dynamic control tasks. The technique builds directly on EXPO-FT, a system for stable, sample-efficient RL finetuning of pretrained VLA policies, and the related Real-Time EXPO-FT work that targets high-frequency control; the tweet itself is truncated, so full technical details are not yet available.

twitter · StanfordAILab · Sep 23, 17:02

**Background**: Vision-language-action (VLA) models are multimodal foundation models that combine vision, language, and robot actions, such as OpenVLA. Reinforcement learning (RL) finetuning can improve their reliability, but real-time control suffers when the policy acts on delayed observations. EXPO-FT is a framework for sample-efficient RL finetuning of VLA policies, and Real-Time EXPO-FT extends it to high-frequency control.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.25477">EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning ...</a></li>
<li><a href="https://pd-perry.github.io/real-time-expo-ft/">Reinforcement Learning for Real-Time Vision-Language-Action ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision–language–action_model">Vision–language–action model - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#robotics`, `#latency`, `#VLA`, `#Stanford`

---

<a id="item-17"></a>
## [Single attention head found important across five in-context learning task families](https://twitter.com/berkeley_ai/status/2102805066084384938) ⭐️ 6.0/10

A tweet from @berkeley_ai retweeting @xyVickyHu highlights a mechanistic interpretability finding that one attention head can be important across five in-context learning (ICL) task families, referencing an original in-depth thread. This suggests that certain attention heads may serve as general-purpose components for in-context learning rather than being task-specific, which could simplify how researchers understand and potentially steer transformer behavior across diverse tasks. The finding comes from a mechanistic interpretability thread and aligns with prior work on induction heads, which are specialized attention heads considered a key mechanism for in-context learning; however, the tweet provides only a brief summary without full experimental details.

twitter · berkeley_ai · Sep 23, 16:59

**Background**: Mechanistic interpretability aims to reverse-engineer the internal computations of transformer models, often by analyzing individual attention heads. In-context learning refers to a model's ability to perform a new task from examples provided in its prompt without any weight updates. Induction heads are a well-known type of attention head that implement a simple copy-and-predict pattern and are thought to underlie much of in-context learning.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lesswrong.com/posts/XGHf7EY3CK4KorBpw/understanding-llms-insights-from-mechanistic">Understanding LLMs: Insights from Mechanistic Interpretability</a></li>
<li><a href="https://arxiv.org/html/2601.04398v1">Interpreting Transformers Through Attention Head Intervention - arXiv</a></li>

</ul>
</details>

**Tags**: `#mechanistic-interpretability`, `#attention-heads`, `#in-context-learning`, `#transformers`, `#AI-research`

---

<a id="item-18"></a>
## [Yann LeCun Retweets Scientist's Critique of AI Hype](https://twitter.com/ylecun/status/2103218483785847169) ⭐️ 5.0/10

Yann LeCun, Meta's Chief AI Scientist, retweeted a post by scientist Simon Maechling arguing that AI hype has become ridiculous, while acknowledging that AI can design a molecule in seconds. The retweet drew roughly 490 retweets, signaling moderate engagement with the debate over AI's real capabilities versus inflated expectations. LeCun is one of the most prominent voices pushing back against inflated AI narratives, and his amplification of a working scientist's perspective adds weight to the argument that AI's real value lies in narrow, domain-specific tasks rather than imminent general intelligence. This matters for how researchers, investors, and the public calibrate expectations about AI in science and drug discovery. The retweeted text is truncated, but it contrasts AI's ability to design a molecule in seconds with what appears to be a cautionary follow-up about the limits of that capability. LeCun has repeatedly criticized the "religion of scaling" and argued that human-level AI remains years away, so this retweet fits his broader skepticism toward AGI hype.

twitter · ylecun · Sep 24, 20:22

**Background**: AI-driven molecule design uses generative models, such as RNNs and graph neural networks, to propose novel chemical structures in silico, potentially speeding up early-stage drug discovery. Yann LeCun is Meta's Chief AI Scientist and a Turing Award winner known for convolutional neural networks, and he has become a leading public skeptic of claims that scaling current large language models will soon yield artificial general intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://finance.yahoo.com/news/meta-chief-ai-scientist-yann-153745262.html">Meta Chief AI Scientist Yann LeCun Slams AI Hype - Yahoo Finance</a></li>
<li><a href="https://medium.com/swlh/ai-de-novo-molecule-design-aed30465e293">AI Molecule Design . Develop a generative LSTM deep... | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#hype`, `#science`, `#Twitter`, `#Yann LeCun`

---

<a id="item-19"></a>
## [Yann LeCun boosts talk by Navier-Stokes mathematician Tristan Buckmaster](https://twitter.com/ylecun/status/2102936941280821634) ⭐️ 5.0/10

Yann LeCun retweeted a post noting that NYU Courant professor Tristan Buckmaster, known for his work on the Navier-Stokes problem, gave a talk at NYU's new "Mathematics in the Age of AI" seminar. NYU Courant's own account described an "absolutely packed house" at the inaugural session. The talk signals how AI is increasingly intersecting with pure mathematics, especially after the September 2026 controversy over an AI-assisted Navier-Stokes result. LeCun's amplification brings the seminar to a much wider machine-learning audience. The tweet itself is only a brief announcement with no technical content, and engagement was moderate at roughly 166 retweets. Buckmaster is known for work on the Euler and Navier-Stokes equations, including results tied to the recent priority dispute.

twitter · ylecun · Sep 24, 01:43

**Background**: The Navier-Stokes existence and smoothness problem asks whether the equations describing fluid motion always have smooth solutions in three-dimensional space, and it is one of the Clay Mathematics Institute's seven Millennium Prize Problems. In September 2026, OpenAI claimed an AI-assisted solution for the smooth-forced case, triggering a priority dispute involving Buckmaster and Anthropic's Levent Alpöge. Buckmaster had earlier derived closely related results on the Euler equations that the AI work built upon.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier–Stokes_priority_controversy">Navier – Stokes priority controversy - Wikipedia</a></li>
<li><a href="https://cims.nyu.edu/dynamic/calendars/seminars/">Seminars | NYU Courant</a></li>

</ul>
</details>

**Tags**: `#Navier-Stokes`, `#mathematics`, `#fluid dynamics`, `#Tristan Buckmaster`, `#Yann LeCun`

---

<a id="item-20"></a>
## [Adam Makes Opus 5.5 Its Default Model, Claiming Cheaper CAD Generation](https://twitter.com/adamdotnew/status/2102813174995231039) ⭐️ 4.0/10

Adam announced that Opus 5.5 is now its default model, claiming it outperforms GPT-6 Sol by a noticeable margin and delivers performance close to GPT-6 Astra at only 20% of the cost per task. The announcement also highlights more capable CAD generation. If the claims hold up, this would make frontier-level AI capability substantially cheaper for tasks like CAD generation, potentially shifting cost-performance expectations across the AI model market. It also signals intensifying competition between Anthropic's Opus line and OpenAI's GPT-6 family. The announcement provides no benchmarks, token pricing, latency figures, or independent verification, and the comparison is framed only against GPT-6 Sol and GPT-6 Astra. The 20% cost figure is stated per task rather than per token, leaving the exact basis of the comparison unclear.

twitter · adamdotnew · Sep 23, 17:31

**Background**: Opus 5.5 is part of Anthropic's Claude Opus model line, which is positioned for demanding professional and coding work. GPT-6 Astra is OpenAI's state-of-the-art model for computer use, software engineering, and professional tasks, while GPT-6 Sol is a faster, more affordable variant built with similar training methods. Adam appears to be a platform that lets users run such models for tasks including CAD (computer-aided design) generation.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5.5">Claude Opus 5 . 5 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://openai.com/index/introducing-gpt-6-sol-and-luna/">Introducing GPT‑6 Sol and Luna - OpenAI</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI models`, `#product announcement`, `#performance comparison`, `#cost efficiency`, `#CAD generation`

---

<a id="item-21"></a>
## [In-person summits still matter as physical AI accelerates](https://twitter.com/lukas_m_ziegler/status/2102774998549078329) ⭐️ 4.0/10

Lukas M. Ziegler argued in a tweet that in-person summits remain valuable given how fast physical AI is moving, pointing to recent milestones from Skild AI, Wayve, and Dyna Robotics. He cited Skild AI crossing a $100 million revenue run rate and shipping its S1 model, Wayve starting supervised autonomous rides in London via Uber, and Dyna Robotics' recent progress. These milestones show physical AI is shifting from research demos to commercial deployment, with revenue, real-world rides, and productized robots arriving within weeks of each other. That pace raises the stakes for founders, investors, and researchers to meet in person and align on standards, safety, and go-to-market strategy. Skild AI's S1 robot foundation model can be prompted by a single demonstration video and execute the task without retraining or fine-tuning its weights, while Wayve's London service is supervised rather than fully driverless. Dyna Robotics builds commercial-grade robots for hospitality, logistics, and factory workflows and has raised $120 million.

twitter · lukas_m_ziegler · Sep 23, 15:00

**Background**: Physical AI refers to AI systems that perceive and act in the real world, such as robots and autonomous vehicles, rather than only generating text or images. Foundation models for robotics aim to let one model generalize across many tasks, similar to how large language models generalize across text. Wayve's supervised rides mean a safety operator is present, a common intermediate step before fully driverless services.

<details><summary>References</summary>
<ul>
<li><a href="https://runtimewire.com/article/skild-ai-s1-robot-model-one-video-prompt">Skild AI ships S 1 , a robot model prompted by one video</a></li>
<li><a href="https://wayve.ai/press/wayve-uber-launch-autonomous-rides/">Wayve and Uber Launch First-Ever Autonomous Rides in the UK</a></li>
<li><a href="https://www.dyna.co/">DYNA Robotics</a></li>

</ul>
</details>

**Tags**: `#physical-ai`, `#robotics`, `#autonomous-vehicles`, `#industry-news`, `#twitter`

---

<a id="item-22"></a>
## [Robotiq ROS 2 and Isaac Sim drivers built by community volunteers](https://twitter.com/lukas_m_ziegler/status/2102752347000639620) ⭐️ 4.0/10

Lukas M. Ziegler pointed out on X that the Robotiq gripper drivers for ROS 2 and Isaac Sim were written by community volunteers on their own time, not by Robotiq itself. He noted that these grippers have worked in ROS 2 and Isaac Sim for years thanks to those unpaid contributions. The post highlights how much of the robotics software ecosystem depends on unpaid volunteer labor rather than hardware vendors, which raises questions about long-term maintenance and sustainability of these drivers. It also reminds users that vendor support for open-source robotics stacks is often indirect and community-driven. The claim covers both the ROS 2 driver and the simulation models used in Isaac Sim, which volunteers reportedly wrote and have kept working over multiple years. The tweet does not specify which gripper models are covered, though Robotiq's adaptive line includes the 2F-85, 2F-140, Hand-E and 3-Finger grippers.

twitter · lukas_m_ziegler · Sep 23, 13:30

**Background**: ROS 2 is the second generation of the Robot Operating System, a widely used open-source framework for building robot software, where drivers let a robot's computer talk to hardware such as grippers. Isaac Sim is NVIDIA's robotics simulation platform built on Omniverse, used to test robots in physically accurate virtual environments before deploying them on real hardware. Robotiq is a well-known maker of adaptive and vacuum grippers for collaborative robots, and its products are common in research and industrial automation.

<details><summary>References</summary>
<ul>
<li><a href="https://robotiq.com/products/adaptive-grippers">Adaptive Grippers - Robotiq</a></li>
<li><a href="https://grokipedia.com/page/NVIDIA_Isaac_Sim">NVIDIA Isaac Sim</a></li>
<li><a href="https://grokipedia.com/page/Parameters_ROS_2">Parameters (ROS 2)</a></li>

</ul>
</details>

**Tags**: `#ROS 2`, `#robotics`, `#open source`, `#community`, `#Robotiq`

---

<a id="item-23"></a>
## [SpaceX Moves Ship 41 to Starbase Launch Pad](https://twitter.com/SpaceX/status/2102781027085320290) ⭐️ 4.0/10

SpaceX announced via its official X (Twitter) account that Ship 41, a Starship upper-stage prototype, has been moved to the launch pad at Starbase in Texas. The post included a photo link but no additional technical details about the rollout or upcoming test plans. Moving Ship 41 to the pad signals continued progress in SpaceX's Starship test campaign, as each rollout typically precedes static fire tests and eventual flight attempts. This matters for the broader space industry because Starship is central to NASA's Artemis lunar plans and SpaceX's ambitions for fully reusable, high-cadence orbital launches. Ship 41 is a Block 3 (v3) Starship upper-stage prototype, the third of its kind, first spotted in May 2025 and previously loaded with propellants for a six-engine static fire test. The rollout was to Pad B at Starbase, one of two launch pads at the site, though SpaceX did not specify the exact test timeline.

twitter · SpaceX · Sep 23, 15:23

**Background**: Starship is SpaceX's fully reusable, two-stage super-heavy-lift rocket, consisting of the Super Heavy booster and the Starship upper stage (also called Ship). Starbase, located near Boca Chica, Texas, is SpaceX's primary Starship development, testing, and launch facility, and it became an incorporated city in May 2025. SpaceX routinely moves Starship prototypes to the launch pad for ground testing before flight attempts.

<details><summary>References</summary>
<ul>
<li><a href="https://starship-spacex.fandom.com/wiki/Ship_41_(S41)">Ship 41 (S41) - Starship SpaceX Wiki - Fandom</a></li>
<li><a href="https://nextspaceflight.com/starship/hardware/68/">Ship 41 | Starship - Next Spaceflight</a></li>
<li><a href="https://en.wikipedia.org/wiki/Starbase_spacex">Starbase spacex</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starship`, `#space exploration`, `#launch pad`, `#Starbase`

---

<a id="item-24"></a>
## [Yann LeCun Amplifies Story of Ex-Anthropic Researcher's AI Fears](https://twitter.com/ylecun/status/2103349162326831407) ⭐️ 4.0/10

Yann LeCun retweeted a PirateWires post stating that former Anthropic researcher Jacob Coxon became a media star after publicly voicing his fears about AI, with the tweet drawing roughly 787 retweets. The amplification by a Turing Award-winning AI scientist like LeCun pushes the debate over AI existential risk further into mainstream tech discourse, intensifying the divide between safety-focused researchers and those who see such warnings as alarmist. Coxon is a Cambridge-trained researcher who worked at both OpenAI and Anthropic, including on GPT-4o, and reportedly resigned accusing the labs of 'gambling with our lives' and warning that AI could 'kill us all by the end of the decade.'

twitter · ylecun · Sep 25, 05:01

**Background**: Anthropic is an AI safety and research company known for building reliable, interpretable and steerable AI systems, and its researchers frequently debate the risks of increasingly capable models. Jacob Coxon's public resignation and warnings fit into a broader industry conversation about whether frontier labs are racing toward self-improving superintelligence too quickly.

<details><summary>References</summary>
<ul>
<li><a href="https://www.indiatimes.com/trending/who-is-jacob-coxon-ai-researcher-quits-anthropic-after-warning-the-race-to-self-improving-superintelligence-could-spiral-out-of-control/articleshow/133951552.html">Who is Jacob Coxon ? AI researcher quits Anthropic after warning the...</a></li>
<li><a href="https://www.tuko.co.ke/world/639222-ai-researcher-quits-job-fears-robots-wipe-human-race/">AI Researcher Quits Job Over Fears Robots Will Wipe... - Tuko.co.ke</a></li>
<li><a href="https://www.anthropic.com/research">Research - Anthropic</a></li>

</ul>
</details>

**Discussion**: The retweet generated significant engagement, with many users debating whether Coxon's warnings reflect genuine insider concern or media-driven alarmism, and LeCun's own known skepticism toward AI doom narratives colored how the post was received.

**Tags**: `#AI safety`, `#AI fears`, `#Anthropic`, `#social media`, `#AI discourse`

---

<a id="item-25"></a>
## [Stanford AI Lab retweets teaser about System 1 models and Jev](https://twitter.com/StanfordAILab/status/2103173908673478842) ⭐️ 4.0/10

The Stanford AI Lab (@StanfordAILab) retweeted a post by @drmapavone noting that System 1 models have generated significant excitement, particularly after the introduction of #Jev, though the tweet text is truncated and gives no further details. The retweet signals that a prominent academic lab is paying attention to TypeSafe AI's newly launched System One model class, which could push the AI industry toward specialized decision-making models rather than relying solely on chat-oriented LLMs. Jev is TypeSafe AI's first System One model, released in limited early access on September 15, 2026 alongside a $40 million seed round led by DCVC, and it returns typed choices, scores, or probabilities in 70–500ms instead of chat responses.

twitter · StanfordAILab · Sep 24, 17:25

**Background**: System 1 models are a class of AI models designed to make fast, structured decisions that software can consume directly, drawing on psychologist Daniel Kahneman's distinction between fast intuitive System 1 thinking and slower deliberate System 2 reasoning. TypeSafe AI, a San Francisco-based company founded in 2024, spent two years in stealth before announcing Jev as its first such model. Unlike traditional LLMs that generate free-form text, Jev is built to return calibrated, typed outputs without hallucinations.

<details><summary>References</summary>
<ul>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Jev_(AI_model)">Jev (AI model) - Wikipedia</a></li>
<li><a href="https://jevai.net/articles/what-is-system-one-jev/">Jev: The System One Model for Fast, Calibrated AI Decisions</a></li>

</ul>
</details>

**Tags**: `#AI`, `#System 1 models`, `#Jev`, `#Stanford AI Lab`, `#Twitter`

---

<a id="item-26"></a>
## [Twitter Thread Lists 10 Open-Source Repos for AI Inference Stacks](https://twitter.com/RodmanAi/status/2103063979954516476) ⭐️ 4.0/10

A Twitter thread by @RodmanAi curated 10 open-source GitHub repositories for building an AI inference stack, explicitly naming SIE and vLLM among them. The thread frames each project as worth bookmarking, though it only provides brief one-line descriptions and links. As LLM deployment moves from experimentation to production, developers increasingly need to assemble their own inference stacks rather than rely on closed APIs, and curated lists like this lower the discovery cost. The inclusion of both a multi-model agent-serving layer (SIE) and a high-throughput LLM server (vLLM) reflects the growing split between general model serving and agent-specific workloads. SIE (Superlinked Inference Engine) is described as a single inference layer for multiple AI models and agent workloads, while vLLM is highlighted for high-throughput LLM serving with batching, quantization, and distributed support. The thread itself offers no benchmarks, version numbers, or technical comparisons, so it functions as a bookmark list rather than an evaluation.

twitter · RodmanAi · Sep 24, 10:08

**Background**: An AI inference stack is the set of software components that load trained models and answer requests in production, typically covering serving, batching, memory management, and quantization. vLLM, originally from UC Berkeley's Sky Computing Lab, is a widely used open-source serving engine known for PagedAttention and continuous batching. SIE is a newer open-source inference server from Superlinked that aims to serve many small models behind one API for agent tasks such as retrieval, document conversion, and content safety.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/superlinked/sie">GitHub - superlinked/sie: Open-source inference server and ...</a></li>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory-efficient...</a></li>
<li><a href="https://themenonlab.blog/blog/superlinked-sie-inference-engine/">SIE: One Inference Server for All Your Agent's Models</a></li>

</ul>
</details>

**Tags**: `#AI inference`, `#open-source`, `#GitHub`, `#LLM serving`, `#curated list`

---

<a id="item-27"></a>
## [Twitter Thread Lists 10 Free GitHub Repos for Python and AI Learning](https://twitter.com/RodmanAi/status/2102742421100519613) ⭐️ 4.0/10

A Twitter thread by @RodmanAi curates 10 free GitHub repositories that guide learners from Python basics through LLMs, AI agents, and production systems. The thread highlights repos like Python-100-Days (Python, data analysis, web dev) and Generative AI for Beginners (LLMs, prompting, RAG, agents, fine-tuning). Curated free learning paths lower the barrier to entry for developers wanting to build with LLMs and AI agents, which are increasingly in demand across the industry. Such lists help self-taught developers and career switchers navigate an otherwise overwhelming landscape of resources. The thread lists repos covering Python fundamentals, data analysis, web development, prompting, RAG, agents, and fine-tuning, but the tweet is truncated and only a few links are visible. It is a curated list rather than original technical content, and engagement was moderate with no substantive discussion.

twitter · RodmanAi · Sep 23, 12:50

**Background**: RAG (Retrieval-Augmented Generation) is a technique that enhances LLMs by retrieving relevant information from external sources before generating a response, improving reliability over relying solely on training data. Fine-tuning adapts a pre-trained model to specific tasks using additional data, and AI agents are autonomous systems that use LLMs to plan and execute tasks, with production deployment requiring distributed systems engineering and rigorous evaluation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fine-tuning_(deep_learning)">Fine - tuning (deep learning) - Wikipedia</a></li>
<li><a href="https://mlflow.org/articles/building-production-ready-ai-agents-in-2026/">Building Production-Ready AI Agents in 2026 - MLflow</a></li>

</ul>
</details>

**Tags**: `#Python`, `#LLM`, `#AI agents`, `#GitHub`, `#learning resources`

---

<a id="item-28"></a>
## [Adam AI CAD Copilot Adds Direct Rhino Integration](https://twitter.com/adamdotnew/status/2102839787808002380) ⭐️ 3.0/10

Adam, an AI CAD copilot for hardware teams, announced via a short tweet from @adamdotnew that it now integrates directly with Rhino. The announcement was shared as a brief promotional post with a link, without accompanying technical documentation or version details. Rhino is a widely used 3D modeling and CAD tool, particularly in industrial design and architecture, so adding native support expands Adam's reach beyond the CAD platforms it already covers, such as Onshape and Autodesk Fusion. This could make AI-assisted CAD workflows more accessible to designers who rely on Rhino and its Grasshopper visual programming environment. The tweet provides no technical specifics, such as which Rhino versions are supported, whether the integration works through Grasshopper, or what capabilities the AI copilot offers inside Rhino. The post received only modest engagement (roughly 14 likes, 1 retweet, and 2 replies), suggesting limited immediate visibility.

twitter · adamdotnew · Sep 23, 19:17

**Background**: Adam is described as an AI CAD copilot for hardware teams, previously working across platforms such as Onshape and Autodesk Fusion. Rhino (Rhinoceros 3D) is a commercial 3D computer graphics and CAD application developed by Robert McNeel & Associates, known for its NURBS-based modeling and its tightly integrated Grasshopper visual programming environment. Integrations like this typically let an AI assistant read and modify CAD models or generate geometry directly within the host application.

<details><summary>References</summary>
<ul>
<li><a href="https://adam.new/">Adam | AI CAD Copilot for Hardware Teams</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rhinoceros_3D">Rhinoceros 3D - Wikipedia</a></li>
<li><a href="https://www.rhino3d.com/">Rhino - Rhinoceros 3D</a></li>

</ul>
</details>

**Tags**: `#integration`, `#Rhino`, `#Adam`, `#announcement`, `#CAD`

---

<a id="item-29"></a>
## [SpaceX Dragon arrives at Pad 40 for Crew-13 ISS mission](https://twitter.com/SpaceX/status/2103277482585870377) ⭐️ 3.0/10

SpaceX announced on X that a Dragon spacecraft has arrived at Space Launch Complex 40 (Pad 40) at Cape Canaveral ahead of the upcoming Crew-13 mission to the International Space Station. The post is a routine operational milestone marking the start of pre-launch processing for the next crew rotation flight. Crew-13 is the 13th crew rotation mission of SpaceX's human space transportation system and its 14th flight with astronauts, continuing NASA's Commercial Crew Program's role as the primary U.S. route to the ISS. The arrival of the capsule at the pad signals that launch preparations are on track for the four-person crew. The Crew-13 crew consists of NASA astronauts Jessica Watkins and Luke Delaney, CSA astronaut Joshua Kutryk, and Roscosmos cosmonaut Sergey (surname per Wikipedia). Pad 40 (SLC-40) has hosted over 345 Falcon 9 launches as of September 2026 and recently gained a new landing zone, LZ-40.

twitter · SpaceX · Sep 25, 00:16

**Background**: SpaceX's Dragon spacecraft is a reusable capsule designed to carry crew and cargo to the International Space Station under NASA's Commercial Crew Program. Crew rotation missions like Crew-13 typically launch from Pad 40 at Cape Canaveral Space Force Station using a Falcon 9 rocket, with the capsule docking to the ISS for a multi-month stay. Pad 40 is one of SpaceX's primary launch sites on the East Coast.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Crew-13">SpaceX Crew-13 - Wikipedia</a></li>
<li><a href="https://www.nasa.gov/mission/nasas-spacex-crew-13/">NASA's SpaceX Crew-13</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cape_Canaveral_Space_Launch_Complex_40">Cape Canaveral Space Launch Complex 40 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#spacex`, `#crew-dragon`, `#iss`, `#spaceflight`, `#launch-update`

---

<a id="item-30"></a>
## [Yann LeCun Retweets Truncated AI Safety Commentary](https://twitter.com/ylecun/status/2103203999939690984) ⭐️ 3.0/10

Yann LeCun retweeted a post by Lenny Pruss that briefly references a podcast interview with an EA-adjacent AI safety expert from Redwood Research, but the tweet is truncated and contains no substantive argument or linked article. LeCun's amplification of this fragment highlights the ongoing public tension between prominent AI researchers and the EA-aligned AI safety community, though the truncated nature of the tweet limits its informational value. The tweet is a retweet of @lennypruss and cuts off mid-sentence after saying the listener 'comes away with 2 obvious realizations,' so the actual points are never stated; no podcast name, episode link, or expert name is provided.

twitter · ylecun · Sep 24, 19:24

**Background**: Redwood Research is a Berkeley-based nonprofit founded in 2021 that conducts empirical AI safety research, focusing on preventing advanced AI systems from acting against their developers' intent. Effective altruism (EA) is a philanthropic movement that has become a major funder and driver of AI existential-risk research, and 'EA-adjacent' describes people or groups sympathetic to but not formally part of that movement. Yann LeCun, Meta's chief AI scientist, is a well-known skeptic of AI existential-risk narratives and frequently debates AI safety advocates on social media.

<details><summary>References</summary>
<ul>
<li><a href="https://www.redwoodresearch.org/">Redwood Research</a></li>
<li><a href="https://en.wikipedia.org/wiki/Effective_altruism">Effective altruism - Wikipedia</a></li>
<li><a href="https://x.com/lennypruss/status/2102875545390428203">Lenny Pruss on X: "Listened to an EA-adjacent AI safety expert from ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#effective altruism`, `#Twitter`, `#AI policy`, `#opinion`

---

<a id="item-31"></a>
## [Yann LeCun Retweets Paris Hiring Call for ML PhD Students and Post-Docs](https://twitter.com/ylecun/status/2103194284874719422) ⭐️ 3.0/10

Yann LeCun retweeted a hiring call from @pascalefung seeking PhD students, post-docs, and ML researchers for a Paris office to collaborate on fundamental research. The announcement was shared on Twitter and received modest engagement, with around 75 retweets. LeCun's amplification gives this academic hiring call unusual visibility, helping connect prospective ML researchers with a fundamental research group in Paris. It reflects the ongoing competition for AI research talent and the role of prominent figures in surfacing academic opportunities. The call targets PhD students, post-docs, and ML researchers interested in fundamental research at a Paris office, though the tweet is truncated and provides no further specifics on the lab, funding, or application process. The original poster is @pascalefung, and the tweet is a retweet rather than an original announcement.

twitter · ylecun · Sep 24, 18:46

**Background**: Yann LeCun is a Turing Award-winning AI researcher, a key figure behind convolutional neural networks, and Chief AI Scientist at Meta, making his social media posts widely followed in the machine learning community. Fundamental research in ML refers to long-horizon, curiosity-driven work rather than short-term product development, and such academic positions are often announced informally on Twitter.

**Tags**: `#hiring`, `#machine-learning`, `#academia`, `#research-positions`, `#twitter`

---

<a id="item-32"></a>
## [Hugging Face CEO Briefs UN Security Council on AI](https://twitter.com/ylecun/status/2102939109887021330) ⭐️ 3.0/10

Clement Delangue, CEO of Hugging Face, publicly thanked French diplomat Jean-Noël Barrot and the United Nations for inviting him to share lessons with the UN Security Council, and Yann LeCun retweeted the message. Delangue noted that Hugging Face was the first company to deliver such a briefing to the Council. The briefing signals that AI governance has become a top-tier international security concern, with open-source AI platforms now included alongside frontier labs like OpenAI and Anthropic in high-level policy discussions. It reflects a broader trend of AI companies seeking to shape global regulation and norms. The tweet is a retweet of a promotional thank-you note and provides no technical detail about what was actually presented to the Council. The truncated text suggests Delangue emphasized Hugging Face being the first company to brief the Security Council, but the full content of the briefing is not disclosed.

twitter · ylecun · Sep 24, 01:52

**Background**: The UN Security Council has recently held briefings on artificial intelligence and international security, hearing from leading AI executives and researchers such as Turing Award winner Yoshua Bengio. Hugging Face is a widely used open platform for sharing machine learning models, datasets, and applications, often described as the 'GitHub of AI.' These briefings are part of growing international efforts to address the risks and benefits of advanced AI.

<details><summary>References</summary>
<ul>
<li><a href="https://news.un.org/en/story/2026/09/1168414">LIVE: OpenAI and Anthropic to brief Security Council as AI ...</a></li>
<li><a href="https://transcripts.un.org/en/sc/10228">Artificial intelligence and international security - Security ...</a></li>
<li><a href="https://huggingface.co/">Hugging Face – The AI community building the future.</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#Hugging Face`, `#UN`, `#social media`, `#policy`

---

<a id="item-33"></a>
## [Yann LeCun Opens NYU CILVR Seminar with Talk on World Models](https://twitter.com/ylecun/status/2102878714023592161) ⭐️ 3.0/10

Yann LeCun, founding director of NYU's Center for Data Science, opened the fall CILVR Seminar series with a talk titled "World Models: Enabling the next AI revolution." The announcement was shared by NYU Data Science and retweeted by LeCun himself. LeCun has become one of the most prominent voices arguing that large language models alone are not the path to human-level AI, and his world-model agenda is increasingly shaping research directions and funding. The talk signals how this alternative paradigm is being promoted through academic venues like NYU's CILVR seminar. The CILVR Seminar is held biweekly on Thursdays at 11 a.m. in NYU's CDS 7th-floor space, starting September 28. The talk's full title, "World Models: Enabling the next AI revolution," reflects LeCun's long-running argument that AI systems need predictive internal models of the physical world rather than pure token prediction.

twitter · ylecun · Sep 23, 21:52

**Background**: CILVR stands for Computation, Intelligence, Learning, Vision, and Robotics, a research group at NYU's Center for Data Science focused on machine learning, computer vision, and related areas. Yann LeCun is a Turing Award winner known for foundational work on convolutional neural networks, and he has recently championed world models and self-supervised learning as alternatives to scaling up LLMs. He left Meta after 12 years and now chairs Advanced Machine Intelligence Labs (AMI), which reportedly raised a $1.03 billion seed round at a $3.5 billion pre-money valuation.

<details><summary>References</summary>
<ul>
<li><a href="https://cims.nyu.edu/ai/seminars/cilvr-seminar-series/">CILVR Seminars</a></li>
<li><a href="https://wp.nyu.edu/cilvr/">CILVR at NYU</a></li>
<li><a href="https://x.com/NYUDataScience/status/2102808170536255488">NYU Center for Data Science on X: "The CILVR Seminar opened its fall ...</a></li>

</ul>
</details>

**Tags**: `#Yann LeCun`, `#seminar`, `#NYU`, `#AI research`, `#announcement`

---

<a id="item-34"></a>
## [Stanford AI Lab retweets project on recovering traits from data](https://twitter.com/StanfordAILab/status/2102640423554720198) ⭐️ 3.0/10

The Stanford AI Lab Twitter account retweeted a post by Sanmi Koyejo mentioning a fun project with collaborators Nathan Hu and Chris Potts, highlighting Section 5 where a trait is recoverable from data even when some conditions are not met. This signals ongoing research at Stanford on trait recovery from data, which could have implications for machine learning interpretability and robustness, though the tweet itself provides no technical details or links. The tweet specifically points to Section 5 of the project, where a trait is recoverable from data even when certain conditions are not satisfied, but no paper title, dataset, or method is mentioned.

twitter · StanfordAILab · Sep 23, 06:05

**Background**: Trait recovery from data is a common problem in machine learning, where the goal is to infer latent attributes (e.g., morphological or personality traits) from observed data. Stanford AI Lab is a prominent research group that frequently shares updates on social media, and Sanmi Koyejo is a faculty member known for work in trustworthy machine learning.

**Tags**: `#AI research`, `#Stanford`, `#tweet`, `#low engagement`

---

<a id="item-35"></a>
## [UC Berkeley Recruits Postdocs for Bakar Computational Program](https://twitter.com/berkeley_ai/status/2102876538215825856) ⭐️ 3.0/10

UC Berkeley AI announced on Twitter that it is recruiting multiple Postdoctoral Fellows as part of the recently launched Bakar Computational program, with researcher Yun S. Song asking followers to help spread the word. This recruitment reflects the growing investment by major universities in computational and AI-driven biomedical research, offering early-career researchers funded positions at the intersection of computer science, statistics, and biomedicine. The positions are tied to the Bakar Computational Biomedicine Initiative, a joint effort between UC Berkeley and UCSF that creates new faculty positions and supports postdoctoral researchers; the announcement itself provides no application deadline or eligibility specifics.

twitter · berkeley_ai · Sep 23, 21:43

**Background**: The Bakar Computational Biomedicine Initiative (BCBI) is a new research institute that brings together computer scientists, statisticians, and biomedical researchers to advance the frontier of AI and biomedicine. Postdoctoral fellowships are temporary, mentored research positions for researchers who have recently completed a PhD, and they are a common pathway into academic research careers.

<details><summary>References</summary>
<ul>
<li><a href="https://cdss.berkeley.edu/bakar-computational-biomedicine-initiative">Bakar Computational Biomedicine Initiative | CDSS at UC Berkeley</a></li>
<li><a href="https://inspire.berkeley.edu/o/uc-berkeley-and-ucsf-launch-computational-biomedicine-initiative/">UC Berkeley and UCSF launch Computational Biomedicine Initiative</a></li>

</ul>
</details>

**Tags**: `#academia`, `#postdoc`, `#recruitment`, `#berkeley`, `#AI research`

---

<a id="item-36"></a>
## [Anthropic clarifies Claude Code cloud session billing and one-time credits](https://twitter.com/ClaudeDevs/status/2102940480736821610) ⭐️ 3.0/10

The @ClaudeDevs account clarified that Claude Code cloud sessions are billed against a user's existing Pro or Max plan, just like the rest of Claude Code, and that the promotional credit is an optional one-time amount that cloud sessions consume first before falling back to normal plan usage. This clarification matters because cloud sessions were recently made generally available, and users were confused about whether the new feature required separate payment or would eat into their existing subscription limits. Clear billing rules reduce friction for Pro and Max subscribers deciding whether to adopt cloud sessions. The one-time promotional credit is optional and is spent first by cloud sessions before normal plan usage applies; according to community reports, existing subscribers received $100 on Pro and larger amounts on Max, and cloud sessions let Claude Code keep working even when the user's laptop is closed.

twitter · ClaudeDevs · Sep 24, 01:57

**Background**: Claude Code is Anthropic's agentic coding tool that can read a codebase, edit files, and run commands. Cloud sessions extend it by running tasks on Anthropic's cloud computers, accessible from a browser, phone, desktop app, or terminal, and they include built-in GitHub tools for reading issues, listing pull requests, and posting comments. Claude Pro and Max are Anthropic's paid subscription tiers, with Max offering roughly 5x or 20x more usage than Pro.

<details><summary>References</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/claude-code-on-the-web">Use Claude Code in the cloud</a></li>
<li><a href="https://www.reddit.com/r/ClaudeCode/comments/1wojd4c/cloud_sessions_are_officially_available_and_out/">Cloud sessions are officially available and out of research preview! They ...</a></li>

</ul>
</details>

**Discussion**: Community discussion around the cloud session launch was largely positive, with users noting that existing subscribers receive a one-time credit ($100 on Pro) and that cloud sessions keep Claude Code working even when a laptop is closed; some users asked how to switch back to local sessions.

**Tags**: `#Claude Code`, `#billing`, `#cloud sessions`, `#Anthropic`, `#customer support`

---

<a id="item-37"></a>
## [Twitter Thread Lists 20 Projects Built on TypeSafe's Jev Model](https://twitter.com/RodmanAi/status/2103155014915199065) ⭐️ 3.0/10

A Twitter thread from user @RodmanAi lists 20 projects built with 'Jev', including a browser agent called JEV-Ultrafast, model routing tools, drone control, and startup idea scoring. The thread provides only project names and links, with minimal technical detail and low engagement (about 50 likes and 13 retweets). This thread highlights the early ecosystem forming around Jev, TypeSafe AI's System One model that returns choices, scores, or probabilities instead of chat responses. If Jev's low-cost API ($0.042 per 1M input tokens) gains traction, it could enable a new class of lightweight decision-making agents for routing, automation, and control tasks. Jev is a proprietary model from San Francisco-based TypeSafe AI, founded in 2024, which released limited early access on 15 September 2026 alongside a $40 million seed round led by DCVC; the hosted API opened on 21 September 2026. The listed projects include a browser agent where Jev selects operations and page elements while a text model handles field input, and a model router that inspects prompts and chooses between local Qwen and hosted Sonnet.

twitter · RodmanAi · Sep 24, 16:10

**Background**: Jev is TypeSafe AI's 'System One' model, designed to return a discrete choice, score, or yes/no probability rather than conversational text, making it suited for decision-making and routing tasks. It was released in limited early access in September 2026 with a $40 million seed round led by DCVC, and its hosted API opened later that month at $0.042 per 1M input tokens with free output. The projects in the thread, such as JEV-Ultrafast and model-routing middleware, demonstrate how developers are using Jev to pick actions or route prompts between models like Qwen and Sonnet.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Jev_(AI_model)">Jev (AI model) - Wikipedia</a></li>
<li><a href="https://jevmodel.org/">Jev AI Model (TypeSafe) — Typed System One Decisions</a></li>
<li><a href="https://www.langchain.com/blog/building-a-harness-with-jev">What Is Jev? A Guide to TypeSafe AI's System One Model - LangChain</a></li>

</ul>
</details>

**Tags**: `#Jev`, `#project-list`, `#AI-agents`, `#promotional`, `#Twitter`

---

<a id="item-38"></a>
## [Promotional Thread Lists 12 JEV Skills for AI Agent Setups](https://twitter.com/RodmanAi/status/2102774321324437746) ⭐️ 3.0/10

A Twitter thread from @RodmanAi lists 12 "must-use JEV skills" for agent setups, including typesafe-mario (an agent that plays Super Mario), jev-ultrafast (a browser agent), fast-jev-compaction (context compression), and json-render (generative rendering), each with a terse description and an opaque t.co link. The thread reflects growing grassroots interest in Jev, a TypeSafe decision-helper model being adopted for agent tasks like browser control and context compaction, but its promotional format and opaque links make it more of an advertisement than a substantive technical resource. The thread only names four of the twelve skills and provides no technical explanation, benchmarks, or repository links; engagement was modest at 68 likes, 19 retweets, and 15 replies, and no meaningful discussion was included.

twitter · RodmanAi · Sep 23, 14:57

**Background**: Jev is a TypeSafe model that acts as a decision helper for software and AI agents: instead of asking an LLM to freely generate text, selectors, or code, it chooses among a small structured set of options. This approach has been applied to browser automation (browser-use's jev-ultrafast, which replaces free-form step generation with structured choice) and to context compaction (fast-jev-compaction, which uses Jev-scored deletions to trim tool calls from transcripts).

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/browser-use/jev-ultrafast">GitHub - browser -use/ jev - ultrafast : Fastest and cheapest web agent</a></li>
<li><a href="https://www.explainx.ai/blog/fast-jev-compaction-claude-code-plugin-2026">Jev-Powered Claude Code Compaction | explainx.ai Blog</a></li>
<li><a href="https://www.reddit.com/r/AI_Agents/comments/1wndjk7/anyone_here_learning_jev/">Anyone here learning JEV? : r/AI_Agents - Reddit</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#Twitter thread`, `#promotional`, `#tools`, `#low-content`

---

<a id="item-39"></a>
## [MecAgent Promotes Copilot V2.0.0 for SolidWorks 2026 Using GPT-6 Astra](https://twitter.com/MecAgent/status/2102754454269305061) ⭐️ 2.0/10

MecAgent announced MecAgent Copilot V2.0.0 for CAD, claiming integration with SolidWorks 2026 and the GPT-6 Astra model. The announcement was made via a brief promotional tweet with no technical details or linked article. If accurate, this would represent an early application of OpenAI's GPT-6 Astra to professional mechanical CAD workflows, potentially signaling broader AI adoption in engineering design tools. However, the lack of verifiable details and low engagement make the claim speculative. The tweet provides no technical specifics, benchmarks, or pricing, and the mention of 'GPT-6 Astra' alongside 'SolidWorks 2026' appears marketing-oriented. MecAgent is known as an AI copilot for mechanical CAD software, but this version's capabilities remain unverified.

twitter · MecAgent · Sep 23, 13:38

**Background**: MecAgent is an AI copilot designed to automate tasks in mechanical CAD software like SolidWorks. GPT-6 Astra is a large language model developed by OpenAI, released in limited preview on September 3, 2026, with general availability the following day. SolidWorks 2026 is a version of Dassault Systèmes' 3D CAD software that incorporates AI-powered design and engineering tools.

<details><summary>References</summary>
<ul>
<li><a href="https://mecagent.com/">MecAgent</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>
<li><a href="https://www.linkedin.com/posts/johncwagnerjr_solidworks-2026-fd01-ai-powered-3d-cad-software-activity-7480602866618138624-Ycu0">SOLIDWORKS 2026 Brings AI to Design and Engineering... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#CAD`, `#SolidWorks`, `#AI`, `#promotional`, `#unverified`

---

<a id="item-40"></a>
## [Link-only tweet with no context offers no technical value](https://twitter.com/adamdotnew/status/2103158741642416143) ⭐️ 1.0/10

A Twitter user (@adamdotnew) posted a tweet containing only a shortened t.co link with no accompanying text, commentary, or explanation. The post received a low engagement score of 1.0/10, with only 9 likes and no visible discussion. This item has no significance for software engineering, AI/ML, or systems research because it lacks any substantive content, context, or technical depth. It serves only as an example of low-value link-only social media posts that provide no actionable information to the community. The tweet contains only the URL https://t.co/7taLArIang, which is a shortened link whose destination is unknown from the provided content. There is no accompanying text, no thread, and no visible engagement beyond 9 likes.

twitter · adamdotnew · Sep 24, 16:24

**Background**: Twitter's t.co service automatically shortens all links posted on the platform, so a bare t.co URL reveals nothing about the destination without clicking it. Link-only tweets are often flagged by content aggregators as low-value because they lack the context needed for readers to understand or evaluate the shared material.

**Tags**: `#twitter`, `#link-only`, `#no-context`, `#low-value`

---

<a id="item-41"></a>
## [Humorous Tweet Mocks England's 'Football's Coming Home' Slogan](https://twitter.com/lukas_m_ziegler/status/2102811228716589382) ⭐️ 1.0/10

A Twitter user posted a humorous tweet referencing England's football history and the famous 'Football's Coming Home' slogan, expressing nostalgia for times when the phrase felt true. The tweet, which includes a crying emoji and the England flag, has received 32 likes and 2 replies. This tweet is a casual sports meme with no technical or academic content, making it irrelevant to a software engineering or AI audience. Its low engagement and off-topic nature mean it has no significant impact on the tech community. The tweet plays on the 'Football's Coming Home' chant, which originates from the 1996 song 'Three Lions' by Baddiel, Skinner, and the Lightning Seeds. The phrase is often used by England fans during major tournaments, but England has only won the World Cup once, in 1966.

twitter · lukas_m_ziegler · Sep 23, 17:23

**Background**: The song 'Three Lions' was released for the 1996 European Championship and has since become an anthem for England fans. The phrase 'Football's Coming Home' reflects the hope that England will win a major tournament, though the team has often fallen short. England's only major tournament victory is the 1966 World Cup.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Three_Lions_(song)">Three Lions (song) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/England_national_football_team">England national football team - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#sports`, `#football`, `#meme`, `#off-topic`

---