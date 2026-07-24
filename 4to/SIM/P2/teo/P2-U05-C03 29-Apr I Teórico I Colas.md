
### II. Resolución Analítica de Sistemas Simples (12:20 - 30:19)

El segundo gran tema marcó una diferencia fundamental con clases pasadas: **no todo sistema de colas necesita ser simulado renglón a renglón**. Si el sistema cumple con ser "simple" (un servidor, o varios idénticos en paralelo bajo una misma cola), se pueden aplicar las fórmulas matemáticas de la **[[Ley de Little]]** y la **[[Notación de Kendall]]**. Este enfoque analítico permite obtener las **[[Medidas de Desempeño]]** promedio (como la cantidad de clientes esperados $L$ o el tiempo de espera $W_q$) de manera instantánea calculando únicamente el **[[Factor de Utilización]] ($\rho$)**, siempre cuidando la trampa teórica de no confundir la frecuencia ($\lambda$) con el tiempo de servicio ($1/\mu$).


#### La [[Notación de Kendall]]
Es la codificación estándar internacional para clasificar modelos analíticos mediante la sintaxis A/B/s/k/t/d.

| Parámetro | Significado Técnico                                                 | Concepto Relacionado                        |
| --------- | ------------------------------------------------------------------- | ------------------------------------------- |
| A         | Distribución de los tiempos entre llegadas.                         | [[Distribución Exponencial]]                |
| B         | Distribución de los tiempos de servicio.                            | [[Distribución Uniforme]]                   |
| s         | Cantidad de servidores en paralelo.                                 | [[Servidores Múltiples]]                    |
| k,t,d     | Capacidad del sistema, Tamaño de la fuente y Disciplina de la cola. | [[Capacidad Infinita]], [[LIFO]] / [[FIFO]] |


#### notacion 
![[{EFBBC405-5C0A-4C90-A0F4-5E8D7FC468B7}.png]]
> [!danger] Error Frecuente: Confundir Tiempos con Tasas "50 peticiones por minuto" es una **[[Tasa de Llegada]]** (λ). Sin embargo, "demora 3 segundos por petición" es un **[[Tiempo Medio de Servicio]]**. Para inyectar este último en una fórmula de tasas, es obligatorio aplicar la inversa (1/Media) y unificar las unidades temporales.

- **Estabilidad del Sistema:** Se explica que la probabilidad de entrar a un estado debe ser igual a la de salir de él para que el sistema no colapse.

> [!note] Fórmula: Factor de Utilización (ρ) Es el indicador absoluto de estabilidad del sistema. Para que el sistema no colapse, ρ debe ser menor a 1 (si ρ≥1, la fila de clientes tenderá a infinito) $$ \rho = \frac{\lambda}{s \cdot \mu} $$ 
> 
> _Donde $\lambda$ es la [[Tasa de Llegada]], $\mu$ es la [[Tasa de Servicio]] y $s$ es la cantidad de servidores._
> 
> **[[Ley de Little]] (Relaciones Fundamentales):** $$ L = \lambda \cdot W $$ $$ L_q = \lambda \cdot W_q $$ $$ W = W_q + \frac{1}{\mu} $$ _Donde_ L _y_ Lq​ _es el valor esperado de clientes en sistema y en cola, respectivamente._ W _y_ Wq​ _son los tiempos medios de respuesta en el sistema y en la cola_

![[{645A3981-3B70-4962-996F-10757AD4C26C} 1.png|447]]
![[{1505417B-251C-4771-AFDE-550F0DD93A64}.png|447]]
![[{D622315A-5070-48AC-8538-479639CFE30F}.png|449]]



### para el caso de un modelo con un solo servidro M/M/1

El **modelo M/M/1** es la configuración analítica más elemental dentro del estudio de los [[Sistemas de Colas]]. A diferencia de la [[Simulación de Montecarlo]] o la iteración manual de un [[Vector de Estado]], este modelo permite obtener resultados exactos y promedios a largo plazo aplicando directamente fórmulas matemáticas basadas en la [[Ley de Little]].

La estructura de su nombre proviene directamente de la **[[Notación de Kendall]]** ($A/B/s/k/t/d$), el estándar internacional para clasificar modelos analíticos de colas.

#### 1. Desglose de la Notación M/M/1

