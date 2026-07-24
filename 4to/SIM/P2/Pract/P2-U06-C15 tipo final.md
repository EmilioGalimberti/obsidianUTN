# Guía de Resolución Definitiva: [[Simulación Combinada]] con [[Destrucción de Objetos]] y [[Condición Inicial Dinámica]]

He analizado la última clase magistral, la cual representa el nivel máximo de exigencia: un modelo de **Examen Final** (el "Caso del Lavadero de Autos"). Este modelo integra la separación y reensamblaje de entidades, junto con la resolución de [[Ecuaciones Diferenciales]] para variables que interactúan en tiempo real.

A continuación, la estructura metodológica, el flujo lógico y las "trampas mortales" que el profesor remarcó explícitamente.

## 1. El Planteo Previo: Anatomía del Modelo con Separación

En modelos donde un objeto se divide, no puedes llevar un solo atributo. Debes aplicar la **[[Destrucción de Objetos]]** y gestionar las partes de forma independiente hasta que se vuelvan a cruzar.

### Clasificación de Entidades y Estados

|Categoría|Elemento|Lógica de Modelado Exigida|
|:--|:--|:--|
|**[[Objetos Temporarios]]**|[[Vehículo Original]]|Llega al sistema, se atiende en la primera estación y **se destruye (se desarma)**, dando origen a sus componentes.|
|**[[Objetos Temporarios]] Derivados**|[[Alfombra]], [[Carrocería]]|Nacen a partir del evento de "Fin de Desarmado". Recorren áreas distintas (Aspirado vs. Lavado/Secado) de manera paralela.|
|**[[Eventos]]**|Llegadas, Fines de Atención|Cuando las dos partes terminan sus circuitos paralelos, confluyen en un evento de `[[Fin Colocación]]` donde se destruyen y **renace el Vehículo Original**.|
|**[[Objetos Permanentes]]**|Empleados, Boxes, Secadora|Estados básicos (`Libre`, `Ocupado`). En áreas múltiples (ej. 2 boxes de lavado), el servidor es el Box, y la Secadora es un servidor que se mueve entre ellos.|

## 2. Dinámica de Simulación: El Flujo de Separación y Reensamblaje

Para no perderte en el [[Vector de Estado]], tu algoritmo mental al avanzar el [[Reloj del Sistema]] debe seguir el circuito fragmentado:

```
graph TD
    A[Llegada de Vehiculo] --> B[Area: Quita Alfombra]
    B --> C{Destruccion y Separacion}
    C -- Genera Alfombra --> D[Area: Aspirado]
    C -- Genera Carroceria --> E[Area: Lavado]
    E --> F{¿Secadora Libre?}
    F -- SI --> G[Secado con Maquina]
    F -- NO --> H[Secado Solo/Natural]
    H --> I[Recalcular Humedad al liberarse Maquina]
    I --> G
    D --> J[Area: Pone Alfombra]
    G --> J
    J --> K{Reensamblaje Correcto}
    K --> L[Area: Encerado y Lustrado]
    L --> M[Salida del Sistema]
```

_Conceptos relacionados:_ `[[Bifurcación Paralela]]`, `[[Match de Entidades]]`, `[[Secado Asintótico]]`.

## 3. Fórmulas Matemáticas y [[Ecuaciones Diferenciales]]

Para el cálculo de los eventos estocásticos y continuos, se utilizan las siguientes directivas matemáticas.

> [!note] Fórmulas Generadoras Básicas **[[Distribución Exponencial Negativa]]** (Llegadas al lavadero): $$X = -Media \cdot \ln(1 - RND)$$ _El profesor aplicó $\mu = 10$ minutos._
> 
> **[[Distribución Uniforme]]** (Lavado de carrocerías entre 6 y 12): $$X = A + RND \cdot (B - A)$$

> [!note] Fórmulas: [[Integración de Euler]] Para la ecuación del secado (humedad de la carrocería en función del tiempo), se avanza el [[Paso de Integración ($h$)]]: $$ t_{i+1} = t_{actual} + h $$ $$ Humedad_{i+1} = Humedad_{actual} + h \cdot \left(\frac{dH}{dt}\right) $$ _Donde la derivada es la función de pérdida de humedad dictada por el enunciado._

## 4. 🚨 Trampas Mortales y Errores a Evitar (Tips de Parcial)

El profesor fue sumamente claro en indicar que los siguientes puntos son los que definen si el parcial está aprobado o si es un aplazo automático.

> [!danger] TRAMPA MORTAL 1: La [[Condición Inicial Dinámica]] **"Esto es lo nuevo que no habíamos hecho hasta ahora... es lo más importante de todo este ejercicio."**. Si una carrocería sale de lavarse y la máquina secadora está ocupada, se empieza a "secar sola" en el ambiente. **El Error:** Cuando la máquina se libera y va a atender esa carrocería, el alumno usa la humedad inicial de $100%$ en la tabla de Euler. **Lo Correcto:** Debes calcular cuánto tiempo se secó sola, usar la ecuación de secado natural para descubrir cuánta humedad perdió en ese tiempo, y arrancar la tabla de Euler de la máquina con esa **nueva humedad reducida** (ej. $55.17%$ en lugar de $100%$).

> [!danger] TRAMPA MORTAL 2: El [[Match de Entidades]] al reensamblar "No vamos a armar un vehículo nuevamente con cualquier alfombra y cualquier carrocería... hacemos un match". **La Regla de Oro:** Si tienes la Alfombra ID 1 esperando, y llega la Carrocería ID 3, **no puedes ensamblarlas**. El área se queda "Esperando contraparte" hasta que llegue la Carrocería ID 1.

> [!danger] TRAMPA MORTAL 3: La Equivalencia Bidireccional de Tiempo Si la unidad de tiempo del Vector (ej. minutos) y la de la Tabla de Euler (ej. intervalos de 10 mins) son diferentes, ocurre una trampa letal. **Dirección 1 (Tabla $\rightarrow$ Vector):** Si la tabla dice que tardó 2.3 intervalos, **multiplicas** por 10 para llevar 23 minutos al reloj. **Dirección 2 (Vector $\rightarrow$ Tabla):** Si necesitas saber cuánta humedad se perdió en 8 minutos reales, al buscar ese tiempo en la tabla de Euler, debes **dividir** por 10 (buscar 0.8 en la columna $t$).

> [!danger] TRAMPA ESTADÍSTICA: Conteo Adelantado y Colas Desordenadas
> 
> 1. **[[Contador de Sistema]]:** Jamás cuentes a los vehículos cuando llegan. Solo se suman al contador (para los promedios) en el instante en que **salen del sistema**.
> 2. **[[Orden de Fila al Final]]:** Como algunos vehículos tardan más que otros en los procesos intermedios, llegan desordenados al último paso (Encerado). Si hay más de uno esperando, no te sirve su ID para saber a quién atender primero; necesitas haberles creado un atributo de `[[Hora de llegada al servidor]]`.

> [!question] Pregunta Conceptual del Profesor: Secado Asintótico **Profesor:** "Con la ecuación diferencial de secado natural (exponencial negativa)... ¿cuándo llega la humedad a cero?". **Respuesta del Alumno:** "Nunca". **Lección:** Funciones como el decaimiento exponencial tienen al cero como asíntota. El tiempo que demora en llegar matemáticamente a 0 es **infinito**. El profesor indicó que en el examen debes anotar explícitamente $\infty$ en la celda o dejarlo registrado para demostrar que te diste cuenta de la trampa matemática.