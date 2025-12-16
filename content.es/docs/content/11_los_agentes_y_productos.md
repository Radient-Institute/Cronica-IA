---
weight: 11
bookFlatSection: true
title: "11 - Los Agentes y Productos"
image: _din_style/banner_images/11_ayp.webp
---

# Los Agentes y Productos

2025 se suponía que sería **el año de los agentes autónomos**. 
No era una expectativa espontánea del público: los influencers lo repetían, la prensa lo anunciaba en titulares y hasta el propio Sam Altman lo mencionó en su blog. La promesa era clara: los agentes operarían por nosotros, tomando decisiones y ejecutando tareas de principio a fin.


Y tenía sentido. A finales del 2024 se filtró el plan interno de OpenAI sobre los niveles hacia la AGI, y todos asumimos que estábamos entrando al siguiente escalón.

{{% details title="El plan de OpenAI para alcanzar AGI" open=false %}}
1. IA conversacional: Chatbots y asistentes conversacionales.  
2. IA razonadora: Modelos capaces de resolver problemas al nivel humano.  
3. IA autónoma: Agentes capaces de tomar acciones.  
4. IA innovadora: Sistemas que ayudan a inventar y crear.  
5. IA organizacional: IA capaz de realizar el trabajo de una organización entera.  
{{% /details %}}

El nivel dos (la IA razonadora) se daba por “resuelto” gracias a la saga O, así que el paso natural era el nivel tres: la IA autónoma. En este capítulo hablaremos de esos agentes, pero no de los relacionados a código (que ya cubrimos), sino del resto.

## El mar de “agentes”

Podríamos llamar “agentes” a esos chats que empezaron a recibir acceso a *tools*: un intérprete de Python para analizar datos, un *web search* para funcionar como pseudo buscadores, conectores para generar diapositivas, graficar datos, planear vacaciones, analizar finanzas… Con la aparición de librerías para orquestar LLMs y otorgarles herramientas, surgió una **oleada inmensa de SaaS con IA**.

Y no solo librerías: también plataformas *low-code* y *no-code* como **n8n**, que permitieron a cualquiera montar flujos de trabajo bastante complejos conectados a modelos de lenguaje.

Sin embargo, hacia finales del 2025 casi todas estas aplicaciones seguían siendo productos de nicho. Funcionaban bien para públicos específicos, pero no lograron masificarse. Quizá podríamos destacar dos excepciones.

La primera fue **NotebookLM**, una app de Google donde uno podía subir fuentes de información, chatear sobre ellas y generar videos explicativos. Pero su popularidad no vino por eso, sino por una función muy específica: crear podcasts automáticamente a partir de documentos.  
Esa característica se volvió viral por lo útil y lo sencillo que resultaba.

La segunda fue **Manus AI** (marzo del 2025), un agente de “propósito general” creado por una *startup* china. No tenía una idea particularmente novedosa: podía buscar datos, analizarlos, escribir fragmentos de código, generar reportes, sitios web, etc.  
Lo que lo diferenció de intentos anteriores fue algo más simple: la gente reportaba que este agente realmente funcionaba bien.

## Los intentos de OpenAI para entrar al mundo de los agentes

A inicios del 2025, OpenAI lanzó sus propios agentes especializados.

El primero fue **Deep Research**, una versión de O3 ajustada para crear reportes extensos o encontrar información puntual; podía tardar varias decenas de minutos en completarse y a la gente le encantó. Tanto que todos los laboratorios frontera lo copiaron… excepto Google, que ya tenía un equivalente desde diciembre del 2024 llamado *Deep Search* que paso desapercibido.

El segundo agente fue **Operator**: una versión de GPT-4o capaz de interactuar con una máquina virtual a través de la terminal y de una interfaz gráfica. A diferencia de Deep Research, Operator requiere entrenamiento real del modelo en interacción con una interfaz, no basta con un simple *prompt*, lo que hizo que otros laboratorios no pudieran copiarlo tan rápido.  
Hasta la fecha, sigue siendo algo distintivo de ChatGPT.

## La interfaz y la madurez

Otro punto interesante es que todavía no está claro cuál debería ser la interfaz ideal de los LLMs.  
La clásica *textbox* con historial de chat no convence a muchos, pero aún no hay un reemplazo definitivo. Todos los experimentos, siguen siendo intentos.

Lo cierto es que los agentes de propósito general **aún no están maduros**.  
No son lo suficientemente confiables, y eso ha frenado su adopción más allá de las comunidades de entusiastas.

Por otro lado, sí existe un consenso amplio en algo: la capa de aplicación es donde están las mayores oportunidades. Y no falta quien asegure que el famoso unicornio de un solo empleado está a la vuelta de la esquina.

