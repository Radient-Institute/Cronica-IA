---
weight: 7
bookFlatSection: true
title: "07 - El Distinto"
image: _din_style/banner_images/07_ed.webp
---


# El Distinto

## Una apuesta interesante

“El distinto” vino a darles paz a quienes apostaban a que la IA transformaría por completo el desarrollo de software. El impacto que causó GitHub Copilot no fue trivial, y el paso natural después de la salida de ChatGPT era evidente: construir un editor con IA integrada, un chat al lado capaz de leer y editar tu código y que, incluso si todas sus ediciones eran malas, al menos fuese útil para no tener que abrir el navegador cada vez que querías preguntarle algo a ChatGPT.

Ya desde inicios del 2023 teníamos varias propuestas: Cursor, Codeium, Replit, Continue, etc.[^1][^2] Todas refinaban poco a poco sus *prompts*, sus *tools* y sus *workflows* para dejar de ser tan inútiles (sin ofender: realmente en ese entonces los resultados eran malos).

Al año siguiente, otros más ambiciosos redoblaron la apuesta. Confiaban en que los modelos mejorarían tanto que su producto sería un **ingeniero de software autónomo**, nivel junior sí, pero autónomo. Un *agente* capaz de implementar una *feature* pedida en lenguaje natural, refactorizar un archivo y ejecutarlo por sí mismo, ganando cada vez más autonomía.

El primero que salió a asustar a los *devs* apareció en marzo del 2024: **Devin**, de Cognition AI.[^4] Para mostrar sus capacidades usaron un *benchmark* poco popular hasta ese entonces: **SWE-bench**, que recoge *issues* reales de GitHub (más de un tercio provenientes de Django) y evalúa si el modelo puede resolverlos.[^3] Devin alcanzaba un 14%, que honestamente era un resultado sorprendente.[^4] En agosto salió **Genie**, de Cosine, y llevó la cifra al 30%.[^5]

## Llega el núcleo del andamiaje

“El distinto” llegó en junio del 2024. **Sonnet 3.5** apareció como un lobo solitario, porque Anthropic no anunció la serie completa de Claude 3.5: soltó únicamente al hermano del medio.[^6]

Y, de forma inmediata, casi como por arte de magia, **toda la infraestructura que estas *startups* habían construido empezó a funcionar**. Las *features* pequeñas pero no triviales se hacían solas, el código compilaba, el *frontend* generado se veía aceptable. La gente lo probaba, se sorprendía y lo compartía, creando un efecto bola de nieve.

En los meses siguientes, el fenómeno se hizo enorme.

## El vibecoding y los agentes de código

En febrero del 2025, Karpathy *senpai* acuñó un término hiperpopular que todo el mundo *tech* terminó escuchando: **vibecoding**.[^7] Se refería a una forma de programar donde te dejas llevar por los *vibes*: ignoras el código, solo das instrucciones al LLM; ante errores, simplemente haces *copy/paste* en el chat y dejas que el modelo lo resuelva. Aceptar todo… y funciona.\
Lo describió como algo divertido para proyectos improvisados de fin de semana.[^7]

Sin embargo, el término fue sobreexplotado y tergiversado por el *mainstream*, haciendo que muchos le tomaran rechazo porque lo entendían de forma distinta a su significado original.

El éxito de los LLMs en código fue tan grande que empujó a los grandes laboratorios a crear sus propios **agentes de código**, que inicialmente funcionaban desde la línea de comandos (CLI):

- **claude-code** en febrero del 2025,[^8]
- **codex-cli** de OpenAI en abril,[^9]
- **gemini-cli** en junio.[^10]

OpenAI quiso ir más allá y lanzó Codex en versión web y *cloud* en mayo.[^11]

---

## Después del éxito de Anthropic

En cuanto al estado actual de SWE-bench, OpenAI ha afirmado que gran parte de los problemas de ese *benchmark* estaban mal planteados o no contaban con la información suficiente para ser resueltos. Por ello seleccionó un subconjunto de problemas que considera “resolubles” y lo rebautizó como **SWE-bench Verified**, dejando relegada la versión original.[^12]\
Los modelos SOTA alcanzan alrededor del 80% en esta nueva (y mucho más resoluble) variante a diciembre del 2025.[^13]

Anthropic continuaría actualizando sus modelos de forma constante, apostando fuerte por su especialidad: el código. Actualizó Sonnet 3.5 a finales del 2024,[^14] lanzó **Sonnet 3.7** (con *CoT*) en febrero del 2025,[^8] presentó la serie **Claude 4** en mayo del 2025,[^15] y con actualizaciones intermedias, para noviembre del 2025 ya contábamos con la versión **4.5** de Sonnet y Opus.[^16][^17]

Anthropic contaba con uno de los CEOs más optimistas sobre la velocidad de desarrollo de la IA. Ha hecho declaraciones como que: para finales 2025, más del 90% del código será generado por IA,[^18] o la AGI podría llegar el 2026 o 2027.[^19] La empresa, además, a menudo solía destacar en cada lanzamiento la supuesta capacidad de sus modelos para “trabajar en un problema durante varias horas de forma continua”.[^15]