En este modelo, las tres primeras letras definen el comportamiento fundamental del sistema, asumiendo por defecto que la capacidad de la cola y la población son infinitas, y que se utiliza una [[Disciplina FIFO]].

|Parámetro de Kendall|Significado en el Modelo M/M/1|Conceptos y Variables Relacionadas|
|:--|:--|:--|
|**M** (Llegadas)|Los tiempos entre llegadas siguen una [[Distribución Exponencial]] (Markoviana).|[[Tasa de Llegada]] ($\lambda$), [[Llegada al Sistema]]|
|**M** (Servicio)|Los tiempos de atención del servidor siguen una [[Distribución Exponencial]].|[[Tasa de Servicio]] ($\mu$), [[Fin de Atención]]|
|**1** (Servidores)|Existe un único servidor procesando toda la cola de manera secuencial.|[[Servidor Único]], [[Sistema Elemental]]|

_Fuente:_.

> [!danger] Trampa de Parcial: Tasas vs. Tiempos Medios El error más común al resolver un modelo M/M/1 es confundir tiempos con tasas. La [[Ley de Little]] y las fórmulas analíticas no operan con tiempos (ej. "demora 3 segundos"), sino exclusivamente con **tasas** (ej. "atiende a 20 clientes por minuto"). Si el enunciado te da el [[Tiempo Medio de Servicio]], debes aplicar obligatoriamente la inversa ($\mu = 1 / \text{Media}$) antes de inyectar el valor en las fórmulas.

#### 2. Condición de Estabilidad

Para que el modelo matemático sea viable y el sistema no colapse, la probabilidad de entrar a un estado debe ser idéntica a la de salir de él.

> [!tip] Tip de Validación Antes de calcular cualquier métrica, siempre debes verificar el [[Factor de Utilización]] ($\rho$). Si los clientes llegan más rápido de lo que el único servidor puede atenderlos ($\rho \ge 1$), la cola tenderá a infinito y las fórmulas arrojarán resultados inconsistentes o negativos.

#### 3. Fórmulas de Desempeño del Modelo M/M/1

El profesor estableció que para un sistema de un único servidor, los promedios del sistema se rigen por las siguientes fórmulas matemáticas derivadas:

> [!note] Fórmula: Factor de Utilización ($\rho$) Es el porcentaje de tiempo que el servidor pasa ocupado. Para que el sistema sea estable, debe ser estrictamente menor a 1. $$ \rho = \frac{\lambda}{\mu} $$

> [!note] Fórmulas: Cantidad Esperada de Clientes ($L$ y $L_q$) 
> 
> **valor esperado de clientes en el sistema ($L$):** $$ L = \frac{\rho}{1 - \rho} $$ **Clientes promedio en la cola ($L_q$):** $$ L_q = \frac{\rho^2}{1 - \rho} $$

> [!note] Fórmulas: Tiempos de Espera ($W$ y $W_q$) 
> 
> **Tiempo medio de respuesta en el sistema ($W$):** $$ W = \frac{1}{\mu(1 - \rho)} $$ **Tiempo medio de espera en la cola ($W_q$):** $$ W_q = \frac{\rho}{\mu(1 - \rho)} $$

probabilidad de que haya, menos de una cierta cantidad k de cliente en el sistema
![[{A7A341DB-E54D-4A43-BF97-FF11607B9E56}.png]]
#### 4. Representación Gráfica del Flujo

A nivel conceptual, el modelo M/M/1 se visualiza con el siguiente flujo continuo, el cual evita la programación de estados si solo se requiere conocer los parámetros generales a largo plazo:

```
graph LR
    A[Llegadas Exponenciales] -->|Tasa Lambda| B(Cola Única Infinita)
    B --> C{1 Servidor Exponencial}
    C -->|Tasa Mu| D[Salida del Sistema]
```

_Conceptos relacionados al gráfico:_ [[Resolución Analítica]], [[Sistemas Dinámicos]], [[Llegada al Sistema]], [[Tasa de Servicio]].
### modelo m/m/s (multiple servidores)
![[{B5EB6841-8D29-492D-8DBC-B37DFB080324}.png]]
### III. Casos Prácticos Analíticos en Excel (30:19 - 1:02:03)

https://youtu.be/sPTQsLcC0TU?si=5HpORNoojZroypPk&t=1854


