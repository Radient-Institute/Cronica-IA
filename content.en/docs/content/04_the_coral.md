---
weight: 4
bookFlatSection: true
title: "04 – The Coral"
image: _din_style/banner_images/04_ec.webp
---

# The Coral

While LLMs were capturing nearly all the headlines, the other—and older—front of the AI revolution (image generation) was far from standing still. By 2023, this technology had ceased to be a laboratory experiment and had become a real industry, with solid products and a rapidly flourishing ecosystem.

The undisputed leader among proprietary models was MidJourney, while Stable Diffusion 1.5–2.1 led the open models. Both had achieved something extraordinary: bringing visual design closer to people without technical backgrounds while, at the same time, pushing industry professionals (after the inevitable stages of anger and denial) to begin incorporating these tools into their workflows. The question was no longer *if* AI would impact graphic design, but *how* and *how fast*.

## Technical Maturation

Do you remember those grotesque images with eight fingers per hand and incomprehensible text that defined the early days of DALL·E 2 and Stable Diffusion? Throughout 2024, those issues gradually became a thing of the past.

Progress did not come from a single breakthrough, but from simultaneous improvements across multiple fronts: more sophisticated techniques, a reconceptualization of how these models were approached that enabled more stable training, and a variety of other tricks. Three paradigms competed to dominate the field:

{{% columns %}}
- {{< card >}}
  #### Variational Paradigm (Noise Prediction Models)  
  Inspired by *Variational Autoencoders* (VAEs), this approach treats the problem as learning to remove noise from a latent representation through multiple iterative steps. (e.g., DDPM, DDIM)
  {{< /card >}}

- {{< card >}}
  #### Score-Based Paradigm (*Score-Based Models*)  
  Borrowing ideas from energy-based models, this approach conceptualizes the problem as learning the gradient of an evolving data distribution. (e.g., DSM, SSM)
  {{< /card >}}

- {{< card >}}
  #### Flow Paradigm (*Flow Models*)  
  Drawing from *normalizing flows*, this approach treats the problem as learning the velocity field that transports samples from pure noise into data space along a smooth, continuous trajectory (e.g., *Flow Matching*, *Rectified Flow*). This paradigm eventually displaced the other two and became the industry standard.
  {{< /card >}}
{{% /columns %}}

Other major improvements came in **architecture**, where the DiT (*Diffusion Transformer*) replaced the venerable U-Net, enabling more scalable and efficient models; latent spaces were also expanded. In addition, more powerful text *encoders* were introduced (sometimes combining multiple ones), along with far more precise synthetic *recaptioning* processes in the *datasets*, allowing models to understand more complex and nuanced instructions.

It is also worth mentioning the arrival of *Consistency Models* (March 2023) and *Latent Consistency Models*, which enabled image generation with far fewer inference steps—reducing generation times from tens of seconds to under a second in some cases. This unlocked near–real-time conditional generation, allowing users to see their ideas materialize almost instantly.

## Commercial Platforms

MidJourney maintained its leadership, but the market was rapidly diversifying. Adobe, leveraging its enterprise muscle and massive user base, launched Firefly in May 2023, integrating it directly into Photoshop and other tools within its Creative Cloud ecosystem. Leonardo AI emerged as a favorite among content creators. Ideogram arrived in September with a differentiated promise: finally, readable text in generated images. And OpenAI—having started it all back in 2021 with DALL·E—doubled down with DALL·E 3, integrated directly into ChatGPT in September at no additional cost, further democratizing access.

Each platform sought its own niche, whether through aesthetics, integration, variety, or other differentiators.

## The Flourishing of the Open Ecosystem

The community was not left behind, having built a vibrant ecosystem around Stable Diffusion. While SD 1.5 remained the reliable workhorse and SD 2.x received mixed reviews due to inconsistent performance, a new generation of models began to emerge.

{{% details title="Relevant foundational image models" open=false %}}
**DeepFloyd IF** (May 2023) was among the first models capable of generating readable text. **Stable Diffusion XL** (July 2023) finally fulfilled the promise of a superior SD version, with better composition and more refined details. **PixArt-Alpha** and **Würstchen** explored alternative architectures. **SDXL Turbo** demonstrated that speed was achievable. **Stable Cascade** (February 2024) and **Stable Diffusion 3** (February 2024) continued pushing the boundaries. **Playground 2.5** (March 2024) shifted the focus toward graphic design rather than photorealism.
{{% /details %}}

