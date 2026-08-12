---
weight: 3
bookFlatSection: true
title: "03 - The Florida Street Incident"
image: _din_style/banner_images/03_imb.webp
---

# The Florida Street Incident

While the race to catch up with GPT-4 continued to accelerate, an unexpected event would shake OpenAI to its core and expose the internal tensions that had been quietly building inside the leading organization.

Let’s move to November 2023. On Friday the 17th, OpenAI’s board of directors did the unthinkable: **they removed Sam Altman** as CEO, under the premise that they had “lost confidence in his leadership” and that Sam had not been “consistently honest in his communications with the board”.[^1] The implications, motives, and consequences are enough to make an entire movie. In fact, one is already being made.[^2]

<!--Among the most frequently cited rumors was that Sam Altman wanted to iterate on the product at a faster pace, sidelining the safety work on which Ilya Sutskever placed much of his focus. According to unconfirmed accounts, Mira Murati had been secretly leaking chats, emails, and internal information to Ilya for over a year—details about actions Sam was taking that both of them considered misguided. Over time, they convinced themselves—and eventually the board—that removing Sam was the right decision. Even as late as 2025, new details continue to surface about what happened behind the scenes to trigger the incident.-->

During a long time (2023-2024), one of the most repeated explanations of the incident was that there was a conflict between Sam Altman, interested in accelerating the development and commercialization of OpenAI’s products, and Ilya Sutskever, increasingly concerned about the safety of advanced systems.[^3][^4]

The news spread around the world and caught the entire community off guard, spawning a wide range of opinions, speculation, and memes—my personal favorite being: *“What did Ilya see?”* However, later documents and testimonies would reveal a more complex story.

In a 2025 court deposition, Ilya acknowledged that he had been considering for **at least a year the possibility of replacing Sam Altman**. At the request of the independent directors, he ended up preparing a 52-page document whose central argument stated that: Sam exhibited a consistent pattern of lying, undermining his executives, and pitting them against each other.[^5]

A significant part of the material used to build this case came from Mira Murati.[^5] She would later, under oath (2026), make similar statements: she described Sam as someone capable of telling one thing to one person and the opposite to another, creating chaos among the executives and making her own work as CTO difficult.[^6]

But to summarize what were days of absolute chaos: after the threat of a mass resignation by hundreds of OpenAI employees and Microsoft’s offer to build Sam an entire organization/lab inside Microsoft itself—along with his entire entourage,[^7] the board was left with no real choice but to **reinstate Sam just five days after his dismissal**, only to see all of its members replaced shortly after, except Adam D’Angelo.[^8]

This episode demonstrated something many of us had long suspected but were not yet ready to accept: OpenAI was no longer that non-profit organization devoted to developing AI for the benefit of humanity, governed by a board free of conflicting interests and guided by what was best for the world. Instead, it had become a company like any other, subject to power dynamics among founders and the pressure of investors.

## SSI (Safe Superintelligence): Ilya’s Lab

The consequences of the November incident did not take long to materialize. Several months later, in May 2024, the first of two major splinterings within OpenAI occurred: the resignation—or more precisely, the **indirect dismissal of Ilya Sutskever**, co-founder and chief scientist of the company.[^9] We speak of an “indirect dismissal” because, according to multiple sources, after the failed attempt to remove Sam Altman, Ilya was effectively isolated within the company[^10], with reduced access to resources and virtually no influence.

Ilya’s response would come in June 2024, with the creation of his own *startup*: Safe Superintelligence Inc., or simply SSI. With a single stated objective: **to build superintelligence safely, without any intermediate products**.[^11] SSI is arguably the most secretive lab in the industry to date.

Although the specific details of their work remain undisclosed, some directions can be inferred from interviews Ilya has given over the past couple of years. Unlike the industry’s dominant approach of ever-larger, increasingly general models, SSI appears to be pursuing something fundamentally different: not absolute intelligence, nor a hyper-ambivalent model like today’s LLMs, but a system (model and learning algorithm) that behaves more like a human teenager. That is, a system that, without being an expert in everything from the start, can be deployed in different environments to learn how to perform specific tasks in the real world. In this vision, Ilya has repeatedly emphasized **the importance of a powerful *value function***—the mechanism that allows a model to evaluate which actions bring it closer to its goals—as the key element underlying human learning capability.[^12]

