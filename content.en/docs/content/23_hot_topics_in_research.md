---
weight: 23
bookFlatSection: true
title: "23 – Hot Topics in Research"
image: _din_style/banner_images/23_tcdi.webp
---

# Hot Topics in Research

Language models have completely transformed the field of AI. Although some detractors label them a *dead end*, the reality is simple: until a superior alternative appears, they are here to stay. They are the central topic of our era, and unsurprisingly, enormous investment is focused on addressing their current limitations.

## The context window

The attention mechanism scales quadratically with the number of *tokens* in the sequence, which makes extremely large context windows impractical. This has improved dramatically in recent years—from 8k in 2023 to a minimum of 256k in 2025, with some standouts like Google reaching 1M. However, industry engineers claim that with current techniques we could reach 10M. To get to 100M, though, we’ll need a new breakthrough.

This problem has given rise to a very active line of research: alternatives to traditional attention. Almost all proposals follow the same intuition—split the sequence, process it in chunks, and maintain a state. This is how Hyena, RWKV, *State Space Models*, Mamba, Titans, and others emerged. Some of them allow sequences to be processed indefinitely thanks to this recurrent state.

The downside is that, honestly, modeling language with any of these algorithms is still worse than with the old, reliable attention—which, incidentally, has already mutated into dozens of variants: *multi-head latent attention*, *grouped-query attention*, *sparse attention*, among many others.

This leaves us with so-called **hybrid models**, which interleave blocks with linear attention and traditional blocks. You sacrifice some performance, but gain scalability.

Another critical point, beyond window size itself, is how well the model actually *uses* that context. In 2024, a startup called Magic.dev claimed to have a model with a 100M context window: **LTM2-mini**. They then almost completely vanished… but later announced a half-billion-dollar funding round, which makes the market appetite clear: if you figure out how to train models with gigantic windows, you instantly have a startup valued at hundreds of millions.

## Diffusion models for language

One of the strongest criticisms of LLMs is their autoregressive nature: they generate one *token* at a time, and once written, it can’t be changed. Combined with sampling randomness, this can cause errors that propagate. Sure, the model can generate more text to correct itself, but that’s not ideal.

In response, researchers began exploring **language models within the diffusion framework**. That is, the answer doesn’t emerge sequentially, but from noise, with the model refining all parts of the text simultaneously. First a sketch, then progressive refinement. It sounds closer to how humans think—and it’s also much faster: to generate 1024 *tokens*, you no longer need 1024 steps, just a few dozen.

The problem?  
They’re still far behind traditional LLMs—by two to three generations, depending on who you ask. They work, yes, but using them feels like traveling two years into the past in quality and five years into the future in speed.

The first decent model of this type appeared in February 2025: **LlaDA**, an 8B *open source* model. A few days later, the startup Inception Labs launched private access to its proprietary model **MercuryCoder**. And the only frontier lab to show results with this approach was Google, which in April published *benchmarks* of its **Gemini Diffusion**, still private but supposedly comparable to Gemini 1.5 Flash.

## Changing the tokenizer

Another source of frustration among researchers is the tokenizer—the way text is represented before entering the model. There’s always a *trade-off* between vocabulary size and sequence length.

Proposals abound:

- training directly on bits,  
- using dynamic tokenizers,  
- tokenizing in UTF-8,  

but so far, no alternative has been proven and validated at commercial scale.

## Continual learning

In October 2025, Karpathy dropped one of his memorable lines:

> “We’re not building animals; we’re summoning spirits.”

He was referring to one of the most criticized limitations of LLMs: **they don’t learn continuously**.

While a chat session is active, everything flows. But opening a new conversation means starting from scratch again. There are stopgaps, like vector databases or documents that act as episodic memory, but true continual learning remains a holy grail of the field.

## Energy-based models

Stepping outside the current paradigm, there are **energy-based models**, popularized by Hinton and LeCun. Unlike probabilistic models, these learn a function that measures affinity between data *x* and data *y*:

> low energy = compatible,  
> high energy = incompatible.

Generating an answer *y* for a question *x* simply involves navigating that *energy landscape* via gradient descent until a low-energy point is found. The concept is elegant, but building frontier-scale models with this approach is still an open challenge.

## World models

What is a “world model”? Curiously, this question became a meme on Twitter a few months ago. It’s an idea that feels intuitive, yet hard to verbalize.

Let’s take Schmidhuber’s definition:  
a world model is **the mental representation we build of the environment from what we perceive**, a simplification of the real system based on selected concepts and relationships.

The question is: *how do we build this in AI?*

Some believe it emerges automatically in LLMs. Others bet on conditioned video generators, like the **Genie** series. Others aim to obtain it through self-supervised learning on images and videos, like Yann LeCun with **JEPAs**, or Fei-Fei Li with her 3D models.

Perhaps—just perhaps—the world models were the friends we made along the way. 🙂

---

In a talk at NeurIPS 2024, Ilya Sutskever said that **the era of pretraining scale had come to an end**. He compared it to fossil fuels: extremely useful, but already exhausted.

He showed a graph of mammalian brain volume as a function of body size. For millions of years, it followed a scaling law—until hominids appeared, whose relationship broke the trend with a much steeper slope.

Nature found a new way to scale in us. We must find it too.

And in October 2025, Ilya posted a tweet saying it was “the best day of his life.”  
Has he found something truly revolutionary?
