---
weight: 5
bookFlatSection: true
title: "05 - Te Tengo"
image: _din_style/banner_images/05_tt.webp
---

# Te Tengo

## La técnica requerida para la escala

En algún momento de junio del 2023, George Hotz, fundador de Comma.ai y Tinycorp, durante una entrevista en un pódcast, filtró información de la arquitectura de GPT-4. Afirmaba que este modelo no era un GPT “normal”, sino un *Mixture of Experts* (MoE), con 8 expertos de 220B parámetros cada uno, sumando un total de 1.8T de parámetros.[^1]

El *Mixture-of-Experts* (MoE) no era una técnica nueva inventada por OpenAI y esencialmente permite aumentar la capacidad de un modelo manteniendo (o reduciendo, a calidad similar) el cómputo por *token*.[^2][^3]

{{% details title="El funcionamiento del MoE" open=false %}}
Lo logra reemplazando la capa *feed-forward* (FFN) del Transformer —la que va después del mecanismo de atención— por múltiples FFN “expertos” y un *router* que, para cada *token*, selecciona solo algunos (top-k) y luego combina sus salidas.

Asumiendo un modelo con 64 expertos, cada uno con 16B parámetros, y solo 8 expertos activos por *token*, al hacer el *forward pass* no necesitamos calcular con los 1024B parámetros del modelo completo, sino solo con los 128B de los expertos activos.

{{% /details %}}

Construir y servir estos modelos es más complejo, pero vale la pena porque obtienes el comportamiento de un modelo enorme mientras ejecutas solo una fracción de sus parámetros en cada paso.

## GPT-3.5-turbo capturado

Luego de esta filtración tendrían que pasar varios meses para que las empresas consiguieran entrenar y servir MoEs a escala. La primera en lograrlo fue la *startup* francesa **Mistral**, que gozaba de gran popularidad en ese entonces. Estaba conformada principalmente por ex empleados de Meta que habían trabajado en LLaMA, además de miembros provenientes de otros laboratorios. Se anunciaron en abril del 2023 como “la respuesta europea” al desarrollo estadounidense en IA.[^4]

Nuestros amigos franceses nos dieron una gran alegría con el lanzamiento de **Mixtral 8x7B** en diciembre.[^5] Por primera vez había un consenso mayoritario en que teníamos un modelo superior a GPT-3.5-turbo.[^6] Encima era *open source* y, aunque no era precisamente pequeño para los estándares de la época, sí estaba al alcance de muchos ejecutarlo en local.

## GPT-4-turbo capturado

Cerraba el 2023, más de un año desde la salida de ChatGPT, OpenAI seguía en la cima y GPT-4 permanecía intocable.

En febrero del 2024, un laboratorio llamado **Allen Institute**, fundado por Paul Allen y dirigido inicialmente por Oren Etzioni,[^7] hizo una propuesta nunca antes vista que merece una mención honorífica. Presentaron **Olmo**,[^8] la única serie de modelos completamente *open source* y reproducibles (al menos hasta el 2025), con un *paper* detallado, pesos, *scripts* de entrenamiento y *datasets* públicos a lo largo de todas las fases de creación de un LLM (pre y *post*-training).[^9]

No alcanzaron a GPT-4-turbo (una versión más rapida, pulida y barata de GPT-4)[^10] en ningún aspecto, pero la transparencia y la filosofía de ciencia abierta fueron destacables.

Quien se haría con esta proeza un mes después, en marzo, fue **Anthropic**. Presentaban la serie de modelos **Claude 3**, en tres tamaños (*Haiku*, *Sonnet* y *Opus*), siendo *Haiku* el más pequeño y *Opus* el más grande.[^11]

Respecto a la pregunta de si *Opus 3* era mejor modelo que el GPT-4-turbo de ese entonces, era debatible.[^12] Pero ese es el punto: **¡era debatible!** La supremacia de OpenAI ya no era inapelable.

Y como evidencia clara de las capacidades de los modelos de Anthropic, mucha gente canceló su suscripción a ChatGPT y se suscribió a Claude, que además tenía una UI muy pulida a la que en los proximos meses se le agregaría una función nueva (tan útil que todos los otros competidores terminaron copiándola): los **artifacts**, un bloque al lado del chat que renderiza el código generado por el modelo, dándonos pistas del enfoque futuro que la empresa tomaría (el código).[^13]

## Referencias

[^1]: Rickard, Matt. ["Mixture of Experts: Is GPT-4 Just Eight Smaller Models?"](https://blog.matt-rickard.com/p/mixture-of-experts-is-gpt-4-just). 21 de junio de 2023.

[^2]: Shazeer, Noam et al. ["Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"](https://arxiv.org/abs/1701.06538). 23 de enero de 2017.

[^3]: Fedus, William; Zoph, Barret; Shazeer, Noam. ["Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"](https://www.jmlr.org/papers/v23/21-0998.html). *Journal of Machine Learning Research*, 2022.

[^4]: Financial Times. ["Four-week-old AI start-up raises record €105mn in European push"](https://www.ft.com/content/cf939ea4-d96c-4908-896a-48a74381f251). 13 de junio de 2023.

[^5]: Mistral AI. ["Mixtral of Experts"](https://mistral.ai/news/mixtral-of-experts/). 11 de diciembre de 2023.

[^6]: Jiang, Albert Q. et al. ["Mixtral of Experts"](https://arxiv.org/abs/2401.04088). 8 de enero de 2024.

[^7]: Allen Institute for AI. ["Oren Etzioni"](https://allenai.org/team/orene). Etzioni fue el director ejecutivo fundador de Ai2, instituto creado por Paul Allen en 2014.

[^8]: Allen Institute for AI. ["OLMo: Open Language Model"](https://allenai.org/blog/olmo-open-language-model-87ccfc95f580). 1 de febrero de 2024.

[^9]: Groeneveld, Dirk et al. ["OLMo: Accelerating the Science of Language Models"](https://arxiv.org/abs/2402.00838). 1 de febrero de 2024.

[^10]: OpenAI. ["New models and developer products announced at DevDay"](https://openai.com/index/new-models-and-developer-products-announced-at-devday/). 6 de noviembre de 2023.

[^11]: Anthropic. ["Introducing the next generation of Claude"](https://www.anthropic.com/news/claude-3-family). 4 de marzo de 2024.

[^12]: Reuters. ["Anthropic releases more powerful Claude 3 AI as tech race continues"](https://www.reuters.com/technology/anthropic-releases-more-powerful-claude-3-ai-tech-race-continues-2024-03-04/). 4 de marzo de 2024.

[^13]: Anthropic. ["Introducing Claude 3.5 Sonnet"](https://www.anthropic.com/news/claude-3-5-sonnet). 20 de junio de 2024.
