¡Hola! Como tu Tutor Académico de Élite, he analizado detalladamente la última transcripción correspondiente al ejercicio del "Ascensor". Esta clase introduce un nivel de complejidad superior: **Sistemas con [[Servidores Intermitentes]]** (servidores que a veces están disponibles y a veces desaparecen del sistema) y el **[[Agrupamiento de Eventos]]** masivos.

A continuación, te presento la guía metodológica definitiva, las fórmulas exigidas y las trampas críticas que el profesor remarcó para que no colapse tu simulación.

# Guía Avanzada: Resolución de Sistemas con Servidores Intermitentes y Agrupados

## 1. El Planteo Previo: Anatomía del Modelo

Cuando el servidor no está fijo en el lugar (como un ascensor o un inspector que hace rondas), la estructura del [[Vector de Estado]] requiere eventos secuenciales en cadena.

|Categoría|Elementos del Sistema|Conceptos Lógicos de Modelado|
|:--|:--|:--|
|**[[Objetos Permanentes]]**|Ascensor / Servidor|Sigue siendo permanente. Sus estados principales son `[[En Piso 15]]`, `[[Esperando Partir]]` y `[[En Tránsito]]` (cuando no está a la vista).|
|**[[Objetos Temporarios]]**|Pasajeros|Sus estados definen su intención para ahorrar columnas: `[[Esperando Subir]]`, `[[Esperando Bajar]]`, `[[Subiendo al Ascensor]]`.|
|**[[Eventos]]**|Llegadas y Fines secuenciales|No hay un simple "Fin de Atención". Se fragmenta en: `[[Llegada del Ascensor]]`, `[[Fin Descenso]]`, `[[Fin Ascenso]]` y `[[Fin Espera]]`.|

> [!tip] Tip Metodológico: Ahorro de Columnas de Atributos El profesor indicó que, en lugar de crear una columna de [[Atributo]] para cada cliente que diga "Dirección deseada", es mucho más eficiente crear estados específicos (`Esperando Subir` vs `Esperando Bajar`). Esto te ahorra espacio visual crítico en la planilla Excel y facilita los cálculos.

## 2. Dinámica de Simulación: Flujo Secuencial del Servidor Intermitente

A diferencia de los modelos anteriores donde un cliente llega y se atiende, aquí el servidor dicta el ritmo en una secuencia ininterrumpida.

```
graph TD
    A[Ocurre Evento: Llegada de Ascensor] --> B[Calcular pasajeros que descienden]
    B --> C[Generar Evento: Fin Descenso]
    C --> D[Al ocurrir Fin Descenso, calcular espacio libre]
    D --> E[Subir pasajeros en espera segun direccion y capacidad]
    E --> F[Generar Evento: Fin Ascenso]
    F --> G[Al ocurrir Fin Ascenso, generar Tiempo de Espera 6 seg]
    G --> H{¿Llega alguien durante la espera?}
    H -- SI --> I[Subir pasajero y RESETEAR los 6 segundos]
    H -- NO --> J[Ascensor pasa a estado En Transito]
```

_Conceptos relacionados al gráfico:_ `[[Evento Secuencial]]`, `[[Capacidad Restringida]]`, `[[Interrupción por Reseteo]]`.

## 3. 🚨 Trampas Mortales y Errores de Modelado

El profesor dedicó gran parte de la clase a explicar errores que anulan el ejercicio por completo. Presta especial atención a estos tres:

> [!danger] TRAMPA 1: Multiplicar Tiempos Constantes vs. Distribuciones **El mayor peligro de la clase:** Cuando agrupan a 3 personas subiendo a un ascensor, ¿pueden multiplicar el tiempo por 3? **Regla de Oro:**
> 
> - Si el tiempo es **CONSTANTE** (ej. "demora 6 segundos exactos por persona"): **SÍ se puede multiplicar**. Tiempo total = $3 \times 6 = 18$ segundos.
> - Si el tiempo es una **[[Distribución Estadística]]** (ej. "demora un tiempo Uniforme entre 4 y 8 segundos"): **PROHIBIDO MULTIPLICAR**. Si lo haces, alteras la varianza del generador. Estás obligado a extraer 3 números aleatorios distintos y sumar los tres resultados individuales.

