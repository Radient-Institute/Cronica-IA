---
weight: 4
bookFlatSection: true
title: "04 – The Coral"
image: _din_style/banner_images/04_ec.webp
---

# The Coral

While LLMs were capturing nearly all the headlines, the other—and older—front of the AI revolution (image generation) was far from standing still. By 2023, this technology had ceased to be a laboratory experiment and had become a real industry, with solid products and a rapidly flourishing ecosystem.

The undisputed leader among proprietary models was MidJourney,[^1] while Stable Diffusion 1.5–2.1 led the open models.[^2] Both had achieved something extraordinary: bringing visual design closer to people without technical backgrounds while, at the same time, pushing industry professionals (after the inevitable stages of anger and denial) to begin incorporating these tools into their workflows. The question was no longer *if* AI would impact graphic design, but *how* and *how fast*.

## Technical Maturation

Do you remember those grotesque images with eight fingers per hand and incomprehensible text that defined the early days of DALL·E 2 and Stable Diffusion? Throughout 2024, those issues gradually became a thing of the past.

Progress did not come from a single breakthrough, but from simultaneous improvements across multiple fronts: more sophisticated techniques, a reconceptualization of how these models were approached that enabled more stable training, and a variety of other tricks. Three paradigms competed to dominate the field:

{{% columns %}}
- {{< card >}}
  #### Variational Paradigm (Noise Prediction Models)  
  Inspired by *Variational Autoencoders* (VAEs), this approach treats the problem as learning to remove noise from a latent representation through multiple iterative steps. (e.g., DDPM, DDIM)[^3]
  {{< /card >}}

- {{< card >}}
  #### Score-Based Paradigm (*Score-Based Models*)  
  Borrowing ideas from energy-based models, this approach conceptualizes the problem as learning the gradient of an evolving data distribution. (e.g., DSM, SSM)[^4]
  {{< /card >}}

- {{< card >}}
  #### Flow Paradigm (*Flow Models*)  
  Drawing from *normalizing flows*, this approach treats the problem as learning the velocity field that transports samples from pure noise into data space along a smooth, continuous trajectory (e.g., *Flow Matching*, *Rectified Flow*).[^5] This paradigm eventually displaced the other two and became the industry standard.
  {{< /card >}}
{{% /columns %}}

Other major improvements came in **architecture**, where the DiT (*Diffusion Transformer*) replaced the venerable U-Net,[^6] enabling more scalable and efficient models; latent spaces were also expanded. In addition, more powerful text *encoders* were introduced (sometimes combining multiple ones),[^7] along with far more precise synthetic *recaptioning* processes in the *datasets*,[^8] allowing models to understand more complex and nuanced instructions.

It is also worth mentioning the arrival of *Consistency Models* (March 2023)[^9] and *Latent Consistency Models*,[^10] which enabled image generation with far fewer inference steps—reducing generation times from tens of seconds to under a second in some cases. This unlocked near–real-time conditional generation, allowing users to see their ideas materialize almost instantly.

## Commercial Platforms

MidJourney maintained its leadership, but the market was rapidly diversifying. Adobe, leveraging its enterprise muscle and massive user base, launched Firefly in March 2023,[^11] later integrating it directly into Photoshop and other tools within its Creative Cloud ecosystem. Leonardo AI emerged as a favorite among content creators.[^12] Ideogram arrived in August[^13] with a differentiated promise: finally, readable text in generated images. And OpenAI—having started it all back in 2021 with DALL·E—doubled down with DALL·E 3,[^14] integrated directly into ChatGPT in September at no additional cost, further democratizing access.

Each platform sought its own niche, whether through aesthetics, integration, variety, or other differentiators.

## The Flourishing of the Open Ecosystem

The community was not left behind, having built a vibrant ecosystem around Stable Diffusion. While SD 1.5 remained the reliable workhorse and SD 2.x received mixed reviews due to inconsistent performance, a new generation of models began to emerge.

{{% details title="Relevant foundational image models" open=false %}}
**DeepFloyd IF** (April 2023)[^15] was among the first models capable of generating readable text. **Stable Diffusion XL** (July 2023)[^16] finally fulfilled the promise of a superior SD version, with better composition and more refined details. **PixArt-Alpha** and **Würstchen** explored alternative architectures.[^17] **SDXL Turbo** demonstrated that speed was achievable.[^18] **Stable Cascade** (February 2024)[^19] and **Stable Diffusion 3** (February 2024)[^20] continued pushing the boundaries. **Playground 2.5** (March 2024)[^21] shifted the focus toward graphic design rather than photorealism.
{{% /details %}}

