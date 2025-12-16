---
weight: 2
bookFlatSection: true
title: "02 – The Capture of GPT-4"
image: _din_style/banner_images/02_cgpt.webp
---

# The Capture of GPT-4

Just days after the release and subsequent massive success of ChatGPT, a **race to catch up with OpenAI’s technology** began. It wouldn’t be the first time some Prometheus seized the fire—and it wouldn’t be the last.

Three fronts took the initiative: competing companies, the *open source* community, and university labs and research groups. I like to call this period “The Capture of GPT-4,” but before capturing the giant, we first had to catch up with the smaller **GPT-3.5 Turbo**.

The **first attempts** began to materialize in **April 2023**. Universities and labs built synthetic *datasets* based on GPT-3.5 Turbo’s responses and used them to *fine-tune* the base language models available at the time, such as LLaMA 1, Pythia, GPT-Neo, BLOOM, and others. This gave rise to Alpaca, Vicuna, Dolly, Guanaco, Koala, among others.

One particularly interesting OSS initiative was led by YouTuber Yannic Kilcher and called **OpenAssistant**, which aimed to build an open, proprietary *dataset* for the same purpose.

Despite the buzz and celebration around these models, there was a problem. Their answers *felt* like ChatGPT, but the moment you increased the difficulty of the questions, it became clear that we were still far from OpenAI’s technology. The models had learned to speak in a chat format, but as truly useful tools they remained limited.

And although the techniques used by these groups evolved over the months—from simple **SFT to DPO and/or RLHF**—it ultimately took companies and *startups* stepping in to truly push both competition and OSS forward.

The rest of the year would be defined by that rhythm: companies releasing increasingly strong open LLMs, slowly closing the gap with OpenAI. Stability AI released StableLM (April), MosaicML released MPT (May), the UAE’s TII released Falcon (June), Meta released Llama 2 (July), and Mistral released Mistral 7B (September).

Institutions that had previously been only loosely involved with AI recognized the technology’s potential and began investing in LLM research and development. The environment became so competitive that it made little sense to attempt to pretrain or align language models unless you were a *startup* with millions in capital or direct government backing.

At the time, there were two major players who, despite lagging significantly behind, chose to keep their models *closed source*. And although expectations around them were high, they had yet to deliver anything even minimally competitive with the leader. I’m referring to Anthropic with Claude 2 (July) and Google with Bard (March).
