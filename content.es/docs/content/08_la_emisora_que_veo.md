---
weight: 8
bookFlatSection: true
title: "08 - La Emisora Que Veo"
image: _din_style/banner_images/08_leqv.webp
---

# La Emisora Que Veo

Creo que en la historia reciente de la IA no hemos visto un *flexeo* tan grande como el de Sora. Estamos en febrero del 2024. Tras el éxito de la generación de imágenes con IA, había un enorme interés en conseguir algo equivalente en vídeo. Muchas *startups* lo estaban intentando, y se estaba invirtiendo sumas importantes de dinero.

La calidad avanzaba poco a poco. Ya quedaba atrás el infame *Will Smith comiendo spaghetti* de marzo del 2023 generado con ModelScope.[^1] Los vídeos empezaban a verse mejor, aunque muchos no eran más que paneos con ligero movimiento. El 2023 cerró con **Runway** liderando el *closed source* con Gen-2[^2] y con **Stability AI** a la cabeza del *open source* con Stable Video Diffusion.[^3]

Hasta que, en febrero del 2024, OpenAI *flexeó* algo absolutamente impactante: **Sora**.[^4] Tenía una consistencia ilógica, una calidad ilógica, acciones dentro de los clips ilógicas, las generaciones duraban hasta un minuto. Todo era ilógico. Ni siquiera lo llamaron “generador de vídeo”, lo presentaron como un **"generador de mundos"**.[^4]

¿Cómo era posible que un solo laboratorio tuviera tanta ventaja? Y recalco: el vídeo no era un área abandonada. Había muchísimo dinero y muchos equipos trabajando intensamente en simultáneo.

El efecto Sora fue inmediato: todo el mundo retrocedió un paso, a replantearse sus objetivos y estrategias. Si antes había dudas sobre qué tan lejos podía llegar el video IA, ahora todos sabíamos que esta calidad era posible. Las *startups* y el ecosistema *open source* se pusieron manos a la obra.

En pocos meses vimos una ola de lanzamientos de la competencia.

{{% details title="Lanzamientos de la competencia" open=false %}}

- **Kling** en China (junio)[^5]
- **Luma AI** entrando al vídeo con Dream Machine (junio)[^6]
- **Runway** anunciando Gen-3 (junio)[^7]
- **PikaLabs v1.5** (octubre)[^8]\
  {{% /details %}}

Incluso algunas grandes corporaciones se vieron obligadas a mostrar demos de cosas que claramente no estaban listas, como Veo 1 de Google[^9] o MovieGen de Meta,[^10] solo para dejar claro que “no estaban tan atrás”.

Mientras tanto, el OSS avanzó rapidísimo gracias a todas las técnicas heredadas de la generación de imágenes: DiT, *flow matching*, *rectified flow*, etc. Tuvimos **Open Sora**,[^11] **LTX-Video**[^12] y **CogVideoX**.[^13]

Podríamos imaginar que OpenAI aprovecharía ese tiempo para dominar el mercado en solitario. Pero… no. Excepto por algunos diseñadores, artistas y directores de cine seleccionados, nadie tuvo acceso real al modelo original de Sora.[^14] Aparentemente el modelo era sumamente grande y sumamente costoso de servir,[^15] sin embargo OpenAI declaraba que mantener el modelo sin acceso público era por motivos de “seguridad” y los riesgos asociados con generar video con ese nivel de realismo.[^14]

Diez meses después del anuncio, en diciembre del 2024, dieron acceso a los suscriptores de ChatGPT a **sora-turbo**, una versión muy inferior.[^16] ¿Dónde estaba la consistencia? ¿Dónde estaban los videos con duración de un minuto? ¿Dónde estaba la calidad? Bueno, había algo de estética… pero en líneas generales sora-turbo fue un fracaso rotundo.

Quien realmente se llevó toda la gloria fue Google. Anunciaron **Veo 3** en mayo del 2025 durante el Google I/O: un salto enorme, calidad ampliamente superior, disponible inmediatamente, con audio integrado.[^17] El rey. Las redes sociales explotaron. Se llenaron de memes, bromas y videos virales hechos con Veo 3. Fue el primer producto de IA verdaderamente viral de Google, y le ganaron la carrera a OpenAI.

