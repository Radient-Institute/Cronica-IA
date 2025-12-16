---
weight: 16
bookFlatSection: true
title: "16 - Una Historia De Ascenso Y Caída"
image: _din_style/banner_images/16_hayc.webp
---

# Una Historia de Ascenso y Caída

El metaverso fue un fracaso monumental, eso ya lo sabemos todos, pero justo cuando se acercaba el fin, llegó una nueva tecnología prometedora: la inteligencia artificial. Afortunadamente para Meta, su línea de salida no era cero. Facebook había creado en 2013 un laboratorio de primer nivel en París: FAIR (Facebook AI Research), así que la compañía tenía una base técnica mucho más que sólida para adentrarse en esta aventura.

Hasta el 2023, Meta era extremadamente influyente en múltiples áreas de la IA. En visión por computadora: DeepMask, Mask R-CNN, Detectron. En audio: HuBERT y wav2vec. En lenguaje: fastText, fairseq, RoBERTa, BART, XLM, NLLB. Y por supuesto, el proyecto más influyente de todos: PyTorch, el que actualmente es el framework de Deep Learning más popular.

Meta practicaba el **open source** y sobre todo **open science**: *reports* detallados, ablations, reflexiones, discusión abierta. Era la época en la que el *machine learning* era más ciencia que negocio.

Cuando empezó el escalado masivo de modelos de lenguaje, y tras el cambio de nombre de Facebook a Meta, FAIR pasó a significar “Fundamental AI Research”, volviéndose un laboratorio semi-independiente dentro de Meta AI, laboratorio que decidio desvincularse del entrenamiento de grandes modelos de lenguaje; esa responsabilidad cayó en otros equipos no del todo priorizados y articulados. 

* Como respuesta a GPT-3 sacaron OPT-175B (2022), 
* Poco antes de ChatGPT (GPT-3.5-turbo) lanzaron Galactica, 
* Y a inicios del 2023 anunciaron la serie de **Llama**: 7B hasta 65B. (También existía el equipo Zeta, pero shh... de eso no se habla).

## Un accidente beneficioso

Con OPT y Llama Meta cambió la estrategia de lanzamiento. Desde GPT-2 OpenAI ya nos metió miedo sobre los riesgos derivados de las capacidades de los LLMs y el peligro que supondría hacerlos publicos. Así que Meta lanzó Llama con un formulario de acceso restringido solo a investigación. En realidad no era tan restringido: hasta un desconocido como yo, sin afiliación relevante, pudo acceder a los pesos sin problemas.

Y así como le dieron acceso a desconocidos, un desconocido decidió filtrar los pesos en 4chan, en marzo del 2023 (no fui yo, lo prometo).

Meta intentó frenar la propagación en HuggingFace, pero fue imposible. La adopción explotó. Eso seguramente motivó que **Llama 2** tuviese nuevamente una filosofía abierta, con paper técnico y muchas variantes accesibles, lanzado en julio, fue un éxito absoluto. Venía incluso con versiones *chat*, una licencia comercial algo rara pero utilizable, y un rendimiento muy sólido. La comunidad lo tomó, lo *finetuneó*, modificó, cuantizó, amplió su contexto, lo puso en producción…  
Sorprendentemente, **los de Meta eran los buenos de la IA**.

En abril del año siguiente decidieron ir *all-in*. Mark Zuckerberg apareció en video anunciando personalmente **Llama 3** (8B y 70B), declarando su amor por el open source: que en la IA el *open source* debía ganar, que invertirían muchísimo dinero en conseguirlo, que tendrían centros de datos gigantescos, cientos de miles de GPUs, que serían la plataforma. Pusieron el modelo de forma gratuita en Meta AI, en las gafas, en las apps (WhatsApp, Facebook, Instagram). Era realmente un *all-in*.

## Contraviento

El lanzamiento fue bueno, pero no extraordinario. Para entonces ya existían alternativas muy fuertes y Llama no conseguía diferenciarse. No podía entender imágenes porque le faltaba un módulo de visión y tambien faltaba mas variedad de tamaños. Intentaron corregirlo con Llama 3.1, 3.2 y 3.3: versiones con visión, versiones diminutas de 1B, y una gigante de 405B. Pero nada terminaba de sorprender. La competencia avanzaba más rápido.

Mientras tanto, FAIR (bajo el mando de Yann LeCun) mantenía su propia agenda. LeCun llevaba tiempo declarando, contra la corriente del resto de la industria, que los LLMs no razonan, que la AGI está lejísimos, que antes de inteligencia humana deberíamos alcanzar la de un perro, y que los LLMs ni a eso llegan. Insistía en que los LLMs no tienen modelo del mundo, que no pueden planificar, que todo debe ocurrir en espacio latente, y que quien busque AGI no debería trabajar en LLMs.  

