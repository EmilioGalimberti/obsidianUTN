
# 🔢 TODAS LAS FÓRMULAS

## Generadores de Variables Aleatorias

| Distribución                      | Fórmula                                                                     | Cuándo usarla                                       |
| :-------------------------------- | :-------------------------------------------------------------------------- | :-------------------------------------------------- |
| **Exponencial Negativa**          | $X = -media \cdot \ln(1 - RND)$                                             | cuando solo te dice 1 cada 90 min                   |
| **Exponencial Negativa**          |                                                                             | cuando te dice ya 6 cada 90 min                     |
| **Uniforme Continua**             | $X = A + RND \cdot (B - A)$                                                 | Tiempos de atención, distancias                     |
| **Uniforme Discreta**             | $X = TRUNCAR(A + RND \cdot ((B+1) - A))$                                    | Cantidades enteras (bidones, complejidad, personas) |
| **Normal (Box-Muller)**           | $N_1 = \mu + \sigma \cdot \sqrt{-2\ln(RND_1)} \cdot \cos(2\pi \cdot RND_2)$ | Tiempos normales (reparación, armado)               |
| **Normal (Box-Muller) 2do valor** | $N_2 = \mu + \sigma \cdot \sqrt{-2\ln(RND_1)} \cdot \sin(2\pi \cdot RND_2)$ | Usa los **MISMOS** 2 RND del N₁                     |


> [!CAUTION]
> **Box-Muller: NO quemar Randoms.** Sacás 2 RND → generás N₁ (coseno). Para el **siguiente** uso, usás los **mismos 2 RND** con la fórmula del seno (N₂). Recién al tercer uso sacás 2 RND nuevos.


## Equivalencia de Tiempo (Euler → Reloj)

$$Tiempo_{Real} = t_{Euler} \times Factor_{Conversión}$$

| Ejemplo | Factor |
|:--|:--|
| 1 unidad Euler = 10 min | ×10 |
| 1 unidad Euler = 60 seg | ×60 |
| 1 unidad Euler = 1 hora → reloj en min | ×60 |

> [!CAUTION]
> **NUNCA bajes el valor de Euler crudo al vector sin verificar la unidad.** Este error baja MUCHOS puntos.

##  (Estadísticas Finales) ==AGG como se arman los acum

Contadores

(ASINCRONO)
Acum tiempo de espera
	imporante guardar la hora de llegada del cliente
		Solo acumular cuando es atendido
	acum tiempo de espera = ValorAnterior+(Reloj Actual - hora llegada cliente)

$$\text{Tiempo Promedio de Espera} = \frac{\text{Acum. Tiempo de Espera}}{\text{Clientes que accedieron al servicio}}$$
ATENTO DE NO OLVIDARSE DE ACUMULAR 0, ES DECIR ENTRA Y NO ESPERA DEBEMOS ACUMULAR ESOS 0, 

acumu de tiempo de permanencia
	importante guardar la hora de llegada
		Solo acumular cuando en fin atencion
	acum tiempo de permanencia = ValorAnterior+(Reloj Actual - hora llegada cliente) 
$$\text{Tiempo Promedio de Permanencia} = \frac{\text{Acumulador de Tiempo}}{\text{Contador de Clientes Atendidos}}$$


SINCRONOS
Acumulador de tiempo ocupacion
	este va acumulando todo el tiempo 
		 DEPENDE DEL ESTADO
	 acum de tiempo de ocupacion= anterior +(reloj actual - hora anterior)
	 Si el estado anterior es ocupado y el actual tmb sera ocupado 
     

y esto es nomas para pasarlo a %
$$\% \text{Ocupación del Servidor} = \frac{\text{Acum. Minutos Trabajados}}{\text{Reloj Final}} \times 100$$
ATENTO si el reloj final termina por ejemplo en 60, y nuestro evento era en 50 y el serviodra estaba ocupado debo sumarle esto 10 remantes al acum

acum tiempo libre
la automatizacion de esa celda seria para un libre por ejemplo 
=SI(estado='libre';valorAnterior+(reloj actual-reloj anterior);valorAnterior)


---

# 🚨 TRAMPAS MORTALES — ERRORES QUE ANULAN EL EJERCICIO

## 3. Equivalencia de Tiempo de Euler
El $t$ de Euler **NO son minutos**. Siempre multiplicar por el factor de conversión.