MidJourney se unió a la fiesta más tarde, en junio, con su estilo y estética característica.[^18] Es impresionante pensar que esta *startup* bootstrappeada alcanzó 500 millones de dólares en ingresos el 2025.[^19]

El resto del año estuvo marcado por actualizaciones constantes de todos los competidores del campo del vídeo: Kling, Hailuo, Luma, Runway… Incluso Google reforzó su liderato sacando **Veo 3.1**.[^20]

## La integración del vídeo IA en el contenido audiovisual

El vídeo generado por IA ha alcanzado un nivel suficientemente bueno para ser consumido, pero para finales del 2025 todavía no había logrado integrarse por completo en todos los tipos de contenido audiovisual.

El cine, los largometrajes, las series y los documentales **aún no lo han adoptado** ampliamente. Las razones mencionadas fueron varias: pequeños detalles de calidad, limitaciones de duración, falta de control fino en los modelos propietarios que superan al OSS… o quizás simplemente la propia lentitud de la industria cinematográfica. Honestamente, no lo sé.

En YouTube se ha adoptado ligeramente, sobre todo como material ilustrativo en mini-documentales. Donde realmente el contenido IA de video encontró refugio fue en el **formato corto**: TikTok, Reels, Shorts. Suficientemente corto como para generarse con uno o un par de *prompts*. Suficientemente banal como para que sus errores ni siquiera ameriten queja.

## La máquina de *AI slop* infinito

Las plataformas de contenido corto se llenaron de vídeos IA. Sabíamos que, en algún momento, alguien lanzaría una red social exclusivamente para vídeos generados con IA. La duda era quién y cuándo. La respuesta vino de dos lugares inesperados: **Meta y OpenAI**, casi en la misma semana, en septiembre del 2025.

Meta lo hizo primero con **Vibes**, un *feed* de vídeos IA dentro de su app Meta AI.[^21] Como no contaban con un modelo de video propio competitivo para generación multimedia, decidieron usar los modelos de MidJourney y de Black Forest Labs.[^22]

Por su parte, OpenAI lanzó una nueva red social completa, exclusiva y en condiciones, que funcionaba usando al también nuevo **Sora 2**,[^23] un modelo muy bueno y con un enfoque evidente en contenido para redes sociales. Al igual que Veo 3, podía generar audio y vídeo en conjunto.[^23] Pero la característica que lo convirtió en un fenómeno viral fueron los **cameos**: cualquier persona podía escanearse a sí misma y pedir a Sora 2 que generara un vídeo con ella en cualquier situación.[^23]

A los pocos días del lanzamiento, internet se llenó de videos de celebridades haciendo cosas absurdas. No era algo que previamente fuese imposible de hacer, pero ahora era más fácil que nunca… y gratuito.[^23]

Los entresijos del nivel de éxito de Sora los meses próximos a su salida, su base de usuarios o la dinámica interna de esa red social, van más allá de mi saber. Puedo adentrarme en megalaberintos para traerles información, pero no voy a meterme a un basurero.

## Referencias

