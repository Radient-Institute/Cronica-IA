---
weight: 19
bookFlatSection: true
title: "19 - La Contracultura"
image: _din_style/banner_images/19_lc.webp
---

# La Contracultura

El *meta* actual de los laboratorios frontera es fácil de describir. Robas un par de *researchers* clave, contactas VCs, levantas decenas o cientos de millones, quemas una montaña de cómputo, entrenas un LLM enorme y lo posicionas como estado del arte para su tamaño o competitivo frente a los modelos frontera. Luego te diferencias por precio, por velocidad, por especialización en algún área… o directamente lo haces **open source** para capturar atención más rápido. Levantas otra ronda, escalas y vuelves a iterar.

Esta dinámica aplica casi igual para startups/laboratorios que trabajan en modelos de video, de audio o de imagen.

Pero, en paralelo, existe un grupo de laboratorios y startups que decidió adoptar una actitud distinta, más anárquica y definitivamente contraria al meta dominante.

## Descentralización

La primera línea “rebelde” surgió alrededor de una idea simple: si algún día llegamos a crear una IA superpoderosa (o incluso una AGI), no debería estar en manos de unos pocos. Debería desarrollarse y ejecutarse de manera descentralizada, distribuida al rededor de todo el globo.

El primer grupo en tomar esta bandera fue **Nous Research**, que empezó en 2023 como una comunidad haciendo *finetunings* de Llama. Con el tiempo se convirtieron en una startup y comenzaron a trabajar en software para preentrenamiento distribuido nuevos optimizadores, *reinforcement learning* asincrónico y, en algún momento, hasta se metieron con cripto y *blockchain*. Mientras tanto mantenían su serie de modelos *instruct* finetuneados: **Hermes**.

Poco después se sumó **Prime Intellect**, mitad *marketplace* de GPUs, mitad laboratorio. Al igual que Nous, desarrollaron software para entrenamiento e inferencia descentralizada y, a mediados de 2025, crearon un hub abierto de entornos para entrenar LLMs con RL.

Entre 2024 y 2025 ambos grupos lanzaron sus primeros entrenamientos “descentralizados”. El resultado: el hardware estaba casi por completo localizado en Estados Unidos (y algo en Europa), y conformado unicamente por H100s y A100s. Es decir, los entrenamientos no fueron tan heterogéneos ni tan distribuidos como sugería la narrativa en la que los individuales podían contribuir con sus GPUs de consumo. Y los modelos resultantes, tanto preentrenados, como los de RL y sus trazas verificadas, no fueron útiles en la práctica. Podemos considerarlos aun como pruebas de concepto.

---

Sin embargo, quien más ha reflexionado públicamente sobre un futuro en el que la IA la controlen las grandes empresas versus uno en el que la tecnologia sea abierta y amplifique el proposito humano en vez de reemplazarlo es **Emad Mostaque**. En 2025 fundó *Intelligent Internet*, publicó un libro donde advierte que la economía actual será disrumpida por la IA y que tenemos unos **1000 días** para reescribir el sistema operativo de la sociedad hacia un modelo de simbiosis humana, evitando tanto el feudalismo digital como un escenario de fragmentación similar a una “guerra fría”.

En términos prácticos, hasta ahora han lanzado un *finetuning* de un modelo de 4B para agentes, un *dataset* y otro *finetuning* para aplicaciones médicas. Interesante como visión, pero sin frutos todavia.

## Nuevos horizontes

Otra corriente contracultural rechaza abiertamente que los modelos actuales, LLMs, escalamiento, más datos, más parámetros, más RL, más de lo mismo, sean el camino hacia la AGI. Su propuesta es buscar **ideas nuevas**, incluso si están lejos de un gran beneficio económico inmediato.

El ejemplo más visible es **Sakana AI**, el laboratorio japonés mas importante, fundado por David Ha en 2023. Su misión es hacer lo opuesto a lo que hace todo el mundo, y esa filosofía los ha llevado a explorar líneas de investigación extremadamente variadas, desde agentes hasta nuevas arquitecturas.

{{% details title="Lanzamientos relevantes de Sakana AI" open=false %}}
- Modelos recurrentes inspirados en el cerebro.  
- Combinaciones de modelos al estilo evolución.  
- Agentes LLM que escriben *papers*.  
- Agentes que reescriben su propio código.  
- Parches a LLMs para mejorar capacidades.  
- Modelos de visión fundacionales que buscan comportamientos similares a la vida en entornos simulados.  
- Agentes que generan *kernels* CUDA.  
{{% /details %}}

No tienen productos. Seguramente tampoco *revenue*. Pero es uno de los laboratorios favoritos del público porque cada nuevo paper es una sorpresa.

La doctora **Fei-Fei Li**, tampoco convencida del paradigma dominante (y con un sesgo natural hacia la visión por computadora), fundó en 2024 una startup llamada **World Labs** centrada en **inteligencia espacial**. Por ahora han lanzado un modelo que convierte imágenes en entornos 3D, pero poco más.

Finalmente está **Yann LeCun**, que también abandona Meta para crear su propia empresa. Apuesta por la **AMI (Artificial Machine Intelligence)**: un sistema basado en *self-supervised learning*, planeación en espacio abstracto y modelos tipo JEPA.

Y así continúa una pequeña lista de otros grupos que buscan rutas distintas.  
Por ahora, **ninguna ha logrado un impacto comparable ni siquiera a las versiones prematuras de los LLMs**, pero representan algo necesario: la diversidad intelectual.


---

Notas:

1. El "meta", hace referencia al "metagame", un termino de los videojuegos que se usa para referirse a la estrategia prevalente en un entorno competitivo.