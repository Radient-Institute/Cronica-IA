---
weight: 10
bookFlatSection: true
title: "10 - La Ballena"
image: _din_style/banner_images/10_lb.webp
---

# La Ballena

## La posición de China previo a DeepSeek R1

El estigma occidental de que China “solo copia” y no es capaz de crear tecnología propia llevó a algunos a imaginar espías del CCP infiltrados en grandes laboratorios de IA robando secretos. Pero la realidad es otra: China nunca estuvo fuera del radar en la última década.

Tiene universidades potentes, profesionales potentes, suficiente capital y, aunque las restricciones de chips de NVIDIA dificultan (sin llegar a bloquear) el acceso al cómputo, aun así encontraban caminos para avanzar.

Al igual que todas las empresas estadounidenses (y algunas europeas), los laboratorios chinos también se sumaron a [la captura de GPT-4]\({{< relref "02\_la\_captura\_de\_gpt\_4.md" >}}). Para finales del 2023 ya había dos figuras especialmente relevantes: Qwen y DeepSeek.

{{% details title="Lanzamientos Chinos 2023" open=false %}}

- **Qwen**, con Tongyi Qianwen (abril),[^1] Qwen-7B/Qwen-VL (agosto),[^2][^3] Qwen-14B (septiembre)[^4] y Qwen-72B/Qwen-1.8B (noviembre).[^5]
- **DeepSeek**, con DeepSeek Coder[^6] y DeepSeek LLM[^7] (noviembre).
  {{% /details %}}

Ambas mostraban un 2024 prometedor. Y efectivamente lo fue.

DeepSeek lanzó en febrero **DeepSeek Math**, un modelo excelente en matemáticas cuyo paper introducía una técnica de *policy gradient* que cobraría importancia más adelante: **GRPO**.[^8] Para julio sacaron una actualización de su modelo **DeepSeek V2**, que lo posicionó como el mejor modelo OSS del mundo según **LMSYS** (ahora conocido como LMArena), un benchmark basado en preferencias humanas que compara respuestas de diferentes modelos lado a lado para armar un ranking de Elo.[^9]

Sí, China ya tenía el mejor modelo open source del planeta a mediados de 2024, medio año antes de que Occidente siquiera procesara la idea de que los laboratorios chinos podían competir al máximo nivel.

Por su parte, Qwen anunció en septiembre su serie **Qwen 2.5**,[^10] cuyos resultados en benchmarks tradicionales eran tan altos que muchos laboratorios evitaban incluirlos en sus tablas comparativas para evitar verse inferiores.

Muchos conocieron a DeepSeek recién en diciembre, cuando lanzaron **DeepSeek V3**.[^11] La ballena no podía fallar, su iteración anterior había sido el mejor modelo abierto y esta vez no fue diferente. V3 arrasaba con todas las alternativas… aunque a un costo alto: era un **MoE de 671B parámetros** en total,[^12] OSS sí, pero sin versiones destiladas más pequeñas. En todo caso, siempre hay formas de probar los modelos gratis, así que no era un gran problema.

La fiebre por los modelos de razonamiento estaba en auge, pero este lanzamiento quedó relativamente contenido dentro del círculo de obsesos por la IA porque DeepSeek V3 era un modelo instruct, no un modelo orientado al razonamiento.

En su paper incluyeron un dato que sorprendió a la comunidad: el entrenamiento del *checkpoint* requirió 2.788 millones de horas de H800, equivalentes a unos **5 millones de dólares**.[^12] Que mencionaran explícitamente esa cifra sería, curiosamente, la chispa del colapso bursátil del mes siguiente.

---

## El shock de Occidente

En enero llegó el terremoto: **DeepSeek R1**,[^13] un modelo de “razonamiento” basado en V3, entrenado con RL usando **GRPO**, destilado a variantes de todos los tamaños y totalmente abierto.[^14] Rivalizaba directamente con **O1 de OpenAI**.[^14]\
Era, literalmente, el primer modelo que se acercaba o igualaba a OpenAI en el nuevo paradigma… era **chino** y **open source**.

Cabe mencionar que, aunque OpenAI había anunciado O3 en diciembre,[^15] como ya era costumbre, tardó en dar acceso al público.[^16] Así que en la práctica O1 era el único modelo razonador disponible para comparar.