But the real magic of OSS wasn’t just in the base models—it was in what the community built on top of them.

Hundreds, then thousands of model variants appeared, each specialized in different styles, concepts, or use cases.

{{% details title="Relevant techniques" open=false %}}
- **LoRA** (*Low-Rank Adaptation*): a technique borrowed from LLMs that enabled training model variants with minimal resources.[^22]  
- **DreamBooth**: for teaching models specific concepts.[^22]  
- **IP-Adapters**: for transferring styles and characteristics from reference images.[^22]  
- **ControlNet and its successors**: revolutionized spatial control, allowing generation to be conditioned on depth maps, sketches, human poses, object edges, and more.[^22]  
- ***Relighting* techniques**: for non-destructive lighting adjustments.  
- **Inpainting and *outpainting***: for editing and extending images.
{{% /details %}}

Academia contributed enormously, publishing a steady stream of *papers* with new controllability techniques that went far beyond simple text-to-image generation. Early-adopter professionals no longer had the excuse of limited control and began integrating these methods into their production *pipelines*.

All of this converged in **ComfyUI**,[^23] the interface that became the de facto standard for advanced users. Its node-based system allowed the creation of complex *workflows* by combining multiple models and techniques. The dynamic was clear: release a new technique and you had to integrate it into ComfyUI; release a new model and it had to be available in ComfyUI—because that’s where the most sophisticated users were.

To be honest, in terms of pure quality, *open source* models were always one step behind commercial leaders. But that slight disadvantage was more than compensated by flexibility, granular control, and an infinitely extensible ecosystem—something only open source can provide.

## The Engine Runs Out of Fuel

The story of Stability AI is a case study in the challenges of monetizing *open source* AI and balancing idealistic mission with commercial reality.

### Cracks Begin to Show

In early 2024, rumors began to circulate: Stability AI, despite its massive popularity and its role as the engine of the *open source* image-generation ecosystem, was facing serious financial trouble.[^24] The company that had given the world Stable Diffusion under a permissive commercial license, that had generously funded compute for *open source* organizations like EleutherAI,[^25] Carper AI, and Harmony AI, and that had earned the community’s love and respect—had failed to find a sustainable business model.

The *startup’s* idea was that the fame and recognition gained from its models would translate into lucrative contracts with governments and corporations needing customized models trained on internal data.[^26] Those contracts never arrived—or at least not at the scale required to cover expenses.

Unfortunately, VC money would not be enough to sustain its “philanthropic actions” for long: training expensive models and giving them away, maintaining community compute *clusters*, and funding open research.

Attempts to patch the deficit failed. They launched subscriptions for using their models in applications, but revenues were insufficient and the scheme didn’t work. Key researchers began leaving the company[^27]—and worse still, in March 2024, Emad Mostaque, CEO and public face of Stability and the *open source* movement, resigned.[^27]

### The Pragmatic Turn

The new CEO, Prem Akkaraju,[^28] executed a rapid pivot with survival-driven measures: cutting compute *grants*, downsizing the in-house GPU *cluster*, laying off non-critical staff, and fully refocusing—from an open research lab to a product company for the audiovisual industry.

With finances stabilized, they secured a new funding round.[^28] They added credibility by bringing legendary director James Cameron onto their board.[^29] They rebranded themselves as “the AI *startup* for artists and creatives,” signed strategic *partnerships* with advertising and media giants like WPP,[^30] and began launching more focused—and less popular—products: Marble, Stable Audio Open, Stable Fast 3D.[^31]

They were no longer the idealistic lab that had captured the hearts of the *open source* community. They were a fairly traditional company. Pragmatic, yes. Inspiring, not so much.

### The Heir: Black Forest Labs

But the story has a poetic twist. Robin Rombach, the lead researcher behind Stable Diffusion, had left Stability AI before Emad did. Together with key colleagues from the original team, he founded **Black Forest Labs**[^32] with a clear mission: to continue the technical legacy of Stable Diffusion.

In August 2024 came their first release: **Flux**,[^32] an image generation model that proved the original team hadn’t lost its touch. They launched three versions: **Flux-Schnell** (*open source*, free commercial license), **Flux Dev** (*open source*, paid commercial license), and **Flux Pro** (accessible only via API or through *partners* such as Fal, Freepik, Krea, Leonardo, and even X.AI temporarily).[^32]

The reception was enthusiastic. Flux quickly replaced Stable Diffusion as the de facto standard of the *open source* ecosystem. Subsequently, incremental updates were released, reaching Flux 1.1[^33] and Flux 2[^34]. The model maintained its leadership in an increasingly contested landscape of Chinese alternatives (Qwen-Image[^35] and Z-Image[^36]), at least throughout the rest of 2025.

