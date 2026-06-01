# Esquema Cronológico de la Clase: Infraestructura y Arquitectura de Redes

![[UTN/4to/REDES/P1/PRACT/P1-U00-P01-actividad_diagnostico.pdf]]

## 1. Introducción al Análisis de Redes y Dispositivos Finales
![[{4ECEA23E-C63B-4BEA-B436-B9D053245E13}.png|363]]

El profesor inició la clase revisando un trabajo de diagnóstico sobre el análisis de un diagrama de red y la identificación de los equipos involucrados en sus extremos. estableciendo los conceptos básicos de infraestructura.

> [!note] Definición Una [[Topología de red]] es una representación gráfica que muestra todos los equipos que están involucrados o intermedian dentro de una red de datos. aunque no suele dibujarlos absolutamente a todos.

- **Identificación de los extremos:** Se introdujo el concepto fundamental de los dispositivos que operan en los extremos de la conexión.

> [!question] Intervención en clase El profesor preguntó: "¿Qué es un [[Host]]?". La respuesta consensuada fue que se trata de "cualquier dispositivo final"
> ![[{AA3E5BC9-1EE7-4B27-B6B8-FCE60FA678D8}.png]]

>[!note] Definición Un [[Host]] es cualquier equipo capaz de conectarse a la red y consumir una [[Dirección IP]], abarcando desde PCs y celulares hasta impresoras, cámaras de vigilancia o incluso un lavarropas industrial.




## 2. Equipos de Conexión Local: El Switch

>[!WARNING] PRGUNTAR, SWITCH = CONMUTADOR DE PAQUETES?

La clase avanzó hacia el análisis de cómo se conectan los dispositivos dentro de un mismo entorno físico , las restricciones físicas y lógicas del cableado..

>[!note] El [[Switch]]: Es un dispositivo concentrador  que permite conectar múltiples equipos a una misma red mediante puertos Ethernet. Los switches no administrables son aquellos que cumplen esta función de conexión local, pero no permiten ningún tipo de configuración

> [!tip] Evolución de la topología El profesor explicó que antes existía la [[Topología en bus]], donde un solo cable unía todo y generaba problemas. El [[Switch]] llegó para "dar los pases" de manera inteligente, recibiendo información por un puerto y reenviándola exactamente al puerto de destino de manera local.

> [!warning] Cuidado con el hardware Es crucial diferenciar un switch avanzado de un [[Switch no administrable]]. Este último no se puede configurar; es _plug-and-play_, por lo que al conectarse a la red eléctrica sus puertos quedan inmediatamente disponibles para su uso.


## 3. solucion Problema planteado

Para resolver la dinámica anterior, se introdujeron los conceptos de capa superior y la función de los intermediarios lógicos
> [!warning] Direccion IP , Protocolo IP  y Direccanomiento IP es todo lo mismo?

Analogía El Protocolo IP y el Direccionamiento IP, [[Dirección IP]] funcionan exactamente igual que la dirección de un domicilio en un mapa. Permiten identificar de forma única a una máquina dentro de la gran red de datos para saber cómo llegar a ella.

- **Desmitificando la nube:**

> [!question] Intervención en clase "¿A qué hace referencia la nube de Internet? ¿A un conjunto de qué?", preguntó el profesor. La respuesta técnica fue que es un enorme conjunto de [[Router| Routers]] que operan como nodos de transmisión.

>[!note] El Router: Es un equipo intermediario encargado de unir, separar o dividir redes y subredes. Su función principal es enrutar y encaminar paquetes de información, decidiendo el camino a tomar gracias a mapas de enrutamiento

> [!tip] Metodología para el Cálculo de Redes (Tip de Parcial) **por cada [[Interfaz de red]] (puerto físico) que sale conectada de un [[Router]], se debe contabilizar una red diferente**. Aplicando este procedimiento, concluyeron que el diagrama base poseía 12 redes en total (7 LAN y 5 WAN).

![[{2EC7D715-05E6-4DA9-9F19-2484BD53CE01}.png]]

En el ejercicio que analizamos en clase, identificamos un total de **12 redes**:

- **7 Redes LAN:** Los segmentos que bajan del router hacia los switches y hosts (la red interna).
    - **Redes LAN (Red de Área Local)**: Son redes de alcance físico pequeño y local que no pueden superar los 100 metros de distancia
- **5 Redes WAN:** Las conexiones entre los propios routers.
![[04.png|564]] ![[05.png|507]]
>[!warning] Ojo con este error común: La conexión entre dos routers se cuenta como una sola red. Aunque hay dos cables o dos puertos involucrados, el "pasillo" que une al Router A con el Router B es un único segmento de red. No lo cuenten dos veces.

![[06.png|284]]![[07.png|506]]