## 4. Contar clientes al ENTRAR en vez de al SALIR
Los clientes se cuentan **SIEMPRE al salir** del sistema. Si contás al entrar, te quedan estadísticas parciales de clientes que no terminaron.

## 5. No contar los que esperan "Cero"
Si un cliente llega y el servidor está libre, su tiempo de espera = 0, pero **SÍ lo contás** en el denominador del promedio. Si no, el promedio da más alto de lo real.
> [!question] ¿Debo contar a los clientes que "esperan cero" para el tiempo de cola? **Profesor:** Sí. Si un auto llega y pasa directamente al surtidor libre, su `[[Tiempo de Espera]]` fue $0$. Debes contarlo igual y acumularle $0$ minutos, porque omitirlo ignoraría los casos exitosos y tu promedio matemático final daría falsamente alto,.
## 6. Inconsistencia visual en la línea
Si Cola = 2, deben haber exactamente 2 clientes en estado "Esperando Atención" en las columnas de objetos temporarios.

## 7. El cliente pregunta al SERVIDOR, no a la Cola
Cuando llega, verifica el **estado del servidor** primero. No la cola.

## 9. Condiciones Iniciales ignoradas
- Si el enunciado dice que arranca con datos previos → cargar acumuladores con esos valores.
- Si Euler tiene $y_0 \neq 0$, usá el valor correcto (ej. 50 líneas de código ya hechas).

## 10. Promediar entidades iniciales sin hora de llegada
Si el sistema arranca con objetos adentro y no te dicen cuándo llegaron → **NO los contés** para estadísticas de tiempo de permanencia.

## 11. Agrupar tiempos de procesamiento
Si un furgón lleva 4 paquetes de 10 min, **NO** hacés 4×10=40. Debés generar 4 eventos separados (uno por paquete)

## 12. El "Evento Fantasma"
Si el enunciado **no te da** el tiempo/distribución de una actividad → no la simulés.

## 13. Mezclar entidades de distinta prioridad en la misma cola
Prioridades distintas = colas separadas obligatoriamente.

## 14. No especificar en QUÉ servidor está el cliente
Con servidores múltiples, anotá siempre "Siendo Atendido en Caja 2" o "Reparando en Box 3". Si no, al llegar Fin_Atencion_sub_i no sabés a quién destruir.

## 15. No tachar/blanquear eventos cancelados
Si interrumpís un proceso, el Fin original **se cancela**. Dejá la celda en blanco para no confundirte y bajarlo al reloj por error.

## 16. Pedido rechazado gasta ID
Si "Pedido 3" llega y se pierde, el siguiente es "Pedido 4", NO "Pedido 3".

> [!tip] Diseño: La regla del [[Evento Sub i]] La cantidad de subíndices de un evento (ej. $Fin_Atencion_sub_i$) no depende de la cantidad de empleados físicos, sino de la **cantidad máxima de objetos temporarios que pueden ser atendidos en simultáneo**. Si hay 2 equipos y cada uno procesa 2 autos, la $i$ va del 1 al 4,,.
---

> [!danger] TRAMPA ESTADÍSTICA: Promedios con Tiempos Parciales Si quieres calcular el `[[Tiempo Promedio de Espera]]` o el `[[Tiempo Promedio de Permanencia]]`, **NUNCA** debes acumular el tiempo si el cliente sigue en cola o sigue en el sistema al momento del corte. "Si yo corto la simulación y meto tiempos parciales, el promedio me da más bajo de lo que en realidad es". Los objetos solo se acumulan y se cuentan en el instante exacto en que dejan de esperar o salen del sistema,. Además, los objetos de las `[[Condiciones Iniciales]]` no se cuentan en estas estadísticas porque desconoces su hora real de llegada original,.

# ✅ CHECKLIST DE RESOLUCIÓN (Paso a Paso)

