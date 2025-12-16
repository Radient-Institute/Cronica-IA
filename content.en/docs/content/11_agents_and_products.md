---
weight: 11
bookFlatSection: true
title: "11 – Agents and Products"
image: _din_style/banner_images/11_ayp.webp
---

# Agents and Products

2025 was supposed to be **the year of autonomous agents**.  
This wasn’t a spontaneous expectation from the public: influencers repeated it, the press proclaimed it in headlines, and even Sam Altman himself mentioned it on his blog. The promise was clear—agents would operate on our behalf, making decisions and executing tasks from start to finish.

And it made sense. Toward the end of 2024, OpenAI’s internal roadmap toward AGI leaked, and we all assumed we were stepping onto the next rung.

{{% details title="OpenAI’s plan to reach AGI" open=false %}}
1. Conversational AI: Chatbots and conversational assistants.  
2. Reasoning AI: Models capable of solving problems at a human level.  
3. Autonomous AI: Agents capable of taking actions.  
4. Innovative AI: Systems that help invent and create.  
5. Organizational AI: AI capable of performing the work of an entire organization.  
{{% /details %}}

Level two (reasoning AI) was considered “solved” thanks to the O series, so the natural next step was level three: autonomous AI. In this chapter, we’ll talk about those agents—but not the code-related ones (which we already covered), rather everything else.

## The Sea of “Agents”

We could call “agents” those chats that began receiving access to *tools*: a Python interpreter to analyze data, *web search* to act as pseudo search engines, connectors to generate slides, plot data, plan vacations, analyze finances… With the emergence of libraries for orchestrating LLMs and giving them tools, a **massive wave of AI-powered SaaS** emerged.

And not just libraries—*low-code* and *no-code* platforms like **n8n** also appeared, allowing anyone to build fairly complex workflows connected to language models.

However, by the end of 2025, almost all of these applications were still niche products. They worked well for specific audiences but failed to reach mass adoption. Perhaps two exceptions stand out.

The first was **NotebookLM**, a Google app where users could upload information sources, chat about them, and generate explanatory videos. But its popularity didn’t come from that—it came from a very specific feature: automatically creating podcasts from documents.  
That feature went viral for being both incredibly useful and remarkably simple.

The second was **Manus AI** (March 2025), a “general-purpose” agent created by a Chinese *startup*. It didn’t have a particularly novel idea: it could search for data, analyze it, write code snippets, generate reports, websites, and more.  
What set it apart from earlier attempts was something simpler: people reported that this agent actually worked well.

## OpenAI’s Attempts to Enter the Agent World

In early 2025, OpenAI launched its own specialized agents.

The first was **Deep Research**, a version of O3 tuned to create long-form reports or retrieve specific information; it could take several dozen minutes to complete, and people loved it. So much so that every frontier lab copied it—except Google, which already had an equivalent since December 2024 called *Deep Search* that largely went unnoticed.

The second agent was **Operator**: a version of GPT-4o capable of interacting with a virtual machine through both the terminal and a graphical interface. Unlike Deep Research, Operator requires actual model training on interface interaction—simple prompting isn’t enough—which made it much harder for other labs to copy quickly.  
To this day, it remains a distinctive feature of ChatGPT.

## Interface and Maturity

Another interesting point is that it’s still unclear what the ideal interface for LLMs should be.  
The classic chat *textbox* with conversation history doesn’t convince everyone, but no definitive replacement has emerged yet. All experiments so far remain just that—experiments.

The truth is that general-purpose agents **are not mature yet**.  
They’re not reliable enough, and that has slowed their adoption beyond enthusiast communities.

On the other hand, there is broad consensus on one thing: the application layer is where the biggest opportunities lie. And there’s no shortage of people claiming that the famous one-person unicorn is just around the corner.
