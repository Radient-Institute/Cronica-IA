---
weight: 6
bookFlatSection: true
title: "06 - All Flavors, Please"
image: _din_style/banner_images/06_afp.webp
---

# All Flavors, Please

Es mayo del 2024. El chiquitín de GPT-3.5-turbo ya había sido capturado por un modelo *open source*, y GPT-4-turbo tenía competencia real por parte de un modelo propietario. OpenAI sabía que era hora de desmarcarse nuevamente. Así que abrieron su cajón de los misterios y sacaron uno de sus proyectos más vistosos: **GPT-4o**, un modelo *omni*, entrenado directamente en texto, audio e imágenes. De ahí el nombre: *GPT-4 omni*.[^1]

{{% details title="La multimodalidad nativa" open=false %}}
Es cierto que GPT-4 ya podía recibir imágenes y responder preguntas sobre ellas. Pero lo hacía mediante un truco distinto[^2]: después de entrenar el modelo de texto, se añadía un modelo de visión para extraer *features* de las imágenes y luego se proyectaban al espacio de *embeddings* del modelo textual.

La multimodalidad nativa, en cambio, implica proyectar todos los tipos de datos en el mismo espacio de *embeddings* y pre-entrenar al modelo en todas las modalidades, ya sea en fases o de forma conjunta. Esto le da la capacidad de manejar, entender y, en algunos casos, generar texto, audio e imagen de forma nativa dentro de una misma secuencia.
{{% /details %}}

## Una promesa temprana

El concepto de la multimodalidad había sido impulsado sobre todo por Google entre 2020 y 2022,[^3][^4] pero fue OpenAI quien logró ejecutarlo de manera prolija. Por primera vez teníamos un modelo que podía *leer, escuchar y ver*… y por consiguiente *escribir, hablar y dibujar*. Una versión de *Her* más poderosa. Nada de *text-to-speech* y *speech-to-text* baratos: eso era tecnología del pasado. El futuro era hoy. O al menos, eso pensamos muchos.

Las demos eran impresionantes:

Un estudiante con problemas en matemáticas podía simplemente abrir ChatGPT, apuntar la cámara al cuaderno y recibir una explicación paso a paso, en voz, viendo exactamente lo que él estaba escribiendo.

Un programador con poca vida social podía abrir ChatGPT y tener, literalmente, a Scarlett Johansson como compañera emocional… bueno, no exactamente, porque la actriz rechazó la oferta de prestar su voz al sistema.[^5]

El problema fue que las funciones tardaron demasiado en llegar.\
El modo de voz estuvo disponible recién en septiembre (cuatro meses después del anuncio).[^6]\
El modo de vídeo, en diciembre (siete meses después).[^7]\
Y la generación de imágenes, en marzo del 2025 (diez meses después).[^8]

Tardaron tanto que la *startup* francesa **Kyutai Labs** se adelantó y lanzó un modelo *open source* llamado **Moshi**.[^9] No soportaba vídeo, solo audio y texto, y era bastante limitado… pero salió antes que el modo de voz de OpenAI. Y además podía correr en una laptop.[^10]

## La pronta realidad

Volviendo a GPT-4o: como simple LLM, era un poco mejor que GPT-4-turbo, pero nada revolucionario. Terminaría reemplazándolo como modelo por defecto en la línea de productos de OpenAI.

A pesar del enorme *hype*, la multimodalidad no terminó de calar. Al principio hubo bastante interés por replicarla —con *papers* como **Chameleon** o **Transfusion**—,[^11][^12] pero no surgió nada parecido a la carrera feroz que existía con los LLMs puros:\
no hubo una explosión de *benchmarks* para evaluar y mejorar en estas nuevas capacidades,[^13] ni una academia obsesionada por empujarlos, ni *startups* construyendo encima de esta tecnología.

Google lanzó su propio modelo “omni” en diciembre,[^14] mientras que X.AI tardó un poco más y lo publicó en febrero del 2025.[^15] Por parte del OSS, solo hubo un modelo de este tipo que consiguió cierto grado de relevancia: **Qwen2.5-Omni**.[^16]

Una razón clave podría ser algo que comentó el CEO de Moonshot AI:\
**preentrenar en otros tipos de dato, como imágenes o audio, no mejora el rendimiento en texto.**[^17]

Y como casi todo el ecosistema giraba alrededor del texto, la multimodalidad perdió prioridad.

