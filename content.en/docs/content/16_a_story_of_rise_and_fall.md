---
weight: 16
bookFlatSection: true
title: "16 – A Story of Rise and Fall"
image: _din_style/banner_images/16_hayc.webp
---

# A Story of Rise and Fall

The metaverse was a monumental failure—we all know that by now—but just as it was nearing its end, a new promising technology arrived: artificial intelligence. Fortunately for Meta, its starting line wasn’t zero. Back in 2013, Facebook had created a top-tier lab in Paris: FAIR (Facebook AI Research), giving the company a more-than-solid technical foundation to embark on this new journey.

Up until 2023, Meta was extremely influential across multiple areas of AI. In computer vision: DeepMask, Mask R-CNN, Detectron. In audio: HuBERT and wav2vec. In language: fastText, fairseq, RoBERTa, BART, XLM, NLLB. And of course, the most influential project of all: PyTorch, now the most popular deep learning framework in the world.

Meta practiced **open source** and, above all, **open science**: detailed reports, ablations, reflections, open discussion. It was a time when *machine learning* was more science than business.

When massive scaling of language models began—and after Facebook rebranded as Meta—FAIR came to stand for “Fundamental AI Research,” becoming a semi-independent lab within Meta AI. That lab decided to step away from training large language models; responsibility for that fell to other teams that were neither fully prioritized nor well coordinated.

- In response to GPT-3, they released OPT-175B (2022).  
- Shortly before ChatGPT (GPT-3.5-turbo), they released Galactica.  
- And in early 2023, they announced the **LLaMA** series: 7B up to 65B. (There was also Team Zeta, but shh… we don’t talk about that.)

## A Beneficial Accident

With OPT and LLaMA, Meta changed its release strategy. Since GPT-2, OpenAI had been warning us about the risks derived from LLM capabilities and the dangers of making them public. So Meta released LLaMA behind a restricted-access form, supposedly only for research. In reality, it wasn’t very restrictive—an unknown like me, with no relevant affiliation, was able to access the weights without much trouble.

And just as they gave access to unknowns, one unknown decided to leak the weights on 4chan in March 2023 (it wasn’t me, I promise).

Meta tried to stop the spread on Hugging Face, but it was impossible. Adoption exploded. That likely motivated **LLaMA 2** to return to a fully open philosophy: a technical paper and many accessible variants. Released in July, it was an absolute success. It even included *chat* versions, a somewhat odd but usable commercial license, and very solid performance. The community embraced it—*fine-tuned* it, modified it, quantized it, extended its context, put it into production…  
Surprisingly, **Meta were the good guys of AI**.

In April of the following year, they decided to go *all-in*. Mark Zuckerberg appeared in a video personally announcing **LLaMA 3** (8B and 70B), declaring his love for open source: that open source should win in AI, that Meta would invest enormous amounts of money to make it happen, that they would build massive data centers with hundreds of thousands of GPUs, that they would become the platform. They made the model freely available in Meta AI, on the glasses, and across their apps (WhatsApp, Facebook, Instagram). It was a true *all-in* move.

## Headwinds

The launch was good—but not extraordinary. By then, very strong alternatives already existed, and LLaMA failed to stand out. It couldn’t understand images due to the lack of a vision module, and it also lacked a wider range of model sizes. They tried to fix this with LLaMA 3.1, 3.2, and 3.3: versions with vision, tiny 1B models, and a massive 405B variant. But nothing truly impressed. The competition was moving faster.

Meanwhile, FAIR (under Yann LeCun’s leadership) maintained its own agenda. LeCun had long been arguing—against the rest of the industry—that LLMs do not reason, that AGI is very far away, that before reaching human intelligence we should reach that of a dog, and that LLMs don’t even get that far. He insisted that LLMs have no world model, cannot plan, that everything should happen in latent space, and that anyone pursuing AGI shouldn’t be working on LLMs.

And he followed through: FAIR did not publish any LLMs. They released DINOv2 (April 2023), ImageBind (May 2023), MusicGen (June 2023), SAM (July 2023), MAGNeT, V-JEPA, SAM 2 (August 2024)… genuinely important research and models—but far removed from the LLM race.

While the community desperately demanded innovation from Meta, the company responded to GPT-4o only with research prototypes like Chameleon (for images) or Spirit (for audio), which—while interesting—were not aimed at users, as their quality wasn’t good enough to be useful.

In hindsight, it was clear they were running out of fuel. But many of us (myself included) chose to trust Zuckerberg, who promised that **LLaMA 4** would be not only the best open model, but the best model in the world.  
An exciting, almost heroic speech in favor of open source.

April 2025 arrived. It was time to pay up on all those promises—and it was a **total failure**.

Only two variants, both relatively large MoEs (109B and 409B), plus the promise of a future monstrosity called *Behemoth*, with 1T parameters—which has yet to see the light of day, likely due to embarrassment over its poor performance. Worse still, they cheated on the LMarena leaderboard by using a different model than the one they released, and trained on the *test set* to inflate benchmark scores.  
All of this, only for the community to discover within hours that the model was bad. Today, almost no one uses it.

I exaggerate a bit… but the backlash was massive. The reputation was in shambles. Some Meta AI employees even clarified on their CVs that they did **not** work on LLaMA 4.

## Let’s Start Again

The situation was terrible. But Mark made an interesting decision: **clean house and buy a new team**. Between resignations, layoffs, and internal reshuffling, the board was wiped clean. And Zuckerberg opted for a radical move:

> “I need a new AI team… but I don’t know much about AI anymore, and I don’t really know how to build teams either (I’ve lost my *founder mode* touch).  
> Better to just buy one.”

And so began the *offer tour*:  
> “Hey, Aravind (founder of **Perplexity**), sell me your startup.” → No.  

> “Hey Mira (founder of **Thinking Machine Labs**), sell me your startup.” → No.  

> “Ilya (founder of **SSI**), want to sell your startup?” → No.  

> “Mark Chen (CRO of **OpenAI**), want to come to Meta?” → No, not even for a billion.  

Until finally:  
> “Hey, Alexandr (founder of **Scale AI**), sell me your startup. I’ll give you almost half for $14B.” → Ok.

And Alexandr accepted. Mark also gave him leadership of the new **Meta Superintelligent Labs**. Because of course—if you’re going for artificial general intelligence, why not skip straight to superintelligence?

At the end of the day, Mark didn’t actually buy an AI lab (Scale AI is a data company), so the team still needed researchers. Meta began offering enormous contracts to researchers from OpenAI, Anthropic, Google DeepMind, Microsoft, Apple—rumors speak of more than $100M over four years.

Many declined. Others accepted.

Meanwhile, FAIR continued publishing research: V-JEPA 2, DINO v3.

Meta announced the new structure, with multiple divisions—infra, product, fundamental research, LLMs—all working in coordination under this new lab, led by Alexandr.

Will Meta be able to compete again at Google’s level? Will they manage to integrate AI effectively into their products? Will they maintain their open source and open science stance? Will there be a positive return on this massive investment?

Questions that only the coming years will answer.

---

**Notes:**

1. FAIR *did* work with LLMs, but not with the intention of training a model or a series of models to compete with AI companies. Their work focused on scientific analysis: understanding how LLMs function, which components drive certain behaviors, and what their limitations are.