Se eleva la teoría de colas a su aplicación gerencial para encontrar el punto de equilibrio financiero y la optimización de decisiones. Utilizando herramientas de cálculo automatizadas, se aplican fórmulas analíticas a dos escenarios:

- **Nodos de Internet (Comparativa de Tiempos):** Se evalúa si es mejor tener 3 servidores lentos (20 peticiones/min) o 1 servidor rápido (60 peticiones/min) para una llegada de 50 peticiones/min. Se demuestra matemáticamente que el servidor único ultra-rápido reduce drásticamente el tiempo total de permanencia (W).
    
- **El Banco (Optimización de Costos):** La gerencia debe decidir matemáticamente cuántas ventanillas abrir (cambiar la variable _s_) basándose en una función de Costo Total. La cantidad óptima no es "la que atienda más rápido", sino la que logre el menor costo compensatorio sumando gastos operativos y penalidades.
    
    - **Cajeros Abiertos (s):** Representan el **Costo de Servicio** ($70/hora). El costo sube linealmente al agregar empleados.
        
    - **Personas en Sistema (L):** Representan el **Costo de Espera** ($180/hora). El costo baja porque un mayor número de cajeros reduce drásticamente el Tiempo Promedio en el Sistema (W).
        
    - **Conclusión:** Mediante la prueba iterativa de escenarios (_s_ = 3, 4, 5, 6), el profesor demostró que la configuración óptima que minimiza la curva del Costo Total es la de **4 cajeros**, superando en rentabilidad a las opciones de tener 3 o 5 ventanillas abiertas.

### IV. Simulación Discreta: Ejercicio "La Panadería" (1:18:06 - 1:40:37)

Retorno a la construcción empírica usando el Método de Montecarlo aplicado a colas (Ejercicio 9) para sistemas con reglas lógicas que escapan a la fórmula analítica simple. Se simula una panadería con llegadas por Distribución Exponencial y 2 empleados operando bajo una Distribución Uniforme.

- **Tip de Modelado para Servidores en Paralelo:** Al tener dos empleados atendiendo de forma independiente, es metodológicamente obligatorio separarlos estructuralmente para evitar colisiones lógicas en el Excel. No se puede usar un evento general; cada empleado requiere su propia columna de **Fin de Atención** para poder registrar el inicio de ocupación individual y calcular su Tiempo Ocioso o tiempo de ocupación exacto.

```
graph TD
    A[Ocurre Evento: Llegada de Cliente] --> B{¿Empleado 1 Libre?}
    B -- SI --> C[Ocupar Empleado 1 y calcular su Fin Atencion]
    B -- NO --> D{¿Empleado 2 Libre?}
    D -- SI --> E[Ocupar Empleado 2 y calcular su Fin Atencion]
    D -- NO --> F[Incrementar variable: Cola de Clientes]
```

### V. Planteo del Ejercicio "CPU y Terminales" (1:40:37 - 1:52:40)

El profesor deja como tarea el complejo Ejercicio 6, retomando el diseño del Vector de Estado pero aplicándolo a escenarios no lineales. Introduce el concepto de interrupción y servicios segmentados en la simulación discreta de alta complejidad.

- **El Sistema:** Un entorno de procesamiento multitarea (_Time-Sharing_) donde la CPU procesa tareas de múltiples terminales.
    
- **Servicio Segmentado:** En lugar de atender a un cliente de principio a fin, la CPU atiende a los requerimientos mediante porciones fijas de tiempo denominadas "Quantum" (**0.1 seg**), sumando un costo por cambio de contexto (**0.015 seg**), y expulsa a la entidad nuevamente a la cola.
    
- **Reglas de Negocio y Eventos:** Se debatió la naturaleza de los eventos, concluyendo que el único evento crítico a simular es el **Fin de Proceso**. El diseño de la simulación debe adaptarse rígidamente a estas reglas.
    
- **Variable Clave:** Esta dinámica obliga a crear nuevas variables de estado. Las entidades deben arrastrar obligatoriamente una variable acumulativa de **Tiempo Remanente** para saber si la tarea vuelve a la cola o si se destruye al finalizar definitivamente.

---







---
### esto nose dsp ver que contenido puede sumar

#### 3. Evaluación Económica y Optimización de Decisiones

