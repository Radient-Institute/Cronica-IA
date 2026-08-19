---
weight: 4
bookFlatSection: true
title: "04 - El Coral"
image: _din_style/banner_images/04_ec.webp
---

# El Coral

Si bien los LLMs acaparaban casi todos los titulares, el otro frente más antiguo de la revolución de la IA (la generación de imágenes) no se quedaba estático. Para 2023, esta tecnología había dejado de ser un experimento de laboratorio para convertirse en una industria real, con productos sólidos y un ecosistema en plena efervescencia.

El líder indiscutible de los modelos propietarios era MidJourney,[^1] y el de los modelos abiertos era Stable Diffusion 1.5–2.1;[^2] ambos habían logrado algo extraordinario: acercar el diseño visual a personas sin formación técnica y, simultáneamente, hacer que los profesionales del sector (después de superar las etapas inevitables de enfado y negación) empezaran a incorporar estas herramientas en sus flujos de trabajo. La pregunta ya no era “si” la IA impactaría en el diseño gráfico, sino “cómo” y “qué tan rápido”.

## La Maduración Técnica

¿Recuerdan aquellas imágenes grotescas con ocho dedos por mano y texto incomprensible que definieron los primeros días de DALL-E 2 y Stable Diffusion? Durante 2024 esos problemas fueron volviéndose parte del pasado poco a poco.

Los avances no provinieron de un solo *breakthrough*, sino de mejoras simultáneas en varios frentes: técnicas más sofisticadas, una reconceptualización del enfoque de estos modelos que trajo entrenamientos más estables y otros trucos varios. Existieron tres paradigmas que compitieron por dominar el campo:

{{% columns %}}
- {{< card >}}
  #### Paradigma Variacional (Noise Prediction Models)  
  Inspirado por los *Variational Autoencoders* (VAE), este enfoque trata el problema como aprender a eliminar ruido de una representación latente en múltiples pasos iterativos. (Ej. DDPM, DDIM)[^3]
  {{< /card >}}

- {{< card >}}
  #### Paradigma Basado en Puntaje (*Score-Based Models*)  
  Tomando ideas de los modelos de energía, este enfoque conceptualiza el problema como aprender el gradiente de una distribución de datos en evolución. (Ej. DSM, SSM)[^4]
  {{< /card >}}

- {{< card >}}
  #### Paradigma del Flujo (*Flow Models*)  
  Prestándose conceptos de los *normalizing flows*, este enfoque trata el problema como aprender el campo de velocidad que transporta muestras desde ruido puro hasta el espacio de datos, siguiendo una trayectoria suave y continua. (Ej. *Flow Matching*, *Rectified Flow*).[^5] Este paradigma eventualmente desplazó a los dos anteriores y se convirtió en el estándar de la industria.
  {{< /card >}}
{{% /columns %}}

Las otras principales mejoras fueron en la **arquitectura**, donde el DiT (*Diffusion Transformer*) reemplazó a la venerable U-Net,[^6] permitiendo modelos más escalables y eficientes; también se hicieron los latentes más grandes. Además, se implementaron nuevos *encoders* de texto más potentes (incluso la combinación de varios de estos)[^7] y un proceso de *recaptioning* sintético mucho más preciso en los *datasets*,[^8] lo que permitió a los modelos entender instrucciones más complejas y matizadas.

También vale la pena mencionar la llegada de los *Consistency Models* (marzo 2023)[^9] y los *Latent Consistency Models*,[^10] que permitieron generar imágenes con muchos menos pasos de inferencia, reduciendo tiempos de generación de decenas de segundos a incluso menos de un segundo, desbloqueando la generación condicionada casi en tiempo real y permitiendo a usuarios ver sus ideas materializarse casi instantáneamente.

## Plataformas Comerciales

MidJourney mantenía su liderazgo, pero el mercado se diversificaba rápidamente. Adobe, con su músculo empresarial y base de usuarios masiva, lanzó Firefly en marzo de 2023,[^11] tiempo despues integrándose directamente en Photoshop y otras herramientas de su ecosistema Creative Cloud. Leonardo AI emergió como favorito de la comunidad de creadores de contenido.[^12] Ideogram llegó en agosto[^13] con una propuesta diferenciada: finalmente, texto legible en imágenes generadas. Y OpenAI, que había iniciado todo allá en 2021 con DALL-E, redobló su apuesta con DALL-E 3,[^14] integrado directamente en ChatGPT en septiembre sin costo adicional para sus usuarios plus, masificando el acceso aún más.