SSI’s opacity is striking. Other details about the *startup* remain tightly guarded: its stage of development, the exact size of the team, the specific techniques being explored. The few data points that have surfaced are fragmentary: the team is small (estimated at a couple dozen researchers), much of it comes from Israel, they are using Google TPUs for their compute infrastructure, and their valuation, according to 2025 reports, has already reached 32 billion dollars.[^13][^14]

But in July 2026, Ilya Sutskever announced that they have research worth scaling, along with a partnership with NVIDIA to access an order of magnitude more compute.[^15]

Some say—rightly so—that if the history of AI were a movie, Ilya Sutskever would be its protagonist.

## Thinking Machines Lab: Mira’s Project

The second major split would arrive just over a year after the Sam Altman incident. In **February 2025**, Mira Murati, who had left her position as OpenAI’s CTO five months earlier, decided to embark on her own venture: **Thinking Machines Lab**.[^16]

Unlike Ilya’s quiet departure, Mira’s exit was a sizable exodus. She took with her a significant number of key OpenAI researchers, as well as select talent from other competing labs.[^16]

Without having launched a single product, Thinking Machines Lab secured an estimated initial valuation of 12 billion dollars.[^17] In the age of AI, pedigree and promises are worth almost as much as results.

But Mira and her team would not remain as mysterious as Ilya for long. Months after raising their initial capital, they began publishing a **series of *blog posts*** sharing genuinely interesting research: they explored the deep causes of non-determinism in LLMs (that seemingly random behavior that persists even at temperature 0), introduced a novel optimization algorithm variant called *Manifold Muon*, developed advanced techniques using LoRA (Low-Rank Adaptation, a method for efficiently adapting large models) for LLM *fine-tuning*, and shared new approaches to model distillation.[^18]

Who would have thought? They ended up being more transparent and more “open” than today’s OpenAI.

However, Thinking Machines Lab’s most significant launch was neither a *paper* nor a model, but a commercial service: **Tinker**. This is an **API-accessible platform** that allows companies and developers to perform customized *fine-tuning* of LLMs, still in private beta as of late 2025. You control the algorithm and the training data; they provide all the computational infrastructure and scalability.[^19]

And in the AI world of 2025, a handful of *blog posts* and a working API are enough to open the doors to the next funding round, which was estimating valuations around 50 billion dollars,[^20] but it ended up stagnating, and becoming an investment from NVIDIA for an undisclosed amount together with an agreement to provide 1GW of compute systems.[^21]

The development of their own models would come later.

---

Be that as it may, this would not be the first time that a seed fallen from OpenAI’s tree germinates and flourishes spectacularly on its own soil.

Right, Dario?

---

**Author’s Note:**  
1. The final question refers to Dario Amodei, co-founder of Anthropic and former Vice President of Research at OpenAI, who left the company in late 2020 along with other key researchers to found what today is one of OpenAI’s main competitors.[^22] Anthropic, creator of the Claude family of models, was born precisely from those same tensions between speed of development and safety considerations that years later would trigger the Florida Street incident.[^23] History, as it often does, tends to rhyme.

## References

