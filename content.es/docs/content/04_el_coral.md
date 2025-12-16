---
weight: 4
bookFlatSection: true
title: "04 - El Coral"
image: _din_style/banner_images/04_ec.webp
---

# El Coral

Si bien los LLMs acaparaban casi todos los titulares, el otro frente más antiguo de la revolución de la IA (la generación de imágenes) no se quedaba estático. Para 2023, esta tecnología había dejado de ser un experimento de laboratorio para convertirse en una industria real, con productos sólidos y un ecosistema en plena efervescencia.

El líder indiscutible de los modelos propietarios era MidJourney, y el de los modelos abiertos era Stable Diffusion 1.5–2.1; ambos habían logrado algo extraordinario: acercar el diseño visual a personas sin formación técnica y, simultáneamente, hacer que los profesionales del sector (después de superar las etapas inevitables de enfado y negación) empezaran a incorporar estas herramientas en sus flujos de trabajo. La pregunta ya no era “si” la IA impactaría en el diseño gráfico, sino “cómo” y “qué tan rápido”.

## La Maduración Técnica

¿Recuerdan aquellas imágenes grotescas con ocho dedos por mano y texto incomprensible que definieron los primeros días de DALL-E 2 y Stable Diffusion? Durante 2024 esos problemas fueron volviéndose parte del pasado poco a poco.

Los avances no provinieron de un solo *breakthrough*, sino de mejoras simultáneas en varios frentes: técnicas más sofisticadas, una reconceptualización del enfoque de estos modelos que trajo entrenamientos más estables y otros trucos varios. Existieron tres paradigmas que compitieron por dominar el campo:

{{% columns %}}
- {{< card >}}
  #### Paradigma Variacional (Noise Prediction Models)  
  Inspirado por los *Variational Autoencoders* (VAE), este enfoque trata el problema como aprender a eliminar ruido de una representación latente en múltiples pasos iterativos. (Ej. DDPM, DDIM)
  {{< /card >}}

- {{< card >}}
  #### Paradigma Basado en Puntaje (*Score-Based Models*)  
  Tomando ideas de los modelos de energía, este enfoque conceptualiza el problema como aprender el gradiente de una distribución de datos en evolución. (Ej. DSM, SSM)
  {{< /card >}}

- {{< card >}}
  #### Paradigma del Flujo (*Flow Models*)  
  Prestándose conceptos de los *normalizing flows*, este enfoque trata el problema como aprender el campo de velocidad que transporta muestras desde ruido puro hasta el espacio de datos, siguiendo una trayectoria suave y continua. (Ej. *Flow Matching*, *Rectified Flow*). Este paradigma eventualmente desplazó a los dos anteriores y se convirtió en el estándar de la industria.
  {{< /card >}}
{{% /columns %}}

Las otras principales mejoras fueron en la **arquitectura**, donde el DiT (*Diffusion Transformer*) reemplazó a la venerable U-Net, permitiendo modelos más escalables y eficientes; también se hicieron los latentes más grandes. Además, se implementaron nuevos *encoders* de texto más potentes (incluso la combinación de varios de estos) y un proceso de *recaptioning* sintético mucho más preciso en los *datasets*, lo que permitió a los modelos entender instrucciones más complejas y matizadas.

También vale la pena mencionar la llegada de los *Consistency Models* (marzo 2023) y los *Latent Consistency Models*, que permitieron generar imágenes con muchos menos pasos de inferencia, reduciendo tiempos de generación de decenas de segundos a incluso menos de un segundo, desbloqueando la generación condicionada casi en tiempo real y permitiendo a usuarios ver sus ideas materializarse casi instantáneamente.

## Plataformas Comerciales

MidJourney mantenía su liderazgo, pero el mercado se diversificaba rápidamente. Adobe, con su músculo empresarial y base de usuarios masiva, lanzó Firefly en mayo de 2023, integrándose directamente en Photoshop y otras herramientas de su ecosistema Creative Cloud. Leonardo AI emergió como favorito de la comunidad de creadores de contenido. Ideogram llegó en septiembre con una propuesta diferenciada: finalmente, texto legible en imágenes generadas. Y OpenAI, que había iniciado todo allá en 2021 con DALL-E, redobló su apuesta con DALL-E 3, integrado directamente en ChatGPT en septiembre sin costo adicional, masificando el acceso aún más.

Cada plataforma intentaba encontrar su nicho, ya fuera estética, integración, variedad, etc.

## El Florecimiento del Ecosistema Abierto

La comunidad no se dejaba adelantar demasiado, ya que había construido un ecosistema vibrante alrededor de Stable Diffusion. Aunque SD 1.5 seguía siendo el caballo de batalla confiable y SD 2.x había recibido críticas mixtas por su rendimiento irregular, una nueva generación de modelos comenzaba a emerger.

{{% details title="Modelos fundacionales de imágenes relevantes" open=false %}}
**DeepFloyd IF** (mayo 2023) fue de los primeros modelos capaces de generar texto legible. **Stable Diffusion XL** (julio 2023) finalmente cumplió la promesa de una versión superior de SD con mejor composición y detalles más refinados. **PixArt-Alpha** y **Würstchen** exploraron arquitecturas alternativas. **SDXL Turbo** demostró que la velocidad era posible. **Stable Cascade** (febrero 2024) y **Stable Diffusion 3** (febrero 2024) continuaron empujando los límites. **Playground 2.5** (marzo 2024) aportó un enfoque en el diseño gráfico en vez del fotorealismo.
{{% /details %}}

Pero la verdadera magia del OSS no estaba solo en los modelos base, sino en lo que la comunidad construía sobre ellos.

