
---
weight: 2
bookFlatSection: true
title: "02 - La Captura de GPT-4"
image: _din_style/banner_images/02_cgpt.webp
---

# La Captura de GPT-4

Desde pocos días después de la salida y el posterior éxito masivo de ChatGPT, empezó una **carrera por alcanzar la tecnología de OpenAI**. No sería la primera vez que algún Prometeo se hacía con su fuego, y no sería la última.

Tres frentes tomaron la iniciativa: las empresas competidoras, el *open source* y los laboratorios y grupos de investigación universitarios. Me gusta llamar a este periodo "La captura de GPT-4", pero antes de capturar al gigante, primero teníamos que alcanzar al pequeño **GPT-3.5 Turbo**.

Los **primeros intentos** se terminan materializando en **abril de 2023**. Universidades y laboratorios habían construido *datasets* sintéticos basados en las respuestas de GPT-3.5 Turbo y los usaron para hacer *fine-tuning* de los modelos base de lenguaje disponibles en la fecha, como LLaMA 1, Pythia, GPT-Neo, BLOOM, etc. Esto dio paso al nacimiento de Alpaca, Vicuna, Dolly, Guanaco, Koala, entre otros.

Una iniciativa del OSS interesante fue la del YouTuber Yannic Kilcher, llamada **OpenAssistant**, donde se pretendía construir un *dataset* propio y abierto para este mismo propósito.

A pesar de que los modelos fueron muy comentados y celebrados, había un problema. Las respuestas que te daban estos modelos se sentían como ChatGPT, pero a la mínima que subías la dificultad de las preguntas te dabas cuenta de que aún no estábamos cerca de la tecnología de OpenAI. Se consiguió que los modelos hablasen en formato chat, pero como herramienta útil aún estaban limitados.

Y aunque las técnicas que usaban estos grupos se fueron modernizando con el pasar de los meses, pasando de un simple **SFT a DPO y/o RLHF**, tuvieron que venir las empresas y *startups* a dar una mano para impulsar tanto la competencia como el OSS.

El resto del año estaría marcado por ese ritmo: empresas sacando LLMs abiertos cada vez superiores, acercándose poco a poco a OpenAI. Stability AI sacó StableLM (abril), MosaicML sacó MPT (mayo), el TII de los Emiratos Árabes Unidos sacó Falcon (junio), Meta sacó Llama 2 (julio), Mistral sacó Mistral 7B (septiembre).

Instituciones previamente poco involucradas con la IA notaron el potencial de la tecnología y comenzaron a invertir en investigación y desarrollo de LLMs. El ambiente se volvió tan competitivo que no tenía sentido intentar preentrenar o alinear modelos de lenguaje a menos que fueras una *startup* con millones de capital o con apoyo del gobierno.

En ese entonces había dos partícipes importantes que, a pesar de estar bastante por detrás, apostaron por mantener sus modelos *closed source*. Y aunque todo el mundo tenía expectativas altas en ellos, aún no nos habían entregado nada mínimamente competitivo con el líder. Hablo de Anthropic con Claude 2 (julio) y Google con Bard (marzo).