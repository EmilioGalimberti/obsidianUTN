Se define como la acción de construir un programa de computadora y hacer evolucionar ese modelo matemático a lo largo del tiempo para observar cómo reacciona y obtener datos que ayuden a la toma de decisiones. Se cita a autores como Robert Shannon y Averill M. Law, destacando que simular es "fingir" y evaluar numéricamente un sistema.

>[!tip] Se hizo hincapié en que la simulación no arroja valores exactos ni realidades absolutas, sino estimaciones de las características del sistema que deben analizarse estadísticamente,.

**Objetivos y áreas de aplicación**: Describir el comportamiento de un sistema, postular hipótesis y predecir escenarios futuros. Se aplica en diseño de sistemas de manufactura, hospitales, redes de telecomunicaciones, bancos, aeropuertos y análisis logísticos.

**Alternativas de estudio**: En lugar de experimentar con el sistema real (que a veces es muy costoso, peligroso o inexistente), se recurre a la simulación con modelos

### Justificación de Uso
Se recurre a la simulación cuando trabajar con el sistema real es:
1. **Imposible:** El sistema aún no existe.
2. **Costoso:** Probar cambios en producción real genera riesgos económicos o de tiempo.
3. **Complejo:** El sistema posee demasiadas variables que impiden un análisis analítico simple.

### Clasificación general de Sistemas

| Dimensión                                        | Tipos                                  |
| ------------------------------------------------ | -------------------------------------- |
| Intercambio con entorno                          | Abiertos / Cerrados                    |
| Origen                                           | Naturales / Artificiales               |
| Comportamiento <br>frente a variables de entrada | Estables / Inestables                  |
| Relacion de variables                            | Lineales / No lineales                 |
| Aleatoriedad                                     | **Estocásticos** / **Determinísticos** |
| Duracion                                         | Terminates/ No terminates              |
#### Definición de cada sistema
- **Sistemas Estocásticos (Probabilísticos):** Intervienen valores y variables estadísticas y aleatorias.
- **Sistemas Determinísticos:** Evolucionan basados en reglas precisas, por lo general representados mediante ecuaciones diferenciales, sin estar atados a factores estadísticos impredecibles.
- **Sistemas Estáticos:** Modelos discretos donde, ante la llegada de una entrada, los componentes internos del sistema no sufren cambios. Ante la misma entrada, la salida siempre será idéntica (ej. modelos de inventario o análisis de riesgo).
- **Sistemas Dinámicos:** Modelos discretos donde el estado interno se modifica con el paso de cada evento. Si se repite exactamente la misma entrada en distintos momentos, la salida será diferente (ej. sistemas de colas).
- **Sistemas Lineales y No Lineales:** En los lineales, el resultado mantiene una proporcionalidad directa con la entrada. En los no lineales esta proporcionalidad directa no ocurre.

> [!danger] Confusión clásica — Estático vs. Dinámico
> Un Sistema Estático no significa que "no se mueva", sino que su **estado interno no cambia** al procesar una entrada. Un Sistema Dinámico **sí modifica su estado**, por eso la misma entrada puede dar resultados distintos en distintos momentos.
#### Sistema Terminante

> [!note] Definición
> Existe un evento natural predefinido que determina el final de la actividad o de la simulación vaciándose el sistema en ese instante. Por esta característica, rara vez alcanzan un estado estable.

*Ejemplos:* sucursal bancaria con horarios fijos, confrontación militar, fábrica con orden específica de producción.
* ==Por lo generan no alcanzan un estado estable==
* ==hay un evento natural que determina el timepo de la simulacion o el fin de la misma ==

#### Sistema No Terminante

> [!note] Definición
> Son aquellos cuya vida se prolonga indefinidamente en el tiempo. Estos sistemas suelen alcanzar un estado estable o de "régimen", aunque al iniciar siempre presentan un estadoclase  transitorio (o warm-up), donde las variables fluctúan bastante antes de estabilizarse.


*Ejemplos:* central telefónica, líneas de ensamblaje continua, salas de emergencias, redes de datos.

* ==Sistemas cuya vida se prolonga indefinidamente en el tiempo 
* ==Suelen alcanzar un estado “Estable” o de “Régimen”
* ==Al inicio presentan un estado transitorio (Warm-Up)==

