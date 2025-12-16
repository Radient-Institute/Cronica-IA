---
weight: 7
bookFlatSection: true
title: "07 – The Different One"
image: _din_style/banner_images/07_ed.webp
---

# The Different One

## An Interesting Bet

“The Different One” brought peace of mind to those who believed AI would completely transform software development. The impact of GitHub Copilot was anything but trivial, and the natural next step after ChatGPT’s release was obvious: build an editor with AI baked in—a side chat capable of reading and editing your code, and that, even if all its edits were bad, would at least save you from opening a browser every time you wanted to ask ChatGPT something.

As early as the beginning of 2023, we already had several proposals: Cursor, Codeium, Replit, Continue, and others. All of them were gradually refining their *prompts*, *tools*, and *workflows* to become less useless (no offense—at that time, the results really were bad).

The following year, more ambitious players doubled down. They trusted that models would improve so much that their product would become an **autonomous software engineer**—junior-level, yes, but autonomous nonetheless. An *agent* capable of implementing a feature described in natural language, refactoring a file, and running it on its own, gaining more autonomy over time.

The first to truly scare developers appeared in March 2024: **Devin**, from Cognition AI. To showcase its capabilities, they used a then-obscure *benchmark*: **SWE-bench**, which collects real GitHub *issues* (half of them from Django) and evaluates whether a model can solve them. Devin reached 14%, which was honestly a surprising result. In August, **Genie**, from Cosine, pushed the number to 30%.

## The Scaffolding Core Arrives

“The Different One” arrived in June 2024. **Sonnet 3.5** appeared like a lone wolf, as Anthropic did not announce the full Claude 3.5 series—only releasing the middle sibling.

And almost immediately, as if by magic, **all the infrastructure these *startups* had built began to work**. Small but non-trivial features implemented themselves, the code compiled, the generated *frontend* looked acceptable. People tried it, were surprised, and shared it, creating a snowball effect.

Over the following months, the phenomenon grew massive.

## Vibecoding and Code Agents

In February 2025, *senpai* Karpathy coined a hyper-popular term that the entire tech world ended up hearing: **vibecoding**. It referred to a style of programming where you go with the *vibes*: you ignore the code and just give instructions to the LLM; when errors appear, you simply *copy/paste* them into the chat and let the model fix things. Accept everything—and it works.  
He described it as something fun for improvised weekend projects.

However, the term was overused and distorted by the *mainstream*, leading many to reject it because they understood it differently from its original meaning.

The success of LLMs in code was so significant that it pushed the major labs to create their own **code agents**, initially operating from the command line (CLI):  
- **claude-code** in February 2025,  
- **codex-cli** from OpenAI in April,  
- **gemini-cli** in June.  

OpenAI went a step further and launched Codex as a web and *cloud* service in May.

---

## After Anthropic’s Success

As for the current state of SWE-bench, OpenAI has claimed that a large portion of the problems in that *benchmark* were poorly specified or lacked sufficient information to be solvable. As a result, it selected a subset of problems it considers “solvable” and rebranded it as **SWE-bench Verified**, sidelining the original version.  
State-of-the-art models reach around 80% on this new (and much easier) variant as of December 2025.

Anthropic continued to update its models steadily, doubling down on its specialty: code. It updated Sonnet 3.5 in late 2024, released **Sonnet 3.7** (with *CoT*) in February 2025, unveiled the **Claude 4** series in May 2025, and with intermediate updates, by November 2025 we already had **version 4.5**