[^1]: Cole, Samantha. ["AI Will Smith Eating Spaghetti Will Haunt You For the Rest of Your Life"](https://www.vice.com/en/article/ai-will-smith-eating-spaghetti-hill-haunt-you-for-the-rest-of-your-life/). VICE. 28 de marzo de 2023.

[^2]: Runway. ["Gen-2: Generate novel videos with text, images or video clips"](https://runwayml.com/research/gen-2). Febrero de 2023.

[^3]: Stability AI. ["Introducing Stable Video Diffusion"](https://stability.ai/news/stable-video-diffusion-open-ai-video-model). 21 de noviembre de 2023.

[^4]: OpenAI. ["Video generation models as world simulators"](https://openai.com/index/video-generation-models-as-world-simulators/). 15 de febrero de 2024.

[^5]: Kuaishou. ["Kuaishou Unveils Proprietary Video Generation Model 'Kling;' Testing Now Available"](https://ir.kuaishou.com/news-releases/news-release-details/kuaishou-unveils-proprietary-video-generation-model-kling). 10 de junio de 2024. El acceso inicial comenzó el 6 de junio.

[^6]: Luma AI. ["Introducing Dream Machine"](https://threadreaderapp.com/thread/1800921380034379951.html). 12 de junio de 2024.

[^7]: Runway. ["Runway Gen-3 Alpha: Next-Generation AI Video Generation"](https://runwayml.com/research/introducing-gen-3-alpha). 17 de junio de 2024.

[^8]: Franzen, Carl. ["Pika 1.5 launches with physics-defying AI special effects"](https://venturebeat.com/ai/pika-1-5-launches-with-physics-defying-ai-special-effects). VentureBeat. 1 de octubre de 2024.

[^9]: Google. ["New generative media models and tools, built with and for creators"](https://blog.google/innovation-and-ai/products/google-generative-ai-veo-imagen-3/). 14 de mayo de 2024. Veo se presentó inicialmente mediante una vista previa privada para creadores seleccionados.

[^10]: Meta. ["How Meta Movie Gen could usher in a new AI-enabled era for content creators"](https://ai.meta.com/blog/movie-gen-media-foundation-models-generative-ai-video/). 4 de octubre de 2024. Meta indicó posteriormente que no planeaba incorporar Movie Gen a productos públicos hasta 2025.

[^11]: HPC-AI Tech. ["Open-Sora: Democratizing Efficient Video Production for All"](https://github.com/hpcaitech/Open-Sora). Marzo de 2024.

[^12]: Lightricks. ["LTX-Video"](https://github.com/Lightricks/LTX-Video). 21 de noviembre de 2024.

[^13]: THUDM. ["CogVideoX"](https://github.com/THUDM/CogVideo). Agosto de 2024. CogVideoX-2B fue abierto el 6 de agosto y CogVideoX-5B el 27 de agosto.

[^14]: OpenAI. ["Sora: Creating video from text"](https://openai.com/index/sora/). Febrero de 2024.

[^15]: Wiggers, Kyle. ["OpenAI's Sora video generator appears to have leaked"](https://techcrunch.com/2024/11/26/artists-appears-to-have-leaked-access-to-openais-sora/). TechCrunch. 26 de noviembre de 2024. Recoge reporting de *The Information* según el cual el Sora original podía tardar más de diez minutos de procesamiento para generar un clip de un minuto.

[^16]: OpenAI. ["Sora is here"](https://openai.com/index/sora-is-here/). 9 de diciembre de 2024.

[^17]: Google. ["Fuel your creativity with new generative media models and tools"](https://blog.google/innovation-and-ai/products/generative-media-models-io-2025/). 20 de mayo de 2025. Veo 3 incorporó generación nativa de audio y estuvo disponible ese mismo día para suscriptores Ultra en Estados Unidos.

[^18]: MidJourney. ["Introducing Midjourney V1 Video"](https://updates.midjourney.com/introducing-our-v1-video-model/). 18 de junio de 2025.

[^19]: Pofeldt, Elaine. ["The Race To Create A Billion-Dollar, One-Person Business"](https://www.forbes.com/sites/elainepofeldt/2025/11/17/the-race-to-create-a-billion-dollar-one-person-business/). Forbes. 17 de noviembre de 2025.

[^20]: Google. ["Introducing Veo 3.1 and advanced capabilities in Flow"](https://blog.google/innovation-and-ai/products/veo-updates-flow/). 15 de octubre de 2025.

[^21]: Meta. ["Presentando Vibes: Una nueva forma de descubrir y crear videos con IA"](https://about.fb.com/ltam/news/2025/09/presentando-vibes-una-nueva-forma-de-descubrir-y-crear-videos-con-ia/). 25 de septiembre de 2025.

[^22]: Wang, Alexandr. Declaraciones durante el lanzamiento de Vibes, 25 de septiembre de 2025. ["For this early version, we've partnered with Midjourney and Black Forest Labs while we continue developing our own models behind the scenes."](https://www.techmeme.com/250926/h0135)

[^23]: OpenAI. ["Sora 2 is here"](https://openai.com/index/sora-2/). 30 de septiembre de 2025. OpenAI lanzó Sora 2 como modelo conjunto de vídeo y audio junto con una app social.
