---
weight: 6
bookFlatSection: true
title: "06 – All Flavors, Please"
image: _din_style/banner_images/06_afp.webp
---

# All Flavors, Please

It’s May 2024. The little GPT-3.5-Turbo had already been captured by an *open source* model, and GPT-4-Turbo now faced real competition from a proprietary one. OpenAI knew it was time to pull ahead once again. So they opened their drawer of mysteries and unveiled one of their most eye-catching projects: **GPT-4o**, an *omni* model trained directly on text, audio, and images. Hence the name: *GPT-4 omni*.[^1]

{{% details title="Native Multimodality" open=false %}}
It’s true that GPT-4 could already accept images and answer questions about them. But it did so through a different trick:[^2] after training the text model, a separate vision model was added to extract image *features*, which were then projected into the text model’s *embedding* space.

Native multimodality, by contrast, means tokenizing all data types into the same *embedding* space and training the model across all modalities, either in stages or jointly. This gives the model the ability to handle, understand, and generate text, audio, and images natively within a single sequence.
{{% /details %}}

## An Early Promise

The concept of multimodality had been driven primarily by Google between 2020 and 2022,[^3][^4] but it was OpenAI that managed to execute it cleanly. For the first time, we had a model that could *read, listen, and see*—and therefore *write, speak, and draw*. A more powerful version of *Her*. No cheap *text-to-speech* and *speech-to-text* hacks; that was old technology. The future was now. Or at least, that’s what many of us believed.

The demos were impressive:

A student struggling with math could simply open ChatGPT, point the camera at their notebook, and receive a step-by-step explanation—spoken aloud—while the model saw exactly what they were writing.

A programmer with little social life could open ChatGPT and, quite literally, have Scarlett Johansson as an emotional companion… well, not exactly, since the actress rejected the offer to lend her voice to the system.[^5]

The problem was that these features took far too long to arrive.  
Voice mode only became available in September (four months after the announcement).[^6]  
Video mode arrived in December (seven months later).[^7]  
And image generation followed in March 2025 (ten months later).[^8]

The delay was long enough that the French *startup* **Kyutai Labs** beat them to the punch with an *open source* model called **Moshi**.[^9] It didn’t support video—only audio and text—and was fairly limited… but it launched before OpenAI’s voice mode. And it could run on a laptop.[^10]

## Reality Sets In

Returning to GPT-4o: as a plain LLM, it was slightly better than GPT-4-Turbo, but nothing revolutionary. It would eventually replace it as the default model across OpenAI’s product lineup.

Despite the massive *hype*, multimodality never fully took off. At first, there was considerable interest in replicating it—with *papers* like **Chameleon** or **Transfusion**—[^11][^12] but nothing resembling the fierce race seen with pure LLMs ever emerged:  
there were no major *benchmarks* to evaluate and improve these new capabilities,[^13] no academia obsessively pushing the field forward, and no *startups* building entire businesses on top of this technology.

Google released its own “omni” model in December,[^14] while X.AI took a bit longer and launched theirs in February 2025.[^15] On the OSS side, there was only one model of this type that achieved some degree of relevance: **Qwen2.5-Omni**.[^16]

One key reason may lie in a comment from the CEO of Moonshot AI:  
**pretraining on other data types, such as images or audio, does not improve text performance.**[^17]

And since almost the entire ecosystem revolves around text, multimodality lost priority.

Since then, the area has been somewhat neglected when it comes to voice. Even many customer support companies prefer to stick with *speech-to-text* followed by *text-to-speech*: although audio contains important information such as tone, emotion, and speaking speed, models remain smarter, more precise, and more reliable when operating purely on text.

Some *startups* continue to work on voice models—such as **Sesame** or **Hume AI**—but their focus is on conversational naturalness, not on increasing the model’s “intelligence”.[^18][^19]

But when it comes to images… that story was very different. As we’ll see later on.

## References

[^1]: OpenAI. ["Hello GPT-4o"](https://openai.com/index/hello-gpt-4o/). May 13, 2024.

[^2]: It has not been confirmed that OpenAI used exactly this methodology to adapt a language model to multimodal data, but it is highly likely because it was the most natural and effective way to do so at the time.

[^3]: Google. ["Google I/O 2021: Being helpful in moments that matter"](https://blog.google/innovation-and-ai/technology/developers-tools/io21-helpful-google/). May 18, 2021.

[^4]: Google. ["MUM: A new AI milestone for understanding information"](https://blog.google/products/search/introducing-mum/). May 18, 2021.

[^5]: Reuters. ["Scarlett Johansson says OpenAI chatbot voice 'eerily similar' to hers"](https://www.reuters.com/technology/scarlett-johansson-says-openai-chatbot-voice-eerily-similar-hers-2024-05-21/). May 21, 2024.

[^6]: Reuters. ["OpenAI starts roll-out of advanced voice mode to some ChatGPT Plus users"](https://www.reuters.com/technology/openai-starts-roll-out-advanced-voice-mode-some-chatgpt-plus-users-2024-07-30/). July 30, 2024.

[^7]: OpenAI. ["Advanced Voice Mode gets video"](https://edunewsletter.openai.com/p/advanced-voice-mode-gets-video-during). December 13, 2024.

[^8]: OpenAI. ["Introducing 4o Image Generation"](https://openai.com/index/introducing-4o-image-generation/). March 25, 2025.

[^9]: Kyutai. ["Moshi: a speech-text foundation model for real-time dialogue"](https://kyutai.org/Moshi.pdf). 2024.

[^10]: Kyutai. ["Moshi"](https://github.com/kyutai-labs/moshi). Official repository; includes an MLX implementation for local execution on Apple Silicon.

[^11]: Chameleon Team. ["Chameleon: Mixed-Modal Early-Fusion Foundation Models"](https://arxiv.org/abs/2405.09818). May 16, 2024.

[^12]: Zhou, Chunting et al. ["Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model"](https://arxiv.org/abs/2408.11039). August 20, 2024.

[^13]: Lin, Guan-Ting et al. ["Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities"](https://arxiv.org/abs/2503.04721). March 6, 2025. The work points out the limitations of existing evaluations for capabilities such as pauses, *backchanneling*, *turn-taking*, and interruptions.

[^14]: Google DeepMind. ["Introducing Gemini 2.0: our new AI model for the agentic era"](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/). December 11, 2024.

[^15]: Edwards, Benj. ["Grok's new 'unhinged' voice mode can curse and scream, simulate phone sex"](https://arstechnica.com/ai/2025/02/groks-uncensored-ai-voice-mode-lets-users-talk-sex-therapy-and-conspiracies/). Ars Technica. February 25, 2025.

[^16]: Xu, Jin et al. ["Qwen2.5-Omni Technical Report"](https://arxiv.org/abs/2503.20215). March 26, 2025.

[^17]: Yang Zhilin. Interview, August 27, 2025. Yang stated: "多模态数据又无法很好提升文本本身的'智商'" — "multimodal data cannot improve the 'intelligence' of text itself."

[^18]: Sesame AI Labs. ["CSM — A Conversational Speech Generation Model"](https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice). 2025.

[^19]: Hume AI. ["Hume Raises $50M Series B and Releases New Empathic Voice Interface"](https://www.hume.ai/blog/series-b). March 25, 2024.
