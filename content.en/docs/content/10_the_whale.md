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
- **Qwen**, with Tongyi Qianwen (April),[^1] Qwen-7B/Qwen-VL (August),[^2][^3] Qwen-14B (September)[^4] and Qwen-72B/Qwen-1.8B (November).[^5]
- **DeepSeek**, with DeepSeek Coder[^6] and DeepSeek LLM[^7] (November).
  {{% /details %}}

Both pointed to a promising 2024. And indeed, it was.

DeepSeek launched **DeepSeek Math** in February—an excellent math model whose paper introduced a *policy gradient* technique that would later become important: **GRPO**.[^8] In July, they released an update to their **DeepSeek V2** model, which positioned it as the best OSS model in the world according to **LMSYS** (now known as LMArena), a benchmark based on human preferences that compares model responses side by side to produce an Elo ranking.[^9]

Yes—by mid-2024, China already had the best open-source model on the planet, half a year before the West had even processed the idea that Chinese labs could compete at the highest level.

Meanwhile, Qwen announced its **Qwen 2.5** series in September,[^10] whose results on traditional benchmarks were so high that many labs avoided including them in comparative tables to avoid looking inferior.

Many people only became aware of DeepSeek in December, when they released **DeepSeek V3**.[^11] The whale could not fail: its previous iteration had been the best open model, and this time was no different. V3 crushed all alternatives… albeit at a high cost: it was a **671B-parameter MoE** in total,[^12] open source, yes, but without smaller distilled versions. Still, there are always ways to try models for free, so it wasn’t a major issue.

The craze for reasoning models was in full swing, but this release remained relatively contained within AI-obsessed circles, since DeepSeek V3 was an instruction-tuned model, not a reasoning-oriented one.

In their paper, they included a data point that surprised the community: training the checkpoint required 2.788 million H800 hours, equivalent to about **$5 million**.[^12] The fact that they explicitly mentioned this number would, curiously, become the spark for the stock market collapse the following month.

---

## The Western Shock

In January came the earthquake: **DeepSeek R1**,[^13] a “reasoning” model based on V3, trained with RL using **GRPO**, distilled into variants of all sizes, and fully open.[^14] It directly rivaled **OpenAI’s O1**.[^14]\
It was, quite literally, the first model to approach or match OpenAI in the new paradigm—and it was **Chinese** and **open source**.

It’s worth noting that although OpenAI had announced O3 in December,[^15] as had become customary, public access was delayed.[^16] So in practice, O1 was the only available reasoning model to compare against.

I don’t think anyone expected the DeepSeek R1 launch to spread the way it did. My sister, my father, and my mother all knew about DeepSeek. According to the press, newspapers, and TV news, the Chinese had replicated “the most powerful technology of the West” (supposedly worth hundreds of millions of dollars) in a matter of months, made it free on *chat.deepseek.ai*, and that it had “only cost 5 million.”[^12][^17] As if employees didn’t earn salaries, experiments didn’t cost money, and all the work since 2023 had simply never happened—the perfect story to sell: a Chinese guy from an investment fund with 5 million dollars and a few months of work had “sunk” OpenAI.

That narrative ignited the chaos. Under this view, the great AI lie was collapsing: what value does NVIDIA have if “you only need 2,000 chips”?[^12][^18] Investors punished the stock. The market crashed.[^17] And then, as always, it corrected and kept going up. Just another fluctuation like any other.

---

Beyond all the misreadings of the situation, one thing became clear: **China was already on the map, pushing the frontier in its own way.** Because no country or company has a monopoly on great ideas.

## References

[^1]: Alibaba Cloud. ["Alibaba Cloud Unveils New AI Model to Support Enterprises’ Intelligence Transformation"](https://home.alibabagroup.com/en-US/document-1582482069362049024). April 11, 2023.

[^2]: Qwen Team. ["Qwen"](https://github.com/QwenLM/Qwen). August 3, 2023. Release of Qwen-7B and Qwen-7B-Chat.

[^3]: Qwen Team. ["Qwen-VL"](https://github.com/QwenLM/Qwen-VL). August 22, 2023.

[^4]: Qwen Team. ["Qwen"](https://github.com/QwenLM/Qwen). September 25, 2023. Release of Qwen-14B and Qwen-14B-Chat.

[^5]: Qwen Team. ["Qwen"](https://github.com/QwenLM/Qwen). November 30, 2023. Release of Qwen-72B/Qwen-72B-Chat and Qwen-1.8B/Qwen-1.8B-Chat.

[^6]: DeepSeek. ["DeepSeek Coder"](https://github.com/deepseek-ai/DeepSeek-Coder). November 2, 2023.

[^7]: DeepSeek. ["DeepSeek LLM"](https://github.com/deepseek-ai/DeepSeek-LLM). November 29, 2023.

[^8]: Shao, Zhihong et al. ["DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"](https://arxiv.org/abs/2402.03300). February 5, 2024.

[^9]: DeepSeek. ["DeepSeek-V2-Chat-0628"](https://huggingface.co/deepseek-ai/DeepSeek-V2-Chat-0628). July 2024. Reached #11 globally and #1 among open-source models on LMSYS Chatbot Arena.

[^10]: Qwen Team. ["Qwen2.5: A Party of Foundation Models!"](https://qwenlm.github.io/blog/qwen2.5/). September 19, 2024.

[^11]: DeepSeek. ["DeepSeek-V3"](https://github.com/deepseek-ai/DeepSeek-V3). December 26, 2024.

[^12]: DeepSeek-AI et al. ["DeepSeek-V3 Technical Report"](https://arxiv.org/abs/2412.19437). December 27, 2024. The reported cost of US$5.576 million corresponds to the accounted training compute for the checkpoint, not the total cost of research and development.

[^13]: DeepSeek. ["DeepSeek-R1"](https://github.com/deepseek-ai/DeepSeek-R1). January 20, 2025.

[^14]: Guo, Daya et al. ["DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"](https://arxiv.org/abs/2501.12948). January 22, 2025.

[^15]: OpenAI. ["12 Days of OpenAI — Day 12: o3 preview & call for safety researchers"](https://openai.com/12-days/?day=12). December 20, 2024.

[^16]: OpenAI. ["Introducing OpenAI o3 and o4-mini"](https://openai.com/index/introducing-o3-and-o4-mini/). April 16, 2025.

[^17]: Reuters. ["DeepSeek sets off global tech selloff, Nvidia sheds nearly $600 billion"](https://www.reuters.com/technology/chinas-deepseek-sets-off-ai-market-rout-2025-01-27/). January 27, 2025.

[^18]: Reuters. ["Nvidia says DeepSeek advances prove need for more of its chips"](https://www.reuters.com/technology/nvidia-says-deepseek-advances-prove-need-more-its-chips-2025-01-27/). January 27, 2025.