El tercer tema elevó la teoría de colas a su aplicación gerencial: **encontrar el punto de equilibrio financiero**. Utilizando el caso del Banco, el profesor demostró que la cantidad de servidores óptima no es simplemente "la que atienda más rápido", sino aquella que logre el menor **Costo Total**. Esto se logra calculando una función de costos compensatoria: sumar el gasto operativo de mantener las ventanillas abiertas (Costo de Servicio) más la penalidad monetaria que el banco asume por tener a sus clientes perdiendo el tiempo (Costo de Espera). Modificando la variable $s$ (cantidad de servidores), se busca el punto matemático más bajo de esa curva.

---
Aplicando la teoría analítica en herramientas de cálculo automatizadas, se evaluaron diferentes configuraciones para lograr la optimización económica del negocio. El caso paradigmático analizado fue el de una sucursal bancaria, donde la gerencia debía determinar matemáticamente cuántas ventanillas abrir (cambiar la variable $s$) basándose en una función de [[Costo Total]].

|Variable del Sistema|Concepto Asociado|Dinámica de Optimización Matemática|
|:--|:--|:--|
|**Cajeros Abiertos ($s$)**|[[Costo de Servicio]]|El costo sube linealmente al agregar empleados.|
|**Personas en Sistema ($L$)**|[[Costo de Espera]]|El costo baja porque un mayor número de cajeros reduce drásticamente el [[Tiempo Promedio en el Sistema]] ($W$).|

Al iterar los escenarios en el Excel, el profesor demostró que contratar 4 cajeros representaba el punto más bajo en la curva de costos, superando en rentabilidad a las opciones de tener 3 o 5 ventanillas abiertas.

#### 4. Simulación Discreta de Alta Complejidad (Servidores Múltiples y Multitarea)

El cuarto tema retomó el diseño del **[[Vector de Estado]]** pero aplicándolo a escenarios no lineales.

- A través del ejercicio de "La Panadería", se enseñó a gestionar **[[Servidores Paralelos]]**, demostrando que cada entidad debe tener su propia columna de evento y acumuladores independientes para evitar colisiones lógicas en el Excel.
- Con el planteo de "CPU y Terminales", se introdujo el concepto de **interrupción y segmentación del servicio**. En lugar de atender a un cliente de principio a fin, el servidor atiende por un fragmento de tiempo fijo y expulsa a la entidad nuevamente a la cola. Esto obliga a los alumnos a crear nuevas variables de estado, como el **[[Tiempo Remanente]]**, demostrando que el diseño de eventos en la simulación discreta debe adaptarse rígidamente a las reglas del negocio.

---
En el último tramo, la clase volvió a la construcción empírica usando el [[Método de Montecarlo]] para sistemas que tienen reglas lógicas que escapan a la fórmula analítica simple.

Se desarrollaron dos escenarios avanzados:

- **[[Servidores en Paralelo]] (La Panadería):** Al tener dos empleados atendiendo de forma independiente, es metodológicamente obligatorio separarlos estructuralmente. No se puede usar un evento general; cada empleado requiere su propia columna de [[Fin de Atención]] para poder aislar y calcular su [[Tiempo Ocioso]] o tiempo de ocupación exacto.
- **Servicios Segmentados (CPU y Terminales):** Se debatió un sistema de procesamiento multitarea (Time-Sharing) donde la CPU atiende a los requerimientos mediante porciones fijas de tiempo denominadas "Quantum". Dado que la CPU expulsa a las tareas de nuevo a la cola al consumir su tiempo, el grupo acordó que el suceso crítico es el evento de [[Fin de Proceso]] y que las entidades deben llevar obligatoriamente una variable acumulativa de [[Tiempo Remanente]] para saber cuándo destruirlas.

```
graph TD
    A[Ocurre Evento: Llegada de Cliente] --> B{¿Empleado 1 Libre?}
    B -- SI --> C[Ocupar Empleado 1]
    C --> D[Calcular Reloj de Fin de Atencion 1]
    B -- NO --> E{¿Empleado 2 Libre?}
    E -- SI --> F[Ocupar Empleado 2]
    F --> G[Calcular Reloj de Fin de Atencion 2]
    E -- NO --> H[Derivar cliente e Incrementar Cola]
```

_Conceptos relacionados para el modelado práctico:_ [[Iteración de Eventos]], [[Vector de Estado]], [[Distribución Uniforme]], [[Condición de Corte]].