## Fase 0: Antes de empezar a iterar
- [ ] Identificar **Objetos Permanentes** (servidores) y sus estados
- [ ] Identificar **Objetos Temporarios** (clientes/entidades) y sus estados
- [ ] Identificar **Eventos** (Llegada, Fin Atención, etc.)
- [ ] ¿Hay servidores múltiples? → Crear `Fin_Atencion_sub_i` para cada uno
- [ ] ¿Hay prioridades? → Crear colas separadas por prioridad
- [ ] ¿Hay interrupciones? → Agregar columna de Tiempo Remanente
- [ ] ¿Hay bloqueos/buffers limitados? → Agregar estado "Bloqueado" a servidores
- [ ] ¿Hay ecuaciones diferenciales? → Preparar tablas de Euler/RK aparte
- [ ] ¿Hay condiciones iniciales? → Cargar acumuladores y estados iniciales
- [ ] Verificar las unidades de todas las distribuciones (¿es λ o media?)
- [ ] Armar columnas del Vector de Estado en orden:
  1. Nombre del Evento (optativo)
  2. Reloj del Sistema
  3. Sección de Eventos (RND, tiempos, próximos)
  4. Objetos Permanentes (estado servidor + cola)
  5. Variables Estadísticas (acumuladores + contadores)
  6. Objetos Temporarios (estado + hora llegada)

## Fase 1: En cada iteración
- [ ] Buscar el **menor tiempo futuro** entre todos los eventos pendientes
- [ ] Avanzar el reloj a ese tiempo
- [ ] Procesar el evento según su tipo:

### Si es LLEGADA:
- [ ] Generar tiempo de la **próxima llegada** (consumir RND)
- [ ] ¿Servidor libre? → Atender (generar Fin Atención)
- [ ] ¿Servidor ocupado? → A la cola + registrar Hora Inicio Espera
- [ ] Con prioridad: ¿Interrumpe? → Calcular Tiempo Remanente, cancelar Fin original

### Si es FIN DE ATENCIÓN:
- [ ] Destruir cliente y registrar estadísticas (acumular tiempos)
- [ ] ¿Hay alguien en cola de alta prioridad? → Atenderlo
- [ ] ¿Hay tarea suspendida? → Retomarla con Tiempo Remanente
- [ ] ¿Hay cola de baja prioridad? → Atender siguiente
- [ ] Si no hay nadie → Servidor pasa a Libre
- [ ] Con bloqueos: ¿Se liberó espacio? → Desbloquear servidor anterior

### Si es EVENTO COMBINADO (Euler):
- [ ] Ir a la tabla de Euler correspondiente
- [ ] Obtener el tiempo de integración
- [ ] **Convertir unidades** (Euler → minutos del reloj)
- [ ] Sumar al reloj actual → Generar evento futuro

## Fase 2: Al terminar la simulación
- [ ] Calcular TODAS las medidas de desempeño pedidas
- [ ] **Escribir el resultado final explícitamente** (no dejar solo acumuladores)
- [ ] Verificar consistencia visual de la última línea
- [ ] No promediar entidades iniciales sin hora de llegada

---

# 🎯 CASOS ESPECIALES — ¿QUÉ HAGO SI...?

| Situación                               | Qué hacer                                                                                                                                                                   |
| :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Choque de eventos** (misma hora)      | Elegir cualquiera, procesar uno. En la **siguiente línea** procesar el otro con el **mismo reloj**. NO procesar ambos en la misma línea.                                    |
| **Servidor de capacidad infinita**      | No existe cola. Todo pasa directo a "Siendo Atendido". No hace falta columna de estado del servidor.                                                                        |
| **Llamada perdida (no hay cola)**       | Si servidor ocupado → Destruir entidad inmediatamente en la misma línea. Contar como "llamada perdida".                                                                     |
| **Servidor intermitente** (ascensor)    | Estados: "En Piso", "En Tránsito". Usar "Última Dirección Conocida" como variable auxiliar.                                                                                 |
| **Tiempo CONSTANTE por persona**        | SÍ se puede multiplicar (ej. 3 personas × 6 seg = 18 seg).                                                                                                                  |
| **Tiempo con DISTRIBUCIÓN por persona** | PROHIBIDO multiplicar. Generar un RND por cada uno y sumar resultados individuales.                                                                                         |
| **Reseteo de espera** (ej. ascensor)    | Si llega alguien durante la espera → resetear el contador de espera a 0.                                                                                                    |
| **Cola única vs Cola múltiple**         | Por defecto: Cola Única (Carrefour). Solo es múltiple si el enunciado lo dice explícitamente.                                                                               |
| **Negocio cierra (fin de llegadas)**    | Si la próxima llegada > hora de cierre → tachar, dejar en blanco, no generar más. No crear evento "Fin_Llegadas".                                                           |
| **Buffer lleno**                        | Servidor anterior pasa a **Bloqueado**. Acumular tiempo de bloqueo.                                                                                                         |
| **Desbloqueo en cascada**               | Cuando se libera espacio → desbloquear servidor → mover entidad → verificar si se desbloquea otro.                                                                          |
| **Cliente que se va sin esperar**       | Si enunciado dice "si hay cola se va" → destruir y contar.                                                                                                                  |
| **Entidad genera otra entidad**         | Separarlas en bloques de columnas distintos (ciclos de vida diferentes).<br>Ejemplo el de llega cliente y deja unos zapatos<br>DOS OBJETOS DISTINTOS, y dos colas distintas |
|                                         |                                                                                                                                                                             |


