---
weight: 5
bookFlatSection: true
title: "05 - Te Tengo"
image: _din_style/banner_images/05_tt.webp
---

# Te Tengo

## La técnica requerida para la escala

En algún momento de junio del 2023, George Hotz, fundador de Comma.ai y Tinycorp, durante una entrevista en un pódcast, filtró información de la arquitectura de GPT-4. Afirmaba que este modelo no era un GPT “normal”, sino un *Mixture of Experts* (MoE), con 8 expertos de 220B parámetros cada uno, sumando un total de 1.8T de parámetros.

El *Mixture-of-Experts* (MoE) no era una técnica nueva inventada por OpenAI y esencialmente permite aumentar la capacidad de un modelo manteniendo (o reduciendo, a calidad similar) el cómputo por *token*.

{{% details title="El funcionamiento del MoE" open=false %}}
Lo logra reemplazando la capa *feed-forward* (FFN) del Transformer —la que va después del mecanismo de atención— por múltiples FFN “expertos” y un *router* que, para cada *token*, selecciona solo algunos (top-k) y luego combina sus salidas.  
Asumiendo un modelo con 64 expertos, cada uno con 16B parámetros, y solo 8 expertos activos por *token*, al hacer el *forward pass* no necesitamos calcular con los 1024B parámetros del modelo completo, sino solo con los 128B de los expertos activos.
{{% /details %}}

Construir y servir estos modelos es más complejo, pero vale la pena porque obtienes el comportamiento de un modelo enorme mientras ejecutas solo una fracción de sus parámetros en cada paso.

## GPT-3.5-turbo capturado

Luego de esta filtración tendrían que pasar varios meses para que las empresas consiguieran entrenar y servir MoEs a escala. La primera en lograrlo fue la *startup* francesa **Mistral**, que gozaba de gran popularidad en ese entonces. Estaba conformada principalmente por ex empleados de Meta que habían trabajado en LLaMA, además de miembros provenientes de otros laboratorios. Se anunciaron en abril del 2023 como “la respuesta europea” al desarrollo estadounidense en IA.

Nuestros amigos franceses nos dieron una gran alegría con el lanzamiento de **Mixtral 8x7B** en diciembre. Por primera vez había un consenso mayoritario en que teníamos un modelo superior a GPT-3.5-turbo. Encima era *open source* y, aunque no era precisamente pequeño para los estándares de la época, sí estaba al alcance de muchos ejecutarlo en local.

## GPT-4-turbo capturado

Cerraba el 2023, más de un año desde la salida de ChatGPT, OpenAI seguía en la cima y GPT-4 permanecía intocable.

En febrero del 2024, un laboratorio llamado **Allen Institute**, fundado por ex empleados de Google Brain, hizo una propuesta nunca antes vista que merece una mención honorífica. Presentaron **Olmo**, la única serie de modelos completamente *open source* y reproducibles hasta la fecha (2025), con un *paper* detallado, pesos, *scripts* de entrenamiento y *datasets* públicos a lo largo de todas las fases de creación de un LLM (pre y *post*-training).  
No alcanzaron a GPT-4-turbo (una versión más pequeña, pulida y barata de GPT-4) en ningún aspecto, pero la transparencia y la filosofía de ciencia abierta fueron destacables.

Quien se haría con esta proeza un mes después, en marzo, fue **Anthropic**. Presentaban la serie de modelos **Claude 3**, en tres tamaños (*Haiku*, *Sonnet* y *Opus*), siendo *Haiku* el más pequeño y *Opus* el más grande.

Respecto a la pregunta de si *Opus 3* era mejor modelo que el GPT-4-turbo de ese entonces, era debatible. Pero ese es el punto: **¡era debatible!** La supremacia de OpenAI ya no era inapelable.

Y como evidencia clara de las capacidades de los modelos de Anthropic, mucha gente canceló su suscripción a ChatGPT y se suscribió a Claude, que además tenía una UI muy pulida con una función nueva (tan útil que todos los otros competidores terminaron copiándola): los **artifacts**, un bloque al lado del chat que renderiza el código generado por el modelo, dándonos pistas del enfoque futuro que la empresa tomaría (el código).
