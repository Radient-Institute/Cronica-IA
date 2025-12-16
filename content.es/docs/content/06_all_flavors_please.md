---
weight: 6
bookFlatSection: true
title: "06 - All Flavors, Please"
image: _din_style/banner_images/06_afp.webp
---

# All Flavors, Please

Es mayo del 2024. El chiquitín de GPT-3.5-turbo ya había sido capturado por un modelo *open source*, y GPT-4-turbo tenía competencia real por parte de un modelo propietario. OpenAI sabía que era hora de desmarcarse nuevamente. Así que abrieron su cajón de los misterios y sacaron uno de sus proyectos más vistosos: **GPT-4o**, un modelo *omni*, entrenado directamente en texto, audio e imágenes. De ahí el nombre: *GPT-4 omni*.

{{% details title="La multimodalidad nativa" open=false %}}
Es cierto que GPT-4 ya podía recibir imágenes y responder preguntas sobre ellas. Pero lo hacía mediante un truco distinto: después de entrenar el modelo de texto, se añadía un modelo de visión para extraer *features* de las imágenes y luego se proyectaban al espacio de *embeddings* del modelo textual.

La multimodalidad nativa, en cambio, implica tokenizar todos los tipos de datos en el mismo espacio de *embeddings* y entrenar al modelo en todas las modalidades, ya sea en fases o de forma conjunta. Esto le da la capacidad de manejar, entender y generar texto, audio e imagen de forma nativa dentro de una misma secuencia.
{{% /details %}}

## Una promesa temprana

El concepto de la multimodalidad había sido impulsado sobre todo por Google entre 2020 y 2022, pero fue OpenAI quien logró ejecutarlo de manera prolija. Por primera vez teníamos un modelo que podía *leer, escuchar y ver*… y por consiguiente *escribir, hablar y dibujar*. Una versión de *Her* más poderosa. Nada de *text-to-speech* y *speech-to-text* baratos: eso era tecnología del pasado. El futuro era hoy. O al menos, eso pensamos muchos.

Las demos eran impresionantes:

Un estudiante con problemas en matemáticas podía simplemente abrir ChatGPT, apuntar la cámara al cuaderno y recibir una explicación paso a paso, en voz, viendo exactamente lo que él estaba escribiendo.

Un programador con poca vida social podía abrir ChatGPT y tener, literalmente, a Scarlett Johansson como compañera emocional… bueno, no exactamente, porque la actriz rechazó que su voz fuese utilizada para entrenar el modelo.

El problema fue que las funciones tardaron demasiado en llegar.  
El modo de voz estuvo disponible recién en septiembre (cuatro meses después del anuncio).  
El modo de vídeo, en diciembre (siete meses después).  
Y la generación de imágenes, en marzo del 2025 (diez meses después).

Tardaron tanto que la *startup* francesa **Kyutai Labs** se adelantó y lanzó un modelo *open source* llamado **Moshi**. No soportaba vídeo, solo audio y texto, y era bastante limitado… pero salió antes que el modo de voz de OpenAI. Y además podía correr en una laptop.

## La pronta realidad

Volviendo a GPT-4o: como simple LLM, era un poco mejor que GPT-4-turbo, pero nada revolucionario. Terminaría reemplazándolo como modelo por defecto en la línea de productos de OpenAI.

A pesar del enorme *hype*, la multimodalidad no terminó de calar. Al principio hubo bastante interés por replicarla —con *papers* como **Chameleon** o **Transfusion**—, pero no surgió nada parecido a la carrera feroz que existía con los LLMs puros:  
no hubo *benchmarks* relevantes, ni una academia obsesionada por empujarlos, ni *startups* construyendo encima de esta tecnología.

Google lanzó su propio modelo “omni” en diciembre, mientras que X.AI tardó un poco más y lo publicó en febrero del 2025. Por parte del OSS, solo hay un modelo relevante de este tipo: **Qwen2.5-Omni**, de hecho no es del todo multimodal nativo. 

Una razón clave podría ser algo que comentó el CEO de Moonshot AI:  
**preentrenar en otros tipos de dato, como imágenes o audio, no mejora el rendimiento en texto.**

Y como casi todo el ecosistema gira alrededor del texto, la multimodalidad perdió prioridad.

Desde entonces, el área ha estado un poco abandonada en lo que respecta a voz. Incluso muchas empresas de asistencia al cliente prefieren seguir usando un *speech-to-text* seguido de un *text-to-speech*: aunque el audio contiene información importante como tono, emoción o velocidad, los modelos siguen siendo más inteligentes, más precisos y más confiables cuando operan únicamente en texto.

Algunas *startups* continúan trabajando en modelos de voz —como **Sesame** o **Hume AI**—, pero su enfoque está en la naturalidad de la conversación, no en aumentar la “inteligencia” del modelo.

Pero respecto a las imágenes… esa historia fue muy diferente. Como veremos más adelante.
