## 4. [[Bridge]] o Puente (28:55 - 36:39)

- **Nivel operativo:** Dispositivo inteligente de [Capa 2]| [[CAPA DE ENLACE DE DATOS]]., combina funciones de capa 1 y capa 2
- **Propósito principal:** Segmenta una red logica y dividir un dominio de colisión muy grande en partes pequeñas. Si hay muchos equipos colisionando, un puente intermedio separa el tráfico.

 funciones principales:
 * Interconecta segmentos de red, dividiendo dominios de colisión y extendiendo el dominio de broadcast.
> [!tip] **Tip para parciales (Dominios):** El profesor enfatizó que un [[Bridge]] o un [Switch] dividen y reducen el [[Dominio de Colisión]] por cada uno de sus puertos, pero **NO** dividen el [[Dominio de Broadcast]] (la difusión masiva sigue pasando a toda la red). Solo el [Router] divide dominios de broadcast.
* Maneja una tabla de direcciones MAC por cada segmento, permitiendo la comunicación entre ellos.
![[{E1B28008-FFC3-4EC8-BEF4-1DE9495D33C3}.png|364]]![[{52C667BD-B327-452B-A545-9CC8419C183A}.png|382]]

ventajas:
* Divide dominios de colisión, creando un dominio por cada puerto del puente
- Puede interconectar diferentes protocolos de [[CAPA DE ENLACE DE DATOS]] enlace
- Permite la interoperabilidad entre diferentes segmentos de red (Ethernet – WiFi)
- Aumenta el número de estaciones y amplía la distancia física entre ellas.
- Mejora el rendimiento y la confiabilidad al reducir el tráfico local y aislar errores.
- No requiere configuración, utiliza autoaprendizaje para aprender direcciones MAC.
- Puede ser equivalente a un Access Point al interconectar redes cableadas e inalámbricas.