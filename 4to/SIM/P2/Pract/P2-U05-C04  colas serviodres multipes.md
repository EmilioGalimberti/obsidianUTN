¡Hola! Como tu Tutor Académico de Élite, he analizado la nueva transcripción correspondiente a la clase de **[[Sistemas de Colas]] con [[Servidores Múltiples]]** (Ejemplos: La Estación de Servicio y La Municipalidad).

Antes de comenzar con la estructura, debo darte una advertencia administrativa fundamental que el profesor dio al inicio de esta clase específica:

> [!danger] Aclaración Administrativa Crítica El profesor aclaró explícitamente que los temas de esta clase (Sistemas de colas y servidores múltiples) **NO entran en el primer parcial**. El primer parcial incluye solo hasta la Unidad 4 (inclusive), abarcando todo lo referente a la [[Simulación de Montecarlo]]. Esta guía te servirá de base para el **Segundo Parcial**.

A continuación, te presento la estructura definitiva de resolución, las fórmulas y las trampas lógicas para modelar sistemas con múltiples servidores.

---

### 1. El Planteo Previo: Definición de Variables Complejas

Cuando un modelo tiene más de un servidor para el mismo servicio (ej. 2 surtidores, 3 cajas de cobro), la estructura cambia drásticamente. Debes realizar el siguiente planteo obligatorio:

|Categoría|Elemento en el Modelo|Concepto de Modelado|
|:--|:--|:--|
|**[[Eventos]]**|Fin de Atención en Cajas 1, 2 o 3|**[[Evento Sub i]]**: Se declara como `Fin_Atencion_sub_i` donde $i = 1, 2, 3$. Se usa siempre que haya más de un cliente siendo atendido simultáneamente para el mismo servicio.|
|**[[Objetos Permanentes]]**|Surtidores / Cajas|Cada servidor individual debe tener su propio atributo de estado (ej. `Estado_Caja_1`, `Estado_Caja_2`).|
|**[[Colas]]**|Fila de espera|Se asume una **[[Cola Única]]** por defecto (ej. supermercado Carrefour) a menos que el enunciado explicite una **[[Cola Múltiple]]** (ej. "irán a la cola con menor número de autos").|
|**[[Objetos Temporarios]]**|Clientes|Requieren obligatoriamente un atributo de **[[Hora de inicio de espera]]** para poder calcular las demoras parciales y totales.|

---

### 2. Lógica de Resolución Iterativa y Fórmulas Clave

A diferencia de un modelo lineal, aquí los clientes pueden tomar múltiples caminos o ser atendidos en distinto orden.

> [!note] Fórmula para Acumulador: [[Tiempo Ocioso]] Para no perder el rastro del tiempo libre de los servidores, el profesor recomienda actualizarlo en cada línea de simulación: $$Tiempo_Ocioso_Acum = Valor_Anterior + (Reloj_Actual - Reloj_Anterior)$$ _Condición:_ Esto se suma **únicamente** si el servidor estaba en estado `Libre` en la línea o evento inmediato anterior.

> [!note] Fórmula para Acumulador: [[Tiempo de Espera]] $$Tiempo_Espera = Reloj_Actual - Hora_Inicio_Espera$$ _Condición:_ Este cálculo se realiza y se acumula **solo en el instante exacto en que el cliente deja de esperar** (cuando accede al servidor). No se acumulan "tiempos parciales" de clientes que siguen en la fila.

#### Diagrama de Flujo: Llegada a Servidores Múltiples

```
graph TD
    A[Ocurre Evento: Llegada Cliente] --> B{¿Hay ALGUN servidor Libre?}
    B -- SI --> C[Elegir un Servidor Libre]
    C --> D[Cliente pasa a Siendo Atendido]
    D --> E[Registrar EN QUE SERVIDOR esta]
    B -- NO --> F{¿Es Cola Unica o Multiple?}
    F -- Unica --> G[Incrementar Cola General]
    F -- Multiple --> H[Buscar Cola mas vacia e incrementar]
    G --> I[Registrar Hora Inicio de Espera]
    H --> I
```

_Conceptos Relacionados:_ [[Vector de Estado]], [[Llegada al Sistema]], [[Atributos Temporarios]].

---

### 3. Errores Comunes y "Trampas" de Parcial

El profesor hizo muchísimo énfasis en los siguientes errores, los cuales arruinan la simulación completa si te equivocas:

> [!danger] Trampa 1: El orden de llegada NO es el orden de salida Cuando un evento `Fin_Atencion_sub_i` ocurre, necesitas saber a qué cliente destruir. Como los tiempos de atención son aleatorios, el Cliente 4 podría terminar su servicio ANTES que el Cliente 3. **Regla de Oro:** Cuando un cliente accede a un servidor múltiple, **debes registrar obligatoriamente en qué servidor exacto está** (ej. `Siendo atendido en Caja 2`). Si no lo haces, la simulación colapsa porque no sabrás a quién sacarle el estado.

> [!danger] Trampa 2: Ignorar a los clientes que esperan "Cero" Si te piden el "Tiempo Promedio de Espera", el error clásico es promediar solo a los que hicieron fila. El profesor aclaró que si un cliente llega y encuentra el servidor libre, su [[Tiempo de Espera]] es $0$. **Debes sumarlo al contador de clientes que accedieron al servicio**. Si los omites, el promedio te dará matemáticamente más alto (peor) de lo que es en realidad.

> [!danger] Trampa 3: Mandar a hacer fila cuando hay lugar Ante una llegada, la lógica mental del simulador (o del cliente) SIEMPRE debe preguntar primero: _"¿Hay algún servidor libre?"_. Si hay un servidor libre, el cliente pasa directo. **Nunca envíes un cliente a hacer fila si hay al menos una instancia del servicio desocupada**.

> [!question] Pregunta Frecuente: Choque de Eventos **Alumno:** _¿Qué hacemos si el tiempo de la 'próxima llegada' y el 'fin de atención' calculan el mismo número exacto?_ **Respuesta del Profesor:** Eliges **cualquiera de los dos** al azar. Bajas ese evento al reloj, procesas todas las reglas de la tabla asumiendo el estado anterior, y en la siguiente línea (o iteración) procesas el evento que dejaste pendiente manteniendo el mismo tiempo en el reloj. No se procesan en la misma línea.