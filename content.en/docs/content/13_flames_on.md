---
weight: 13
bookFlatSection: true
title: "13 – Flames On"
image: _din_style/banner_images/13_fo.webp
---

# Flames On

## A Taste

We knew OpenAI had a powerful image generator inside GPT-4o, and we also knew Gemini 2 was multimodal. But Google was the first to let us actually try what it meant to generate and edit images with a natively multimodal model. This happened in March 2025.

It wasn’t the first time a competitor got ahead of OpenAI by making a technology available that OpenAI had previously shown only as a demo.

The model still had a lot of rough edges: it failed frequently, produced strange results, and sometimes did nothing at all—just returning the original image. But when it worked, it was genuinely impressive. You uploaded a photo and simply typed: change this object to that one, change the lighting, change the color—and it did it. No masks, no complicated workflows: just natural language. For a limited but meaningful set of cases, clearly expressing your intent was enough.

## The World Learns What’s Possible

OpenAI couldn’t wait any longer. It had to compete on a field it had originally showcased itself, so two weeks later it announced **GPT-4o image generation**, available for free to all ChatGPT users.

The result? It was much better. The quality and instruction-following were on a completely different level.

The only downside—if we really want to nitpick—was that when editing photographs it often altered the entire image even when not asked to, likely due to the refiner/upscaler. It also applied a strange orange filter that made images easily recognizable.

But no one cared. Everyone wanted their **Studio Ghibli–style** photo. Even my former classmates, who didn’t even know what OpenAI was, suddenly had AI-generated images on their profiles. AI went mainstream again, marking OpenAI’s second biggest viral moment after ChatGPT. It was even said they gained **one million new users in a single hour**. Insane.

In August 2025, Google released its second iteration: **Gemini 2.5 Flash** with image generation, nicknamed “nano-banana.” Two months later, they introduced **nano-banana Pro**, based on Gemini 3. The best model to date. What once required training a LoRA with photos of a person, applying a pose ControlNet, and then a relighting model… could now be solved by dragging in an image and typing: “put them sitting at night with neon lights.” It’s still not perfect—but we’re getting there.

## Meanwhile, in OSS

The market for image editing via text instructions was massive, and both Black Forest Labs and Qwen knew it. That’s why, two months after the boom of OpenAI’s image generator, they launched **Kontext** (based on Flux) and **Qwen Image Edit** (based on Qwen Image), respectively.  
Both were still OSS diffusion models (MMDiT: *multimodal diffusion transformers*). They weren’t natively multimodal models like those from Google and OpenAI, but they did a respectable job.

So far, no open lab has managed to deliver a natively multimodal model on par with Google or OpenAI. The OSS standard remains MMDiT. There have been some attempts—such as **Janus** from DeepSeek—but the quality still doesn’t quite measure up.

{{% details title="What is an MMDiT?" open=false %}}
An MMDiT is a multimodal DiT that processes each modality (text, image, etc.) in its own stream, but computes attention over all tokens simultaneously. Each stream has its own layers, but they communicate through joint attention and are later merged in subsequent layers.
{{% /details %}}

In November 2025, Flux made a serious mistake with the release of **Flux 2.0**. With Flux 1.0, there were three versions: Pro (API-only), Dev (OSS with a paid commercial license per image), and Schnell (fully open with a free commercial license). But for Flux 2.0, they released only the private version (Pro) and the OSS version (Dev) with a commercial license costing a minimum of $2,000 per month. The second mistake was technical: the model was enormous—32B parameters (around 90 GB of VRAM)—putting it out of reach for most individual users. Even with aggressive quantization, it barely fit on an RTX 4090.

Alibaba seized the opportunity. Tongyi Lab (Qwen’s sibling lab) launched **Z-Image** and **Z-Image Edit**, with quality close to Flux 2.0 but at a much smaller size: **6B parameters**, fully OSS and with a free commercial license.

It seems Black Forest Labs may be losing the title of OSS standard by prioritizing the corporate market—while Alibaba takes over the community.
