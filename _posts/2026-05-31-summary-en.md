---
layout: default
title: "Horizon Summary: 2026-05-31 (EN)"
date: 2026-05-31
lang: en
---

> From 21 items, 16 important content pieces were selected

---

1. [Stanford AI Lab Releases GPIC: 100M Image-Text Dataset](#item-1) ⭐️ 8.0/10
2. [Political Sign-Off Proposed for Federal Research Grants](#item-2) ⭐️ 7.0/10
3. [Microsoft open-sources SkillOpt for AI agent learning](#item-3) ⭐️ 7.0/10
4. [Duke's Argus Robot: 20 Legs, No Front or Back](#item-4) ⭐️ 6.0/10
5. [Midea Unveils Six-Armed Humanoid Robot MIRO U](#item-5) ⭐️ 6.0/10
6. [Anthropic's 31-Page Prompting Guide Distilled into 9 Rules](#item-6) ⭐️ 6.0/10
7. [Robot Hands: Hard to Build, Hard to Ignore](#item-7) ⭐️ 5.0/10
8. [SpaceX Launches 24 Starlink Satellites on Falcon 9](#item-8) ⭐️ 5.0/10
9. [ESMFold2 Benchmarking Confusion Clarified](#item-9) ⭐️ 5.0/10
10. [OpenAI Codex Now Free to Run Locally with Ollama](#item-10) ⭐️ 5.0/10
11. [Renishaw REVO CMM Enables High-Speed Part Inspection](#item-11) ⭐️ 4.0/10
12. [SpaceX Launches 29 Starlink Satellites on Falcon 9](#item-12) ⭐️ 4.0/10
13. [Exxon Warns of Petrol Armageddon in Two Weeks](#item-13) ⭐️ 2.0/10
14. [Yann LeCun Criticizes MAGA in Retweet](#item-14) ⭐️ 2.0/10
15. [Tweet Compares US Economy 2024 vs 2026](#item-15) ⭐️ 2.0/10
16. [Stanford AI Lab Tweets Link Without Context](#item-16) ⭐️ 1.0/10

---

<a id="item-1"></a>
## [Stanford AI Lab Releases GPIC: 100M Image-Text Dataset](https://twitter.com/StanfordAILab/status/2060484521129332833) ⭐️ 8.0/10

Stanford AI Lab announced GPIC, a Giant Permissive Image Corpus containing 100M training image-text pairs captioned by a state-of-the-art vision-language model, along with a benchmark for visual generation. GPIC provides a large-scale, permissively licensed dataset that enables fair comparison and scalable research in visual generative modeling, addressing the need for stable, accessible resources in the modern era of large generative models. The dataset comprises approximately 28 trillion pixels, with 100M training, 200K validation, and 1M test examples, all safety-filtered, deduplicated, and centrally hosted on Hugging Face.

twitter · StanfordAILab · May 29, 22:12

**Background**: Visual generative modeling requires large, diverse, and high-quality image-text datasets. Previous datasets like COCO or LAION have limitations in scale, licensing, or caption quality. GPIC addresses these by using a VLM to generate captions for permissively licensed internet images, ensuring a large and clean corpus.

<details><summary>References</summary>
<ul>
<li><a href="https://gpic.stanford.edu/">GPIC: A Giant Permissive Image Corpus for Visual Generation</a></li>
<li><a href="https://arxiv.org/abs/2605.30341">GPIC: A Giant Permissive Image Corpus for Visual Generation</a></li>
<li><a href="https://www.machinebrief.com/news/gpic-a-dataset-thats-changing-the-game-for-visual-generative-qpi0">GPIC: A Dataset That's Changing the Game for Visual...</a></li>

</ul>
</details>

**Discussion**: The community expressed excitement, with one researcher noting that training one epoch on GPIC costs the same as 100 epochs on previous datasets, highlighting its efficiency and potential as a new standard benchmark.

**Tags**: `#AI`, `#Computer Vision`, `#Dataset`, `#Visual Generation`, `#Benchmark`

---

<a id="item-2"></a>
## [Political Sign-Off Proposed for Federal Research Grants](https://twitter.com/ylecun/status/2060764165778915335) ⭐️ 7.0/10

A proposed policy change would require every federal research grant to obtain political sign-off before being awarded, potentially altering the landscape of American science funding. This shift could introduce political considerations into scientific funding decisions, threatening the merit-based peer review system that has been a cornerstone of U.S. research excellence. The proposal, highlighted by Dr. Catharine Young and retweeted by Yann LeCun, suggests that political sign-off would be required for all federal research grants, though specific details on implementation remain unclear.

twitter · ylecun · May 30, 16:43

**Background**: Federal research grants in the U.S. are typically awarded through a peer-review process that evaluates scientific merit. Introducing political sign-off could politicize science funding, potentially impacting research directions and academic freedom.

**Discussion**: The tweet has garnered significant engagement (449 retweets), indicating strong interest and concern within the scientific community about the potential erosion of merit-based funding.

**Tags**: `#research policy`, `#science funding`, `#government`, `#academia`

---

<a id="item-3"></a>
## [Microsoft open-sources SkillOpt for AI agent learning](https://twitter.com/RodmanAi/status/2060603132124750283) ⭐️ 7.0/10

Microsoft has open-sourced SkillOpt, a system that improves AI agents by training a markdown file instead of retraining the underlying model. The system uses techniques like learning rates, minibatches, and validation checks to optimize a natural-language skill document. This approach significantly reduces the cost and complexity of improving AI agents, as it avoids expensive model retraining. It could accelerate the development of more capable and adaptable AI agents across various applications. SkillOpt treats a compact natural-language skill document as the trainable state of a frozen language agent, then learns through rollouts, reflection, bounded edits, and held-out validation gates. The final output is a deployable best_skill.md artifact.

twitter · RodmanAi · May 30, 06:04

**Background**: Traditional AI agent improvement often requires fine-tuning large language models, which is computationally expensive. SkillOpt instead optimizes a text-based skill document that guides the agent's behavior, making the process more efficient and accessible. Markdown files are increasingly used in agentic AI to persist rules, workflows, and prompts.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/SkillOpt">GitHub - microsoft/SkillOpt: SkillOpt is a text-space ...</a></li>
<li><a href="https://arxiv.org/abs/2605.23904">[2605.23904] SkillOpt: Executive Strategy for Self-Evolving ...</a></li>
<li><a href="https://microsoft.github.io/SkillOpt/">SkillOpt | Executive Strategy for Self-Evolving Agent Skills</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Microsoft`, `#open-source`, `#machine learning`, `#agents`

---

<a id="item-4"></a>
## [Duke's Argus Robot: 20 Legs, No Front or Back](https://twitter.com/lukas_m_ziegler/status/2060484890496324028) ⭐️ 6.0/10

Duke University researchers have unveiled Argus, a sea-urchin-inspired robot with 20 telescoping legs, each tipped with a depth camera, enabling omnidirectional movement and perception. Argus introduces a novel design principle called 'dynamic symmetry,' which could lead to more robust and versatile robots for search-and-rescue, exploration, and other tasks in unstructured environments. The robot has no designated front, back, top, or bottom, and its 20 cameras provide nearly 360-degree vision. The telescoping legs allow it to roll, climb, and traverse rough terrain like grass, sand, and wet ground.

twitter · lukas_m_ziegler · May 29, 22:14

**Background**: Traditional robots often mimic bilateral symmetry (e.g., humans, dogs) or use wheels/tracks, limiting their mobility in complex environments. Argus takes inspiration from sea urchins, which have radial symmetry and can move in any direction. The concept of 'dynamic symmetry' focuses on uniform action rather than static shape, allowing the robot to adapt its movement based on the environment.

<details><summary>References</summary>
<ul>
<li><a href="https://pratt.duke.edu/news/argus-robot-design/">Omnidirectional, Sea-Urchin-Like Robot Defies Traditional ...</a></li>
<li><a href="https://apnews.com/article/robot-duke-argus-6ba9651ba6553ebc4405ffc07a26afed">Duke engineers develop robot with 20 legs and eyes | AP News</a></li>
<li><a href="https://www.zmescience.com/science/news-science/20-legged-robot-argus/">This Weird 20- Legged Robot Moves Like Nothing Else on Earth and It...</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#research`, `#bio-inspired`, `#Duke University`

---

<a id="item-5"></a>
## [Midea Unveils Six-Armed Humanoid Robot MIRO U](https://twitter.com/lukas_m_ziegler/status/2060350452202365420) ⭐️ 6.0/10

Midea Group has unveiled MIRO U, a six-armed humanoid robot designed for industrial assembly tasks, capable of handling heavy components with its lower limbs and performing fine assembly with its upper limbs. This robot challenges the conventional 1:1 human mimicry in humanoid robotics, prioritizing industrial utility and efficiency over anthropomorphic design, potentially boosting factory productivity significantly. MIRO U features full 360-degree rotation, stable vertical lifting, and rapid tool-swapping capabilities, and is scheduled to be deployed at Midea's Wuxi washing machine plant by the end of December 2025.

twitter · lukas_m_ziegler · May 29, 13:20

**Background**: Humanoid robots are typically designed with two arms and two legs to mimic human form. Midea's MIRO U breaks this convention by adding four extra arms, using wheels for mobility instead of legs, to maximize industrial efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.scmp.com/tech/tech-trends/article/3335721/chinese-home-appliance-giant-midea-unveils-six-arm-robot-factory-work">Chinese home appliance giant Midea unveils 6-arm robot for factory work | South China Morning Post</a></li>
<li><a href="https://www.humanoidsdaily.com/news/midea-s-super-humanoid-miro-u-has-six-arms-and-wheels-challenges-1-1-human-mimicry">Midea’s ‘Super Humanoid’ MIRO U Has Six Arms and Wheels, Challenges 1:1 Human Mimicry | Humanoids Daily</a></li>
<li><a href="https://indiandefencereview.com/mideas-super-humanoid-six-arms-zero-rest/">Midea’s Super Humanoid: Six Arms, Zero Rest, and More Factory Output!</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#humanoid robot`, `#industrial automation`

---

<a id="item-6"></a>
## [Anthropic's 31-Page Prompting Guide Distilled into 9 Rules](https://twitter.com/RodmanAi/status/2060263146103980092) ⭐️ 6.0/10

A Twitter thread by @RodmanAi summarizes Anthropic's 31-page prompting guide into 9 practical rules, such as 'Name the output, not the task' to improve prompt engineering. This distillation makes Anthropic's best practices accessible to a wider audience, helping developers and AI users craft more effective prompts for large language models. The first rule advises specifying the desired output format (e.g., thread, table, email, JSON) rather than describing the task, leading to clearer results.

twitter · RodmanAi · May 29, 07:33

**Background**: Prompt engineering is the practice of designing inputs to guide AI models to produce desired outputs. Anthropic, a leading AI company, released a comprehensive 31-page guide on this topic, which the Twitter thread condenses into actionable rules.

**Tags**: `#prompt engineering`, `#Anthropic`, `#AI`, `#LLM`, `#best practices`

---

<a id="item-7"></a>
## [Robot Hands: Hard to Build, Hard to Ignore](https://twitter.com/lukas_m_ziegler/status/2060358895797784770) ⭐️ 5.0/10

Chris Paxton published a blog post discussing why building good robot hands is extremely difficult and why they are still necessary for advanced robotics. This topic is crucial for the robotics community because dexterous manipulation remains a bottleneck for many real-world applications, from manufacturing to healthcare. The blog post likely covers mechanical complexity, sensor integration, and control challenges, as well as the trade-offs between cost, durability, and dexterity.

twitter · lukas_m_ziegler · May 29, 13:53

**Background**: Robot hands are notoriously difficult to engineer because they require a balance of strength, precision, and sensitivity, often mimicking the human hand's 27 degrees of freedom. Most current robotic grippers are simple claws or suction cups, which lack the dexterity for tasks like assembling delicate electronics or performing surgery.

**Tags**: `#robotics`, `#robot hands`, `#engineering`

---

<a id="item-8"></a>
## [SpaceX Launches 24 Starlink Satellites on Falcon 9](https://twitter.com/SpaceX/status/2060766975404462459) ⭐️ 5.0/10

SpaceX successfully launched 24 Starlink satellites aboard a Falcon 9 rocket from California, with deployment confirmed. This launch continues SpaceX's rapid expansion of the Starlink constellation, which aims to provide global broadband internet coverage. The Falcon 9 first stage likely landed on a droneship, though not specified; the mission adds to over 6,000 Starlink satellites launched to date.

twitter · SpaceX · May 30, 16:55

**Background**: Starlink is a satellite internet constellation operated by SpaceX, providing low-latency broadband to underserved areas. Falcon 9 is a reusable two-stage rocket that has become the workhorse for SpaceX launches.

**Tags**: `#SpaceX`, `#Starlink`, `#satellite launch`, `#Falcon 9`

---

<a id="item-9"></a>
## [ESMFold2 Benchmarking Confusion Clarified](https://twitter.com/ylecun/status/2060622786196918445) ⭐️ 5.0/10

Sylvain Gariel tweeted that it took him a while to understand the excitement around ESMFold2 because initial benchmarking data did not appear impressive. Yann LeCun retweeted this observation. This highlights the importance of careful benchmarking in AI protein folding, where initial results may be misleading. It also shows that even experts need time to evaluate new models like ESMFold2. ESMFold2 is a protein structure prediction model from Meta AI that offers a balance of speed and accuracy. The tweet suggests that initial benchmarking data may not have reflected its true performance.

twitter · ylecun · May 30, 07:22

**Background**: Protein folding prediction is a key challenge in computational biology. ESMFold2 uses a language model approach to predict protein structures from amino acid sequences, competing with models like AlphaFold2.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tamarind.bio/tools/esmfold2">ESMFold 2 Online | Next Generation Structure Prediction</a></li>
<li><a href="https://310.ai/blog/benchmarking-machine-learning-methods-for-protein-folding-a-comparative-study-of-esmfold-omegafold-and-alphafold">Benchmarking Machine Learning Methods for Protein Folding ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#protein folding`, `#ESMFold2`

---

<a id="item-10"></a>
## [OpenAI Codex Now Free to Run Locally with Ollama](https://twitter.com/RodmanAi/status/2060711654908912065) ⭐️ 5.0/10

OpenAI's Codex, previously requiring API access, can now be run locally for free using Ollama with open-source models like DeepSeek V4, Gemma 4, and Qwen 3.6. This eliminates API costs and rate limits, enabling private, offline AI coding assistance for developers, potentially accelerating adoption of local AI tools. The setup involves using Ollama to run open-weight models locally, then connecting Codex CLI or the Codex App to the local model. Codex CLI is available on macOS, Windows, and Linux.

twitter · RodmanAi · May 30, 13:15

**Background**: Codex is OpenAI's AI coding agent that originally required a subscription and cloud API. Ollama is a platform for running large language models locally on personal computers, providing a command-line interface and REST API.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/codex/cli">CLI – Codex | OpenAI Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ollama">Ollama - Wikipedia</a></li>
<li><a href="https://ollama.com/">Ollama</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Codex`, `#Ollama`, `#local AI`, `#open-source`

---

<a id="item-11"></a>
## [Renishaw REVO CMM Enables High-Speed Part Inspection](https://twitter.com/lukas_m_ziegler/status/2060793388048519278) ⭐️ 4.0/10

A tweet by @lukas_m_ziegler highlights the Renishaw REVO 5-axis CMM system, which uses Renscan5 technology to inspect parts at dramatically higher speeds than traditional CMMs. This technology can significantly reduce inspection cycle times in manufacturing, improving throughput without sacrificing accuracy, which is critical for quality control in industries like aerospace and automotive. The REVO system uses a 5-axis measuring head and probe that minimizes dynamic errors at high speeds, achieving cycle times less than half of conventional CMMs while maintaining high accuracy.

twitter · lukas_m_ziegler · May 30, 18:40

**Background**: Coordinate measuring machines (CMMs) are used to measure the physical geometry of manufactured parts. Traditional CMMs move the entire machine structure to capture each measurement point, which is slow. The Renishaw REVO system instead uses a fast, lightweight 5-axis probe that moves independently, drastically reducing inspection time.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=FUgWBlEewyk">Renishaw Revo CMM Demonstration - YouTube</a></li>
<li><a href="https://www.cmmxyz.com/new-cmms/probing-and-accessories/5-axis-systems/renishaw-revo/">Renishaw REVO 5-Axis Measurement System | CMMXYZ</a></li>
<li><a href="https://www.thome-precision.com/Renishaw-Revo.html">THOME Präzision GmbH | Renishaw REVO</a></li>

</ul>
</details>

**Tags**: `#manufacturing`, `#CMM`, `#inspection`, `#Renishaw`

---

<a id="item-12"></a>
## [SpaceX Launches 29 Starlink Satellites on Falcon 9](https://twitter.com/SpaceX/status/2060342610623959109) ⭐️ 4.0/10

SpaceX launched 29 Starlink satellites to low Earth orbit aboard a Falcon 9 rocket from Florida, as announced on Twitter. The deployment of the satellites was confirmed shortly after launch. This launch continues the rapid expansion of the Starlink constellation, which aims to provide global broadband internet coverage. Each launch adds capacity and improves service for users in underserved areas. The Falcon 9 first stage is reusable, and this mission likely used a flight-proven booster, though specific booster details were not provided. Starlink satellites operate in low Earth orbit at approximately 550 km altitude.

twitter · SpaceX · May 29, 12:48

**Background**: Falcon 9 is a partially reusable two-stage rocket designed by SpaceX, and it is the most-flown orbital rocket of the 2020s. Starlink is a satellite internet constellation operated by SpaceX, with over 10,000 satellites launched to date, providing broadband to around 150 countries.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falcon_9">Falcon 9 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Starlink">Starlink - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starlink`, `#satellite`, `#launch`

---

<a id="item-13"></a>
## [Exxon Warns of Petrol Armageddon in Two Weeks](https://twitter.com/ylecun/status/2060784862483632292) ⭐️ 2.0/10

A retweet by Yann LeCun highlights Exxon's warning that the world is two weeks away from a petrol armageddon due to the closure of a critical oil choke point. This news is off-topic for a technical audience, as it concerns oil supply rather than software engineering, AI/ML, or systems research, and has low relevance to the community. The tweet references Exxon's statement about closing the world's most important oil choke point, but provides no technical details or context about the specific location or event.

twitter · ylecun · May 30, 18:06

**Tags**: `#off-topic`, `#oil`, `#energy`

---

<a id="item-14"></a>
## [Yann LeCun Criticizes MAGA in Retweet](https://twitter.com/ylecun/status/2060718725884699003) ⭐️ 2.0/10

Yann LeCun retweeted a post criticizing the MAGA movement's sense of reality and morality, referencing his work as a scientist on treatments and vaccines. This tweet is off-topic for the AI/ML community and has low relevance to technical discussions, but it shows LeCun's personal political stance. The tweet is a retweet with no additional technical content, and the original post appears to be a political commentary.

twitter · ylecun · May 30, 13:43

**Tags**: `#politics`, `#twitter`, `#off-topic`

---

<a id="item-15"></a>
## [Tweet Compares US Economy 2024 vs 2026](https://twitter.com/ylecun/status/2060615788956991976) ⭐️ 2.0/10

A retweet by Yann LeCun shares a comparison of US economic indicators between 2024 and 2026, showing GDP growth falling from 2.8% to 1.6%, inflation rising from 2.9% to 3.8%, and wages growing slower. This tweet highlights a potential economic slowdown and stagflation risk, which could affect tech investment, hiring, and consumer spending in the AI/ML ecosystem. The data points are attributed to Jared Ryan Sears and appear to be from US government statistics; no source or methodology is provided in the tweet.

twitter · ylecun · May 30, 06:54

**Background**: GDP growth, inflation, and wage trends are key macroeconomic indicators. A combination of slowing growth and rising inflation is often called stagflation, which can lead to higher unemployment and reduced business investment.

**Tags**: `#economy`, `#politics`, `#twitter`

---

<a id="item-16"></a>
## [Stanford AI Lab Tweets Link Without Context](https://twitter.com/StanfordAILab/status/2060431489544925263) ⭐️ 1.0/10

Stanford AI Lab tweeted a link to an external piece with no description or context, providing no substantive information. This tweet lacks value for readers as it offers no insight into the linked content, reducing its potential impact and engagement. The tweet scored 1.0/10 due to low engagement and no discussion, and it contains only a URL with no additional text.

twitter · StanfordAILab · May 29, 18:42

**Tags**: `#tweet`, `#link`, `#low-value`

---