Cada plataforma intentaba encontrar su nicho, ya fuera estética, integración, variedad, etc.

## El Florecimiento del Ecosistema Abierto

La comunidad no se dejaba adelantar demasiado, ya que había construido un ecosistema vibrante alrededor de Stable Diffusion. Aunque SD 1.5 seguía siendo el caballo de batalla confiable y SD 2.x había recibido críticas mixtas por su rendimiento irregular, una nueva generación de modelos comenzaba a emerger.

{{% details title="Modelos fundacionales de imágenes relevantes" open=false %}}
**DeepFloyd IF** (abril 2023)[^15] fue de los primeros modelos capaces de generar texto legible. **Stable Diffusion XL** (julio 2023)[^16] finalmente cumplió la promesa de una versión superior de SD con mejor composición y detalles más refinados. **PixArt-Alpha** y **Würstchen** exploraron arquitecturas alternativas.[^17] **SDXL Turbo** demostró que la velocidad era posible.[^18] **Stable Cascade** (febrero 2024)[^19] y **Stable Diffusion 3** (febrero 2024)[^20] continuaron empujando los límites. **Playground 2.5** (marzo 2024)[^21] aportó un enfoque en el diseño gráfico en vez del fotorealismo.
{{% /details %}}

Pero la verdadera magia del OSS no estaba solo en los modelos base, sino en lo que la comunidad construía sobre ellos.

Cientos, luego miles de variantes de modelos aparecieron, cada una especializada en diferentes estilos, conceptos o casos de uso.

{{% details title="Técnicas relevantes" open=false %}}
- **LoRA** (*Low-Rank Adaptation*): técnica prestada de los LLMs que permitía entrenar variaciones de modelos con recursos mínimos.[^22]  
- **DreamBooth**: para enseñar a los modelos conceptos específicos.[^22]  
- **IP-Adapters**: para transferir estilos y características de imágenes de referencia.[^22]  
- **ControlNet y sus sucesores**: revolucionaron el control espacial, permitiendo condicionar la generación con mapas de profundidad, *sketches*, poses de cuerpos humanos, bordes de objetos, etc.[^22]  
- **Técnicas de *relighting***: para ajustar iluminación de forma no destructiva.  
- **Inpainting y *outpainting***: para editar y extender imágenes.
{{% /details %}}

La academia contribuyó enormemente, publicando un flujo constante de *papers* con nuevas técnicas de controlabilidad que iban muchísimo más allá del simple texto-a-imagen. Los profesionales *early adopters* ya no tenían la excusa de la falta de control y empezaron a implementar estas técnicas en sus *pipelines* de producción.

Y todo convergía en **ComfyUI**,[^23] la interfaz que se convirtió en el estándar de facto para usuarios avanzados. Su sistema de nodos permitía crear *workflows* complejos combinando múltiples modelos y técnicas. La dinámica era clara: sacabas una nueva técnica y tenías que integrarla en ComfyUI; lanzabas un nuevo modelo y debía estar disponible en ComfyUI, porque era donde estaban los usuarios más sofisticados.

Para ser honestos, en términos de calidad pura, los modelos *open source* siempre estaban un paso por detrás de los líderes comerciales. Pero esa ligera desventaja se compensaba con creces por la flexibilidad, el control granular y el ecosistema infinitamente extensible que solo el código abierto puede ofrecer.

## El Motor Se Queda Sin Combustible

La historia de Stability AI es un caso de estudio sobre los desafíos de monetizar la IA *open source* y el equilibrio entre misión idealista y realidad comercial.

### Las Grietas Aparecen

A inicios de 2024 comenzaron a circular rumores: Stability AI, a pesar de su popularidad masiva y su papel como motor del ecosistema *open source* de generación de imágenes, enfrentaba serios problemas financieros.[^24] La compañía que había dado al mundo Stable Diffusion bajo una licencia comercial permisiva, había financiado generosamente el cómputo de organizaciones *open source* como EleutherAI,[^25] Carper AI y Harmony AI, había encontrado el amor y el respeto de la comunidad… pero no había encontrado un modelo de negocio sostenible.

