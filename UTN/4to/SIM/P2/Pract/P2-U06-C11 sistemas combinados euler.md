
# Guía de Resolución Definitiva: [[Sistemas Combinados]] de Nivel Medio

He analizado la resolución en vivo del profesor sobre el ejercicio de "Venta de Agua Embotellada". Este caso representa un modelo de parcial clásico porque combina la generación de múltiples [[Variables Aleatorias]], restricciones lógicas estrictas y resolución numérica mediante [[Ecuaciones Diferenciales]].

Aquí tienes la estructura detallada, las fórmulas obligatorias y las "trampas" críticas que debes evitar para aprobar.

---

## 1. Planteo del Modelo y Diseño del [[Vector de Estado]]

El primer paso es clasificar las entidades y definir cómo interactuarán en tu planilla.

|Categoría|Elemento en el Modelo|Diseño en el [[Vector de Estado]]|
|:--|:--|:--|
|**[[Objetos Temporarios]]**|[[Pedido]] / [[Llamada]]|Nace cuando un cliente llama. Sus estados son: `[[Siendo Registrado]]`, `[[Esperando Reparto]]` y `[[Siendo Entregado]]`.|
|**[[Objetos Permanentes]]**|[[Empleado]] (Teléfono)|Actúa como servidor principal para tomar los pedidos. Estados: `[[Libre]]` o `[[Ocupado]]`.|
|**[[Objetos Permanentes]]**|[[Vehículos]] de Reparto|Servidores secundarios (hay 2 en este caso). Estados: `[[Libre]]` o `[[Ocupado]]`.|

> [!danger] TRAMPA TEÓRICA: La Cola Inexistente El enunciado establecía que si la línea telefónica está ocupada, la llamada se pierde,. **Nunca debes crear una columna de `Cola de Espera` para el teléfono**. El pedido pasa directamente del estado de `[[Creación]]` a `[[Destrucción]]`.

---

## 2. Lógica de Simulación (Flujo del Sistema)

Para procesar cada línea de tu Excel sin equivocarte, debes seguir esta secuencia lógica mental cada vez que ocurre un evento de llegada:

```
graph TD
    A[Llegada de Llamada/Pedido] --> B{¿Empleado Libre?}
    B -- NO --> C[Pedido pasa a Destruccion y se registra Llamada Perdida]
    B -- SI --> D[Empleado Ocupado: Inicia Registro]
    D --> E[Calcular Fin de Registro]
    E --> F[Al finalizar registro: Generar Tamaño y Distancia]
    F --> G{¿Vehiculo Libre?}
    G -- NO --> H[Guardar Atributos y pasar a Esperando Reparto]
    G -- SI --> I[Ocupar Vehiculo y pasar a Siendo Entregado]
    I --> J[Integrar con Euler para obtener Tiempo]
    J --> K[Generar Fin de Reparto]
```

_Conceptos relacionados:_ `[[Transición de Estados]]`, `[[Integración Numérica]]`, `[[Atributos de Entidad]]`.

---

## 3. Fórmulas y Generación de [[Variables Aleatorias]]

El profesor aplicó diferentes generadores dependiendo de la naturaleza de la variable (continua o discreta).

> [!note] Fórmula: Tiempo entre Llegadas ([[Distribución Exponencial]]) $$X = -Media \cdot \ln(1 - RND)$$ _Aplicación en clase:_ Se utilizó una media de 8 minutos para las llegadas,.

> [!note] Fórmula: Distancia a Recorrir ([[Distribución Uniforme Continua]]) $$X = A + RND \cdot (B - A)$$ _Aplicación en clase:_ Para distancias entre 1 y 2 km,.

### El Problema de la Variable Uniforme Discreta

El tamaño del pedido era una variable uniforme entre 5 y 30 bidones, pero en números enteros (no puedes llevar 5.3 bidones).

> [!tip] Tip Metodológico: Cómo generar la [[Uniforme Discreta]] **No uses la fórmula continua truncada directamente** porque el límite superior ($B=30$) nunca saldrá, ya que el $RND$ nunca vale 1 exacto. Tienes dos opciones correctas:
> 
> 1. **La ideal:** Crear una [[Tabla de Probabilidad Acumulada]] (tipo Montecarlo) dividiendo $1$ sobre la cantidad de opciones (ej. $1/26$),.
> 2. **El atajo matemático:** Sumarle 1 al límite superior y aplicar truncamiento. $$X = TRUNCAR(A + RND \cdot ((B + 1) - A))$$

---

## 4. Resolución de [[Sistemas Combinados]] mediante [[Euler]]