#### ---

#### 2. La "Trampa" de la Tasa vs. Tiempo Medio

En la parte analítica, el profesor hizo una pausa para advertir sobre el error más común al calcular el [[Factor de Utilización]] ($\rho$). En los enunciados, los datos pueden venir expresados de dos formas distintas, y confundirlos arruina todo el ejercicio.

|Concepto|Formato en el Enunciado|Operación Matemática Requerida|
|:--|:--|:--|
|**[[Tasa de Llegada / Servicio]]** ($\lambda$ o $\mu$)|"50 peticiones por minuto"|Se usa **directamente** en la fórmula.|
|**[[Tiempo Medio]]**|"Demora 3 segundos por petición"|Se debe **calcular la inversa** ($1 / \text{Media}$) para obtener la tasa.|

---

#### 🙋‍♂️ Consultas Relevantes de los Alumnos en Clase

La clase tuvo una alta participación. A continuación, se resumen las preguntas clave de los estudiantes y las respuestas del profesor:


> [!question] 3. Intuición sobre la optimización de servidores (Múltiples vs. Único) **Profesor:** Al presentar el caso de reemplazar 3 servidores lentos por 1 servidor rápido, el profesor invirtió el rol y preguntó a la clase: _“¿Qué les dice la intuición? ¿Va a haber algún cambio en el tiempo de espera?”_ **Alumno:** _“El factor $\rho$ va a ser el mismo... pero sí, sí va a haber un cambio en el tiempo de espera ($W_q$).”_ **Respuesta del profesor:** Validó la respuesta. Confirmó que aunque el [[Factor de Utilización]] ($\rho$) se mantiene igual, concentrar el trabajo en un **único servidor ultra-rápido reduce drásticamente el [[Tiempo Promedio en el Sistema]]** ($W$), rompiendo la intuición de que "más servidores siempre es mejor".

> [!question] 4. Dudas matemáticas sobre el pasaje de Tiempo a Tasa **Alumno:** _“Profe, no sé cómo calcular uno sobre la media... ¿de dónde sale ese 20?”_ (Refiriéndose a la [[Tasa de Servicio]]). **Respuesta del profesor:** Explicó paso a paso la conversión de unidades. Si el tiempo es de 3 segundos por petición, la tasa es de $1/3$ peticiones por segundo. Para igualar las unidades a minutos (ya que las llegadas estaban en minutos), multiplicó ese tercio por 60 segundos, obteniendo una tasa final de **20 peticiones por minuto**.

> [!question] 5. Lógica del Sistema "Time-Sharing" (CPU y Terminales) - Tamaño de la Cola **Alumno:** _“O sea profe, ¿siempre va a haber una cola de tamaño $m$?”_ (Refiriéndose a las terminales enviando tareas). **Respuesta del profesor:** _“Exacto.”_ Le confirmó que, dado que el sistema dicta que en el instante en que una tarea termina, la terminal dispara automáticamente otra para reemplazarla, el sistema mantendrá de forma constante un volumen $m$ de tareas circulando.

> [!question] 6. Lógica del Sistema "Time-Sharing" - Identificación de Eventos **Profesor:** _“¿Qué eventos les parece que hay en el sistema?”_ **Alumno 1:** _“Un fin de tarea.”_ **Alumno 2:** _“¿Habría también un fin de tiempo de servicio que no es lo mismo que el fin de la tarea?”_ (refiriéndose a cuando se acaba el 'quantum' o porción de tiempo que da la CPU pero la tarea aún no se completó). **Respuesta del profesor:** Guió a los alumnos para unificar ambos conceptos en el [[Vector de Estado]]. Les indicó que **no es necesario crear múltiples eventos**, sino que se modela un único evento llamado **[[Fin de Proceso]]**. La diferencia estructural radicará en que las entidades arrastrarán un atributo interno de **[[Tiempo Remanente]]**.

```
graph TD
    A[Evento Único: Fin de Proceso] --> B{¿Tiempo Remanente > 0?}
    B -- SÍ --> C[La tarea vuelve a la Cola]
    B -- NO --> D[La tarea finaliza y se destruye]
    D --> E[La terminal dispara una Nueva Tarea]
```

_(Diagrama Lógico de la resolución acordada entre el profesor y los alumnos para el ejercicio de la CPU)_