---
weight: 2
bookFlatSection: true
title: "02 – The Capture of GPT-4"
image: _din_style/banner_images/02_cgpt.webp
---

# The Capture of GPT-4

Just days after the release and subsequent massive success of ChatGPT, a **race to catch up with OpenAI’s technology** began. It wouldn’t be the first time some Prometheus seized the fire—and it wouldn’t be the last.

Three fronts took the initiative: competing companies, the *open source* community, and university labs and research groups. I like to call this period “The Capture of GPT-4,” but before capturing the giant, we first had to catch up with the smaller **GPT-3.5 Turbo**.

The **first attempts** began to materialize between **March and April 2023**. Universities and labs had built synthetic *datasets* of responses and conversations—many of them obtained from the responses of OpenAI’s proprietary models—and used them to *fine-tune* the base language models available at the time, such as LLaMA 1,[^1] Pythia,[^2] GPT-Neo,[^3] BLOOM,[^4] and others. This gave rise to Alpaca,[^5] Vicuna,[^6] Dolly,[^7] Koala,[^8] among others, and shortly after, Guanaco.[^9]

One particularly interesting OSS initiative was **OpenAssistant**, a community project driven within LAION and co-founded, among others, by researcher and YouTuber Yannic Kilcher, which aimed to build its own open *dataset* for the same purpose.[^10][^11]

Despite the buzz and celebration around these models, there was a problem. Their answers *felt* like ChatGPT, but the moment you increased the difficulty of the questions, it became clear that we were still far from OpenAI’s technology. The models had learned to speak in a chat format, but as truly useful tools they remained limited.[^12]

And although the techniques used by these groups evolved over the months—from simple **SFT to DPO and/or RLHF**[^13][^14]—it ultimately took companies and *startups* stepping in to truly push both competition and OSS forward.

The rest of the year would be defined by that rhythm: companies releasing increasingly strong open LLMs, slowly closing the gap with OpenAI. Stability AI released StableLM[^15] (April), MosaicML released MPT[^16] (May), the UAE’s TII released Falcon[^17] (May), Meta released Llama 2[^18] (July), and Mistral released Mistral 7B[^19] (September).

Institutions that had previously been only loosely involved with AI recognized the technology’s potential and began investing in LLM research and development. The environment became so competitive that it made little sense to attempt to pretrain or align language models unless you were a *startup* with millions in capital or direct government backing.

At the time, there were two major players who, despite lagging significantly behind, chose to keep their models *closed source*. And although expectations around them were high, they had yet to deliver anything even minimally competitive with the leader. I’m referring to Anthropic with Claude[^20] (March) and Claude 2[^21] (July), and Google with Bard[^22] (March).

---

## References

[^1]: Meta AI. ["LLaMA: Open and Efficient Foundation Language Models"](https://ai.meta.com/blog/large-language-model-llama-meta-ai/). February 24, 2023.

[^2]: EleutherAI. ["Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling"](https://blog.eleuther.ai/pythia/). 2023.

[^3]: EleutherAI. ["GPT-Neo: Large-Scale Autoregressive Language Modeling with Mesh-Tensorflow"](https://github.com/EleutherAI/gpt-neo). 2021.

[^4]: BigScience. ["BLOOM: A 176B-Parameter Open-Access Multilingual Language Model"](https://arxiv.org/abs/2211.05100). November 9, 2022.

[^5]: Stanford CRFM. ["Alpaca: A Strong, Replicable Instruction-Following Model"](https://crfm.stanford.edu/2023/03/13/alpaca.html). March 13, 2023.

[^6]: LMSYS Org. ["Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90% ChatGPT Quality"](https://www.lmsys.org/blog/2023-03-30-vicuna/). March 30, 2023.

[^7]: Databricks. ["Hello Dolly: Democratizing the magic of ChatGPT with open models"](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html). March 24, 2023.

[^8]: Geng, Xinyang et al. ["Koala: A Dialogue Model for Academic Research"](https://bair.berkeley.edu/blog/2023/04/03/koala/). Berkeley Artificial Intelligence Research, April 3, 2023.

[^9]: Dettmers, Tim, et al. ["QLoRA: Efficient Finetuning of Quantized LLMs"](https://arxiv.org/abs/2305.14314). May 23, 2023. Guanaco, a 65B model trained with QLoRA, outperformed all previous open models on the Vicuna benchmark.

[^10]: LAION AI. ["OpenAssistant"](https://open-assistant.io/). LAION community / Yannic Kilcher. Project to build an open assistant *dataset* and model.

[^11]: Köpf, Andreas et al. ["OpenAssistant Conversations — Democratizing Large Language Model Alignment"](https://arxiv.org/abs/2304.07327). April 14, 2023.

[^12]: Gudibande, Arnav et al. ["The False Promise of Imitating Proprietary LLMs"](https://arxiv.org/abs/2305.15717). May 25, 2023.

[^13]: Stability AI. ["StableVicuna: The AI World's First Open Source RLHF LLM Chatbot"](https://stability.ai/news-updates/stablevicuna-open-source-rlhf-chatbot). April 28, 2023.

[^14]: Rafailov, Rafael et al. ["Direct Preference Optimization: Your Language Model is Secretly a Reward Model"](https://arxiv.org/abs/2305.18290). May 29, 2023.

[^15]: Stability AI. ["StableLM"](https://github.com/Stability-AI/StableLM). April 2023.

[^16]: MosaicML. ["Introducing MPT-7B: A New Standard for Open-Source, Commercially Usable LLMs"](https://www.mosaicml.com/blog/mpt-7b). May 5, 2023.

[^17]: Technology Innovation Institute. ["UAE's Technology Innovation Institute Launches Open-Source Falcon 40B Large Language Model"](https://www.tii.ae/news/uaes-technology-innovation-institute-launches-open-source-falcon-40b-large-language-model). May 25, 2023.

[^18]: Meta AI. ["Meta and Microsoft Introduce the Next Generation of Llama"](https://ai.meta.com/blog/llama-2/). July 18, 2023.

[^19]: Mistral AI. ["Mistral 7B"](https://mistral.ai/news/announcing-mistral-7b/). September 27, 2023.

[^20]: Anthropic. ["Introducing Claude"](https://www.anthropic.com/news/introducing-claude). March 14, 2023.

[^21]: Anthropic. ["Claude 2"](https://www.anthropic.com/news/claude-2). July 11, 2023.

[^22]: Google. ["Try Bard and share your feedback"](https://blog.google/technology/ai/try-bard/). March 21, 2023.