But the real magic of OSS wasn’t just in the base models—it was in what the community built on top of them.

Hundreds, then thousands of model variants appeared, each specialized in different styles, concepts, or use cases.

{{% details title="Relevant techniques" open=false %}}
- **LoRA** (*Low-Rank Adaptation*): a technique borrowed from LLMs that enabled training model variants with minimal resources.  
- **DreamBooth**: for teaching models specific concepts.  
- **IP-Adapters**: for transferring styles and characteristics from reference images.  
- **ControlNet and its successors**: revolutionized spatial control, allowing generation to be conditioned on depth maps, sketches, human poses, object edges, and more.  
- ***Relighting* techniques**: for non-destructive lighting adjustments.  
- **Inpainting and *outpainting***: for editing and extending images.
{{% /details %}}

Academia contributed enormously, publishing a steady stream of *papers* with new controllability techniques that went far beyond simple text-to-image generation. Early-adopter professionals no longer had the excuse of limited control and began integrating these methods into their production *pipelines*.

All of this converged in **ComfyUI**, the interface that became the de facto standard for advanced users. Its node-based system allowed the creation of complex *workflows* by combining multiple models and techniques. The dynamic was clear: release a new technique and you had to integrate it into ComfyUI; release a new model and it had to be available in ComfyUI—because that’s where the most sophisticated users were.

To be honest, in terms of pure quality, *open source* models were always one step behind commercial leaders. But that slight disadvantage was more than compensated by flexibility, granular control, and an infinitely extensible ecosystem—something only open source can provide.

## The Engine Runs Out of Fuel

The story of Stability AI is a case study in the challenges of monetizing *open source* AI and balancing idealistic mission with commercial reality.

### Cracks Begin to Show

In early 2024, rumors began to circulate: Stability AI, despite its massive popularity and its role as the engine of the *open source* image-generation ecosystem, was facing serious financial trouble. The company that had given the world Stable Diffusion under the Apache 2.0 license, that had generously funded compute for *open source* organizations like EleutherAI, Carper AI, and Harmony AI, and that had earned the community’s love and respect—had failed to find a sustainable business model.

The *startup’s* idea was that the fame and recognition gained from its models would translate into lucrative contracts with governments and corporations needing customized models trained on internal data. Those contracts never arrived—or at least not at the scale required to cover expenses.

Unfortunately, VC money would not be enough to sustain its “philanthropic actions” for long: training expensive models and giving them away, maintaining community compute *clusters*, and funding open research.

Attempts to patch the deficit failed. They launched subscriptions for using their models in applications, but revenues were insufficient and the scheme didn’t work. Key researchers began leaving the company—and worse still, in March 2024, Emad Mostaque, CEO and public face of Stability and the *open source* movement, resigned.

### The Pragmatic Turn

The new CEO, Prem Akkaraju, executed a rapid pivot with survival-driven measures: cutting compute *grants*, downsizing the in-house GPU *cluster*, laying off non-critical staff, and fully refocusing—from an open research lab to a product company for the audiovisual industry.

With finances stabilized, they secured a new funding round. They added credibility by bringing legendary director James Cameron onto their board. They rebranded themselves as “the AI *startup* for artists and creatives,” signed strategic *partnerships* with advertising and media giants like WPP, and began launching more focused—and less popular—products: Marble, Stable Audio Open, Stable Fast 3D.

They were no longer the idealistic lab that had captured the hearts of the *open source* community. They were a fairly traditional company. Pragmatic, yes. Inspiring, not so much.

### The Heir: Black Forest Labs

But the story has a poetic twist. Robin Rombach, the lead researcher behind Stable Diffusion, had left Stability AI before Emad did. Together with key colleagues from the original team, he founded **Black Forest Labs** with a clear mission: to continue the technical legacy of Stable Diffusion.

In August 2024 came their first release: **Flux**, an image generation model that proved the original team hadn’t lost its touch. They launched three versions: **Flux-Schnell** (*open source*, free commercial license), **Flux Dev** (*open source*, paid commercial license), and **Flux Pro** (accessible only via API or through *partners* such as Fal, Freepik, Krea, Leonardo, and even X.AI temporarily).

The reception was enthusiastic. Flux quickly replaced Stable Diffusion as the de facto standard of the *open source* ecosystem. With incremental updates reaching Flux 1.1, the model maintained its leadership at least through mid-2025.
