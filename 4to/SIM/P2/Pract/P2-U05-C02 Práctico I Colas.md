¡Hola! Como tu Tutor Académico de Élite, he analizado detalladamente la transcripción de la clase teórica-práctica para extraer la metodología exacta que exige el profesor.

Aquí tienes la guía definitiva estructurada para resolver simulaciones de colas, incluyendo las fórmulas matemáticas requeridas y las "trampas" clásicas que debes evitar en el examen.

# Guía de Resolución: Simulación de Sistemas de Colas mediante Vector de Estado

La resolución de estos problemas de simulación paso a paso se divide en dos fases: el análisis previo y la iteración del [[Vector de Estado]].

## 1. El Planteo Previo (Análisis del Sistema)

Antes de dibujar la tabla en Excel, es obligatorio listar los componentes lógicos del sistema y definir sus distribuciones.

### Clasificación de Componentes

|Categoría|Elementos y Ejemplos|[[Estados]] Asociados|
|:--|:--|:--|
|**[[Objetos Permanentes]]**|[[Servidor]] (ej. Peluquero, Cajero)|[[Libre]], [[Ocupado]]|
|**[[Objetos Temporarios]]**|[[Cliente]] (ej. Personas, Tareas)|[[Esperando Atención]], [[Siendo Atendido]]|
|**[[Eventos]]**|[[Llegada al Sistema]], [[Fin de Atención]]|N/A|

## 2. Estructura del [[Vector de Estado]]

El profesor indicó que las columnas deben agruparse rígidamente en secciones lógicas (de izquierda a derecha):

1. **Nombre del Evento (Optativo):** Ayuda a rastrear errores.
2. **[[Reloj del Sistema]]:** El momento exacto en el que ocurre el evento.
3. **Sección de Eventos:** Columnas para calcular los tiempos futuros (RND, Tiempo de Llegada/Atención, Próxima Llegada/Atención).
4. **Sección de Objetos Permanentes:** Estado del servidor y tamaño de la [[Cola]].
5. **Sección de Variables Estadísticas:** Aquí van los [[Acumuladores]] (ej. Tiempo de Permanencia) y [[Contadores]] (ej. Clientes Atendidos).
6. **Sección de Objetos Temporarios:** Columnas por cada cliente activo mostrando su Estado y su Hora de Llegada.

---

## 3. Dinámica de Iteración: ¿Cómo procesar cada línea?

La simulación avanza buscando el evento futuro más cercano. El siguiente diagrama ilustra la lógica mental que debes aplicar en cada renglón:

```
graph TD
    A[Inicio de Iteracion] --> B{¿Cual es el menor tiempo proyectado?}
    B -- Proxima Llegada --> C[Avanzar reloj y procesar LLEGADA]
    B -- Fin Atencion --> D[Avanzar reloj y procesar SALIDA]

    C --> C1[Generar el tiempo de la proxima llegada futura]
    C1 --> C2{¿Servidor Libre?}
    C2 -- SI --> C3[Cliente: Siendo Atendido / Servidor: Ocupado / Generar Fin Atencion]
    C2 -- NO --> C4[Cliente: Esperando / Incrementa Cola]

    D --> D1[Destruir cliente actual y registrar estadisticas]
    D1 --> D2{¿Hay alguien en la cola?}
    D2 -- SI --> D3[Pasar cliente a Siendo Atendido / Decrementar Cola / Generar Fin Atencion]
    D2 -- NO --> D4[Servidor pasa a Libre]
```

_Conceptos relacionados al flujo:_ [[Reloj del Sistema]], [[Iteración de Simulación]], [[Transición de Estados]], [[Generador de Variables Aleatorias]].

---

## 4. Fórmulas Matemáticas a utilizar

En estos ejercicios, las frecuencias están dictadas por distribuciones estadísticas conocidas.