[^1]: OpenAI. ["OpenAI announces leadership transition"](https://openai.com/index/openai-announces-leadership-transition/). November 17, 2023. The board announced the removal of Sam Altman stating that he had not been "*consistently candid in his communications with the board*" and that they had lost confidence in his ability to continue leading OpenAI.

[^2]: Associated Press. ["OpenAI film 'Artificial,' dropped by Amazon, finds a new home with Neon"](https://apnews.com/article/6879fc8605701a3254f0f4fedb7a2e8c). June 30, 2026. *Artificial*, directed by Luca Guadagnino and starring Andrew Garfield as Sam Altman, dramatizes the events around the removal and reinstatement of Altman in 2023.

[^3]: The Guardian. ["'Huge egos are in play': behind the firing and rehiring of OpenAI's Sam Altman"](https://www.theguardian.com/technology/2023/nov/23/huge-egos-are-in-play-behind-the-firing-and-rehiring-of-openais-sam-altman). November 23, 2023. The article captures the contemporary interpretation of the conflict as part of a broader divide between those who favored accelerating the deployment of AI and those who advocated a more cautious approach.

[^4]: Fortune. ["Exclusive: OpenAI promised 20% of its computing power to combat the most dangerous kind of AI—but never delivered"](https://fortune.com/2024/05/21/openai-superalignment-20-compute-commitment-never-fulfilled-sutskever-leike-altman-brockman-murati/). May 21, 2024. According to sources familiar with the Superalignment team, OpenAI never allocated the promised 20% of compute and repeatedly denied the team's GPU requests.

[^5]: Sutskever, Ilya. ["Videotaped Deposition of Ilya Sutskever"](https://archive.org/download/gov.uscourts.cand.433688/gov.uscourts.cand.433688.379.92.pdf). *Musk v. Altman*, U.S. District Court for the Northern District of California, October 1, 2025. Sutskever testified about the 52-page document prepared for the independent directors and about the material provided by Mira Murati. See also Reuters. ["Ex-OpenAI exec Sutskever says he spent a year gathering proof of alleged Altman dishonesty"](https://www.reuters.com/business/former-openai-executive-sutskever-discloses-nearly-7-billion-stake-ai-firm-2026-05-11/). May 11, 2026.

[^6]: Reuters. ["In OpenAI trial, former technology chief says Altman sowed 'chaos,' distrust among top executives"](https://www.reuters.com/legal/litigation/openai-trial-former-technology-chief-says-altman-sowed-chaos-distrust-among-top-2026-05-06/). May 6, 2026. Murati testified under oath about the contradictions in Altman's communications, the chaos among executives, and the difficulties this created for fulfilling her role as CTO.

[^7]: Reuters. ["OpenAI staff threaten to quit unless board resigns, letter says"](https://www.reuters.com/technology/openai-staff-threaten-quit-unless-board-resigns-letter-2023-11-20/). November 20, 2023. Hundreds of employees threatened to leave OpenAI while Microsoft offered to hire Altman, Brockman, and the employees who decided to follow them.

[^8]: Reuters. ["Sam Altman to return as OpenAI CEO after his tumultuous ouster"](https://www.reuters.com/technology/sam-altman-return-openai-ceo-2023-11-22/). November 22, 2023. The initial new board was formed by Bret Taylor, Larry Summers, and Adam D'Angelo, the only member of the previous board who remained.

[^9]: Reuters. ["OpenAI co-founder Ilya Sutskever departs ChatGPT maker"](https://www.reuters.com/technology/openai-co-founder-ilya-sutskever-departs-2024-05-14/). May 14, 2024. Ilya is no longer part of the company after this dismissal.

[^10]: Business Insider. ["OpenAI Cofounder Ilya Sutskever Has Become Invisible Lately, With His Future Uncertain"](https://www.businessinsider.com/openai-cofounder-ilya-sutskever-invisible-future-uncertain-2023-12). December 8, 2023. Internal sources confirmed that Sutskever had not been seen in OpenAI's offices since the November 2023 incident, with his role and his future within the company shrouded in uncertainty.

[^11]: Safe Superintelligence Inc. ["Safe Superintelligence Inc."](https://ssi.inc/). June 19, 2024. SSI presented itself as a lab with "*one goal and one product: a safe superintelligence*", without distractions arising from product cycles or short-term commercial pressures.

[^12]: Patel, Dwarkesh. ["Ilya Sutskever — We're moving from the age of scaling to the age of research"](https://www.dwarkesh.com/p/ilya-sutskever-2). November 25, 2025. Sutskever discusses the *value functions* and explicitly uses the example of a teenager learning to drive to explain how humans can evaluate their own performance and learn quickly from experience.

[^13]: Reuters. ["OpenAI co-founder Sutskever's new safety-focused AI startup SSI raises $1 billion"](https://www.reuters.com/technology/artificial-intelligence/openai-co-founder-sutskevers-new-safety-focused-ai-startup-ssi-raises-1-billion-2024-09-04/). September 4, 2024. SSI began with an extremely small team and operations between Palo Alto and Tel Aviv.

[^14]: Reuters. ["Alphabet, Nvidia invest in OpenAI co-founder Sutskever's SSI, source says"](https://www.reuters.com/technology/artificial-intelligence/alphabet-nvidia-invest-openai-co-founder-sutskevers-ssi-source-says-2025-04-12/). April 14, 2025. SSI was mainly using Google TPUs for research and development and had reached a reported valuation of approximately 32 billion dollars.

[^15]: NVIDIA. ["Ilya Sutskever's Safe Superintelligence Inc. and NVIDIA Announce Long-Term Strategic Partnership"](https://nvidianews.nvidia.com/news/ilya-sutskevers-safe-superintelligence-inc-and-nvidia-announce-long-term-strategic-partnership). July 27, 2026. The agreement provides access to Vera Rubin systems and expands SSI's compute by approximately an order of magnitude. Sutskever stated: "*We have research that is worthy of scaling up*."

[^16]: Reuters. ["Former OpenAI tech chief Murati's AI startup comes to light with 20 hires from ChatGPT maker"](https://www.reuters.com/technology/artificial-intelligence/former-openai-technology-chief-mira-muratis-ai-startup-taps-top-researchers-2025-02-18/). February 18, 2025. Thinking Machines Lab was presented with around 30 researchers and engineers from OpenAI, Meta, and Mistral; approximately two-thirds of the team were former OpenAI employees.

[^17]: Reuters. ["Mira Murati's AI startup Thinking Machines valued at $12 billion in early-stage funding"](https://www.reuters.com/technology/mira-muratis-ai-startup-thinking-machines-raises-2-billion-a16z-led-round-2025-07-15/). July 15, 2025. Thinking Machines raised approximately 2 billion dollars at a valuation of 12 billion.

[^18]: Thinking Machines Lab. ["Connectionism"](https://thinkingmachines.ai/blog/). 2025. The research blog includes *Defeating Nondeterminism in LLM Inference*, *Modular Manifolds*, *LoRA Without Regret*, and *On-Policy Distillation*.

[^19]: Thinking Machines Lab. ["Announcing Tinker"](https://thinkingmachines.ai/news/announcing-tinker/). October 1, 2025. Tinker was introduced as a flexible *fine-tuning* API that allows control over the algorithms and data while Thinking Machines manages the distributed training and infrastructure.

[^20]: Reuters. ["Mira Murati's Thinking Machines seeks $50 billion valuation in funding talks"](https://www.reuters.com/technology/mira-muratis-thinking-machines-seeks-50-billion-valuation-funding-talks-2025-11-13/). November 13, 2025. The company was in initial talks for a round at an approximate valuation of 50 billion dollars.

[^21]: Thinking Machines Lab. ["Thinking Machines Lab and NVIDIA Announce Long-Term Gigawatt-Scale Strategic Partnership"](https://thinkingmachines.ai/news/nvidia-partnership/). March 10, 2026. NVIDIA made an investment of undisclosed amount and agreed to deploy at least one gigawatt of Vera Rubin systems. See also Reuters. ["AI startup Thinking Machines clinches capital and a major chip supply deal from Nvidia"](https://www.reuters.com/business/ai-startup-thinking-machines-clinches-capital-major-chip-supply-deal-nvidia-2026-03-10/).

[^22]: OpenAI. ["Organizational update from OpenAI"](https://openai.com/index/organizational-update/). December 29, 2020. OpenAI announced the departure of Dario Amodei, then vice president of research.

[^23]: Reuters. ["Anthropic v. OpenAI: Behind the bitter battle for the future of AI"](https://www.reuters.com/legal/transactional/anthropic-v-openai-behind-bitter-battle-future-ai-2026-06-11/). June 11, 2026. Reuters places the rupture that gave rise to Anthropic in disagreements around safety, commercialization, strategy, governance, and leadership.