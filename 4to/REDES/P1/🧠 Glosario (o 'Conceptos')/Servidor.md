> [!note] Un [[Servidor]] es cualquier equipo que está "corriendo y brindando un servicio" de fondo (por ejemplo, un servidor web, de archivos o de sincronización de tiempo). Cualquier dispositivo puede serlo, pero se requiere hardware que soporte estar encendido 24/7 de forma redundante.

- **Restricciones de Ubicación Física:**
> [!warning] Trampa de diseño: Los servidores no deben ubicarse en zonas comunes (como la sala operativa o administrativa) por dos razones críticas: **seguridad** (evitar que personal no autorizado los desconecte) y **climatización** (necesitan normativas de aire acondicionado y ventilación).


>[!question] un servidor es un host?

No exactamente, aunque están muy relacionados. La regla de oro es: **Todo [[Servidor]] es un [[Host]], pero no todo host es un servidor.**

Aquí te explico la diferencia de forma simple:

### 1. El Host (El término general)
Como dice tu apunte, un **host** es cualquier dispositivo que tiene una dirección IP y está conectado a la red. Es el "anfitrión" de una dirección.
*   **Ejemplos:** Tu celular, la PC de un alumno, una impresora, una cámara IP y, por supuesto, un servidor.

### 2. El Servidor (El rol específico)
Un **servidor** es un host que tiene una función especial: **ofrecer un servicio** a otros equipos (llamados clientes). 
*   En tu ejercicio, los servidores de Web, Correo y Archivos son hosts porque tienen su propia IP, pero se les llama "servidores" porque su trabajo es "servir" datos a las PCs de los profesores y alumnos.

### Resumen para tu examen:
*   **Host:** Se refiere a la **identidad** en la red (tener una IP).
*   **Servidor:** Se refiere a la **función** o trabajo que hace ese equipo (dar un servicio).

> [!tip] Analogía simple
> En un restaurante, **todos son personas** (Hosts), pero solo algunos tienen el **rol de mozo** (Servidores) porque están ahí para dar un servicio a los demás. El cliente es una persona, pero no es un mozo.