Cuando el pedido sale a reparto, el tiempo de entrega no es estadístico, sino que depende de una [[Ecuación Diferencial]] que debes resolver en una tabla auxiliar.

> [!note] Fórmulas Base: [[Integración de Euler]] $$ t_{i+1} = t_{actual} + h $$ $$ y_{i+1} = y_{actual} + h \cdot y'_{actual} $$ _Iteras estas fórmulas arrastrando en Excel hasta que $y$ (la distancia simulada) supere el valor objetivo generado aleatoriamente_,.

> [!note] Fórmula CRÍTICA: [[Equivalencia de Tiempo]] Cuando la tabla de Euler supera el objetivo, el valor de $t$ obtenido NO son minutos, son unidades de integración. $$ Tiempo_Real = t_Euler \times Factor_de_Conversion $$ _Ejemplo del profe:_ Si $t=0.8$ y el enunciado dice que 1 unidad equivale a 10 minutos, el tiempo a sumar en tu reloj es $0.8 \times 10 = 8$ minutos,.

---

## 5. Tips de Parcial (Atajos del Profesor)

> [!tip] Tip de Parcial: El valor de $h$ (Paso de Integración) Si el enunciado del parcial no te especifica qué valor de $h$ utilizar para Euler, debes asumir $h=0.1$ por defecto,. Aunque un $h$ más pequeño (como $0.0001$) da resultados más precisos y cercanos a la solución analítica real, no es viable para resolver rápidamente a menos que se exija.

> [!tip] Tip Metodológico: Memoria de Atributos ¿Cuándo saco los randoms del pedido? El profesor aconseja que **generes la cantidad de bidones y la distancia justo cuando el empleado termina de registrar la llamada**,. _Obligatoriedad:_ Si el pedido no encuentra vehículo y debe ir a la cola de espera, **es obligatorio que guardes esos valores generados en atributos** de la entidad, porque si no lo haces, perderás esa información para cuando el vehículo finalmente se libere,.

> [!tip] Tip de Identificación: [[Subíndices de Servidor]] Cuando uses múltiples servidores idénticos (ej. Vehículo 1 y Vehículo 2), debes registrar en una columna **qué vehículo exacto está llevando qué pedido** (ej. "Siendo entregado por Vehículo 2"),. Esto evita inconsistencias cuando ocurra un evento de `[[Fin de Reparto]]` y necesites saber qué servidor se acaba de liberar.

---

## 6. Trampas Mortales y Errores Frecuentes

El profesor remarcó errores lógicos severos que anulan la consistencia de tu simulación:

> [!danger] TRAMPA 1: Asumir tiempos de Ida y Vuelta La ecuación diferencial modela el viaje completo. **No puedes asumir arbitrariamente que la mitad del tiempo es para ir y la mitad para volver**. El pedido se considera entregado estadísticamente en el instante en que el vehículo regresa a la empresa y libera el recurso, no a la mitad del trayecto,.

> [!danger] TRAMPA 2: El Identificador de los Objetos Rechazados Si llega el "Pedido 3" y el empleado está ocupado, la llamada se pierde. El error común es pensar que el siguiente cliente que entre exitosamente tomará el ID 3. **Falso.** El pedido rechazado **gasta un ID numérico**. El próximo cliente que llegue será obligatoriamente el "Pedido 4",.

---

## 7. Preguntas de Lógica en Clase

Durante la resolución, el profesor y los alumnos debatieron detalles clave de diseño:

> [!question] ¿Debo destruir la entidad en la misma línea en la que llega si es rechazada? **Alumno (Gaspar):** Preguntó si se debía poner el pedido en estado "Cancelado" y destruirlo en la iteración del siguiente evento futuro. **Respuesta del Profesor:** No. Es desfasado destruirlo en otro momento. En la misma iteración en la que el pedido llega y encuentra el servidor ocupado, pasa directamente del estado de `[[Creación]]` a `[[Destrucción]]`,.

> [!question] ¿Por qué un pedido con un trayecto más corto demora el mismo tiempo que uno largo? **Profesor:** Hizo notar que un pedido que debía viajar menos distancia tardó los mismos 8 minutos que el pedido anterior. ¿Por qué ocurre esto en la simulación combinada?. **Respuesta de los alumnos (validada):** Porque llevaba **más bidones**. En la ecuación diferencial, la cantidad de bidones ($k$) estaba dividiendo el incremento de la derivada. A mayor cantidad de bidones, menor velocidad del vehículo, lo que alarga el tiempo requerido en la tabla de Euler,.