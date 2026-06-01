
MI SOLUCION Y APUNTES DE LA CLASE:
![[P1-U00-P02-diagnostico_GalimbertiEmilio90747_260407_082741.pdf]]
# Esquema Cronológico de Clase: Servidores, Seguridad, Resiliencia y Redes Virtuales

## 1. Concepto y Ubicación Física de los Servidores

El análisis del caso práctico inició debatiendo qué características definen a un equipo de servicio y dónde debe instalarse físicamente.

> [!note] Un [[Servidor]] es cualquier equipo que está "corriendo y brindando un servicio" de fondo (por ejemplo, un servidor web, de archivos o de sincronización de tiempo). Cualquier dispositivo puede serlo, pero se requiere hardware que soporte estar encendido 24/7 de forma redundante.

- **Restricciones de Ubicación Física:**
> [!warning] Trampa de diseño: Los servidores no deben ubicarse en zonas comunes (como la sala operativa o administrativa) por dos razones críticas: **seguridad** (evitar que personal no autorizado los desconecte) y **climatización** (necesitan normativas de aire acondicionado y ventilación).

Y la misma recomendaicon para el resto de dispositivos
![[{9F879B00-010C-4327-8C7B-CEC6D3EA4DB0}.png]]
## 2. Conectividad Inalámbrica y Medidas de Seguridad Base

Se abordó la integración de redes Wi-Fi a la infraestructura cableada mediante un [[Access Point]] y cómo aplicar restricciones de acceso para ciertos usuarios (como los estudiantes).

- **Función del [[Access Point]]:** Es el dispositivo que convierte la señal de los cables a señales de radio, permitiendo que dispositivos inalámbricos entren a la Red LAN.
- **Implementación de Seguridad en el AP:**

> [!question] ¿Cómo evitamos que los estudiantes se conecten a la red Wi-Fi de profesores? (Pregunta del profesor). **Soluciones debatidas:**
> 
> 1. Configurar un SSID oculto o con contraseña segura.
> 2. Implementar una White List (Lista Blanca) utilizando la Dirección MAC de los dispositivos autorizados, evitando depender de direcciones IP.

## 3. Segmentación Lógica: Routers, ACLs y Dominios de Difusión

El profesor aclaró que para realizar filtros lógicos entre redes no se utiliza un **[[Firewall]]** (típico de sistemas operativos), sino que los enrutadores controlan la seguridad mediante **[[ACL]]** (Listas de Control de Acceso). Estas son reglas que dictaminan exactamente qué redes tienen permiso para interactuar con otras. (ej. los estudiantes pueden salir a Internet pero no acceder a los servidores).

- **Motivos Fundamentales para Segmentar Redes:**

>[!tip] Tip de Parcial: Motivos Críticos para Segmentar Existen dos motivos fundamentales por los que la infraestructura debe dividirse en múltiples redes más pequeñas:
> 
> 1. **Seguridad y Control de Tráfico:** Para aplicar **[[ACL]]** que impidan que un área (ej. estudiantes) acceda libremente a los recursos críticos de otra (ej. servidores).
> 2. **Reducción del [[Dominio de Broadcast]] (Dominio de Difusión):** En una red LAN masiva, los paquetes de difusión se replican constantemente a todos los puertos del switch. Esto genera una sobrecarga de "tráfico basura" que satura el hardware y destruye la eficiencia de la conectividad.

![[{6A8EF800-FDEC-45AF-82DD-C9EEC6FE1665}.png|373]]
	![[{E4931F2C-A123-4C02-B28B-480086743F1A} 1.png|499]]
![[{CF04FC92-A35E-4A34-A03B-35A4D89B0E0F}.png|449]]
## 4. Resiliencia Física, Topología y Cableado Estructurado

El último tema vinculó las decisiones físicas ante contingencias eléctricas con la introducción a soluciones lógicas de segmentación avanzada.

- Ante la eventualidad de que se apaguen las llaves térmicas en las aulas, se advirtió sobre el peligro de conectar un switch en cada aula en formato de cascada, ya que un corte intermedio dejaría sin red a los tramos subsiguientes.

> [!warning] Riesgo de Seguridad y Normativa Dejar un switch de red accesible en zonas con estudiantes abre la puerta a sabotajes físicos, como el corte malicioso de cables **UTP**. La norma de **Cableado Estructurado** dicta que el **Cableado Horizontal** debe viajar centralizado desde las estaciones de trabajo hasta un **Armario de Comunicación** (o Sala Técnica) donde el acceso sea seguro.

Para solucionar la necesidad de segmentar lógicamente sin comprar un router sumamente costoso con múltiples interfaces físicas, se introdujo el uso del **Switch Administrable** compatible con la **[[Norma 802.1Q]]**.


## 5. Implementación Avanzada: Introducción a las VLANs

La clase cerró introduciendo la tecnología que permite segmentar redes lógicamente sin multiplicar el hardware físico.

- **Limitación física vs. Solución Lógica:** Para tener múltiples redes sin comprar un [[Router]] con decenas de interfaces, se utiliza un [[Switch|Switch administrable]] que soporte la [[Norma 802.1Q]].
- **Concepto de [[VLAN]] (Virtual LAN):**
> [!note] Definición Lógica de Redes La tecnología **[[VLAN]]** (Virtual LAN) permite dividir lógicamente un switch para crear múltiples redes independientes utilizando el mismo hardware. El tráfico de todas estas **[[VLAN]]** viaja hacia el router simplificando el cableado mediante una "autopista" de conexión especial denominada **Puerto Trunk** (Enlace Troncal).

![[{E2B25269-FFDE-4984-BE88-61C35122BB3B} 1.png|486]]



---




## MI SOLUCION
![[P1-U00-C02 Practico_Diagnostico_Red_Escuela]]