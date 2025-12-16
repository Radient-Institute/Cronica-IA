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

Al igual que todas las empresas estadounidenses (y algunas europeas), los laboratorios chinos también se sumaron a [la captura de GPT-4]({{< relref "02_la_captura_de_gpt_4.md" >}}). Para finales del 2023 ya había dos figuras especialmente relevantes: Qwen y DeepSeek.

{{% details title="Lanzamientos Chinos 2023" open=false %}}
- **Qwen**, con Tongyi Qianwen, Qwen VL y Qwen 1.5 (agosto, septiembre y diciembre).
- **DeepSeek**, con DeepSeek Coder y DeepSeek LLM (noviembre).
{{% /details %}}

Ambas mostraban un 2024 prometedor. Y efectivamente lo fue.

DeepSeek lanzó en abril **DeepSeek Math**, un modelo excelente en matemáticas cuyo paper introducía una técnica de *policy gradient* que cobraría importancia más adelante: **GRPO**. Para julio sacaron una actualización de su modelo **DeepSeek V2**, que lo posicionó como el mejor modelo OSS del mundo según **LMarena**, un benchmark basado en preferencias humanas que compara respuestas de diferentes modelos lado a lado para armar un ranking de Elo.

Sí, China ya tenía el mejor modelo open source del planeta a mediados de 2024, medio año antes de que Occidente siquiera procesara la idea de que los laboratorios chinos podían competir al máximo nivel.

Por su parte, Qwen anunció en septiembre su serie **Qwen 2.5**, cuyos resultados en benchmarks tradicionales eran tan altos que muchos laboratorios evitaban incluirlos en sus tablas comparativas para evitar verse inferiores.

Muchos conocieron a DeepSeek recién en diciembre, cuando lanzaron **DeepSeek V3**. La ballena no podía fallar, su iteración anterior había sido el mejor modelo abierto y esta vez no fue diferente. V3 arrasaba con todas las alternativas… aunque a un costo alto: era un **MoE de 675B parámetros** en total, OSS sí, pero sin versiones destiladas más pequeñas. En todo caso, siempre hay formas de probar los modelos gratis, así que no era un gran problema.

La fiebre por los modelos de razonamiento estaba en auge, pero este lanzamiento quedó relativamente contenido dentro del círculo de obsesos por la IA porque DeepSeek V3 era un modelo instruct, no un modelo orientado al razonamiento.

En su paper incluyeron un dato que sorprendió a la comunidad: el entrenamiento del *checkpoint* requirió 2.82 millones de horas de H800, equivalentes a unos **5 millones de dólares**. Que mencionaran explícitamente esa cifra sería, curiosamente, la chispa del colapso bursátil del mes siguiente.

---

## El shock de Occidente

En enero llegó el terremoto: **DeepSeek R1**, un modelo de “razonamiento” basado en V3, entrenado con RL usando **GRPO**, destilado a variantes de todos los tamaños y totalmente abierto. Rivalizaba directamente con **O1 de OpenAI**.  
Era, literalmente, el primer modelo que se acercaba o igualaba a OpenAI en el nuevo paradigma… era **chino** y **open source**.

Cabe mencionar que, aunque OpenAI había anunciado O3 en diciembre, como ya era costumbre, tardó en dar acceso al público. Así que en la práctica O1 era el único modelo razonador disponible para comparar.

No creo que nadie esperara que el lanzamiento de DeepSeek R1 tuviera la propagación que tuvo. Mi hermana, mi padre y mi madre sabían de DeepSeek. Según la prensa, los diarios y los noticieros, los chinos habían replicado “la tecnología más poderosa de Occidente” (supuestamente de cientos de millones de dólares), en unos meses, la habían puesto gratis en *chat.deepseek.ai*, y "solo había costado 5 millones". Efectivamente, los empleados no cobran sueldo, los experimentos no cuestan dinero y los esfuerzos desde el 2023 simplemente no existieron; la historia perfecta para vender: un chino de un fondo de inversión con 5 millones y unos meses de trabajo “hundió” a OpenAI.

Ese fue el relato que encendió el caos. Según esta visión, la gran mentira de la IA se derrumbaba: ¿qué valor tiene NVIDIA si “solo hacen falta 2 000 chips”? Los inversores castigaron la acción. El mercado colapsó. Y luego, como siempre, corrigió y siguió subiendo. Una fluctuación más de toda la vida.

---

Más allá de todas las malas lecturas que se hicieron de la situación, una cosa quedó clara: **China ya estaba en el mapa, empujando la frontera a su modo.** Porque ningún país o empresa tiene el monopolio de las grandes ideas.
