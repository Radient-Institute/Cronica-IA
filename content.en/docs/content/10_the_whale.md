---
weight: 10
bookFlatSection: true
title: "10 – The Whale"
image: _din_style/banner_images/10_lb.webp
---

# The Whale

## China’s Position Prior to DeepSeek R1

The Western stigma that China “only copies” and is incapable of creating its own technology led some to imagine CCP spies infiltrating major AI labs to steal secrets. But the reality is quite different: China has never been off the radar over the past decade.

It has strong universities, strong professionals, sufficient capital, and although NVIDIA chip restrictions made access to compute more difficult (without fully blocking it), they still found ways to move forward.

Like all U.S. companies (and some European ones), Chinese labs also joined [the capture of GPT-4]({{< relref "02_the_capture_of_gpt_4.md" >}}). By the end of 2023, two players in particular had become especially relevant: Qwen and DeepSeek.

{{% details title="Chinese launches in 2023" open=false %}}
- **Qwen**, with Tongyi Qianwen, Qwen VL, and Qwen 1.5 (August, September, and December).
- **DeepSeek**, with DeepSeek Coder and DeepSeek LLM (November).
{{% /details %}}

Both pointed to a promising 2024. And indeed, it was.

DeepSeek launched **DeepSeek Math** in April—an excellent math model whose paper introduced a *policy gradient* technique that would later become important: **GRPO**. In July, they released an update to their **DeepSeek V2** model, which positioned it as the best OSS model in the world according to **LMarena**, a benchmark based on human preferences that compares model responses side by side to produce an Elo ranking.

Yes—by mid-2024, China already had the best open-source model on the planet, half a year before the West had even processed the idea that Chinese labs could compete at the highest level.

Meanwhile, Qwen announced its **Qwen 2.5** series in September, whose results on traditional benchmarks were so high that many labs avoided including them in comparative tables to avoid looking inferior.

Many people only became aware of DeepSeek in December, when they released **DeepSeek V3**. The whale could not fail: its previous iteration had been the best open model, and this time was no different. V3 crushed all alternatives… albeit at a high cost: it was a **675B-parameter MoE** in total—open source, yes, but without smaller distilled versions. Still, there are always ways to try models for free, so it wasn’t a major issue.

The craze for reasoning models was in full swing, but this release remained relatively contained within AI-obsessed circles, since DeepSeek V3 was an instruction-tuned model, not a reasoning-oriented one.

In their paper, they included a data point that surprised the community: training the checkpoint required 2.82 million H800 hours, equivalent to about **5 million dollars**. The fact that they explicitly mentioned this number would, curiously, become the spark for the stock market collapse the following month.

---

## The Western Shock

In January came the earthquake: **DeepSeek R1**, a “reasoning” model based on V3, trained with RL using **GRPO**, distilled into variants of all sizes, and fully open. It directly rivaled **OpenAI’s O1**.  
It was, quite literally, the first model to approach or match OpenAI in the new paradigm—and it was **Chinese** and **open source**.

It’s worth noting that although OpenAI had announced O3 in December, as had become customary, access to the public was delayed. So in practice, O1 was the only available reasoning model to compare against.

I don’t think anyone expected the DeepSeek R1 launch to spread the way it did. My sister, my father, and my mother all knew about DeepSeek. According to the press, newspapers, and TV news, the Chinese had replicated “the most powerful technology of the West” (supposedly worth hundreds of millions of dollars) in a matter of months, made it free on *chat.deepseek.ai*, and that it had “only cost 5 million.”  
As if employees didn’t earn salaries, experiments didn’t cost money, and all the work since 2023 had simply never happened—the perfect story to sell: a Chinese guy from an investment fund with 5 million dollars and a few months of work had “sunk” OpenAI.

That narrative ignited the chaos. Under this view, the great AI lie was collapsing: what value does NVIDIA have if “you only need 2,000 chips”? Investors punished the stock. The market crashed. And then, as always, it corrected and kept going up. Just another fluctuation like any other.

---

Beyond all the misreadings of the situation, one thing became clear: **China was already on the map, pushing the frontier in its own way.** Because no country or company has a monopoly on great ideas.
