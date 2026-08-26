---
weight: 8
bookFlatSection: true
title: "08 – La Emisora Que Veo"
image: _din_style/banner_images/08_leqv.webp
---

# La Emisora Que Veo

I think that in recent AI history we haven’t seen a flex as big as Sora. It’s February 2024. After the success of AI image generation, there was massive interest in achieving something equivalent for video. Many *startups* were trying, and huge amounts of money were being invested.

Quality was improving slowly. The infamous *Will Smith eating spaghetti* from March 2023, generated with ModelScope,[^1] was already behind us. Videos were starting to look better, though many were little more than pans with slight motion. 2023 closed with **Runway** leading the *closed source* space with Gen-2[^2] and **Stability AI** at the forefront of *open source* with Stable Video Diffusion.[^3]

Then, in February 2024, OpenAI dropped something absolutely shocking: **Sora**.[^4] It had illogical consistency, illogical quality, illogical actions within clips, and generations lasting up to a minute. Everything was illogical. They didn’t even call it a “video generator”—they presented it as a **“world generator.”**[^4]

How was it possible that a single lab had such an advantage? And let me stress this: video was not a neglected area. There was a lot of money and many teams working intensely in parallel.

The Sora effect was immediate: everyone took a step back to rethink goals and strategies. If there had been doubts about how far AI video could go, now we all knew this level of quality was possible. *Startups* and the *open source* ecosystem got to work.

Within a few months, we saw a wave of competitive launches.

{{% details title="Competitor launches" open=false %}}
- **Kling** in China (June)[^5]
- **Luma AI** entering video with Dream Machine (June)[^6]
- **Runway** announcing Gen-3 (June)[^7]
- **PikaLabs v1.5** (October)[^8]\
  {{% /details %}}

Even some large corporations felt compelled to show demos of things that clearly weren’t ready yet—like Veo 1 from Google[^9] or MovieGen from Meta,[^10] just to make it clear they “weren’t that far behind.”

Meanwhile, OSS advanced at breakneck speed thanks to techniques inherited from image generation: DiT, *flow matching*, *rectified flow*, and more. We got **Open Sora**,[^11] **LTX-Video**[^12] and **CogVideoX**.[^13]

You might imagine OpenAI would use that time to dominate the market alone. But… no. Except for a few selected designers, artists, and film directors, no one had real access to the original Sora model.[^14] Apparently the model was extremely large and extremely expensive to serve,[^15] yet OpenAI claimed that keeping the model without public access was for “safety” reasons and the risks associated with generating video at that level of realism.[^14]

Ten months after the announcement, in December 2024, ChatGPT subscribers were given access to **sora-turbo**, a much inferior version.[^16] Where was the consistency? Where were the one-minute videos? Where was the quality? Well, there was some aesthetic appeal… but overall, sora-turbo was an outright failure.

The one who truly took all the glory was Google. They announced **Veo 3** in May 2025 during Google I/O: a massive leap forward, far superior quality, immediately available, with integrated audio.[^17] The king. Social media exploded. Memes, jokes, and viral videos made with Veo 3 flooded the internet. It was Google’s first truly viral AI product—and they won the race against OpenAI.

MidJourney joined the party later, in June, with its characteristic style and aesthetic.[^18] It’s astonishing to think that this bootstrapped *startup* reached $500 million in revenue in 2025.[^19]

The rest of the year was marked by constant updates from all competitors in the video space: Kling, Hailuo, Luma, Runway… Even Google reinforced its leadership by releasing **Veo 3.1**.[^20]

## Integrating AI Video into Audiovisual Content

AI-generated video has reached a level good enough to be consumed, but it still hasn’t fully integrated into all types of audiovisual content.

Cinema—feature films, series, documentaries—**has not adopted it yet**. The reasons could be many: small quality details, duration limitations, lack of fine-grained control in proprietary models that outperform OSS… or perhaps simply the inherent slowness of the film industry. Honestly, I don’t know.

YouTube has adopted it slightly, mostly as illustrative material. Where AI video truly found its refuge was in **short-form content**: TikTok, Reels, Shorts. Short enough to be generated with one or two *prompts*. Trivial enough that its mistakes don’t even warrant complaint.

## The Infinite *AI Slop* Machine

Short-form platforms filled up with AI videos. We knew that, at some point, someone would launch a social network exclusively for AI-generated video. The question was who—and when. The answer came from two unexpected places: **Meta and OpenAI**, almost in the same week, in September 2025.

Meta went first with **Vibes**, an AI video *feed* inside its Meta AI app.[^21] Since they didn’t have a competitive in-house video model for multimedia generation, they decided to use models from MidJourney and Black Forest Labs.[^22]

OpenAI, on the other hand, launched a full-fledged, standalone social network powered by the also-new **Sora 2**,[^23] a very strong model with a clear focus on social media content. Like Veo 3, it could generate audio and video together.[^23] But the feature that turned it into a viral phenomenon was **cameos**: anyone could scan themselves and ask Sora 2 to generate a video featuring them in any situation.[^23]

