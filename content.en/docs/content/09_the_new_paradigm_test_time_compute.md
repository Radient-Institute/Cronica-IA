---
weight: 9
bookFlatSection: true
title: "09 – The New Paradigm (Test Time Compute)"
image: _din_style/banner_images/09_enpttc.webp
---

# The New Paradigm (Test Time Compute)

In late 2023 rumors began to circulate: press leaks, anonymous Twitter posts, and vagueposting from OpenAI researchers. These rumors revolved around an alleged major internal breakthrough. It was said they had a model that had “rediscovered mathematics,” something that could represent a total paradigm shift. Among the names mentioned were **Q\***[^1] and, later on in July, **Strawberry**.[^2]

Strawberry was officially presented in September 2024 under the name **O1**, inaugurating a new series of language models.[^3] These were models trained with *reinforcement learning* so that, when faced with a question, they would first generate a sequence of tokens known as a *chain of thought* (CoT) before producing the final answer.[^3]

Chain-of-thought was not new. Even before ChatGPT, we already had papers like *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*[^4] or *STAR*,[^5] which explored this idea. And in the post-ChatGPT era, chain-of-thought became an extremely popular prompting technique.

The idea of spending more compute at inference time wasn’t new either. There were already proposals such as OpenAI’s *Let’s Verify Step by Step*,[^6] along with methods like *ReAct*[^7] or *Tree-of-Thoughts*,[^8] all pushing in the same direction: squeezing more out of test-time compute to improve reasoning.

The truth is that believing we could obtain perfect answers to complex problems simply by scaling Transformer pretraining was naive—especially when those problems don’t appear in large quantities within the training dataset.\
Now there was a new dimension to scale: test-time compute. And from it, more “intelligence” could be extracted.[^3]

Somewhat surprisingly, OpenAI gave access to O1 to all ChatGPT subscribers.[^3]

---

With this novelty came new benchmarks, which were not designed to evaluate AI models but now served to showcase their strengths, such as **AIME 2024** or the **Codeforces** ranking.[^3] OpenAI also helped popularize others, like **GPQA Diamond**.[^9]

The models were trained with a base of reasoning chains to push them toward responses of the form: “First I’m going to think about this, then about that…”.[^3] On top of that, a large amount of RL was applied in some synthetic environment. Areas with easy verification—such as **code** and **mathematics**—benefited especially. The models became more reliable at complex tasks, particularly those requiring **backtracking**.[^3]\
Naturally, this was marketed as models that now “think and reason.”

As usual, the OSS community rushed headfirst to try to replicate it. Notable efforts included GAIR’s work, which documented their entire journey,[^10] and Qwen’s, which managed to prototype QwQ very quickly—though it was still immature.[^11] In 2024, RL was still considered a highly unstable and difficult process to execute, and generally “not as effective” as one might hope.

Those who would eventually find a reproducible formula would appear the following year, from the Middle Kingdom, and would shake the global economy.

---

With reasoning and RL, OpenAI hinted that they had found a nearly unlimited improvement technique. And the next version didn’t take long: in December, they introduced **O3-preview** (skipping a number for branding reasons).[^12]

While **O1-preview** hovered around the **62nd percentile** on Codeforces,[^13] **O3-preview** reached **global rank 175**, roughly the **99.8th percentile**.[^12] An especially trained version even managed to defeat **ARC-AGI**, a previously unbeaten benchmark aimed at measuring fluid intelligence.[^14]

O3-preview itself was never released to the public.[^14] Instead, **O3** (a smaller, more polished version) arrived alongside **O4 mini**, both in April.[^15]\
That was the last model of the O series—at least from a user-facing perspective—as OpenAI decided to merge the O saga into its main line: GPT.[^15]

## References

[^1]: Reuters. ["OpenAI researchers warned board of AI breakthrough ahead of CEO ouster, sources say"](https://www.reuters.com/technology/openai-researchers-warned-board-ai-breakthrough-ahead-ceo-ouster-sources-2023-11-22/). November 22, 2023.

[^2]: Reuters. ["OpenAI working on new reasoning technology under code name 'Strawberry'"](https://www.reuters.com/technology/artificial-intelligence/openai-working-new-reasoning-technology-under-code-name-strawberry-2024-07-12/). July 12, 2024.

[^3]: OpenAI. ["Learning to reason with LLMs"](https://openai.com/index/learning-to-reason-with-llms/). September 12, 2024. OpenAI presented o1-preview.

[^4]: Wei, Jason et al. ["Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"](https://arxiv.org/abs/2201.11903). January 28, 2022.

[^5]: Zelikman, Eric et al. ["STaR: Bootstrapping Reasoning With Reasoning"](https://arxiv.org/abs/2203.14465). March 28, 2022.

[^6]: Lightman, Hunter et al. ["Let's Verify Step by Step"](https://arxiv.org/abs/2305.20050). May 31, 2023.

[^7]: Yao, Shunyu et al. ["ReAct: Synergizing Reasoning and Acting in Language Models"](https://arxiv.org/abs/2210.03629). October 6, 2022.

[^8]: Yao, Shunyu et al. ["Tree of Thoughts: Deliberate Problem Solving with Large Language Models"](https://arxiv.org/abs/2305.10601). May 17, 2023.

[^9]: Rein, David et al. ["GPQA: A Graduate-Level Google-Proof Q&A Benchmark"](https://arxiv.org/abs/2311.12022). November 20, 2023.

[^10]: GAIR-NLP. ["O1 Replication Journey"](https://github.com/GAIR-NLP/O1-Journey). October 2024.

[^11]: Qwen Team. ["QwQ: Reflect Deeply on the Boundaries of the Unknown"](https://qwenlm.github.io/blog/qwq-32b-preview/). November 28, 2024.

[^12]: OpenAI. ["12 Days of OpenAI — Day 12: o3 preview & call for safety researchers"](https://openai.com/12-days/?day=12). December 20, 2024. OpenAI presented o3 and o3-mini without releasing them to the public.

[^13]: OpenAI. ["Learning to reason with LLMs"](https://openai.com/index/learning-to-reason-with-llms/). September 12, 2024. o1-preview obtained a rating of 1258 on Codeforces, approximately the 62nd percentile.

[^14]: Chollet, François. ["OpenAI o3 Breakthrough High Score on ARC-AGI-Pub"](https://arcprize.org/blog/oai-o3-pub-breakthrough). ARC Prize. December 20, 2024. The o3 evaluated had been trained on part of the public training set of ARC-AGI-1 and obtained 75.7% with lower compute and 87.5% using approximately 172 times more.

[^15]: OpenAI. ["Introducing OpenAI o3 and o4-mini"](https://openai.com/index/introducing-o3-and-o4-mini/). April 16, 2025. OpenAI released o3 and o4-mini and stated it was converging the specialized reasoning capabilities of the O series with the conversational capabilities of the GPT series.
