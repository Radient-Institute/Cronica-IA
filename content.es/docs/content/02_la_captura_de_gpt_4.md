
---
weight: 2
bookFlatSection: true
title: "02 - La Captura de GPT-4"
image: _din_style/banner_images/02_cgpt.webp
---

# La Captura de GPT-4

Desde pocos días después de la salida y el posterior éxito masivo de ChatGPT, empezó una **carrera por alcanzar la tecnología de OpenAI**. No sería la primera vez que algún Prometeo se hacía con su fuego, y no sería la última.

Tres frentes tomaron la iniciativa: las empresas competidoras, el *open source* y los laboratorios/grupos de investigación universitarios. Me gusta llamar a este periodo "La captura de GPT-4", pero antes de capturar al gigante, primero se debia alcanzar al pequeño **GPT-3.5 Turbo**.

Los **primeros intentos** se terminan materializando entre **marzo y abril de 2023**. Universidades y laboratorios habían construido *datasets* sintéticos de respuestas y conversaciones, muchos de ellos obtenidos en base a las respuestas de modelos propietarios de OpenAI y los usaron para hacer *fine-tuning* de los modelos base de lenguaje disponibles en la fecha, como LLaMA 1,[^1] Pythia,[^2] GPT-Neo,[^3] BLOOM,[^4] etc. Esto dio paso al nacimiento de Alpaca,[^5] Vicuna,[^6] Dolly,[^7] Koala,[^8] entre otros, y poco después Guanaco.[^9]

Una iniciativa del OSS interesante fue **OpenAssistant**, un proyecto comunitario impulsado dentro de LAION y cofundado, entre otros, por el investigador y YouTuber Yannic Kilcher, donde se pretendía construir un *dataset* humano propio y abierto para este mismo propósito.[^10][^11]

A pesar de que los modelos fueron muy comentados y celebrados, había un problema. Las respuestas que te daban estos modelos se sentían como ChatGPT, pero a la mínima que subías la dificultad de las preguntas te dabas cuenta de que aún no estábamos cerca de la tecnología de OpenAI. Se consiguió que los modelos hablasen en formato chat, pero como herramienta útil aún estaban limitados.[^12]

Y aunque las técnicas que usaban estos grupos se fueron modernizando con el pasar de los meses, pasando de un simple **SFT a DPO y/o RLHF**,[^13][^14] tuvieron que venir las empresas y *startups* a dar una mano para impulsar tanto la competencia como el OSS.

El resto del año estaría marcado por ese ritmo: empresas sacando LLMs abiertos cada vez superiores, acercándose poco a poco a OpenAI. Stability AI sacó StableLM[^15] (abril), MosaicML sacó MPT[^16] (mayo), el TII de los Emiratos Árabes Unidos sacó Falcon[^17] (mayo), Meta sacó Llama 2[^18] (julio), Mistral sacó Mistral 7B[^19] (septiembre).

Instituciones previamente poco involucradas con la IA notaron el potencial de la tecnología y comenzaron a invertir en investigación y desarrollo de LLMs. El ambiente se volvió tan competitivo que no tenía sentido intentar preentrenar o alinear modelos de lenguaje a menos que fueras una *startup* con millones de capital o con apoyo del gobierno.

En ese entonces había dos partícipes importantes que, a pesar de estar bastante por detrás, apostaron por mantener sus modelos *closed source*. Y aunque todo el mundo tenía expectativas altas en ellos, aún no nos habían entregado nada mínimamente competitivo con el líder. Hablo de Anthropic con Claude[^20] (marzo) y Claude 2[^21] (julio) y Google con Bard[^22] (marzo).

## Referencias

