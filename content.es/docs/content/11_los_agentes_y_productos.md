---
weight: 11
bookFlatSection: true
title: "11 - Los Agentes y Productos"
image: _din_style/banner_images/11_ayp.webp
---


# Los Agentes y Productos

2025 se suponía que sería **el año de los agentes autónomos**.[^1][^2]
No era una expectativa espontánea del público: los influencers lo repetían, la prensa lo anunciaba en titulares y hasta el propio Sam Altman lo mencionó en su blog.[^3] La promesa era clara: los agentes operarían por nosotros, tomando decisiones y ejecutando tareas de principio a fin.

Y tenía sentido. A mediados del 2024 se filtró el plan interno de OpenAI sobre los niveles hacia la AGI,[^4] y todos asumimos que estábamos entrando al siguiente escalón.

{{% details title="El plan de OpenAI para alcanzar AGI" open=false %}}

1. IA conversacional: Chatbots y asistentes conversacionales.
2. IA razonadora: Modelos capaces de resolver problemas al nivel humano.
3. IA autónoma: Agentes capaces de tomar acciones.
4. IA innovadora: Sistemas que ayudan a inventar y crear.
5. IA organizacional: IA capaz de realizar el trabajo de una organización entera.[^4]\
   {{% /details %}}

El nivel dos (la IA razonadora) se daba por “resuelto” gracias a la saga O, así que el paso natural era el nivel tres: la IA autónoma. En este capítulo hablaremos de esos agentes, pero no de los relacionados a código (que ya cubrimos), sino del resto.

## El mar de “agentes”

Podríamos llamar “agentes” a esos chats que empezaron a recibir acceso a *tools*: un intérprete de Python para analizar datos, un *web search* para funcionar como pseudo buscadores, conectores para generar diapositivas, graficar datos, planear vacaciones, analizar finanzas…[^5] Con la aparición de librerías para orquestar LLMs y otorgarles herramientas,[^6][^7] surgió una **oleada inmensa de SaaS con IA**.

Y no solo librerías: también plataformas *low-code* y *no-code* como **n8n**, que permitieron a cualquiera montar flujos de trabajo bastante complejos conectados a modelos de lenguaje.[^8]

Sin embargo, hacia finales del 2025 casi todas estas aplicaciones seguían siendo productos de nicho. Funcionaban bien para públicos específicos, pero no lograron masificarse.[^9] Quizá podríamos destacar dos excepciones.

La primera fue **NotebookLM**, una app de Google donde uno podía subir fuentes de información, chatear sobre ellas y generar videos explicativos.[^10] Pero su popularidad no vino por eso, sino por una función muy específica: crear podcasts automáticamente a partir de documentos (septiembre del 2024).[^11]\
Esa característica se volvió viral por lo útil y lo sencillo que resultaba.[^12][^13]

La segunda fue **Manus AI** (marzo del 2025),[^14] un agente de “propósito general” creado por una *startup* china.[^15] No tenía una idea particularmente novedosa: podía buscar datos, analizarlos, escribir fragmentos de código, generar reportes, sitios web, etc.[^16]\
Lo que lo diferenció de intentos anteriores fue algo más simple: la gente reportaba que este agente realmente funcionaba bien.[^17]

## Los intentos de OpenAI para entrar al mundo de los agentes

A inicios del 2025, OpenAI lanzó sus propios agentes especializados.

Uno de ellos fue **Deep Research**, una versión de O3 ajustada para crear reportes extensos o encontrar información puntual; podía tardar varias decenas de minutos en completarse y a la gente le encantó.[^18] Tanto que todos los laboratorios frontera lo copiaron…[^20][^21][^22] excepto Google, que ya tenía un equivalente desde diciembre del 2024, con el mismo nombre, y que paso desapercibido.[^19]

El otro agente fue **Operator**:[^23] un nuevo modelo presuntamente basado en GPT-4o capaz de interactuar con la interfaz grafica de una máquina virtual.[^24] A diferencia de Deep Research, Operator requiere entrenamiento real del modelo en interacción con una interfaz, no basta con un simple *prompt*,[^24][^25] lo que hizo que otros laboratorios no pudieran copiar sus capacidades tan rápido. Su uso no se masifico y poco a poco fue pasando al olvido.[^23]

## La interfaz y la madurez

Otro punto interesante que se empezo a barajar a lo largo del 2025 y todavía no está claro cuál debería ser la interfaz ideal de los LLMs.[^26]\
La clásica *textbox* con historial de chat no convencia a muchos, pero aún no se encontraba un reemplazo definitivo. Todos los experimentos, siguian siendo intentos.

Lo cierto es que los agentes de propósito general **aún no estaban maduros**.[^25]\
No eran lo suficientemente confiables,[^25] y eso habia frenado su adopción más allá de las comunidades de entusiastas.[^9]

Por otro lado, habia un consenso amplio en algo: la capa de aplicación es donde se creia estaban las mayores oportunidades.[^27][^28] Y estaban en su punto algido aquellas voces que aseguraban que el famoso unicornio de un solo empleado estaba a la vuelta de la esquina.[^29]

## Referencias

