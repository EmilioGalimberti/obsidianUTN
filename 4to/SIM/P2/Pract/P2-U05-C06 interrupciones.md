¡Hola! Como tu Tutor Académico de Élite, he analizado detalladamente la transcripción de tu última clase. Esta sesión introduce uno de los escenarios más complejos en el modelado de [[Sistemas de Colas]]: los **Sistemas con [[Interrupciones]] y Diferentes Niveles de [[Prioridad]]** (ejemplificados con la Zapatería y el Consultorio Médico).

A continuación, te presento la guía metodológica definitiva, las fórmulas requeridas y las "trampas" críticas que el profesor señaló para evitar que tu simulación colapse en el examen.

---

# Guía de Resolución: Sistemas con Interrupciones y Prioridades

## 1. El Planteo Previo (Análisis de Prioridades)

Cuando un modelo indica que un evento puede "suspender" a otro, la estructura tradicional del [[Vector de Estado]] cambia. Debes clasificar los [[Objetos Temporarios]] en niveles de prioridad.

|Nivel de Prioridad|Ejemplos en Clase|Regla Lógica de Modelado|
|:--|:--|:--|
|**Alta Prioridad**|[[Cliente]] (Zapatería), [[Urgencia]] (Consultorio)|Su llegada interrumpe inmediatamente cualquier tarea de menor prioridad.|
|**Baja Prioridad**|Zapatos, Consulta Normal|Su atención solo inicia o se reanuda si la cola de Alta Prioridad está vacía.|

> [!danger] TRAMPA DE MODELADO: Mezclar Entidades en una Cola El profesor fue tajante: **"No puedo meter a estos dos en la misma cola porque tienen distinta prioridad"**. Si tienes objetos de distinta jerarquía, es obligatorio crear una columna de [[Cola]] separada para cada uno (ej. `Cola de Consultas` y `Cola de Urgencias`).

## 2. Lógica de Resolución Iterativa: La Interrupción

El motor de la simulación cambia drásticamente cuando ocurre un evento de alta prioridad. Debes seguir este algoritmo mental:

```
graph TD
    A[Llegada de Entidad de Alta Prioridad] --> B{¿Servidor atendiendo Baja Prioridad?}
    B -- SI --> C[Suspender tarea actual]
    C --> D[Calcular y guardar Tiempo Remanente]
    D --> E[Tachar/Cancelar el evento de Fin Original]
    E --> F[Pasar Servidor a atender Alta Prioridad]
    B -- NO --> G{¿Servidor Libre?}
    G -- SI --> H[Atender Alta Prioridad]
    G -- NO --> I[Derivar a Cola de Alta Prioridad]
```

_Conceptos Relacionados:_ [[Procesos Suspendidos]], [[Vector de Estado]], [[Llegada al Sistema]].

### Reanudación del Servicio (Fin de Atención)

Cuando el servidor termina con la entidad de Alta Prioridad, las preguntas que se hace (en orden estricto) son:

1. _¿Hay más entidades de Alta Prioridad en espera?_ Si la respuesta es NO, pasa a la 2.
2. _¿Tengo alguna tarea de Baja Prioridad suspendida a medias?_ Si la respuesta es SÍ, la retoma.
3. _¿Hay nuevas tareas de Baja Prioridad en su cola?_ Solo las atiende si las respuestas 1 y 2 fueron negativas.

## 3. Fórmulas Matemáticas Clave

Para gestionar correctamente la interrupción sin que el objeto pierda su progreso, debes dominar el concepto de **[[Tiempo Remanente]]** (o tiempo faltante).

> [!note] Fórmula: Cálculo del Tiempo Remanente (Al Interrumpir) En el instante exacto en que llega la interrupción, debes calcular cuánto le faltaba a la tarea original para terminar y guardarlo en una columna dedicada: $$Tiempo_Remanente = Hora_Fin_Original - Reloj_Actual$$ _Ejemplo del profe:_ Si iba a terminar en el min 28.98 y la interrupción ocurrió en el 22.21, le faltaban 6.77 minutos.

> [!note] Fórmula: Reanudación de la Tarea (Nuevo Fin) Cuando el servidor finalmente se libera y retoma la tarea suspendida, se calcula su nuevo tiempo de finalización usando el remanente guardado: $$Nuevo_Fin_Atencion = Reloj_Actual + Tiempo_Remanente$$ _(Una vez usado, el valor de tiempo remanente se borra o se deja en blanco para la siguiente línea)_.

---

## 4. Advertencias Críticas y "Trampas" de Parcial

El profesor hizo muchísimo énfasis en los siguientes errores que destruyen la consistencia del [[Vector de Estado]]:

> [!danger] TRAMPA MORTAL 1: Predecir el futuro al reanudar **Error común:** Al interrumpir una tarea, sumar inmediatamente el tiempo de la urgencia al fin original para saber a qué hora terminará en el futuro. **Por qué está mal:** El profesor advirtió que _"si en el medio te llega otro cliente, te tumba también ese evento"_. **NUNCA calcules el nuevo fin de atención anticipadamente**. Guarda el [[Tiempo Remanente]] y vuelve a calcular el evento ÚNICAMENTE cuando el servidor pase efectivamente a retomar la tarea.

> [!danger] TRAMPA MORTAL 2: Ignorar las Condiciones Iniciales Por defecto los sistemas arrancan vacíos, pero en los parciales suelen dar **[[Condiciones Iniciales]]**. En el ejemplo de la zapatería, el enunciado decía que el local ya tenía 3 pares reparados con 45 minutos acumulados de trabajo. Si inicias tus contadores y acumuladores en 0 ignorando esto, **toda tu estadística final será incorrecta** y el problema estará mal.

> [!danger] TRAMPA MORTAL 3: Eliminar el evento cancelado sin tachar Cuando un proceso es interrumpido, el evento de "Fin de Reparación/Consulta" que estaba proyectado en el futuro **se cancela**. Para evitar confundirte y bajar ese número al reloj por accidente en la siguiente línea, el profesor recomienda **dejar la celda en blanco** en la nueva iteración (o hacerle una línea de tachado si estás en papel).

> [!question] Pregunta Frecuente: El estado de la entidad interrumpida **Profesor:** _"¿A qué estado pasa el zapato cuando llega el cliente?"_ **Respuesta Oficial:** No pasa a "Esperando Reparación", porque ya fue procesado a medias. Debe pasar a un estado especial y único llamado **[[Reparación Suspendida]]**. Esto lo diferencia de los objetos que están en la cola y a los que les falta el 100% del proceso.