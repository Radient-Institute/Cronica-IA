---
weight: 9
bookFlatSection: true
title: "09 - El Nuevo Paradigma (Test Time Compute)"
image: _din_style/banner_images/09_enpttc.webp
---

# El Nuevo Paradigma (Test Time Compute)

A finales del 2023 empezaron a aparecer rumores: filtraciones en prensa, posts en Twitter de cuentas anónimas y también vagueposting de researchers en OpenAI. Estos rumores giraban en torno a un supuesto gran descubrimiento interno. Se decía que tenían un modelo que había “redescubierto las matemáticas”, que podría suponer un cambio de paradigma total. Entre los nombres mencionados estaban **Q\***[^1] y, más adelante, en julio **Strawberry**.[^2]

Strawberry fue presentado oficialmente en septiembre del 2024 bajo el nombre **O1**, inaugurando una nueva serie de modelos de lenguaje.[^3] Eran modelos entrenados con *reinforcement learning* para que, ante una pregunta, generaran primero una secuencia de tokens conocida como *cadena de pensamiento* (*Chain of Thought*, CoT) antes de dar la respuesta final.[^3]

El CoT no era nuevo. Incluso antes de ChatGPT ya teníamos papers como *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*[^4] o *STAR*,[^5] donde se exploraba este truco. Y en la era post-ChatGPT, el chain-of-thought se volvió una técnica de prompting extremadamente popular.

Tampoco era nueva la idea de gastar más cómputo en inferencia. Ya existían propuestas como *Let’s Verify Step by Step* de OpenAI,[^6] además de métodos como *ReAct*[^7] o *Tree-of-Thoughts*,[^8] todos empujando en la misma dirección: exprimir el cómputo en tiempo de inferencia para mejorar el razonamiento.

La verdad es que creer que simplemente escalando el preentrenamiento del Transformer íbamos a obtener respuestas perfectas a problemas complejos era ingenuo. Especialmente cuando esos problemas no aparecen en grandes cantidades dentro del dataset de entrenamiento.\
Ahora había una nueva dimensión para escalar: el cómputo en test time, y de ahí podía extraerse más “inteligencia”.[^3]

Sorpresivamente, OpenAI dio acceso a O1 a todos los suscriptores de ChatGPT.[^3]

---

Con esta novedad llegaron también nuevos benchmarks, que no fueron diseñados para evaluar modelos de IA, pero que ahora servían para mostrar sus virtudes, como **AIME 2024** o el ranking de **Codeforces**.[^3] OpenAI también ayudó a popularizar otros como **GPQA Diamond**.[^9]

Los modelos se entrenaron con una base de cadenas de razonamiento para empujarlos a producir respuestas del tipo: “Primero voy a pensar en esto, luego en esto otro…”.[^3] Encima de eso, se aplicó una gran cantidad de RL en algún conjunto de entornos sintéticos. Las áreas con verificación fácil (como **código** y **matemáticas**) resultaron especialmente beneficiadas. Los modelos se volvieron más confiables en tareas complejas, especialmente en aquellas que requieren **backtracking**.[^3]\
Naturalmente, lo marketearon bajo la consigna de que ahora los modelos “piensan y razonan”.

Como era habitual, el OSS se lanzó de cabeza a intentar replicarlo. Destacó el trabajo de GAIR, que documentó toda su travesía,[^10] y también el de Qwen, que logró prototipar QwQ muy rápido… aunque todavía inmaduro.[^11] En 2024 el RL seguía considerándose un proceso muy inestable y difícil de ejecutar, y en general “no tan efectivo” como se deseaba.

Quienes finalmente darían con una fórmula reproducible aparecerían al año siguiente, desde la nación del centro, y sacudirían la economía global.

---

Con el razonamiento y el RL, OpenAI insinuaba que habían encontrado una técnica de mejora casi ilimitada. Y la siguiente versión no tardó: en diciembre presentaron **O3-preview** (se saltaron un número por temas de marca).[^12]