Desde entonces hasta finales del 2025, el área ha estado un poco abandonada en lo que respecta a voz. Incluso muchas empresas de asistencia al cliente siguieron usando un *speech-to-text* seguido de un *text-to-speech*: aunque el audio contiene información importante como tono, emoción o velocidad, los modelos seguían siendo más inteligentes, más precisos y más confiables cuando operan únicamente en texto.

Algunas *startups* continuaron trabajando en modelos de voz —como **Sesame** o **Hume AI**—, con enfoque en la naturalidad de la conversación, no en aumentar la "inteligencia" del modelo.[^18][^19]

Pero respecto a las imágenes… esa historia fue muy diferente. Como veremos más adelante.

## Referencias

[^1]: OpenAI. ["Hello GPT-4o"](https://openai.com/index/hello-gpt-4o/). 13 de mayo de 2024.

[^2]: No está confirmado que OpenAI haya usado exactamente esta metodología para adaptar un modelo de lenguaje a datos multimodales, pero es muy probable porque era la forma más natural y efectiva de hacerlo en ese entonces.

[^3]: Google. ["Google I/O 2021: Being helpful in moments that matter"](https://blog.google/innovation-and-ai/technology/developers-tools/io21-helpful-google/). 18 de mayo de 2021.

[^4]: Google. ["MUM: A new AI milestone for understanding information"](https://blog.google/products/search/introducing-mum/). 18 de mayo de 2021.

[^5]: Reuters. ["Scarlett Johansson says OpenAI chatbot voice 'eerily similar' to hers"](https://www.reuters.com/technology/scarlett-johansson-says-openai-chatbot-voice-eerily-similar-hers-2024-05-21/). 21 de mayo de 2024.

[^6]: Reuters. ["OpenAI starts roll-out of advanced voice mode to some ChatGPT Plus users"](https://www.reuters.com/technology/openai-starts-roll-out-advanced-voice-mode-some-chatgpt-plus-users-2024-07-30/). 30 de julio de 2024.

[^7]: OpenAI. ["Advanced Voice Mode gets video"](https://edunewsletter.openai.com/p/advanced-voice-mode-gets-video-during). 13 de diciembre de 2024.

[^8]: OpenAI. ["Introducing 4o Image Generation"](https://openai.com/index/introducing-4o-image-generation/). 25 de marzo de 2025.

[^9]: Kyutai. ["Moshi: a speech-text foundation model for real-time dialogue"](https://kyutai.org/Moshi.pdf). 2024.

[^10]: Kyutai. ["Moshi"](https://github.com/kyutai-labs/moshi). Repositorio oficial; incluye implementación MLX para ejecución local en Apple Silicon.

[^11]: Chameleon Team. ["Chameleon: Mixed-Modal Early-Fusion Foundation Models"](https://arxiv.org/abs/2405.09818). 16 de mayo de 2024.

[^12]: Zhou, Chunting et al. ["Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model"](https://arxiv.org/abs/2408.11039). 20 de agosto de 2024.

[^13]: Lin, Guan-Ting et al. ["Full-Duplex-Bench: A Benchmark to Evaluate Full-duplex Spoken Dialogue Models on Turn-taking Capabilities"](https://arxiv.org/abs/2503.04721). 6 de marzo de 2025. El trabajo señala las limitaciones de las evaluaciones existentes para capacidades como pausas, *backchanneling*, *turn-taking* e interrupciones.

[^14]: Google DeepMind. ["Introducing Gemini 2.0: our new AI model for the agentic era"](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/). 11 de diciembre de 2024.

[^15]: Edwards, Benj. ["Grok's new 'unhinged' voice mode can curse and scream, simulate phone sex"](https://arstechnica.com/ai/2025/02/groks-uncensored-ai-voice-mode-lets-users-talk-sex-therapy-and-conspiracies/). Ars Technica. 25 de febrero de 2025.

[^16]: Xu, Jin et al. ["Qwen2.5-Omni Technical Report"](https://arxiv.org/abs/2503.20215). 26 de marzo de 2025.

[^17]: Yang Zhilin. Entrevista, 27 de agosto de 2025. Yang afirmó: “多模态数据又无法很好提升文本本身的‘智商’” —“los datos multimodales no consiguen mejorar bien la ‘inteligencia’ del texto en sí”.

[^18]: Sesame AI Labs. ["CSM — A Conversational Speech Generation Model"](https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice). 2025.

[^19]: Hume AI. ["Hume Raises $50M Series B and Releases New Empathic Voice Interface"](https://www.hume.ai/blog/series-b). 25 de marzo de 2024.
