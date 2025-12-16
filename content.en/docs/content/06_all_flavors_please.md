---
weight: 6
bookFlatSection: true
title: "06 – All Flavors, Please"
image: _din_style/banner_images/06_afp.webp
---

# All Flavors, Please

It’s May 2024. The little GPT-3.5-Turbo had already been captured by an *open source* model, and GPT-4-Turbo now faced real competition from a proprietary one. OpenAI knew it was time to pull ahead once again. So they opened their drawer of mysteries and unveiled one of their most eye-catching projects: **GPT-4o**, an *omni* model trained directly on text, audio, and images. Hence the name: *GPT-4 omni*.

{{% details title="Native Multimodality" open=false %}}
It’s true that GPT-4 could already accept images and answer questions about them. But it did so through a different trick: after training the text model, a separate vision model was added to extract image *features*, which were then projected into the text model’s *embedding* space.

Native multimodality, by contrast, means tokenizing all data types into the same *embedding* space and training the model across all modalities, either in stages or jointly. This gives the model the ability to handle, understand, and generate text, audio, and images natively within a single sequence.
{{% /details %}}

## An Early Promise

The concept of multimodality had been driven primarily by Google between 2020 and 2022, but it was OpenAI that managed to execute it cleanly. For the first time, we had a model that could *read, listen, and see*—and therefore *write, speak, and draw*. A more powerful version of *Her*. No cheap *text-to-speech* and *speech-to-text* hacks; that was old technology. The future was now. Or at least, that’s what many of us believed.

The demos were impressive:

A student struggling with math could simply open ChatGPT, point the camera at their notebook, and receive a step-by-step explanation—spoken aloud—while the model saw exactly what they were writing.

A programmer with little social life could open ChatGPT and, quite literally, have Scarlett Johansson as an emotional companion… well, not exactly, since the actress refused to allow her voice to be used to train the model.

The problem was that these features took far too long to arrive.  
Voice mode only became available in September (four months after the announcement).  
Video mode arrived in December (seven months later).  
And image generation followed in March 2025 (ten months later).

The delay was long enough that the French *startup* **Kyutai Labs** beat them to the punch with an *open source* model called **Moshi**. It didn’t support video—only audio and text—and was fairly limited… but it launched before OpenAI’s voice mode. And it could run on a laptop.

## Reality Sets In

Returning to GPT-4o: as a plain LLM, it was slightly better than GPT-4-Turbo, but nothing revolutionary. It would eventually replace it as the default model across OpenAI’s product lineup.

Despite the massive *hype*, multimodality never fully took off. At first, there was considerable interest in replicating it—with *papers* like **Chameleon** or **Transfusion**—but nothing resembling the fierce race seen with pure LLMs ever emerged:  
there were no major *benchmarks*, no academia obsessively pushing the field forward, and no *startups* building entire businesses on top of this technology.

Google released its own “omni” model in December, while X.AI took a bit longer and launched theirs in February 2025. On the OSS side, there is only one truly relevant model of this type: **Qwen2.5-Omni**, and even that one is not fully natively multimodal.

One key reason may lie in a comment from the CEO of Moonshot AI:  
**pretraining on other data types, such as images or audio, does not improve text performance.**

And since almost the entire ecosystem revolves around text, multimodality lost priority.

Since then, the area has been somewhat neglected when it comes to voice. Even many customer support companies prefer to stick with *speech-to-text* followed by *text-to-speech*: although audio contains important information such as tone, emotion, and speaking speed, models remain smarter, more precise, and more reliable when operating purely on text.

Some *startups* continue to work on voice models—such as **Sesame** or **Hume AI**—but their focus is on conversational naturalness, not on increasing the model’s “intelligence.”

But when it comes to images… that story was very different. As we’ll see later on.
