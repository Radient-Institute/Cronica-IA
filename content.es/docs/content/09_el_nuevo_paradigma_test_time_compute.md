---
weight: 9
bookFlatSection: true
title: "09 - El Nuevo Paradigma (Test Time Compute)"
image: _din_style/banner_images/09_enpttc.webp
---

# El Nuevo Paradigma (Test Time Compute)

En marzo del 2024 empezaron a aparecer rumores: filtraciones en prensa, posts en Twitter de cuentas anónimas y también vagueposting de researchers en OpenAI. Estos rumores giraban en torno a un supuesto gran descubrimiento interno. Se decía que tenían un modelo que había “redescubierto las matemáticas”, que podría suponer un cambio de paradigma total. Entre los nombres mencionados estaban **Q\*** y, más adelante, **Strawberry**.

Strawberry fue presentado oficialmente en septiembre del 2024 bajo el nombre **O1**, inaugurando una nueva serie de modelos de lenguaje. Eran modelos entrenados con *reinforcement learning* para que, ante una pregunta, generaran primero una secuencia de tokens conocida como *cadena de pensamiento* (*Chain of Thought*, CoT) antes de dar la respuesta final.

El CoT no era nuevo. Incluso antes de ChatGPT ya teníamos papers como *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* o *STAR*, donde se exploraba este truco. Y en la era post-ChatGPT, el chain-of-thought se volvió una técnica de prompting extremadamente popular.

Tampoco era nueva la idea de gastar más cómputo en inferencia. Ya existían propuestas como *Let’s Verify Step by Step* de OpenAI, además de métodos como *ReAct* o *Tree-of-Thoughts*, todos empujando en la misma dirección: exprimir el cómputo en tiempo de inferencia para mejorar el razonamiento.

La verdad es que creer que simplemente escalando el preentrenamiento del Transformer íbamos a obtener respuestas perfectas a problemas complejos era ingenuo. Especialmente cuando esos problemas no aparecen en grandes cantidades dentro del dataset de entrenamiento.  
Ahora había una nueva dimensión para escalar: el cómputo en test time, y de ahí podía extraerse más “inteligencia”.

Sorpresivamente, OpenAI dio acceso a O1 a todos los suscriptores de ChatGPT.

---

Con esta novedad llegaron también nuevos benchmarks diseñados para mostrar sus virtudes, como **AIME 2024** o el ranking de **Codeforces**. OpenAI también ayudó a popularizar otros como **GPQA Diamond**.

Los modelos se entrenaron con una base de cadenas de razonamiento para empujarlos a producir respuestas del tipo: “Primero voy a pensar en esto, luego en esto otro…”. Encima de eso, se aplicó una gran cantidad de RL en algún entorno sintético. Las áreas con verificación fácil —como **código** y **matemáticas**— resultaron especialmente beneficiadas. Los modelos se volvieron más confiables en tareas complejas, especialmente en aquellas que requieren **backtracking**.  
Naturalmente, lo marketearon como que ahora los modelos “piensan y razonan”.

Como era habitual, el OSS se lanzó de cabeza a intentar replicarlo. Destacó el trabajo de GAIR, que documentó toda su travesía, y también el de Qwen, que logró prototipar QwQ muy rápido… aunque todavía inmaduro. En 2024 el RL seguía considerándose un proceso muy inestable y difícil de ejecutar, y en general “no tan efectivo” como se deseaba.

Quienes finalmente darían con una fórmula reproducible aparecerían al año siguiente, desde la nación del centro, y sacudirían la economía global.

---

Con el razonamiento y el RL, OpenAI insinuaba que habían encontrado una técnica de mejora casi ilimitada. Y la siguiente versión no tardó: en diciembre presentaron **O3-preview** (se saltaron un número por temas de marca).

Mientras que **O1-preview** estaba en torno al **percentil 62** en Codeforces, **O3-preview** alcanzaba el puesto **175 global**, es decir, alrededor del **percentil 99**. Incluso una versión especialmente entrenada logró vencer **ARC-AGI**, un benchmark hasta entonces imbatible que intenta medir inteligencia fluida.

O3-preview, tal cual, nunca se lanzó al público. En su lugar llegó **O3** (una versión más pulida y pequeña) junto con **O4 mini**, ambos en abril.  
Ese fue el último modelo de la serie O, al menos de cara al usuario, ya que OpenAI decidió unificar la saga O con su línea principal: GPT.