> [!note] Fórmulas de Generación de Eventos ([[Variables Aleatorias]]) **[[Distribución Exponencial Negativa]]** (Típicamente usada para Llegadas): $$X = -media \cdot \ln(1 - RND)$$
> 
> **[[Distribución Uniforme]]** (Típicamente usada para Tiempos de Atención): $$X = A + RND \cdot (B - A)$$

> [!note] Fórmulas de Desempeño Final ([[Medidas de Desempeño]]) **Tiempo Promedio de Permanencia:** $$Promedio = \frac{\text{Acumulador de Tiempo de Permanencia}}{\text{Contador de Clientes Atendidos}}$$
> 
> **[[Porcentaje de Ocupación del Servidor]]:** $$% Ocupación = \left( \frac{\text{Acumulador de Minutos Trabajados}}{\text{Reloj Final (Corte)}} \right) \cdot 100$$

---

## 5. Tips de Parcial y Metodología (Palabras del Profesor)

> [!tip] Tip de Parcial: Los Randoms ya vienen dados El profesor confirmó que en el parcial les entregarán una lista fija de números pseudoaleatorios (RND) para consumir. No deberán inventarlos con funciones de Excel, asegurando que todos tengan el mismo resultado.

> [!tip] Tip de Metodología: El Reloj en Formato Decimal Es altamente recomendable manejar el [[Reloj del Sistema]] como un valor decimal expresando minutos fraccionados (ej. `1.50` significa 1 minuto y medio) en lugar del formato hh:mm:ss. Esto facilita enormemente sumar tiempos generados.

> [!tip] Tip de Metodología: No intentes automatizar todo El Excel funciona como una "hoja de papel infinita". Puedes automatizar fragmentos lógicos pequeños (como la acumulación de tiempos libres/ocupados usando un `IF`), pero es muy difícil automatizar toda la simulación de colas y no es obligatorio.

---

## 6. Advertencias Críticas: Trampas y Errores Comunes

Presta especial atención a estas situaciones que el profesor recalcó como los peores errores en los exámenes:

> [!danger] TRAMPA MORTAL 1: Confundir Lambda ($\lambda$) con Media ($\mu$) El profesor fue tajante al respecto. Si el enunciado dice _"Frecuencia de 15 clientes por hora"_, **eso no es una media de 15**, es la tasa de llegadas ($\lambda$). Para inyectarlo en la fórmula exponencial, debes calcular la **media real** invirtiendo el valor: $\frac{60 \text{ min}}{15 \text{ clientes}} = \text{Media de 4 minutos}$. Si metes el 15 en la fórmula, anulas todo el ejercicio.

> [!question] Pregunta Frecuente del Profesor en Clase: El Conteo de Clientes **Profesor:** _"¿En qué momento tengo que contar a los clientes? ¿Cuando ingresan al sistema o cuando salen?"_ **Respuesta Oficial:** SIEMPRE CUANDO SALEN. **Peligro:** Si cuentas a un cliente cuando apenas entra, te quedarán cálculos estadísticos parciales si la simulación se corta antes de que termine de ser atendido, dándote un promedio falso y reduciendo tu calificación.

> [!danger] TRAMPA MORTAL 2: Inconsistencia Visual de Línea No puede existir una línea en tu Excel que diga en la columna de Servidor: `Cola = 2`, pero en tus columnas de Clientes temporales solo tengas un (1) cliente en estado `Esperando Atención`. Debe haber **consistencia absoluta**; el número entero de la cola refleja exactamente cuántas entidades están en espera.

> [!danger] TRAMPA MORTAL 3: ¿A quién interroga el Cliente? Cuando un cliente llega, NUNCA pregunta por la cola. Pregunta explícitamente por el **[[Estado del Servidor]]**. Si la cola está en cero y el cliente mira la cola, podría asumir falsamente que puede ser atendido inmediatamente, incluso si el servidor ya está `Ocupado` con alguien más. El flujo lógico siempre interroga al Servidor primero.