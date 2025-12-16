---
weight: 20
bookFlatSection: true
title: "20 – Hardware & Robotics"
image: _din_style/banner_images/20_hyr.webp
---

# Hardware & Robotics

## Hardware

### NVIDIA’s Rise and Structural Advantage

It’s worth digging into NVIDIA’s history. They went from being a graphics card company stuck in a rough half-decade to becoming **the most valuable company in the world**.

The reason is fairly simple to explain. By sheer coincidence, the same devices they manufacture (graphics cards) that boost FPS in *Cyberpunk 2077* also turned out to be perfect for training neural networks. Jensen Huang noticed this early and began to **bet heavily on GPUs for data centers**: more VRAM, more bandwidth, better interconnects, massive racks. On the software side, they did the same: CUDA, libraries, framework support for Deep Learning, and so on.

The victory was obvious because there was no real alternative.  
> Want to train an LLM?  
> CPU → impossible  
> AMD GPU → ROCm didn’t work well with PyTorch  
> → So NVIDIA. There was no other option.

### TPUs: The Alternative… Sort Of

Seeing the potential future of AI, one might ask: does it really make sense to use hardware designed for graphics instead of something specialized for tensor computations? Google said no—and released its TPUs (Tensor Processing Units), with ultra-powerful Tensor Cores, robustness, and massive scalability in pods of up to 8,000 units.

But they also come with major drawbacks:

1. **Limited availability.**  
   The beta only began in 2018, they became generally available in 2022, and they can only be rented via Google Cloud (though expansion to other providers is underway).  
   The newest generation (e.g., Ironwood v7) is never available—except to key partners.

2. **Different architecture.**  
   They don’t have hundreds of SMs like GPUs, but rather 1–2 highly optimized cores. This requires a **static-graph–based workflow**, where the entire program must be compiled before execution. PyTorch doesn’t fit this model well, despite attempts to adapt it. If you want to work seriously with TPUs, you need **JAX**.

3. **Price.**  
   A TPU v6 costs around \$3/hour with 32 GB of memory and 1.8 PFLOPS.  
   An NVIDIA B200 costs around \$18/hour (on demand) on Google Cloud with 140 GB of memory and 14 PFLOPS… but you can rent it on GPUList, FAL, or Prime Intellect for **less than \$3/hour**. And if you have enough money, you can buy the GPUs outright. That last option simply doesn’t exist with TPUs.

So… if NVIDIA is superior to the competition, why do we see headlines about major labs (like Meta, OpenAI, Anthropic, or SSI) starting to use Google TPUs and AMD GPUs?

Beyond the fact that **diversification** is critically important—having your entire compute infrastructure tied to a single company is risky—if you’re spending tens of billions per year on compute, it might make sense to assign dozens of employees to build infrastructure and adapt codebases to alternative hardware from a company that’s likely offering special discounts.

Only frontier labs can afford this luxury.  
They can even be more ambitious: if you’re going to spend that much money, why not spend it on designing and manufacturing your own chips? In the second half of 2025, we learned that this is exactly what OpenAI, Meta, and xAI have begun to do.

### Ultra-Fast Inference Chips

Another interesting trend is startups building **chips specialized for inference**, optimized to generate over a thousand tokens per second across different LLMs.

The three major players in this area are **Groq**, **SambaNova**, and **Cerebras**.

They achieve inference *speedups* of around 4× compared to NVIDIA GPUs (not counting gains from *speculative decoding*).

How do they do it? One of NVIDIA chips’ main bottlenecks is HBM bandwidth (VRAM), so these companies build chips with **enormous SRAM memories** that, combined, are large enough to hold all the weights of a mid-sized model—eliminating the need for constant VRAM access. Obviously, this is extremely expensive.

### Radically Different Chips

I eagerly await the day my 8-year-old son asks me to buy him a 3-exaflop compute unit he saw on sale in the metaverse for just \$500 (or its future equivalent). I’ll tell him:  
> “Nah, I’ll get you the 2-exaflop one. You won’t even fully use it. What are you going to do with that anyway—replicate GPT-5?”

Since we’re talking fantasies, we should also mention the startups promising chips not just 10× faster than today’s GPUs, but **1,000× faster**. That’s the fantasy pitched by Etched, whose idea is to engrave the Transformer architecture directly into silicon.

---

An honorary mention goes to those still promising quantum computing. Sure, tell us again—last time was ten years ago and it wasn’t quite clear. Oh wait, this time it is. This time, definitely.

---

Another experimental direction is probabilistic chips, often based on **p-bits**. P-bits are basically bits that physically fluctuate between 0 and 1 with a certain probability. A network of p-bits would allow you to implement an energy-based model (EBM) *physically*, and by letting the network evolve, you could find low-energy states far more efficiently than by simulating them on GPUs.

Several groups are working on this: Tohoku University, IBM, Quantum Dice. But the most advanced in pushing this toward a commercial product seems to be **Extropic**, co-founded by the famous Beff Jezoz, a major proponent of accelerationism. In October 2025, they released their first room-temperature desktop prototype with dozens of p-bits. The problem is that almost no one wants a chip specialized in EBMs—because EBMs aren’t popular in today’s AI.

As a more marketable alternative, **Normal Computing** is working on probabilistic hardware where the units aren’t discrete bits but continuous variables (voltages, currents) governed by SDEs (stochastic differential equations), the same kind used in diffusion models.

---

Somewhere out there, there’s probably also a photonic chip promising the future.

## Robotics

The humanoid robots we see in movies are deeply tied to artificial intelligence. If we already have models that win university-level programming competitions, wouldn’t it just be a matter of putting one into a robot and calling it a day? Not yet. Models still need to develop fairly advanced **motor and spatial intelligence**.

*Machine learning* has spent more than 15 years trying to solve this, and while it’s still not mastered, we now have more sophisticated algorithms, vastly more compute, and a flood of investment. That’s why so many startups have emerged to tackle the problem.

We can divide them into two groups:

**1. “Demonstration” robots**  
The leader here is **Figure AI**, which claims to already have robots deployed in partner factories and is valued at around \$39 billion. There’s also **Tesla** with Optimus, **1X** with Neo, and even **XPeng**, which jumped from cars to humanoids. Their bet is to sell **robotic services** once the product is ready.

**2. Robots accessible to anyone**  
Here, **Unitree Robotics** stands out. They’re about to go public and sell robots starting at \$6,000. They’re freely programmable and even sold at Walmart. Most universities and research labs use Unitree robots. Other companies, like **Romela** or **Pollen Robotics**, have chosen to make their robots **open source**. These companies aim to sell the robot as the final product, with basic functionality and a development kit so you can build—or choose—whatever software you want to run on it.

Every week, a new impressive demo appears (always in controlled environments), fueling excitement about the possibility that the age of humanoid robots is near.

For now, **general-purpose robots haven’t arrived**—neither for factories nor for homes. But if you want to experiment with one:

- If you’re a massive manufacturing company: talk to Figure.  
- If you don’t make hundreds of millions per year: go to Unitree’s site and buy one.

A very comprehensive map of the robotics ecosystem by @Robotuo can be seen [here](https://x.com/Robo_Tuo/status/1997481988220146078?s=20).