> [!danger] TRAMPA 2: Inventar Estados "Incomprobables" Cuando el ascensor se va del Piso 15 hacia arriba, el instinto es ponerle estado `Subiendo`. **Esto es un error conceptual grave**. Como tu sistema solo monitorea el Piso 15, no sabes en qué momento exacto el ascensor llega a la terraza y empieza a bajar. Por ende, debes asignarle el estado `[[En Tránsito]]` y crear una variable auxiliar llamada `[[Última Dirección Conocida]]` para recordar para dónde se había ido, recién actualizándola cuando vuelva a aparecer en tu piso.

> [!danger] TRAMPA 3: Tablas Infinitas de Probabilidad vs. Truncamiento El enunciado decía que la cantidad de personas que baja es una variable uniforme discreta entre $0$ y $H$ (la gente a bordo). Si haces una tabla de Montecarlo clásica para calcular esto, tendrías que hacer una tabla distinta para $H=1$, $H=2$, $H=3$, etc. ¡Un infierno en el Excel! _Ver la solución en la sección de fórmulas abajo._

## 4. Fórmulas Matemáticas y el Atajo de la Uniforme Discreta

> [!note] Fórmula: Generador Exponencial Negativo Se utiliza para el evento de `[[Llegada de Pasajero]]` (la media debe estar en la misma unidad que el reloj, ej. minutos). $$X = -media \cdot \ln(1 - RND)$$

> [!tip] EL GRAN ATAJO (Tip de Parcial): Convertir Uniforme Continua a Discreta Para evitar hacer múltiples tablas de probabilidades para saber cuánta gente baja, el profesor enseñó a utilizar la fórmula de la **[[Distribución Uniforme]] Continua**, sumándole $1$ al límite superior ($B$) y aplicando la función `TRUNCAR` (quitar decimales sin redondear).
> 
> **Fórmula Original Continua:** $X = A + RND \cdot (B - A)$ **Adaptación Discreta:** $$X = TRUNCAR(A + RND \cdot ((B + 1) - A))$$ _Ejemplo del profe:_ Si vienen 5 personas ($B=5$, $A=0$), la fórmula queda $X = TRUNCAR(0 + RND \cdot 6)$. Esto le da equidad exacta a las probabilidades del $0, 1, 2, 3, 4$ y $5$, ahorrándote 6 tablas de cálculo.

## 5. Consultas Relevantes de los Alumnos

Al final de la clase, los alumnos aprovecharon para preguntar sobre otro ejercicio complejo que suele ser material de parcial.

> [!question] Lógica de Atributos: El Ejercicio del Parquímetro **Alumno:** Consultó sobre el ejercicio 39 (estacionamiento/parquímetros), donde los autos tienen diferentes intenciones de tiempo, y algunos pagan y otros no. Preguntó cómo manejar si un auto está en infracción. **Respuesta del Profesor:** Le explicó que, al ser un modelo avanzado, **no debe mezclar las decisiones**. Debe crear atributos completamente separados para cada auto en el instante de su llegada:
> 
> 1. Un atributo para **"¿Cuánto tiempo real desea quedarse?"** (1 o 2 horas).
> 2. Un atributo aleatorio independiente para **"¿Paga o no paga?"** (3% paga, 97% no). El profesor aclaró que recién cruzando esas dos variables lógicas, el sistema puede determinar si un auto pasa a un estado de `[[Infracción]]` o no. Las parcelas de estacionamiento, al igual que los cajeros, funcionan como los `[[Objetos Permanentes]]`.