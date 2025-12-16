---
weight: 20
bookFlatSection: true
title: "20 - Hardware & Robótica"
image: _din_style/banner_images/20_hyr.webp
---

# Hardware & Robótica


## Hardware

### El ascenso y ventaja de NVIDIA

Vale la pena indagar bastante en la historia de NVIDIA. Pasaron de ser una empresa de tarjetas gráficas con una mala racha de media década a convertirse en **la compañía más valiosa del mundo**.

La razón es bastante facil de explicar. Dio la casualidad que los mismos dispositivos que ellos fabrican (tarjetas gráficas) a parte de dar más FPS en *Cyberpunk 2077* también resultaron perfectos para entrenar redes neuronales. Jensen Huang lo notó temprano y empezó a **apostar fuerte por GPUs para centros de datos**: más VRAM, más bandwidth, interconexiones mejores, racks enormes. Y en software hicieron lo mismo: CUDA, librerías, soporte a frameworks de Deep Learning, etc.

La victoria era obvia porque no había alternativa.  
> ¿Quieres entrenar un LLM?  
> CPU → imposible  
> GPU AMD → ROCm no iba bien en PyTorch  
> → Entonces NVIDIA. No había más.

### TPUs: la alternativa… a medias

Viendo el potencial que podia tener la IA en el futuro ¿Vale la pena usar un hardware diseñado para gráficos en vez de uno especializado en cálculos tensoriales? Google dijo que no y saco sus TPUs (Tensor Processing Unit), con un Tensor Core ultra poderoso, robustez y escalabilidad en pods masivos de hasta 8 mil unidades.

Pero también con grandes desventajas:

1. **Disponibilidad limitada.**  
   La beta empezó recién en 2018, pero se hicieron disponibles para uso general en 2022 y solo se pueden alquilar en Google Cloud (aunque estan en proceso de expandirlo a otros proveedores).  
   La generación más nueva (p. ej., Ironwood v7) nunca está disponible, excepto para los socios importantes.

2. **Arquitectura diferente.**  
   No tienen cientos de SMs como las GPUs, sino 1–2 núcleos optimizados. Eso exige un flujo de trabajo **basado en grafos estáticos**, donde hay que compilar el programa completo antes de ejecutar. PyTorch no encaja bien en ese modelo por mas que se haya intentado adaptar. Si quieres trabajar seriamente con TPUs, necesitas **JAX**.

3. **Precio.**  
   Una TPU v6 cuesta ~3 USD/hora con 32 GB de memoria y 1.8 PFLOPS.  Una NVIDIA B200 cuesta ~18 USD/hora (on demand) en Google Cloud con 140GB de memoria y 14 PFLOPS… pero puedes alquilarla en GPUList, FAL o PrimeIntellect incluso por **menos de 3 USD/hora**. Y si tienes suficiente dinero, puedes comprar las propias GPUs. Este último simplemente no es una opción con las TPUs.

Entonces… si NVIDIA es superior a la competencia ¿Por qué vemos titulares de laboratorios grandes (como Meta, OpenAI, Anthropic o SSI) empezando a usar TPUs de Google y GPUs de AMD? 

A parte de que la **diversificación** es sumamente importante ya que tener toda tu infraestructura de cómputo en una sola empresa es riesgoso. Si gastas decenas de miles de millones al año en cómputo, quizas sea conveniente poner a varias de decenas de empleados a armar la infraestructura y adaptar los *codebases* a un hardware alternativo de una empresa que seguramente este ofreciendo descuentos especiales. 

Solo los laboratorios frontera pueden darse este lujo.
Incluso pueden ser mas ambiciosos, si vas a gastar tanto dinero ¿Porque no gastarlo en diseñar y fabricar chips propios? Durante la segunda mitad del 2025 nos enteramos que esto es exactamente lo que empieza a hacer la gente de OpenAI, Meta y X.AI.


### Chips para inferencia ultrarrápida

Otra tendencia interesante es la de startups que fabrican **chips especializados en inferencia**, optimizados para generar mas de mil tokens por segundo en diferentes LLMs.

Los tres grandes jugadores en esta area son: **Groq**, **Sambanova** y **Cerebras**.

Logran *speedups* de cerca de 4x en inferencia comparados con GPUs NVIDIA (sin contar las ganancias del *speculative decoding*).  

¿Cómo lo hacen? Uno de los principales cuellos de botella en los chips de NVIDIA es el ancho de banda del HBM (conocida como VRAM), por lo que construyen chips con **enormes memorias SRAM** que combinados tienen suficiente espacio para cargar con todos los pesos de un modelo mediano, eliminando la necesidad de un acceso constante a la VRAM. Evidentemente esto es sumamente costoso.