[^1]: Meta AI. ["LLaMA: Open and Efficient Foundation Language Models"](https://ai.meta.com/blog/large-language-model-llama-meta-ai/). 24 de febrero de 2023.

[^2]: EleutherAI. ["Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling"](https://blog.eleuther.ai/pythia/). 2023.

[^3]: EleutherAI. ["GPT-Neo: Large-Scale Autoregressive Language Modeling with Mesh-Tensorflow"](https://github.com/EleutherAI/gpt-neo). 2021.

[^4]: BigScience. ["BLOOM: A 176B-Parameter Open-Access Multilingual Language Model"](https://arxiv.org/abs/2211.05100). 9 de noviembre de 2022.

[^5]: Stanford CRFM. ["Alpaca: A Strong, Replicable Instruction-Following Model"](https://crfm.stanford.edu/2023/03/13/alpaca.html). 13 de marzo de 2023.

[^6]: LMSYS Org. ["Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90% ChatGPT Quality"](https://www.lmsys.org/blog/2023-03-30-vicuna/). 30 de marzo de 2023.

[^7]: Databricks. ["Hello Dolly: Democratizing the magic of ChatGPT with open models"](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html). 24 de marzo de 2023.

[^8]: Geng, Xinyang et al. ["Koala: A Dialogue Model for Academic Research"](https://bair.berkeley.edu/blog/2023/04/03/koala/). Berkeley Artificial Intelligence Research, 3 de abril de 2023.

[^9]: Dettmers, Tim, et al. ["QLoRA: Efficient Finetuning of Quantized LLMs"](https://arxiv.org/abs/2305.14314). 23 de mayo de 2023. Guanaco, un modelo de 65B entrenado con QLoRA, superó a todos los modelos abiertos anteriores en el benchmark de Vicuna.

[^10]: LAION AI. ["OpenAssistant"](https://open-assistant.io/). Comunidad LAION / Yannic Kilcher. Proyecto para construir un *dataset* y modelo de asistente abierto.

[^11]: Köpf, Andreas et al. ["OpenAssistant Conversations — Democratizing Large Language Model Alignment"](https://arxiv.org/abs/2304.07327). 14 de abril de 2023.

[^12]: Gudibande, Arnav et al. ["The False Promise of Imitating Proprietary LLMs"](https://arxiv.org/abs/2305.15717). 25 de mayo de 2023.

[^13]: Stability AI. ["StableVicuna: The AI World's First Open Source RLHF LLM Chatbot"](https://stability.ai/news-updates/stablevicuna-open-source-rlhf-chatbot). 28 de abril de 2023.

[^14]: Rafailov, Rafael et al. ["Direct Preference Optimization: Your Language Model is Secretly a Reward Model"](https://arxiv.org/abs/2305.18290). 29 de mayo de 2023.

[^15]: Stability AI. ["StableLM"](https://github.com/Stability-AI/StableLM). Abril de 2023.

[^16]: MosaicML. ["Introducing MPT-7B: A New Standard for Open-Source, Commercially Usable LLMs"](https://www.mosaicml.com/blog/mpt-7b). 5 de mayo de 2023.

[^17]: Technology Innovation Institute. ["UAE's Technology Innovation Institute Launches Open-Source Falcon 40B Large Language Model"](https://www.tii.ae/news/uaes-technology-innovation-institute-launches-open-source-falcon-40b-large-language-model). 25 de mayo de 2023.

[^18]: Meta AI. ["Meta and Microsoft Introduce the Next Generation of Llama"](https://ai.meta.com/blog/llama-2/). 18 de julio de 2023.

[^19]: Mistral AI. ["Mistral 7B"](https://mistral.ai/news/announcing-mistral-7b/). 27 de septiembre de 2023.

[^20]: Anthropic. ["Introducing Claude"](https://www.anthropic.com/news/introducing-claude). 14 de marzo de 2023.

[^21]: Anthropic. ["Claude 2"](https://www.anthropic.com/news/claude-2). 11 de julio de 2023.

[^22]: Google. ["Try Bard and share your feedback"](https://blog.google/technology/ai/try-bard/). 21 de marzo de 2023.