La idea que manejaba la *startup* consistía en que la fama y reconocimiento obtenidos por sus modelos se traducirían en contratos lucrativos con gobiernos y corporaciones que necesitaran modelos personalizados entrenados con datos internos.[^26] Esos contratos no llegaron, al menos no en el volumen esperado para costear sus gastos. 

Lamentablemente, el dinero de los VCs no sería suficiente para mantener por mucho tiempo sus “acciones filantrópicas”: entrenar modelos caros y regalarlos, mantener *clusters* de cómputo para la comunidad y financiar investigación abierta.

Los intentos de paliar el déficit fracasaron. Lanzaron suscripciones para usar sus modelos en aplicaciones, pero los ingresos fueron insuficientes y este esquema no funcionó. Investigadores clave comenzaron a abandonar la empresa[^27] y, aun peor, en marzo de 2024 Emad Mostaque, CEO y rostro público de Stability y del movimiento *open source*, renunció.[^27]

### El Giro Pragmático

El nuevo CEO, Prem Akkaraju,[^28] ejecutó un giro rápido, con acciones necesarias para la supervivencia, como el corte de *grants* de cómputo, la reducción del *cluster* de GPUs propio, despidos en áreas no críticas y un reenfoque completo: de laboratorio de investigación abierta a empresa de productos para la industria audiovisual.

Con las cuentas saneadas consiguieron una nueva ronda de financiamiento.[^28] Añadieron credibilidad llevando al legendario director James Cameron a su mesa directiva.[^29] Se *rebrandearon* como “la *startup* de IA para artistas y creativos”, firmaron *partnerships* estratégicos con gigantes de publicidad y medios como WPP,[^30] y comenzaron a lanzar productos más enfocados y menos populares: Marble, Stable Audio Open, Stable Fast 3D.[^31]

Ya no eran el laboratorio idealista que había capturado los corazones de la comunidad *open source*. Eran una empresa relativamente tradicional. Pragmática, sí. Inspiradora, no tanto.

### El Heredero: Black Forest Labs

Pero la historia tiene un giro poético. Robin Rombach, el investigador principal detrás de Stable Diffusion, había abandonado Stability AI antes que Emad. Junto con colegas clave del equipo original, fundó **Black Forest Labs**[^32] con una misión clara: continuar el legado técnico de Stable Diffusion.

En agosto de 2024 llegó su primer lanzamiento: **Flux**,[^32] un modelo de generación de imágenes que demostraba que el equipo original no había perdido su toque. Lanzaron tres versiones:  **Flux-Schnell** (*open source*, licencia comercial gratuita), **Flux Dev** (*open source*, licencia comercial de pago) y **Flux Pro** (accesible solo vía API o a través de *partners* como Fal, Freepik, Krea, Leonardo e incluso X.AI temporalmente).[^32]

La recepción fue entusiasta. Flux rápidamente reemplazó a Stable Diffusion como el estándar de facto del ecosistema *open source*. Posteriormente, se presentaron actualizaciones incrementales llegando a Flux 1.1[^33] y Flux 2[^34]. El modelo mantuvo su posición de liderazgo en un escenario cada vez más competido por alternativas Chinas (Qwen-Image[^35] y Z-Image[^36]), al menos a lo largo del 2025.

## Referencias

