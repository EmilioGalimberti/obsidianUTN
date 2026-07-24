


## V. Consultas Clave de los Alumnos en Clase



- **Criterio de Evaluación Crítico**: El profesor penaliza no mostrar explícitamente el resultado final. Debes tomar el valor del `[[Acumulador]]` final, dividirlo por el `[[Contador]]`, y anotar "Promedio = X" en una celda visible para que no te resten puntos.

---

# 2. 🛠 METODOLOGÍA DE RESOLUCIÓN (Paso a Paso)

El profesor insiste en NO empezar a dibujar la tabla de Excel sin antes hacer un planteo o "croquis" previo.

### Paso 1: Mapeo de Entidades y Estados

Identifica todos los elementos del sistema y clasifícalos en esta estructura obligatoria:

|Tipo de Elemento|Comportamiento en Simulación|Estados Comunes|
|:--|:--|:--|
|**[[Eventos]]**|Ocurrencias que cambian el [[Reloj del Sistema]].|N/A (Solo generan tiempo)|
|**[[Objetos Permanentes]]**|Servidores, cajas o empleados. Deben tener un atributo de `[[Cola]]` asociado.|`[[Libre]]`, `[[Ocupado]]`, `[[Bloqueado]]`|
|**[[Objetos Temporarios]]**|Clientes, vehículos o tareas.|`[[Esperando Atención]]`, `[[Siendo Atendido]]`, `[[Reparación Suspendida]]`|

