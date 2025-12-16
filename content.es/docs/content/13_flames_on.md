---
weight: 13
bookFlatSection: true
title: "13 - Flames On"
image: _din_style/banner_images/13_fo.webp
---

# Flames On

## Una probada

Sabíamos que OpenAI tenía un generador potente dentro de GPT-4o, y también sabíamos que Gemini 2 era multimodal. Pero Google fue el primero en dejarnos probar lo que significaba generar y editar imágenes con un modelo multimodal nativo. Ocurrió en marzo del 2025.

No era la primera vez que un competidor se adelantaba a OpenAI haciendo disponible una tecnología que OpenAI había mostrado antes solo como demo.

El modelo todavía tenía mucho por pulir: fallaba con frecuencia, generaba resultados extraños y a veces no hacía nada y te devolvía la imagen original. Pero cuando funcionaba, sorprendía de verdad. Subías una foto y simplemente escribías: cambia este objeto por este otro, cambia la luz, cambia el color, y lo hacía. Sin máscaras, sin flujos complicados: solo lenguaje natural. Para un rango limitado de casos, bastaba con manifestar tu intención claramente.

## El mundo se entera de lo que es posible

OpenAI no podía esperar más. Tenía que competir en un terreno que ellos mismos habían mostrado primero, así que dos semanas después anunciaron la **generación de imágenes de GPT-4o**, disponible gratis para todos los usuarios de ChatGPT.

¿El resultado? Era mucho mejor. La calidad y la adherencia a las instrucciones estaban en otro nivel.

La única pega (si queremos buscarle una) es que al editar fotografías solía alterar toda la imagen incluso sin pedírselo, probablemente por el refiner/upscaler. También aplicaba un filtro naranja extraño que hacía que las imágenes fueran facilmente reconocibles.

Pero a nadie le importó. Todo el mundo quería su foto con estilo de **Studio Ghibli**. Hasta mis excompañeros de colegio, que no sabían ni qué era OpenAI, aparecían con fotos generadas por IA en sus perfiles. La IA volvía a ser mainstream, y fue el segundo mayor momento de viralidad de OpenAI después de ChatGPT. Se decía incluso que habían conseguido **1 millón de usuarios nuevos en una hora**. Una locura.

En agosto del 2025 llegó la segunda iteración de Google: **Gemini 2.5 Flash** con generación de imágenes, apodado “nano-banana”. Dos meses más tarde presentaron **nano-banana Pro**, basado en Gemini 3. El mejor modelo hasta la fecha, lo que antes requería entrenar un LoRA con fotos de una persona, aplicar un ControlNet de pose y después un modelo de relighting… ahora se resolvía arrastrando una imagen y escribiendo: “ponlo sentado de noche con luces neón”. Aún no es perfecto, pero vamos en camino.

## Mientras tanto, en el OSS

El mercado de edición de imágenes mediante instrucciones de texto era enorme, y tanto Black Forest Labs como Qwen lo sabían. Por eso, dos meses después del boom del generador de imágenes de OpenAI, lanzaron **Kontext** (basado en Flux) y **Qwen Image Edit** (basado en Qwen Image).  
Ambos seguían siendo modelos de difusión OSS (MMDiT: *multimodal diffusion transformers*). No eran modelos multimodales nativos como los de Google y OpenAI, pero hacían un trabajo respetable.

Hasta ahora ningún laboratorio abierto ha logrado entregar un modelo multimodal nativo al nivel de Google u OpenAI. El estándar del OSS siguen siendo los MMDiT. Hubo algunos intentos, como **Janus** de DeepSeek, pero la calidad aún no alcanza.

{{% details title="¿Qué es un MMDiT?" open=false %}}
Un MMDiT es un DiT multimodal que procesa cada modalidad (texto, imagen, etc.) en su propio flujo, pero calcula la atención sobre todos los tokens simultáneamente. Cada flujo tiene sus propias capas, pero se comunican mediante la atención conjunta y luego se combinan en capas posteriores.
{{% /details %}}

En noviembre del 2025, Flux cometió un error grave con su lanzamiento de **Flux 2.0**. En Flux 1.0 tenían tres versiones: la versión Pro (solo por API), la versión Dev (OSS con licencia comercial de pago por imagen), y la versión Schnell (totalmente abierta con licencia comercial gratuita). Pero para Flux 2.0 solo presentaron la versión privada (Pro) y la versión OSS (Dev) con una licencia comercial de minimo 2000 dólares al mes. Y el segundo error fue técnico: el modelo era enorme, 32B de parámetros (alrededor de 90 GB de VRAM), dejando fuera a la mayoría de usuarios particulares. Incluso con cuantización agresiva apenas entraba en una RTX 4090.

Alibaba aprovechó la oportunidad. Tongyi Lab (laboratorio primo de Qwen) lanzó **Z-Image** y **Z-Image Edit**, con calidad cercana a Flux 2.0 pero con un tamaño mucho menor: **6B parámetros**, totalmente OSS y con licencia comercial gratuita.

Parece que a Black Forest Labs se le escapa el título de estándar del OSS por priorizar al mercado corporativo mientras Alibaba se queda con la comunidad.