No creo que nadie esperara que el lanzamiento de DeepSeek R1 tuviera la propagación que tuvo. Mi hermana, mi padre y mi madre sabían de DeepSeek. Según la prensa, los diarios y los noticieros, los chinos habían replicado “la tecnología más poderosa de Occidente” (supuestamente de cientos de millones de dólares), en unos meses, la habían puesto gratis en *chat.deepseek.ai*, y "solo había costado 5 millones".[^12][^17] Efectivamente, los empleados no cobran sueldo, los experimentos no cuestan dinero y los esfuerzos desde el 2023 simplemente no existieron; la historia perfecta para vender: un chino de un fondo de inversión con 5 millones y unos meses de trabajo “hundió” a OpenAI.

Ese fue el relato que encendió el caos. Según esta visión, la gran mentira de la IA se derrumbaba: ¿qué valor tiene NVIDIA si “solo hacen falta 2 000 chips”?[^12][^18] Los inversores castigaron la acción. El mercado colapsó.[^17] Y luego, como siempre, corrigió y siguió subiendo. Una fluctuación más de toda la vida.

---

Más allá de todas las malas lecturas que se hicieron de la situación, una cosa quedó clara: **China ya estaba en el mapa, empujando la frontera a su modo.** Porque ningún país o empresa tiene el monopolio de las grandes ideas.

## Referencias

[^1]: Alibaba Cloud. ["Alibaba Cloud Unveils New AI Model to Support Enterprises’ Intelligence Transformation"](https://home.alibabagroup.com/en-US/document-1582482069362049024). 11 de abril de 2023.

[^2]: Qwen Team. ["Qwen"](https://github.com/QwenLM/Qwen). 3 de agosto de 2023. Lanzamiento de Qwen-7B y Qwen-7B-Chat.

[^3]: Qwen Team. ["Qwen-VL"](https://github.com/QwenLM/Qwen-VL). 22 de agosto de 2023.

[^4]: Qwen Team. ["Qwen"](https://github.com/QwenLM/Qwen). 25 de septiembre de 2023. Lanzamiento de Qwen-14B y Qwen-14B-Chat.

[^5]: Qwen Team. ["Qwen"](https://github.com/QwenLM/Qwen). 30 de noviembre de 2023. Lanzamiento de Qwen-72B/Qwen-72B-Chat y Qwen-1.8B/Qwen-1.8B-Chat.

[^6]: DeepSeek. ["DeepSeek Coder"](https://github.com/deepseek-ai/DeepSeek-Coder). 2 de noviembre de 2023.

[^7]: DeepSeek. ["DeepSeek LLM"](https://github.com/deepseek-ai/DeepSeek-LLM). 29 de noviembre de 2023.

[^8]: Shao, Zhihong et al. ["DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"](https://arxiv.org/abs/2402.03300). 5 de febrero de 2024.

[^9]: DeepSeek. ["DeepSeek-V2-Chat-0628"](https://huggingface.co/deepseek-ai/DeepSeek-V2-Chat-0628). Julio de 2024. Alcanzó el puesto #11 global y #1 entre modelos open source en LMSYS Chatbot Arena.

[^10]: Qwen Team. ["Qwen2.5: A Party of Foundation Models!"](https://qwenlm.github.io/blog/qwen2.5/). 19 de septiembre de 2024.

[^11]: DeepSeek. ["DeepSeek-V3"](https://github.com/deepseek-ai/DeepSeek-V3). 26 de diciembre de 2024.

[^12]: DeepSeek-AI et al. ["DeepSeek-V3 Technical Report"](https://arxiv.org/abs/2412.19437). 27 de diciembre de 2024. El coste reportado de US$5,576 millones corresponde al cómputo del entrenamiento contabilizado del checkpoint, no al coste total de investigación y desarrollo.

[^13]: DeepSeek. ["DeepSeek-R1"](https://github.com/deepseek-ai/DeepSeek-R1). 20 de enero de 2025.

[^14]: Guo, Daya et al. ["DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"](https://arxiv.org/abs/2501.12948). 22 de enero de 2025.

[^15]: OpenAI. ["12 Days of OpenAI — Day 12: o3 preview & call for safety researchers"](https://openai.com/12-days/?day=12). 20 de diciembre de 2024.

[^16]: OpenAI. ["Introducing OpenAI o3 and o4-mini"](https://openai.com/index/introducing-o3-and-o4-mini/). 16 de abril de 2025.

[^17]: Reuters. ["DeepSeek sets off global tech selloff, Nvidia sheds nearly $600 billion"](https://www.reuters.com/technology/chinas-deepseek-sets-off-ai-market-rout-2025-01-27/). 27 de enero de 2025.

[^18]: Reuters. ["Nvidia says DeepSeek advances prove need for more of its chips"](https://www.reuters.com/technology/nvidia-says-deepseek-advances-prove-need-more-its-chips-2025-01-27/). 27 de enero de 2025.