Cientos, luego miles de variantes de modelos aparecieron, cada una especializada en diferentes estilos, conceptos o casos de uso.

{{% details title="Técnicas relevantes" open=false %}}
- **LoRA** (*Low-Rank Adaptation*): técnica prestada de los LLMs que permitía entrenar variaciones de modelos con recursos mínimos.  
- **DreamBooth**: para enseñar a los modelos conceptos específicos.  
- **IP-Adapters**: para transferir estilos y características de imágenes de referencia.  
- **ControlNet y sus sucesores**: revolucionaron el control espacial, permitiendo condicionar la generación con mapas de profundidad, *sketches*, poses de cuerpos humanos, bordes de objetos, etc.  
- **Técnicas de *relighting***: para ajustar iluminación de forma no destructiva.  
- **Inpainting y *outpainting***: para editar y extender imágenes.
{{% /details %}}

La academia contribuyó enormemente, publicando un flujo constante de *papers* con nuevas técnicas de controlabilidad que iban muchísimo más allá del simple texto-a-imagen. Los profesionales *early adopters* ya no tenían la excusa de la falta de control y empezaron a implementar estas técnicas en sus *pipelines* de producción.

Y todo convergía en **ComfyUI**, la interfaz que se convirtió en el estándar de facto para usuarios avanzados. Su sistema de nodos permitía crear *workflows* complejos combinando múltiples modelos y técnicas. La dinámica era clara: sacabas una nueva técnica y tenías que integrarla en ComfyUI; lanzabas un nuevo modelo y debía estar disponible en ComfyUI, porque era donde estaban los usuarios más sofisticados.

Para ser honestos, en términos de calidad pura, los modelos *open source* siempre estaban un paso por detrás de los líderes comerciales. Pero esa ligera desventaja se compensaba con creces por la flexibilidad, el control granular y el ecosistema infinitamente extensible que solo el código abierto puede ofrecer.

## El Motor Se Queda Sin Combustible

La historia de Stability AI es un caso de estudio sobre los desafíos de monetizar la IA *open source* y el equilibrio entre misión idealista y realidad comercial.

### Las Grietas Aparecen

A inicios de 2024 comenzaron a circular rumores: Stability AI, a pesar de su popularidad masiva y su papel como motor del ecosistema *open source* de generación de imágenes, enfrentaba serios problemas financieros. La compañía que había dado al mundo Stable Diffusion bajo licencia Apache 2.0, había financiado generosamente el cómputo de organizaciones *open source* como EleutherAI, Carper AI y Harmony AI, había encontrado el amor y el respeto de la comunidad… pero no había encontrado un modelo de negocio sostenible.

La idea que manejaba la *startup* consistía en que la fama y reconocimiento obtenidos por sus modelos se traducirían en contratos lucrativos con gobiernos y corporaciones que necesitaran modelos personalizados entrenados con datos internos. Esos contratos no llegaron, al menos no en el volumen esperado para costear sus gastos. 

Lamentablemente, el dinero de los VCs no sería suficiente para mantener por mucho tiempo sus “acciones filantrópicas”: entrenar modelos caros y regalarlos, mantener *clusters* de cómputo para la comunidad y financiar investigación abierta.

Los intentos de paliar el déficit fracasaron. Lanzaron suscripciones para usar sus modelos en aplicaciones, pero los ingresos fueron insuficientes y este esquema no funcionó. Investigadores clave comenzaron a abandonar la empresa y, aun peor, en marzo de 2024 Emad Mostaque, CEO y rostro público de Stability y del movimiento *open source*, renunció.

### El Giro Pragmático

El nuevo CEO, Prem Akkaraju, ejecutó un giro rápido, con acciones necesarias para la supervivencia, como el corte de *grants* de cómputo, la reducción del *cluster* de GPUs propio, despidos en áreas no críticas y un reenfoque completo: de laboratorio de investigación abierta a empresa de productos para la industria audiovisual.

Con las cuentas saneadas consiguieron una nueva ronda de financiamiento. Añadieron credibilidad llevando al legendario director James Cameron a su mesa directiva. Se *rebrandearon* como “la *startup* de IA para artistas y creativos”, firmaron *partnerships* estratégicos con gigantes de publicidad y medios como WPP, y comenzaron a lanzar productos más enfocados y menos populares: Marble, Stable Audio Open, Stable Fast 3D.

Ya no eran el laboratorio idealista que había capturado los corazones de la comunidad *open source*. Eran una empresa relativamente tradicional. Pragmática, sí. Inspiradora, no tanto.

### El Heredero: Black Forest Labs

Pero la historia tiene un giro poético. Robin Rombach, el investigador principal detrás de Stable Diffusion, había abandonado Stability AI antes que Emad. Junto con colegas clave del equipo original, fundó **Black Forest Labs** con una misión clara: continuar el legado técnico de Stable Diffusion.

En agosto de 2024 llegó su primer lanzamiento: **Flux**, un modelo de generación de imágenes que demostraba que el equipo original no había perdido su toque. Lanzaron tres versiones:  **Flux-Schnell** (*open source*, licencia comercial gratuita), **Flux Dev** (*open source*, licencia comercial de pago) y **Flux Pro** (accesible solo vía API o a través de *partners* como Fal, Freepik, Krea, Leonardo e incluso X.AI temporalmente).

La recepción fue entusiasta. Flux rápidamente reemplazó a Stable Diffusion como el estándar de facto del ecosistema *open source*. Con actualizaciones incrementales llegando a Flux 1.1, el modelo mantuvo su posición de liderazgo al menos hasta mediados de 2025.
