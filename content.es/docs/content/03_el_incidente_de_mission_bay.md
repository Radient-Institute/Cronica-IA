---
weight: 3
bookFlatSection: true
title: "03 - El Incidente de Mission Bay"
image: _din_style/banner_images/03_imb.webp
---

# El Incidente de Mission Bay

Mientras la carrera por alcanzar a GPT-4 continuaba acelerándose, un evento inesperado sacudiría los cimientos de OpenAI y revelaría las tensiones internas que se habían estado gestando en la organización líder.

Movámonos a noviembre de 2023. El viernes 17, la junta de directivos de OpenAI hace algo impensable: **destituye a Sam Altman** como CEO bajo la premisa de que habían "perdido la confianza en su liderazgo" y que Sam no había sido "consistentemente honesto con su comunicación". Las implicaciones, motivos y consecuencias dan para hacer una película entera. De hecho, ya la están haciendo.

Entre los rumores más mencionados está que Sam Altman quería iterar sobre el producto de manera más rápida, dejando de lado el área de seguridad en la que Ilya Sutskever ponía gran parte de su foco. Según versiones no confirmadas, Mira Murati, a escondidas durante más de un año, le filtraba chats, correos e información a Ilya sobre acciones que Sam estaba tomando y que ambos consideraban equivocadas. Con el tiempo se fueron convenciendo a ellos mismos y a la junta de directivos de que lo mejor era quitar a Sam del puesto. Hasta 2025 continúan saliendo nuevos detalles acerca de lo que pasó por detrás para desencadenar el suceso.

Esta noticia dio la vuelta al mundo y pilló por sorpresa a toda la comunidad, creando una variedad de opiniones, especulaciones y memes como mi favorito personal: "*What did Ilya see?*" (¿Qué vio Ilya?).

Pero, resumiendo lo que fueron días de caos absoluto: después de una amenaza de renuncia masiva de cientos de empleados de OpenAI y la oferta de Microsoft para armarle una organización/laboratorio a Sam junto a todo su séquito dentro del propio Microsoft, no le quedó otra opción a la junta de directivos que **restituir a Sam tan solo cinco días después** de su despido, para luego ser removidos poco después.

Este episodio nos demostró algo que muchos ya sospechábamos pero aún no queríamos aceptar: que OpenAI ya no es aquella organización sin ánimo de lucro que busca el desarrollo de la IA para el beneficio de la humanidad, con una directiva sin intereses cruzados que tomaría las mejores decisiones para el mundo. En cambio, se había convertido en una empresa como cualquier otra, sujeta a las dinámicas de poder entre fundadores y a la presión de los inversionistas.

## SSI (Safe Superintelligence): El Laboratorio de Ilya

Las consecuencias del incidente de noviembre no tardarían en materializarse. Varios meses después, en junio de 2024, ocurrió la primera de dos fragmentaciones importantes en OpenAI: la renuncia o, más precisamente, el **despido indirecto de Ilya Sutskever**, cofundador y científico jefe de la compañía. Hablamos de "despido indirecto" porque, según múltiples fuentes, después del intento fallido de remover a Sam Altman, Ilya quedó efectivamente aislado dentro de la empresa, con acceso reducido a recursos e influencia prácticamente nula.

La respuesta de Ilya sería crear su propia *startup*: Safe Superintelligence Inc., o simplemente SSI. Con un solo objetivo declarado: **construir superinteligencia de manera segura, sin ningún producto intermedio**. SSI representa probablemente el laboratorio más hermético de la industria hasta la fecha.

Aunque los detalles específicos de su trabajo permanecen en secreto, se pueden inferir algunas direcciones a partir de entrevistas que Ilya ha brindado a lo largo de estos casi dos años. A diferencia del enfoque de modelos cada vez más grandes y generalistas que domina la industria, SSI parece estar interesado en algo fundamentalmente diferente: no en una inteligencia absoluta o en un modelo superambivalente como los LLMs actuales, sino en un sistema (modelo & algoritmo de aprendizaje) que funcione más como un adolescente humano. Es decir, un sistema que, sin ser experto en todo desde el principio, pueda ser desplegado en diferentes ambientes para aprender a desempeñar tareas específicas en el mundo real. En esta visión, Ilya ha remarcado repetidamente **la importancia de una poderosa *value function*** (función de valor, el mecanismo que permite a un modelo evaluar qué acciones lo acercan a sus objetivos) como la pieza clave que sustenta la capacidad de aprendizaje humana.