Within days of launch, the internet was flooded with videos of celebrities doing absurd things. It wasn’t impossible before—but now it was easier than ever… and free.[^23]

The ins and outs of Sora’s level of success in the months after its launch, its user base, or the internal dynamics of that social network, are beyond my knowledge. I could dive into mega-labyrinths to bring you information, but I’m not going dumpster diving.

## References

[^1]: Cole, Samantha. ["AI Will Smith Eating Spaghetti Will Haunt You For the Rest of Your Life"](https://www.vice.com/en/article/ai-will-smith-eating-spaghetti-hill-haunt-you-for-the-rest-of-your-life/). VICE. March 28, 2023.

[^2]: Runway. ["Gen-2: Generate novel videos with text, images or video clips"](https://runwayml.com/research/gen-2). February 2023.

[^3]: Stability AI. ["Introducing Stable Video Diffusion"](https://stability.ai/news/stable-video-diffusion-open-ai-video-model). November 21, 2023.

[^4]: OpenAI. ["Video generation models as world simulators"](https://openai.com/index/video-generation-models-as-world-simulators/). February 15, 2024.

[^5]: Kuaishou. ["Kuaishou Unveils Proprietary Video Generation Model 'Kling;' Testing Now Available"](https://ir.kuaishou.com/news-releases/news-release-details/kuaishou-unveils-proprietary-video-generation-model-kling). June 10, 2024. Initial access began June 6.

[^6]: Luma AI. ["Introducing Dream Machine"](https://threadreaderapp.com/thread/1800921380034379951.html). June 12, 2024.

[^7]: Runway. ["Runway Gen-3 Alpha: Next-Generation AI Video Generation"](https://runwayml.com/research/introducing-gen-3-alpha). June 17, 2024.

[^8]: Franzen, Carl. ["Pika 1.5 launches with physics-defying AI special effects"](https://venturebeat.com/ai/pika-1-5-launches-with-physics-defying-ai-special-effects). VentureBeat. October 1, 2024.

[^9]: Google. ["New generative media models and tools, built with and for creators"](https://blog.google/innovation-and-ai/products/google-generative-ai-veo-imagen-3/). May 14, 2024. Veo was initially presented through a private preview for selected creators.

[^10]: Meta. ["How Meta Movie Gen could usher in a new AI-enabled era for content creators"](https://ai.meta.com/blog/movie-gen-media-foundation-models-generative-ai-video/). October 4, 2024. Meta later indicated it did not plan to incorporate Movie Gen into public products until 2025.

[^11]: HPC-AI Tech. ["Open-Sora: Democratizing Efficient Video Production for All"](https://github.com/hpcaitech/Open-Sora). March 2024.

[^12]: Lightricks. ["LTX-Video"](https://github.com/Lightricks/LTX-Video). November 21, 2024.

[^13]: THUDM. ["CogVideoX"](https://github.com/THUDM/CogVideo). August 2024. CogVideoX-2B was released on August 6 and CogVideoX-5B on August 27.

[^14]: OpenAI. ["Sora: Creating video from text"](https://openai.com/index/sora/). February 2024.

[^15]: Wiggers, Kyle. ["OpenAI's Sora video generator appears to have leaked"](https://techcrunch.com/2024/11/26/artists-appears-to-have-leaked-access-to-openais-sora/). TechCrunch. November 26, 2024. Reports on *The Information* according to which the original Sora could take more than ten minutes of processing to generate a one-minute clip.

[^16]: OpenAI. ["Sora is here"](https://openai.com/index/sora-is-here/). December 9, 2024.

[^17]: Google. ["Fuel your creativity with new generative media models and tools"](https://blog.google/innovation-and-ai/products/generative-media-models-io-2025/). May 20, 2025. Veo 3 incorporated native audio generation and was available that same day for Ultra subscribers in the United States.

[^18]: MidJourney. ["Introducing Midjourney V1 Video"](https://updates.midjourney.com/introducing-our-v1-video-model/). June 18, 2025.

[^19]: Pofeldt, Elaine. ["The Race To Create A Billion-Dollar, One-Person Business"](https://www.forbes.com/sites/elainepofeldt/2025/11/17/the-race-to-create-a-billion-dollar-one-person-business/). Forbes. November 17, 2025.

[^20]: Google. ["Introducing Veo 3.1 and advanced capabilities in Flow"](https://blog.google/innovation-and-ai/products/veo-updates-flow/). October 15, 2025.

[^21]: Meta. ["Introducing Vibes: A new way to discover and create videos with AI"](https://about.fb.com/ltam/news/2025/09/presentando-vibes-una-nueva-forma-de-descubrir-y-crear-videos-con-ia/). September 25, 2025.

[^22]: Wang, Alexandr. Statements during the Vibes launch, September 25, 2025. ["For this early version, we've partnered with Midjourney and Black Forest Labs while we continue developing our own models behind the scenes."](https://www.techmeme.com/250926/h0135)

[^23]: OpenAI. ["Sora 2 is here"](https://openai.com/index/sora-2/). September 30, 2025. OpenAI launched Sora 2 as a joint video and audio model alongside a social app.