Durante estos dos años de despegue, construyeron una base sólida de fans que defiende los modelos de Anthropic a capa y espada. A pesar de no ser SOTA en todos los *benchmarks*, para temas de código la gente los seguía prefiriendo ampliamente. Decían que tienen algo especial. Algo distinto.

---

Cerraron el 2025 con una valuación actual de **183 mil millones de dólares**,[^20] y catalogados como la competencia más fuerte de OpenAI sin contar a las grandes corporaciones.

## Referencias

[^1]: Cursor. ["Introducing Cursor 0.2.0!"](https://cursor.com/changelog/0-2-0). 6 de abril de 2023.

[^2]: Replit. ["Announcing Ghostwriter Chat: The first conversational AI programmer"](https://replit.com/blog/gw-chat-launch). 14 de febrero de 2023.

[^3]: Jimenez, Carlos E. et al. ["SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"](https://openreview.net/forum?id=VTF8yNQM66). ICLR 2024. El conjunto original contiene 2.294 tareas de 12 repositorios; 850 provienen de Django, aproximadamente el 37%.

[^4]: Cognition. ["Introducing Devin, the first AI software engineer"](https://cognition.com/blog/introducing-devin). 12 de marzo de 2024. Cognition reportó un 13,86% en SWE-bench.

[^5]: Pullen, Alistair / Cosine. ["Genie"](https://www.linkedin.com/posts/alistair-pullen-616129226_im-excited-to-share-that-weve-built-the-activity-7228747100056924163-w2sR). 12 de agosto de 2024. Cosine reportó un 30,08% en SWE-bench.

[^6]: Anthropic. ["Claude 3.5 Sonnet"](https://www.anthropic.com/news/claude-3-5-sonnet). 21 de junio de 2024. Anthropic lo presentó como la primera publicación de la futura familia Claude 3.5.

[^7]: Karpathy, Andrej. ["There's a new kind of coding I call 'vibe coding'"](https://x.com/karpathy/status/1886192184808149383). 2 de febrero de 2025.

[^8]: Anthropic. ["Claude 3.7 Sonnet and Claude Code"](https://www.anthropic.com/news/claude-3-7-sonnet). 24 de febrero de 2025.

[^9]: OpenAI. ["This week's launches: o3, o4-mini, GPT-4.1, and Codex CLI"](https://community.openai.com/t/this-weeks-launches-o3-o4-mini-gpt-4-1-and-codex-cli/1230312). 17 de abril de 2025.

[^10]: Google. ["Gemini CLI: your open-source AI agent"](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-open-source-ai-agent/). 25 de junio de 2025.

[^11]: OpenAI. ["Introducing Codex"](https://openai.com/index/introducing-codex/). 16 de mayo de 2025.

[^12]: Chowdhury, Neil et al. ["Introducing SWE-bench Verified"](https://openai.com/index/introducing-swe-bench-verified/). 2024. El subconjunto contiene 500 problemas revisados por desarrolladores humanos y considerados resolubles.

[^13]: SWE-bench. ["Official Leaderboards"](https://www.swebench.com/). Diciembre de 2025. Claude Opus 4.5 alcanzó 79,2% en SWE-bench Verified el 5 y el 15 de diciembre.

[^14]: Anthropic. ["Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku"](https://www.anthropic.com/news/3-5-models-and-computer-use). 22 de octubre de 2024.

[^15]: Anthropic. ["Introducing Claude 4"](https://www.anthropic.com/news/claude-4). 22 de mayo de 2025. Anthropic afirmó que Opus 4 podía trabajar continuamente durante varias horas y reportó una prueba de Rakuten de siete horas.

[^16]: Anthropic. ["Introducing Claude Sonnet 4.5"](https://www.anthropic.com/news/claude-sonnet-4-5). 29 de septiembre de 2025.

[^17]: Anthropic. ["Introducing Claude Opus 4.5"](https://www.anthropic.com/news/claude-opus-4-5). 24 de noviembre de 2025.

[^18]: Council on Foreign Relations / Dario Amodei. Declaraciones del 10 de marzo de 2025. Amodei dijo que esperaba que en tres a seis meses la IA escribiera el 90% del código y que en doce meses pudiera escribir esencialmente todo. Véase también WIRED, ["How to Become a Vibe Coder"](https://www.wired.com/story/uncanny-valley-podcast-how-to-become-a-vibe-coder/).

[^19]: Fridman, Lex. ["Dario Amodei: Anthropic CEO on Claude, AGI & the Future of AI & Humanity"](https://lexfridman.com/?p=6075). Noviembre de 2024. Amodei dijo que extrapolando el ritmo de progreso se podría llegar allí en 2026 o 2027, aunque añadió numerosas reservas sobre esa predicción.

[^20]: Reuters. ["Anthropic's valuation more than doubles to $183 billion after $13 billion fundraise"](https://www.reuters.com/business/anthropics-valuation-more-than-doubles-183-billion-after-13-billion-fundraise-2025-09-02/). 2 de septiembre de 2025.