[^1]: Edwards, Benj. ["AI-imager Midjourney v5 stuns with photorealistic images—and 5-fingered hands"](https://arstechnica.com/information-technology/2023/03/ai-imager-midjourney-v5-stuns-with-photorealistic-images-and-5-fingered-hands/). *Ars Technica*, 16 de marzo de 2023.

[^2]: Stability AI. ["Stable Diffusion Public Release"](https://stability.ai/news-updates/stable-diffusion-public-release). 22 de agosto de 2022; Stability AI. ["Stable Diffusion v2.1 and DreamStudio Updates"](https://stability.ai/news-updates/stablediffusion2-1-release7-dec-2022). 7 de diciembre de 2022.

[^3]: Ho, Jonathan; Jain, Ajay; Abbeel, Pieter. ["Denoising Diffusion Probabilistic Models"](https://arxiv.org/abs/2006.11239). 19 de junio de 2020.

[^4]: Song, Yang et al. ["Score-Based Generative Modeling through Stochastic Differential Equations"](https://arxiv.org/abs/2011.13456). 26 de noviembre de 2020.

[^5]: Lipman, Yaron et al. ["Flow Matching for Generative Modeling"](https://arxiv.org/abs/2210.02747). 6 de octubre de 2022; Liu, Xingchao; Gong, Chengyue; Liu, Qiang. ["Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow"](https://arxiv.org/abs/2209.03003). Septiembre de 2022.

[^6]: Peebles, William; Xie, Saining. ["Scalable Diffusion Models with Transformers"](https://arxiv.org/abs/2212.09748). 19 de diciembre de 2022.

[^7]: Podell, Dustin et al. ["SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis"](https://arxiv.org/abs/2307.01952). Julio de 2023.

[^8]: Chen, Junsong et al. ["PixArt-α: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis"](https://arxiv.org/abs/2310.00426). 30 de septiembre de 2023.

[^9]: Song, Yang et al. ["Consistency Models"](https://arxiv.org/abs/2303.01469). 2 de marzo de 2023.

[^10]: Luo, Simian et al. ["Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference"](https://arxiv.org/abs/2310.04378). 6 de octubre de 2023.

[^11]: Adobe. ["Adobe Unveils Firefly, a Family of New Creative Generative AI"](https://news.adobe.com/news/news-details/2023/adobe-unveils-firefly-a-family-of-new-creative-generative-ai). 21 de marzo de 2023; Adobe. ["Adobe Unveils Future of Creative Cloud With Generative AI as a Creative Co-Pilot in Photoshop"](https://news.adobe.com/news/news-details/2023/adobe-unveils-future-of-creative-cloud-with-generative-ai-as-a-creative-co-pilot-in-photoshop). 23 de mayo de 2023.

[^12]: Canva. ["Welcome to Canva, Leonardo!"](https://www.canva.com/newsroom/news/leonardo-ai/). 29 de julio de 2024.

[^13]: Ideogram. ["Ideogram 0.1 is open to everyone for free"](https://ideogram.ai/publicly-available). 29 de agosto de 2023.

[^14]: OpenAI. ["DALL·E 3"](https://openai.com/index/dall-e-3/). Septiembre de 2023.

[^15]: Stability AI. ["Stability AI releases DeepFloyd IF, a powerful text-to-image model that can smartly integrate text into images"](https://stability.ai/news-updates/deepfloyd-if-text-to-image-model). 28 de abril de 2023.

[^16]: Podell, Dustin et al. ["SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis"](https://arxiv.org/abs/2307.01952). Julio de 2023.

[^17]: Chen, Junsong et al. ["PixArt-α: Fast Training of Diffusion Transformer for Photorealistic Text-to-Image Synthesis"](https://arxiv.org/abs/2310.00426). 30 de septiembre de 2023; Pernias, Pablo; Rampas, Dominic; Aubreville, Marc. ["Wuerstchen: Efficient Pretraining of Text-to-Image Models"](https://arxiv.org/abs/2306.00637). 1 de junio de 2023.

[^18]: Stability AI. ["Introducing SDXL Turbo: A Real-Time Text-to-Image Generation Model"](https://stability.ai/news-updates/sdxl-turbo). 28 de noviembre de 2023.

[^19]: Stability AI. ["Introducing Stable Cascade"](https://stability.ai/news-updates/introducing-stable-cascade). 12 de febrero de 2024.

[^20]: Stability AI. ["Stable Diffusion 3"](https://stability.ai/news-updates/stable-diffusion-3). 22 de febrero de 2024.

[^21]: Li, Daiqing et al. ["Playground v2.5: Three Insights towards Enhancing Aesthetic Quality in Text-to-Image Generation"](https://arxiv.org/abs/2402.17245). 27 de febrero de 2024.

[^22]: Hu, Edward J. et al. ["LoRA: Low-Rank Adaptation of Large Language Models"](https://arxiv.org/abs/2106.09685). 17 de junio de 2021; Ruiz, Nataniel et al. ["DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation"](https://arxiv.org/abs/2208.12242). 25 de agosto de 2022; Ye, Hu et al. ["IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models"](https://arxiv.org/abs/2308.06721). 13 de agosto de 2023; Zhang, Lvmin; Rao, Anyi; Agrawala, Maneesh. ["Adding Conditional Control to Text-to-Image Diffusion Models"](https://arxiv.org/abs/2302.05543). 10 de febrero de 2023.

[^23]: ComfyUI. ["ComfyUI"](https://github.com/comfyanonymous/ComfyUI). Proyecto *open source* de interfaz gráfica basada en nodos para construir y ejecutar *workflows* modulares de generación con modelos de difusión.

[^24]: Reuters. ["Stability AI discusses sale amid cash crunch, The Information reports"](https://www.reuters.com/markets/deals/stability-ai-discusses-sale-amid-cash-crunch-information-reports-2024-05-16/). 16 de mayo de 2024.

[^25]: Wiggers, Kyle. ["Stability AI, Hugging Face and Canva back new AI research nonprofit"](https://techcrunch.com/2023/03/02/stability-ai-hugging-face-and-canva-back-new-ai-research-nonprofit/). *TechCrunch*, 2 de marzo de 2023. Documenta que Stability AI cedió parte de la capacidad de su *cluster* de AWS para investigación de EleutherAI.

[^26]: Cai, Kenrick. ["How Stability AI’s Founder Tanked His Billion-Dollar Startup"](https://www.forbes.com/sites/kenrickcai/2024/03/29/how-stability-ais-founder-tanked-his-billion-dollar-startup/). *Forbes*, 29 de marzo de 2024.

[^27]: Reuters. ["Stability AI to lay off staff weeks after founder Mostaque resigned as CEO"](https://www.reuters.com/technology/stability-ai-lay-off-staff-weeks-after-founder-mostaque-resigned-ceo-2024-04-18/). 18 de abril de 2024.

[^28]: Reuters. ["Cash-strapped Stability AI raises $80 mln with new CEO and board"](https://www.reuters.com/technology/artificial-intelligence/cash-strapped-stability-ai-raises-80-mln-with-new-ceo-board-2024-06-25/). 25 de junio de 2024.

[^29]: Stability AI. ["James Cameron, Academy Award-Winning Filmmaker, Joins Stability AI Board of Directors"](https://stability.ai/news-updates/james-cameron-joins-stability-ai-board-of-directors). 24 de septiembre de 2024.

[^30]: Stability AI. ["Stability AI Announces Investment from WPP and New Partnership to Shape the Future of Media and Entertainment Production"](https://stability.ai/news-updates/stability-ai-announces-investment-from-wpp-and-new-partnership-to-shape-the-future-of-media-and-entertainment-production). 5 de marzo de 2025; WPP. ["WPP announces investment in Stability AI and new partnership"](https://www.wpp.com/en/news/2025/03/wpp-announces-investment-in-stability-ai). 5 de marzo de 2025.

[^31]: Stability AI. ["Introducing Stable Audio Open - An Open Source Model for Audio Samples and Sound Design"](https://stability.ai/news-updates/introducing-stable-audio-open). 5 de junio de 2024; Stability AI. ["Introducing Stable Fast 3D: Rapid 3D Asset Generation From Single Images"](https://stability.ai/news-updates/introducing-stable-fast-3d). 1 de agosto de 2024; Stability AI. ["MARBLE: Material Recomposition and Blending in CLIP-Space"](https://stability.ai/research/marble-material-recomposition-and-blending-in-clip-space). 5 de junio de 2025.

[^32]: Black Forest Labs. ["Announcing Black Forest Labs"](https://bfl.ai/blog/24-08-01-bfl). 1 de agosto de 2024.

[^33]: Black Forest Labs. ["Announcing FLUX1.1 [pro] and the BFL API"](https://bfl.ai/blog/24-10-02-flux). 2 de octubre de 2024.

[^34]: Black Forest Labs. ["FLUX.2: Frontier Visual Intelligence"](https://bfl.ai/blog/flux-2). 25 de noviembre de 2025; Black Forest Labs. ["FLUX.2 [dev] is now open source"](https://github.com/black-forest-labs/flux2). 25 de noviembre de 2025.

[^35]: Qwen Team. ["Qwen-Image: Crafting with Native Text Rendering"](https://qwenlm.github.io/blog/qwen-image/). 4 de agosto de 2025; Qwen Team. ["Qwen-Image Technical Report"](https://arxiv.org/abs/2508.02324). 4 de agosto de 2025.

[^36]: Cai, Huanqia et al. ["Z-Image: An Efficient Image Generation Foundation Model with Single-Stream Diffusion Transformer"](https://arxiv.org/abs/2511.22699). 27 de noviembre de 2025; Tongyi-MAI. ["Z-Image"](https://github.com/Tongyi-MAI/Z-Image). Proyecto *open source* de Alibaba (Tongyi Lab).