### Chips radicalmente distintos

Yo espero con ansias el día en que mi hijo de 8 años me pida que le compre una unidad de cómputo de 3 exaflops que vio en una oferta del metaverso por tan solo 500 dólares (o su equivalente en el futuro). Le diré: 
> “Nah, que va, te compro la de 2 exaflops, ni siquiera lo vas a usar totalmente. ¿Qué vas a hacer con eso? ¿Replicar GPT-5?”

Ya que hablamos de fantasías tambien debemos mencionar a las startups que aparecieron prometiendo chips, no solo 10 veces mas rapido que las GPUs actuales, sino 1000 veces mas rapido. Esa es la fantasia que promete Etched, cuya idea es grabar la arquitectura del transformer directamente en silicio.

---

Mención honorífica para quienes siguen prometiendo computación cuántica, si cuentanoslo de nuevo, la ultima vez fue hace diez años y no nos habia quedado claro. Ah no, espera, esta vez si, esta vez si.

---

Otra línea experimental es la de los chips probabilísticos, tecnologías que suelen basarse en los **p-bits**. Los p-bits basicamente son como bits pero que fluctúan físicamente entre 0 y 1 con cierta probabilidad. Una red de p-bits te permitiría implementar un modelo de energía (EBM) de manera *física*, y al dejar evolucionar esta red puedes encontrar los estados de menor energía, mucho más eficientemente que simulándolos en GPU.

Hay varios grupos trabajando en esto: la Universidad de Tohoku, IBM, Quantum Dice. Pero los más avanzados en enfocarlo a un producto comercial parecen ser **Extropic**, cofundada por el célebre Beff Jezoz, gran impulsor del aceleracionismo. En octubre de 2025 lanzaron su primer prototipo de escritorio a temperatura ambiente con decenas de p-bits. El problema es que casi nadie quiere un chip especializado en EBMs, porque los EBMs no son populares en la IA actual.

Como una alternativa con más mercado, **Normal Computing** trabaja en hardware probabilístico cuyas unidades no son bits discretos sino variables continuas (voltajes, corrientes) controladas por SDEs (stochastic differential equations), del mismo tipo que usan los modelos de difusión.

---

En algún lugar también habrá un chip de fotones prometiendo el futuro.

## Robótica

Los robots humanoides que vemos en películas están íntimamente ligados a la inteligencia artificial. Si hoy tenemos modelos que ganan olimpiadas universitarias de programación, ¿no sería cosa de meter uno en un robot y listo?  Aún no. Hace falta que los modelos desarrollen una **inteligencia motriz y espacial** relativamente avanzada.  

El *machine learning* lleva más de 15 años intentando resolverla, y aunque todavía no está dominada, ahora contamos con algoritmos más sofisticados, mucho más cómputo y una avalancha de inversión. Por eso surgieron tantas startups atacando el problema.

Podemos separarlas en dos grupos:

**1. Robots “de demostración”**   
El líder es **Figure AI**, que en teoría ya tiene robots desplegados en fábricas de socios y cuyo valor ronda los 39 mil millones de dólares. También están **Tesla** con Optimus, **1X** con Neo e incluso **XPeng**, que saltó de autos a humanoides. Su apuesta es vender **servicios robóticos** cuando el producto esté listo.

**2. Robots accesibles para cualquiera.**  
Aquí destaca **Unitree Robotics**, que está por salir a bolsa y vende robots desde 6 mil dólares. Se pueden programar libremente y hasta se venden en Walmart. La mayoría de universidades y laboratorios de investigación usan robots de Unitree. Otras compañías, como **Romela** o **Pollen Robotics**, han optado por hacer sus robots **open source**. Estas empresas apuntan a vender el robot como el producto final, con unas funcionalidades basicas y un kit de desarrollo para que puedas tu desarrolles o decidas que software ponerle.

Cada semana aparece una nueva demo impresionante (aunque siempre en entornos controlados) que nos emociona con la posibilidad de que la era de los robots humanoides este pronta.

Por ahora **los robots de propósito general no han llegado** (ni para fábricas ni para hogares). Pero en caso que quieras experimentar con uno:

- Si eres una empresa gigante de manufactura: habla con Figure.  
- Si no facturas cientos de millones al año: entra al sitio de Unitree y compra uno.

Un mapa muy completo del ecosistema robótico de la mano de @Robotuo puede verse [aquí](https://x.com/Robo_Tuo/status/1997481988220146078?s=20).