---

# 🔑 TIPS DEL PROFESOR PARA EL PARCIAL

1. **Reloj en formato decimal** (ej. 1.50 = 1 min 30 seg). No usar hh:mm:ss.
2. **Fracciones a decimal:** 50 seg = 50/60 = 0.83 min. No complicarse con reglas de tres.
3. **Servidores múltiples sin regla explícita:** Mandá al que quieras, pero **anotá a cuál**.
4. **Respetar orden de series RND.** Si Fila 1 = Llegadas, Fila 2 = Atención → mantener ese mapeo todo el ejercicio.

---

# 🔄 FLUJO DE INTERRUPCIONES (Prioridades)

PARA LAS PRIORIDADES DOS COLAS DIFERENTES, Y LO MISMO PARA INTERRUPCIONES
TAMBE SON DOS OBJETOS DIFERNETES POR EJEMPLO:

PACIENTE CONSULTA GENERAL
PACIENTE URGENCIA

### Al llegar Alta Prioridad:
1. ¿Servidor atendiendo baja prioridad? →
   - **Suspender** la tarea actual (SI EL ENUNCIADO LO ACLARA)
	   - SE GUARDA EL TIEMPO REMANENTE EN UNA COLUMNA ESPECIAL
	     Calcular: $Tiempo_{Remanente} = Reloj_{Actual} - Hora_{Fin\_Original} $ 
   - **Tachar** el Fin original (en la columan de su fin atencinon poner INTERRUMPIDA)
   - Atender la interrupcion (generar Fin en otra columna tipo (urgencia))
   - Entidad suspendida pasa a estado "**Suspendida** o interrumpida" 

### Al terminar la atención (orden estricto de preguntas):
1. ¿Hay más de alta prioridad en espera? → Sí → Atender
2. ¿Hay tarea suspendida a medias? → Sí → Retomar
	1. : $Nuevo_{Fin} = Reloj_{Actual} + Tiempo_{Remanente}$
	2.   - se retoma volviendo a la columna que estaba INTERRUMPIDA 
3. ¿Hay baja prioridad en cola? → Sí → Atender
4. Ninguna → Servidor Libre

> [!CAUTION]
> **NUNCA calcules el nuevo fin de atención anticipadamente.** Si durante la urgencia llega otra urgencia, te tumba el evento otra vez. Guardá el Remanente y calculá el fin SOLO cuando el servidor efectivamente retoma.

---

# 🏗️ FLUJO DE BLOQUEOS (Buffers Limitados)

### Al terminar atención en una etapa:
1. ¿Hay lugar en el buffer/cola siguiente? →
   - **Sí** → Mover entidad al buffer → Servidor queda Libre → ¿Hay alguien en cola propia? → Atender
   - **No** → Servidor pasa a **BLOQUEADO** → Entidad queda atrapada → Acumular tiempo de bloqueo

### Al liberarse un espacio (alguien avanza):
1. ¿Hay servidor bloqueado atrás? →
   - **Sí** → Desbloquear → Mover la entidad atrapada al buffer → Servidor ahora Libre → ¿Hay cola? → Atender
   - Verificar si el desbloqueo **libera otro espacio en cascada**

### Estados obligatorios de servidores con bloqueo:
| Estado | Significado |
|:--|:--|
| **Libre** | Sin entidad, puede recibir |
| **Ocupado** | Procesando una entidad |
| **Bloqueado** | Terminó pero no puede soltar la entidad (buffer siguiente lleno) |

---

> [!question] Dudas sobre el estado de un Servidor Bloqueado **Alumno:** "Si el servidor 1 terminó, pero la cola del servidor 2 está llena, ¿está esperando atención o qué estado le pongo?" **Respuesta del Profesor:** El objeto cliente pasa a estado `[[Proceso Finalizado]]` y el servidor queda en un estado especial llamado `[[Bloqueado]]`. Físicamente, el objeto no está en la cola del siguiente servidor, está atrapado dentro de la máquina anterior,,.