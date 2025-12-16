---
weight: 23
bookFlatSection: true
title: "23 - Temas Calientes de Investigacion"
image: _din_style/banner_images/23_tcdi.webp
---

# Temas Calientes de Investigación

Los modelos de lenguaje cambiaron por completo el campo de la IA. Aunque algunos detractores los catalogan como un *dead end* o un callejón sin salida, la realidad es simple: mientras no aparezca una alternativa superior, van a seguir con nosotros. Son el tema central de la época, y como era de esperarse, hay muchísima inversión enfocada en resolver sus limitaciones actuales.



## La ventana de contexto

El mecanismo de atención escala cuadráticamente con el número de *tokens* de la secuencia, lo que hace que ventanas de contexto enormes sigan siendo inviables. Esto ha mejorado muchísimo en los últimos años, pasando de 8k en 2023 a un mínimo de 256k en 2025, con algunos destacados como Google quien tiene 1M. Sin embargo, ingenieros del sector aseguran que con las técnicas actuales podríamos llegar a los 10M. Pero para alcanzar 100M necesitaremos un descubrimiento nuevo.

De este problema nace una línea de investigación muy activa: buscar alternativas a la atención tradicional. Casi todas las propuestas siguen la misma intuición: partir la secuencia, procesarla por secciones y mantener un estado. Así aparecieron Hyena, RMKV, los *State Space Models*, Mamba, Titans y otros. Algunos de ellos permiten procesar secuencias indefinidamente gracias a este estado recurrente.

El inconveniente es que, seamos honestos, modelar lenguaje con cualquiera de estos algoritmos sigue siendo peor que con la vieja y confiable atención… que, por cierto, ya ha mutado en decenas de variantes: *multi-head latent attention*, *grouped-query attention*, *sparse attention*, entre muchas otras.

Esto nos deja con los llamados **modelos híbridos**, que intercalan bloques con atención lineal y bloques tradicionales. Se sacrifica algo de rendimiento, pero se gana escalabilidad.

Otro punto crítico, más allá del tamaño de la ventana, es qué tan bien usa el modelo ese contexto. En 2024 apareció una startup llamada Magic.dev que afirmaba tener un modelo con 100M de contexto: **LTM2-mini**. Desde entonces desaparecieron casi por completo… pero anunciaron una ronda de inversión de medio billón, lo cual deja claro el apetito del mercado: si descubres cómo entrenar modelos con ventanas descomunales, tienes una startup valuada en cientos de millones instantáneamente.


## Modelos de difusión para lenguaje

Una de las críticas más fuertes a los LLMs es su naturaleza autoregresiva: generan un *token* a la vez y, una vez escrito, no puede cambiarse. Esto, junto con la aleatoriedad del muestreo, puede causar errores que se propagan. Claro, el modelo puede generar más texto para corregirlos, pero no es lo óptimo.

Ante esto, los investigadores decidieron intentar **modelos de lenguaje dentro del marco de difusión**. Es decir, que la respuesta no nazca de forma secuencial, sino desde ruido, y que el modelo vaya refinando simultáneamente todas las partes del texto. Primero un boceto, luego un refinamiento progresivo. Suena más cercano a cómo pensamos los humanos… y además es muchísimo más rápido: para generar 1024 *tokens* ya no necesitas 1024 pasos, sino unas pocas decenas.

¿El problema?  
Que aún están muy por detrás de los LLMs tradicionales: entre dos y tres generaciones, dependiendo de a quién preguntes. Funcionan, sí, pero usarlos se siente como viajar dos años al pasado en calidad y cinco al futuro en velocidad.

El primer modelo decente de este tipo apareció en febrero del 2025: **LlaDA**, un 8B *open source*. Unos días después, la startup Inception Labs lanzó acceso privado a su modelo propietario **MercuryCoder**. Y el único laboratorio frontera que mostró resultados con esta variante fue Google, que en abril publicó *benchmarks* de su **Gemini Diffusion**, aún privado pero supuestamente comparable a Gemini 1.5 Flash.


## Cambiar el tokenizer

Otro punto de frustración entre investigadores es el tokenizer: la forma en que se representa el texto antes de entrar al modelo. Siempre hay un *trade-off* entre tamaño del vocabulario y longitud de la secuencia.

Las propuestas abundan:

- entrenar directamente sobre bits,  
- usar tokenizadores dinámicos,  
- tokenizar en UTF-8,  

pero de momento ninguna alternativa ha sido probada y validada a escala comercial.

## Continual learning

En octubre del 2025, Karpathy soltó una de sus frases memorables:  

> “No estamos construyendo animales; estamos invocando espíritus.”

Se refería a una de las limitaciones más criticadas de los LLMs: **no aprenden de manera continua**.

Mientras el chat está activo, todo fluye. Pero abrir una conversación nueva es empezar desde cero otra vez. Existen paliativos, como bases vectoriales o documentos que sirvan de memoria episódica, pero el aprendizaje continuo real sigue siendo un santo grial del campo.

## Modelos de energía

Saliéndonos del paradigma actual, están los **modelos de energía**, popularizados por Hinton y LeCun. A diferencia de los modelos probabilísticos, estos aprenden una función que mide la afinidad entre un dato *x* y un dato *y*:  

> energía baja = compatibles,  
> energía alta = incompatibles.

Generar una respuesta *y* para una pregunta *x* consiste simplemente en navegar ese *mapa de energía* con descenso de gradiente hasta encontrar un punto de baja energía. El concepto es elegante, pero construir modelos frontera con este enfoque todavía es un desafío abierto.

## Modelos del mundo

¿Qué es un “modelo del mundo”? Curiosamente, hace unos meses esta pregunta se volvió un meme en Twitter. Es una noción que parece intuitiva, pero cuesta verbalizarla.

Tomemos la definición de Schmidhuber:  
un modelo del mundo es **la representación mental que construimos del entorno a partir de lo que percibimos**, una simplificación del sistema real basada en conceptos y relaciones seleccionadas.

{{< image src="general_assets/world_model_comic.jpeg" alt="Modelo del mundo" title="Modelo del mundo" loading="lazy" class="img-small img-center" >}}

La pregunta es: *¿cómo construirlo en IA?*

Algunos creen que emerge automáticamente en los LLMs. Otros apuestan por generadores de vídeo condicionados, como la serie **Genie**. Otros buscan obtenerlo mediante aprendizaje autosupervisado en imágenes y vídeos, como Yan LeCun con las **JEPAs**, o Fei-Fei Li con sus modelos 3D.

Quizás, solo quizás, los modelos del mundo fueron los amigos que hicimos en el camino. 🙂

---

Ilya Sutskever en una charla en la NeurIPS 2024 dijo que **la era del escalado del preentrenamiento había llegado a su fin**. Lo comparó con los combustibles fósiles: extremadamente útiles, pero ya agotados.

Mostró una gráfica del volumen cerebral de los mamíferos en función del tamaño del cuerpo. Durante millones de años siguió una ley de escala… hasta que aparecieron los homínidos, cuya relación rompió la tendencia con una pendiente mucho más agresiva.

La naturaleza encontró una nueva manera de escalar en nosotros mismos. Nosotros también debemos encontrarla.

Y en octubre del 2025, Ilya publicó un tuit diciendo que era “el mejor día de su vida”. ¿Habrá encontrado algo realmente revolucionario?
