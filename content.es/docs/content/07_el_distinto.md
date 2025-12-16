---
weight: 7
bookFlatSection: true
title: "07 - El Distinto"
image: _din_style/banner_images/07_ed.webp
---

# El Distinto

## Una apuesta interesante

“El distinto” vino a darles paz a quienes apostaban a que la IA transformaría por completo el desarrollo de software. El impacto que causó GitHub Copilot no fue trivial, y el paso natural después de la salida de ChatGPT era evidente: construir un editor con IA integrada, un chat al lado capaz de leer y editar tu código y que, incluso si todas sus ediciones eran malas, al menos fuese útil para no tener que abrir el navegador cada vez que querías preguntarle algo a ChatGPT.

Ya desde inicios del 2023 teníamos varias propuestas: Cursor, Codeium, Replit, Continue, etc. Todas refinaban poco a poco sus *prompts*, sus *tools* y sus *workflows* para dejar de ser tan inútiles (sin ofender: realmente en ese entonces los resultados eran malos).

Al año siguiente, otros más ambiciosos redoblaron la apuesta. Confiaban en que los modelos mejorarían tanto que su producto sería un **ingeniero de software autónomo**, nivel junior sí, pero autónomo. Un *agente* capaz de implementar una *feature* pedida en lenguaje natural, refactorizar un archivo y ejecutarlo por sí mismo, ganando cada vez más autonomía.

El primero que salió a asustar a los *devs* apareció en marzo del 2024: **Devin**, de Cognition AI. Para mostrar sus capacidades usaron un *benchmark* poco popular hasta ese entonces: **SWE-bench**, que recoge *issues* reales de GitHub (la mitad provenientes de Django) y evalúa si el modelo puede resolverlos. Devin alcanzaba un 14%, que honestamente era un resultado sorprendente. En agosto salió **Genie**, de Cosine, y llevó la cifra al 30%.

## Llega el núcleo del andamiaje

“El distinto” llegó en junio del 2024. **Sonnet 3.5** apareció como un lobo solitario, porque Anthropic no anunció la serie completa de Claude 3.5: soltó únicamente al hermano del medio.

Y, de forma inmediata, casi como por arte de magia, **toda la infraestructura que estas *startups* habían construido empezó a funcionar**. Las *features* pequeñas pero no triviales se hacían solas, el código compilaba, el *frontend* generado se veía aceptable. La gente lo probaba, se sorprendía y lo compartía, creando un efecto bola de nieve.

En los meses siguientes, el fenómeno se hizo enorme.

## El vibecoding y los agentes de código

En febrero del 2025, Karpathy *senpai* acuñó un término hiperpopular que todo el mundo *tech* terminó escuchando: **vibecoding**. Se refería a una forma de programar donde te dejas llevar por los *vibes*: ignoras el código, solo das instrucciones al LLM; ante errores, simplemente haces *copy/paste* en el chat y dejas que el modelo lo resuelva. Aceptar todo… y funciona.  
Lo describió como algo divertido para proyectos improvisados de fin de semana.

Sin embargo, el término fue sobreexplotado y tergiversado por el *mainstream*, haciendo que muchos le tomaran rechazo porque lo entendían de forma distinta a su significado original.

El éxito de los LLMs en código fue tan grande que empujó a los grandes laboratorios a crear sus propios **agentes de código**, que inicialmente funcionaban desde la línea de comandos (CLI):  
- **claude-code** en febrero del 2025,  
- **codex-cli** de OpenAI en abril,  
- **gemini-cli** en junio.  

OpenAI quiso ir más allá y lanzó Codex en versión web y *cloud* en mayo.

---

## Después del éxito de Anthropic

En cuanto al estado actual de SWE-bench, OpenAI ha afirmado que gran parte de los problemas de ese *benchmark* estaban mal planteados o no contaban con la información suficiente para ser resueltos. Por ello seleccionó un subconjunto de problemas que considera “resolubles” y lo rebautizó como **SWE-bench Verified**, dejando relegada la versión original.  
Los modelos SOTA alcanzan alrededor del 80% en esta nueva (y mucho más fácil) variante a diciembre del 2025.

Anthropic continuaría actualizando sus modelos de forma constante, apostando fuerte por su especialidad: el código. Actualizó Sonnet 3.5 a finales del 2024, lanzó **Sonnet 3.7** (con *CoT*) en febrero del 2025, presentó la serie **Claude 4** en mayo del 2025, y con actualizaciones intermedias, para noviembre del 2025 ya contábamos con la versión **4.5** de Sonnet y Opus.

Anthropic tiene uno de los CEOs más optimistas sobre la IA. Ha hecho declaraciones como: “Para 2025, más del 80% del código será generado por IA”, o “La AGI podría llegar en dos años” (refiriéndose al 2026 cuando lo dijo). La empresa, además, suele destacar en cada lanzamiento la supuesta capacidad de sus modelos para “trabajar en un problema durante varias horas de forma continua”.

Hay una base sólida de fans que defiende los modelos de Anthropic a capa y espada. No tendrán SOTA en todos los *benchmarks*, pero para código la gente los sigue prefiriendo. Dicen que tienen algo especial. Algo distinto.

---

Su valuación actual es de **173 mil millones de dólares**, y es la competencia más fuerte de OpenAI sin contar a las grandes corporaciones.