La opacidad de SSI es notable. Otros detalles de la *startup* permanecen también bajo llave: en qué estado de desarrollo se encuentran, cuántos empleados conforman el equipo, qué técnicas específicas están explorando. Los pocos datos que han trascendido son fragmentarios: el equipo es pequeño (se estima un par de docenas de investigadores), gran parte del equipo proviene de Israel, están utilizando TPUs de Google para su infraestructura de cómputo, y su valuación, según reportes de 2025, alcanza ya los 30 mil millones de dólares.

Hay quien dice, no sin razón, que si la historia de la IA fuese una película, Ilya Sutskever sería el protagonista.

## Thinking Machines Lab: El Proyecto de Mira

La segunda fragmentación importante llegaría poco más de un año después del incidente con Sam Altman. En **febrero de 2025**, Mira Murati, quien hasta entonces había servido como CTO de OpenAI, decidió iniciar su propia aventura: **Thinking Machines Lab**.

A diferencia de la salida discreta de Ilya, la partida de Mira fue un éxodo considerable. Se llevó consigo una cantidad significativa de investigadores clave de OpenAI, así como talento selecto de otros laboratorios competidores.

Sin ningún producto lanzado, Thinking Machines Lab consiguió una valuación inicial estimada en 10 mil millones de dólares. En la era de la IA, el pedigrí y las promesas valen casi lo mismo que los resultados.

Pero Mira y su equipo no se quedarían en el misterio tanto tiempo como Ilya. Meses después de recaudar el capital inicial, comenzaron a publicar una **serie de *blog posts*** compartiendo investigación genuinamente interesante: exploraron las razones profundas del no determinismo en los LLMs (ese comportamiento aparentemente aleatorio que persiste incluso con temperatura 0), presentaron una variante novedosa de algoritmo de optimización llamada Manifold Muon, desarrollaron técnicas avanzadas con LoRA (Low-Rank Adaptation, un método para adaptar modelos grandes de manera eficiente) para el *fine-tuning* de LLMs, y compartieron nuevas técnicas de destilación de modelos.

¿Quién lo diría? Al final resultaron más transparentes y "*open*" que el actual OpenAI.

Sin embargo, el lanzamiento más relevante de Thinking Machines Lab no fue un *paper* ni un modelo, sino un servicio comercial: **Tinker**. Se trata de una **plataforma accesible vía API** que permite a empresas y desarrolladores hacer *fine-tuning* de LLMs de manera personalizada, aun en beta privada a finales del 2025. Tú controlas el algoritmo y los datos de entrenamiento; ellos ponen toda la infraestructura computacional y la escalabilidad.

Y en el mundo de la IA de 2025, unos cuantos *blog posts* y una API funcional son suficiente para abrir las puertas de la siguiente ronda de financiamiento. Según stimaciones, esta ronda pondría a Thinking Machines Lab en una valuación de 50 mil millones de dólares.

---

Sea como fuese, no sería la primera vez que una semilla caída del árbol de OpenAI germina y florece de manera espectacular en suelo propio.

¿Verdad, Dario?

---

**Nota del autor:** 
1. La última pregunta hace referencia a Dario Amodei, cofundador de Anthropic y exvicepresidente de investigación de OpenAI, quien abandonó la compañía en 2021 junto con otros investigadores clave para fundar lo que hoy es uno de los principales competidores de OpenAI. Anthropic, creadora de la familia de modelos Claude, nació precisamente de esas mismas tensiones entre velocidad de desarrollo y consideraciones de seguridad que años después provocarían el incidente de Mission Bay. La historia, como suele hacer, tiende a rimar.