Mientras que **O1-preview** estaba en torno al **percentil 62** en Codeforces,[^13] **O3-preview** alcanzaba el puesto **175 global**, es decir, alrededor del **percentil 99.8**.[^12] Incluso una versión especialmente entrenada logró vencer **ARC-AGI**, un benchmark hasta entonces imbatible que intentaba medir inteligencia fluida.[^14]

O3-preview, tal cual, nunca se lanzó al público.[^14] En su lugar llegó **O3** (una versión más pulida y pequeña) junto con **O4 mini**, ambos en abril.[^15]\
Ese fue el último modelo de la serie O, al menos de cara al usuario, ya que OpenAI decidió unificar la saga O con su línea principal: GPT.[^15]

## Referencias

[^1]: Reuters. ["OpenAI researchers warned board of AI breakthrough ahead of CEO ouster, sources say"](https://www.reuters.com/technology/openai-researchers-warned-board-ai-breakthrough-ahead-ceo-ouster-sources-2023-11-22/). 22 de noviembre de 2023.

[^2]: Reuters. ["OpenAI working on new reasoning technology under code name 'Strawberry'"](https://www.reuters.com/technology/artificial-intelligence/openai-working-new-reasoning-technology-under-code-name-strawberry-2024-07-12/). 12 de julio de 2024.

[^3]: OpenAI. ["Learning to reason with LLMs"](https://openai.com/index/learning-to-reason-with-llms/). 12 de septiembre de 2024. OpenAI presentó o1-preview.

[^4]: Wei, Jason et al. ["Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"](https://arxiv.org/abs/2201.11903). 28 de enero de 2022.

[^5]: Zelikman, Eric et al. ["STaR: Bootstrapping Reasoning With Reasoning"](https://arxiv.org/abs/2203.14465). 28 de marzo de 2022.

[^6]: Lightman, Hunter et al. ["Let's Verify Step by Step"](https://arxiv.org/abs/2305.20050). 31 de mayo de 2023.

[^7]: Yao, Shunyu et al. ["ReAct: Synergizing Reasoning and Acting in Language Models"](https://arxiv.org/abs/2210.03629). 6 de octubre de 2022.

[^8]: Yao, Shunyu et al. ["Tree of Thoughts: Deliberate Problem Solving with Large Language Models"](https://arxiv.org/abs/2305.10601). 17 de mayo de 2023.

[^9]: Rein, David et al. ["GPQA: A Graduate-Level Google-Proof Q&A Benchmark"](https://arxiv.org/abs/2311.12022). 20 de noviembre de 2023.

[^10]: GAIR-NLP. ["O1 Replication Journey"](https://github.com/GAIR-NLP/O1-Journey). Octubre de 2024.

[^11]: Qwen Team. ["QwQ: Reflect Deeply on the Boundaries of the Unknown"](https://qwenlm.github.io/blog/qwq-32b-preview/). 28 de noviembre de 2024. Qwen presentó QwQ-32B-Preview como un modelo experimental de razonamiento.

[^12]: OpenAI. ["12 Days of OpenAI — Day 12: o3 preview & call for safety researchers"](https://openai.com/12-days/?day=12). 20 de diciembre de 2024. OpenAI presentó o3 y o3-mini sin lanzarlos al público.

[^13]: OpenAI. ["Learning to reason with LLMs"](https://openai.com/index/learning-to-reason-with-llms/). 12 de septiembre de 2024. o1-preview obtuvo un rating de 1258 en Codeforces, aproximadamente el percentil 62.

[^14]: Chollet, François. ["OpenAI o3 Breakthrough High Score on ARC-AGI-Pub"](https://arcprize.org/blog/oai-o3-pub-breakthrough). ARC Prize. 20 de diciembre de 2024. El o3 evaluado había sido entrenado sobre parte del conjunto público de entrenamiento de ARC-AGI-1 y obtuvo 75,7% con menor cómputo y 87,5% usando aproximadamente 172 veces más.

[^15]: OpenAI. ["Introducing OpenAI o3 and o4-mini"](https://openai.com/index/introducing-o3-and-o4-mini/). 16 de abril de 2025. OpenAI lanzó o3 y o4-mini y declaró que estaba convergiendo las capacidades especializadas de razonamiento de la serie O con las capacidades conversacionales de la serie GPT.
