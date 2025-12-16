---
weight: 9
bookFlatSection: true
title: "09 – The New Paradigm (Test Time Compute)"
image: _din_style/banner_images/09_enpttc.webp
---

# The New Paradigm (Test Time Compute)

In March 2024, rumors began to circulate: press leaks, anonymous Twitter posts, and vagueposting from OpenAI researchers. These rumors revolved around an alleged major internal breakthrough. It was said they had a model that had “rediscovered mathematics,” something that could represent a total paradigm shift. Among the names mentioned were **Q\*** and, later on, **Strawberry**.

Strawberry was officially presented in September 2024 under the name **O1**, inaugurating a new series of language models. These were models trained with *reinforcement learning* so that, when faced with a question, they would first generate a sequence of tokens known as a *chain of thought* (CoT) before producing the final answer.

Chain-of-thought was not new. Even before ChatGPT, we already had papers like *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* or *STAR*, which explored this idea. And in the post-ChatGPT era, chain-of-thought became an extremely popular prompting technique.

The idea of spending more compute at inference time wasn’t new either. There were already proposals such as OpenAI’s *Let’s Verify Step by Step*, along with methods like *ReAct* or *Tree-of-Thoughts*, all pushing in the same direction: squeezing more out of test-time compute to improve reasoning.

The truth is that believing we could obtain perfect answers to complex problems simply by scaling Transformer pretraining was naive—especially when those problems don’t appear in large quantities within the training dataset.  
Now there was a new dimension to scale: test-time compute. And from it, more “intelligence” could be extracted.

Somewhat surprisingly, OpenAI gave access to O1 to all ChatGPT subscribers.

---

With this novelty came new benchmarks designed to showcase its strengths, such as **AIME 2024** or the **Codeforces** ranking. OpenAI also helped popularize others, like **GPQA Diamond**.

The models were trained with a base of reasoning chains to push them toward responses of the form: “First I’m going to think about this, then about that…”. On top of that, a large amount of RL was applied in some synthetic environment. Areas with easy verification—such as **code** and **mathematics**—benefited especially. The models became more reliable at complex tasks, particularly those requiring **backtracking**.  
Naturally, this was marketed as models that now “think and reason.”

As usual, the OSS community rushed headfirst to try to replicate it. Notable efforts included GAIR’s work, which documented their entire journey, and Qwen’s, which managed to prototype QwQ very quickly—though it was still immature. In 2024, RL was still considered a highly unstable and difficult process to execute, and generally “not as effective” as one might hope.

Those who would eventually find a reproducible formula would appear the following year, from the Middle Kingdom, and would shake the global economy.

---

With reasoning and RL, OpenAI hinted that they had found a nearly unlimited improvement technique. And the next version didn’t take long: in December, they introduced **O3-preview** (skipping a number for branding reasons).

While **O1-preview** hovered around the **62nd percentile** on Codeforces, **O3-preview** reached **global rank 175**, roughly the **99th percentile**. An especially trained version even managed to defeat **ARC-AGI**, a previously unbeaten benchmark aimed at measuring fluid intelligence.

O3-preview itself was never released to the public. Instead, **O3** (a smaller, more polished version) arrived alongside **O4 mini**, both in April.  
That was the last model of the O series—at least from a user-facing perspective—as OpenAI decided to merge the O saga into its main line: GPT.