Y cumplió su palabra: FAIR no publicó ningún LLM. Publicaron DINOv2 (abril 2023), ImageBind (mayo 2023), MusicGen (junio 2023), SAM (julio 2023), MAGNeT, V-JEPA, SAM 2 (agosto 2024)… investigaciones y modelos realmente relevantes, pero lejos de la carrera de los LLMs.

Mientras la comunidad pedía a gritos innovación del lado de Meta, la compañía respondía a GPT-4o solo con prototipos de investigación como Chameleon (para imágenes) o Spirit (para audio) que, aunque interesantes, no estaban dirigidos a usuarios porque su calidad no llegaba a ser útil para ellos. 

En retrospectiva, era evidente que se estaban quedando sin combustible. Pero muchos (entre ellos yo) decidimos confiar en Zuckerberg, quien prometía que **Llama 4** sería no solo el mejor modelo abierto, sino el mejor modelo del mundo. 
Un discurso emocionante, casi heroico, a favor del open source.

Llegó abril del 2025, era hora de pagar todas las promesas que nos hicieron, y fue un **fracaso total**.

Solo dos variantes, ambas MoE relativamente grandes (109B y 409B), y la promesa de una monstruosidad futura llamada *Behemoth*, de 1T de parámetros, que hasta ahora no ha visto la luz, seguramente por la vergüenza de su mal rendimiento. Lo que fue aún peor es que hicieron trampa en la tabla de posiciones de LMarena usando un modelo distinto al publicado, y entrenaron sobre el *test set* para inflar los benchmarks.  
Todo para que, en cuestión de horas, la comunidad descubriera que el modelo era malo. Hoy casi nadie lo usa.  

Exagero un poco… pero el rechazo fue masivo. La reputación quedó por el suelo. Incluso empleados de Meta AI aclaraban en sus CVs que no trabajaron en Llama 4.

## Volvamos a empezar

La situación era pésima. Pero Mark tomó una decisión interesante: **depurar el equipo y comprar uno nuevo**. Entre renuncias, despidos y reubicaciones internas, el tablero quedó vacío. Y Zuckerberg optó por un movimiento radical:

> “Necesito un nuevo equipo de IA… pero no se mucho de IA y tampoco sé ya como formar equipos (perdí el toque del *founder mode*).  
> Mejor compro uno.”

Y empezó el *tour de ofertas*:  
> “Hey, Aravind (fundador de **Perplexity**), véndeme tu startup.” → No.  

> “Hey Mira (fundadora de **Thinking Machine Labs**), vende tu startup.” → No.  

> “Ilya (fundador de **SSI**), ¿quieres vender tu startup?” → No.  

> “Mark Chen (CRO de **OpenAI**), ¿quieres venir a Meta?” → No, ni por mil millones.  

Hasta que finalmente:  
> “Hey, Alexandr (fundador de **Scale AI**), véndeme tu startup. Te doy casi la mitad por 14B.” → Ok.  

Y Alexandr aceptó, ademas Mark le dio el liderazgo del nuevo **Meta Superintelligent Labs**. Porque, claro, para que ir por la inteligencia artificial general, mejor vamos directo a por la superinteligencia.

Al final del dia, Mark no logró comprar un laboratorio de IA (Scale AI es una empresa de datos), por lo tanto debían completar el equipo con investigadores. Y Meta empezó a ofrecer contratos enormes a investigadores de OpenAI, Anthropic, Google DeepMind, Microsoft, Apple, los rumores hablan de más de $100M por cuatro años.

Muchos declinaron. Otros aceptaron.

Mientras tanto, FAIR continuó publicando investigación: V-JEPA 2, DINO v3.

Meta anunció la nueva estructura, con varias divisiones: infraestructura, producto, investigación fundamental, LLMs, todas trabajaban articuladas bajo este nuevo laboratorio, liderado por Alexandr.

¿Podrá Meta volver a competir al nivel de Google? ¿Conseguirán integrar IA de forma efectiva en sus productos? ¿Mantendrán su discurso de open source y open science? ¿Habrá retorno positivo para toda esta inversión gigantesca?

Preguntas que solo podrán responderse en los próximos años.


---

Notas:

1. FAIR si trabajo con LLMs, pero no en animos de entrenar un modelo o una serie de modelos para competir con las empresas de IA. Hicieron análisis desde el punto de vista científico, para entender como funcionan, que componentes son relevantes para determinados comportamientos y sus limitaciones.