[^1]: Bloomberg Technology. ["Why 2025 Will Be The Year of AI Agents"](https://www.bloomberg.com/news/videos/2024-12-03/why-2025-will-be-the-year-of-ai-agents-video). 3 de diciembre de 2024.

[^2]: TechTarget. ["2025 will be the year of AI agents"](https://www.techtarget.com/searchEnterpriseAI/feature/Next-year-will-be-the-year-of-AI-agents). 26 de diciembre de 2024.

[^3]: Sam Altman. ["Reflections"](https://blog.samaltman.com/reflections). 6 de enero de 2025.

[^4]: Rachel Metz, Bloomberg. ["OpenAI Scale Ranks Progress Toward ‘Human-Level’ Problem Solving"](https://www.bloomberg.com/news/articles/2024-07-11/openai-sets-levels-to-track-progress-toward-superintelligent-ai). 11 de julio de 2024.

[^5]: Anthropic. ["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents). 19 de diciembre de 2024.

[^6]: LangChain. ["Tool Calling with LangChain"](https://www.langchain.com/blog/tool-calling-with-langchain). 11 de abril de 2024.

[^7]: OpenAI. ["New tools for building agents"](https://openai.com/index/new-tools-for-building-agents/). 11 de marzo de 2025.

[^8]: n8n. ["AI agentic workflows: a practical guide for n8n automation"](https://blog.n8n.io/ai-agentic-workflows/). 27 de diciembre de 2024.

[^9]: Gartner. ["Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026, Up from Less Than 5% in 2025"](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025). 26 de agosto de 2025.

[^10]: Google. ["What’s new in NotebookLM: Video Overviews and an upgraded Studio"](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-video-overviews-studio-upgrades/). 29 de julio de 2025.

[^11]: Google. ["NotebookLM now lets you listen to a conversation about your sources"](https://blog.google/innovation-and-ai/products/notebooklm-audio-overviews/). 11 de septiembre de 2024.

[^12]: Similarweb. ["AI Podcasts Power Huge Growth for Google’s NotebookLM"](https://www.similarweb.com/blog/insights/ai-news/ai-podcasts-power-huge-growth-for-googles-notebooklm/). 17 de octubre de 2024.

[^13]: TechCrunch. ["Google's NotebookLM now lets you guide AI-generated audio conversations, launches business pilot"](https://techcrunch.com/2024/10/17/googles-notebooklm-now-lets-you-guide-ai-generated-audio-conversations-launches-business-pilot/). 17 de octubre de 2024.

[^14]: Info-Tech Research Group. ["Assessing Manus: The Future of Agentic AI"](https://www.infotech.com/research/assessing-manus-the-future-of-agentic-ai). Marzo de 2025.

[^15]: Reuters. ["Beijing boosts AI startup Manus, as China looks for the next DeepSeek"](https://www.reuters.com/technology/artificial-intelligence/beijing-boosts-ai-startup-manus-china-looks-next-deepseek-2025-03-21/). 21 de marzo de 2025.

[^16]: South China Morning Post. ["Another DeepSeek moment? General AI agent Manus shows ability to handle complex tasks"](https://tech.yahoo.com/ai/articles/another-deepseek-moment-general-ai-093000724.html). 6 de marzo de 2025.

[^17]: MIT Technology Review. ["Ponemos a prueba Manus, la nueva competencia de DeepSeek"](https://technologyreview.es/article/ponemos-a-prueba-manus-la-nueva-competencia-de-deepseek). 12 de marzo de 2025.

[^18]: OpenAI. ["Introducing deep research"](https://openai.com/index/introducing-deep-research/). 2 de febrero de 2025.

[^19]: Google. ["Try Deep Research and our new experimental model in Gemini, your AI assistant"](https://blog.google/products-and-platforms/products/gemini/google-gemini-deep-research/). 11 de diciembre de 2024.

[^20]: xAI. ["Grok 3 Beta — The Age of Reasoning Agents"](https://x.ai/news/grok-3). 19 de febrero de 2025.

[^21]: Anthropic. ["Claude takes research to new places"](https://www.anthropic.com/news/research). 15 de abril de 2025.

[^22]: Microsoft. ["Introducing Researcher and Analyst in Microsoft 365 Copilot"](https://www.microsoft.com/en-us/microsoft-365/blog/2025/03/25/introducing-researcher-and-analyst-in-microsoft-365-copilot/). 25 de marzo de 2025.

[^23]: OpenAI. ["Introducing Operator"](https://openai.com/index/introducing-operator/). 23 de enero de 2025.

[^24]: OpenAI. ["Computer-Using Agent"](https://openai.com/index/computer-using-agent/). 23 de enero de 2025.

[^25]: OpenAI. ["Operator System Card"](https://openai.com/index/operator-system-card/). 23 de enero de 2025.

[^26]: Andreessen Horowitz. ["Big Ideas in Tech for 2025"](https://a16z.com/big-ideas-in-tech-2025/). Diciembre de 2024.

[^27]: Prosus. ["Betting on the Application Layer: How Prosus Is Building AI Ecosystems"](https://www.naspers.com/our-insights/investment-insights/2025/betting-on-the-application-layer-how-prosus-is-building-ai-ecosystems). 30 de abril de 2025.

[^28]: Betaworks. ["Apply to Betaworks’ Spring ’25 AI Camp: App Layer"](https://www.betaworks.com/writing/apply-to-betaworks-ai-camp-app-layer-for-500k-in-funding). 2025.

[^29]: TechCrunch. ["AI agents could birth the first one-person unicorn — but at what societal cost?"](https://techcrunch.com/2025/02/01/ai-agents-could-birth-the-first-one-person-unicorn-but-at-what-societal-cost/). 1 de febrero de 2025.