## References

[^1]: Edwards, Benj. ["AI-imager Midjourney v5 stuns with photorealistic images—and 5-fingered hands"](https://arstechnica.com/information-technology/2023/03/ai-imager-midjourney-v5-stuns-with-photorealistic-images-and-5-fingered-hands/). *Ars Technica*, March 16, 2023.

[^2]: Stability AI. ["Stable Diffusion Public Release"](https://stability.ai/news-updates/stable-diffusion-public-release). August 22, 2022; Stability AI. ["Stable Diffusion v2.1 and DreamStudio Updates"](https://stability.ai/news-updates/stablediffusion2-1-release7-dec-2022). December 7, 2022.

[^3]: Ho, Jonathan; Jain, Ajay; Abbeel, Pieter. ["Denoising Diffusion Probabilistic Models"](https://arxiv.org/abs/2006.11239). June 19, 2020.

[^4]: Song, Yang et al. ["Score-Based Generative Modeling through Stochastic Differential Equations"](https://arxiv.org/abs/2011.13456). November 26, 2020.

[^5]: Lipman, Yaron et al. ["Flow Matching for Generative Modeling"](https://arxiv.org/abs/2210.02747). October 6, 2022; Liu, Xingchao; Gong, Chengyue; Liu, Qiang. ["Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow"](https://arxiv.org/abs/2209.03003). September 2022.

[^6]: Peebles, William; Xie, Saining. ["Scalable Diffusion Models with Transformers"](https://arxiv.org/abs/2212.09748). December 19, 2022.

[^7]: Podell, Dustin et al. ["SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis"](https://arxiv.org/abs/2307.01952). July 2023.

[^8]: Chen, Junsong et al. ["PixArt-α: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis"](https://arxiv.org/abs/2310.00426). September 30, 2023.

[^9]: Song, Yang et al. ["Consistency Models"](https://arxiv.org/abs/2303.01469). March 2, 2023.

[^10]: Luo, Simian et al. ["Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference"](https://arxiv.org/abs/2310.04378). October 6, 2023.

[^11]: Adobe. ["Adobe Unveils Firefly, a Family of New Creative Generative AI"](https://news.adobe.com/news/news-details/2023/adobe-unveils-firefly-a-family-of-new-creative-generative-ai). March 21, 2023; Adobe. ["Adobe Unveils Future of Creative Cloud With Generative AI as a Creative Co-Pilot in Photoshop"](https://news.adobe.com/news/news-details/2023/adobe-unveils-future-of-creative-cloud-with-generative-ai-as-a-creative-co-pilot-in-photoshop). May 23, 2023.

[^12]: Canva. ["Welcome to Canva, Leonardo!"](https://www.canva.com/newsroom/news/leonardo-ai/). July 29, 2024.

[^13]: Ideogram. ["Ideogram 0.1 is open to everyone for free"](https://ideogram.ai/publicly-available). August 29, 2023.

[^14]: OpenAI. ["DALL·E 3"](https://openai.com/index/dall-e-3/). September 2023.

[^15]: Stability AI. ["Stability AI releases DeepFloyd IF, a powerful text-to-image model that can smartly integrate text into images"](https://stability.ai/news-updates/deepfloyd-if-text-to-image-model). April 28, 2023.

[^16]: Podell, Dustin et al. ["SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis"](https://arxiv.org/abs/2307.01952). July 2023.

[^17]: Chen, Junsong et al. ["PixArt-α: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis"](https://arxiv.org/abs/2310.00426). September 30, 2023; Pernias, Pablo; Rampas, Dominic; Aubreville, Marc. ["Wuerstchen: Efficient Pretraining of Text-to-Image Models"](https://arxiv.org/abs/2306.00637). June 1, 2023.

[^18]: Stability AI. ["Introducing SDXL Turbo: A Real-Time Text-to-Image Generation Model"](https://stability.ai/news-updates/sdxl-turbo). November 28, 2023.

[^19]: Stability AI. ["Introducing Stable Cascade"](https://stability.ai/news-updates/introducing-stable-cascade). February 12, 2024.

[^20]: Stability AI. ["Stable Diffusion 3"](https://stability.ai/news-updates/stable-diffusion-3). February 22, 2024.

[^21]: Li, Daiqing et al. ["Playground v2.5: Three Insights towards Enhancing Aesthetic Quality in Text-to-Image Generation"](https://arxiv.org/abs/2402.17245). February 27, 2024.

[^22]: Hu, Edward J. et al. ["LoRA: Low-Rank Adaptation of Large Language Models"](https://arxiv.org/abs/2106.09685). June 17, 2021; Ruiz, Nataniel et al. ["DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation"](https://arxiv.org/abs/2208.12242). August 25, 2022; Ye, Hu et al. ["IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models"](https://arxiv.org/abs/2308.06721). August 13, 2023; Zhang, Lvmin; Rao, Anyi; Agrawala, Maneesh. ["Adding Conditional Control to Text-to-Image Diffusion Models"](https://arxiv.org/abs/2302.05543). February 10, 2023.

[^23]: ComfyUI. ["ComfyUI"](https://github.com/comfyanonymous/ComfyUI). *Open source* project of a node-based graphical interface for building and running modular generation *workflows* with diffusion models.

[^24]: Reuters. ["Stability AI discusses sale amid cash crunch, The Information reports"](https://www.reuters.com/markets/deals/stability-ai-discusses-sale-amid-cash-crunch-information-reports-2024-05-16/). May 16, 2024.

[^25]: Wiggers, Kyle. ["Stability AI, Hugging Face and Canva back new AI research nonprofit"](https://techcrunch.com/2023/03/02/stability-ai-hugging-face-and-canva-back-new-ai-research-nonprofit/). *TechCrunch*, March 2, 2023. Documents that Stability AI allocated part of the capacity of its AWS *cluster* for EleutherAI research.

[^26]: Cai, Kenrick. ["How Stability AI’s Founder Tanked His Billion-Dollar Startup"](https://www.forbes.com/sites/kenrickcai/2024/03/29/how-stability-ais-founder-tanked-his-billion-dollar-startup/). *Forbes*, March 29, 2024.

[^27]: Reuters. ["Stability AI to lay off staff weeks after founder Mostaque resigned as CEO"](https://www.reuters.com/technology/stability-ai-lay-off-staff-weeks-after-founder-mostaque-resigned-ceo-2024-04-18/). April 18, 2024.

[^28]: Reuters. ["Cash-strapped Stability AI raises $80 mln with new CEO and board"](https://www.reuters.com/technology/artificial-intelligence/cash-strapped-stability-ai-raises-80-mln-with-new-ceo-board-2024-06-25/). June 25, 2024.

[^29]: Stability AI. ["James Cameron, Academy Award-Winning Filmmaker, Joins Stability AI Board of Directors"](https://stability.ai/news-updates/james-cameron-joins-stability-ai-board-of-directors). September 24, 2024.

[^30]: Stability AI. ["Stability AI Announces Investment from WPP and New Partnership to Shape the Future of Media and Entertainment Production"](https://stability.ai/news-updates/stability-ai-announces-investment-from-wpp-and-new-partnership-to-shape-the-future-of-media-and-entertainment-production). March 5, 2025; WPP. ["WPP announces investment in Stability AI and new partnership"](https://www.wpp.com/en/news/2025/03/wpp-announces-investment-in-stability-ai). March 5, 2025.

[^31]: Stability AI. ["Introducing Stable Audio Open - An Open Source Model for Audio Samples and Sound Design"](https://stability.ai/news-updates/introducing-stable-audio-open). June 5, 2024; Stability AI. ["Introducing Stable Fast 3D: Rapid 3D Asset Generation From Single Images"](https://stability.ai/news-updates/introducing-stable-fast-3d). August 1, 2024; Stability AI. ["MARBLE: Material Recomposition and Blending in CLIP-Space"](https://stability.ai/research/marble-material-recomposition-and-blending-in-clip-space). June 5, 2025.

[^32]: Black Forest Labs. ["Announcing Black Forest Labs"](https://bfl.ai/blog/24-08-01-bfl). August 1, 2024.

[^33]: Black Forest Labs. ["Announcing FLUX1.1 [pro] and the BFL API"](https://bfl.ai/blog/24-10-02-flux). October 2, 2024.

[^34]: Black Forest Labs. ["FLUX.2: Frontier Visual Intelligence"](https://bfl.ai/blog/flux-2). November 25, 2025; Black Forest Labs. ["FLUX.2 [dev] is now open source"](https://github.com/black-forest-labs/flux2). November 25, 2025.

[^35]: Qwen Team. ["Qwen-Image: Crafting with Native Text Rendering"](https://qwenlm.github.io/blog/qwen-image/). August 4, 2025; Qwen Team. ["Qwen-Image Technical Report"](https://arxiv.org/abs/2508.02324). August 4, 2025.

[^36]: Cai, Huanqia et al. ["Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer"](https://arxiv.org/abs/2511.22699). November 27, 2025; Tongyi-MAI. ["Z-Image"](https://github.com/Tongyi-MAI/Z-Image). Alibaba (Tongyi Lab) *open source* project.