> [!tip] Tip de parcial — Sistemas No Terminantes
> Para que los resultados sean válidos en un Sistema No Terminante:
> - Realizar **corridas prolongadas** (el modelo debe superar el Warm-Up).
> - Aplicar **Eliminación de Datos Iniciales** para evitar que el sesgo del arranque distorsione las medias globales.
> - Forzar una **"inicialización adecuada"** que ponga el modelo ya en movimiento simulado.

### Estado Transitorio (Warm-Up)

> [!note] Definición
> Etapa inicial inestable de un Sistema No Terminante donde las variables de interés (costos, ganancias, tiempos) **fluctúan agresivamente** antes de estabilizarse en el Estado Estable.

**Estrategias de supresión del Estado Transitorio:**
- Usar corridas muy largas.
- Eliminar / truncar los primeros datos erráticos.
- Inicializar el modelo "ya en movimiento" (*warm start*).

> [!danger] Error común
> Incluir los datos del Estado Transitorio en el cálculo de las medias finales **contamina los resultados** y hace que las estimaciones sean inválidas. Siempre hay que **eliminar o truncar** esa etapa inicial.

![[{601301BE-0D0A-4C86-925A-28938EE4FAF4}.png]]
# ventajas,desventajas y peligros

| Ventajas                                                                            | Desventajas                                                                              | Peligro                                                                                            |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| 1. Estimacion de medidas de desempeño, bajo diferentes escenarios                   | 1. Puede aparentar reflejar con precision un sistema real, cuando en verdad no lo hace   | 1. Inferir resultaso con una sola corrida asumiendo independencia                                  |
| 2. Manejo arbitrario del tiempo                                                     | 2. No permite encontrar soluciones optimas                                               | 2. Uso arbitrario  de distribuciones y suposiciones                                                |
| 3. Estudio de sistemas etocasticos                                                  | 3. No se puede medir el grado de impresicion                                             | 3. Impresionarse con el gran volumen de informacion, pero que no refleje el sistema estudiado      |
| 4. Control sobre condiciones de entorno y de entrada                                | 4. No siempre es conveniente desde la perspectiva de los costos (economicos y en tiempo) | ---                                                                                                |
| ---                                                                                 | 5. No es sustituto de un analsis detallado                                               | 4. Los resultados pueden dar lugar a una excesiva confianza                                        |
| 5. Es util cuando no hay una formulacion analitica                                  | ---                                                                                      | 5. Es posible que se ignoren factores tecnológicos y de indole humana                              |
| 6. ayuda a estudiar sistemas inexistentes                                           | 6. Costos                                                                                | 7. Basar las decisiones en el promedio de estadísticas cuando los resultados son de hecho cíclicos |
| 7. Puede ser usado repetidamente una vez construido                                 | 7. Dificultades para "vender" la idea al managment                                       |                                                                                                    |
| 8. puede utilizarce como entrenamiento de personal                                  |                                                                                          |                                                                                                    |
| 9. cuando se introducen nuevos elementos en el sistema, permite anticipar problemas |                                                                                          |                                                                                                    |

# Las 10 Etapas del [[Simulacion|Proceso de Simulacion]]

> [!note] Concepto clave
> La [[Simulacion]] es un **proceso iterativo y metodológico**, no un acto de programación aislada. Las etapas no son siempre lineales: el paso de [[Validación del modelo|Validación]] puede forzar volver a etapas anteriores.

| N°  | Etapa                                                                                    |
| --- | ---------------------------------------------------------------------------------------- |
| 1   | Definición del Sistema y objetivos                                                       |
| 2   | Formulación del Modelo Conceptual                                                        |
| 3   | Adquisición y preparación de datos                                                       |
| 4   | Traslación / Programación del modelo en computadora                                      |
| 5   | **[[Validación del modelo]]** *(punto crítico — puede implicar volver a etapas previas)* |
| 6   | Planeación Táctica y Estratégica (cantidad y tipos de corridas)                          |
| 7   | Experimentación (ejecutar las simulaciones)                                              |
| 8   | Interpretación y Análisis de Resultados                                                  |
| 9   | Implantación de la solución                                                              |
| 10  | **Documentación detallada** *(subestimada pero muy valiosa a futuro)*                    |

> [!tip] Tip de parcial — Etapa crítica
> La etapa **5 — [[Validación del modelo]]** es el punto crítico del proceso. Si el modelo no representa fielmente la realidad, se debe volver a etapas anteriores. Es iterativo, no lineal.

---



