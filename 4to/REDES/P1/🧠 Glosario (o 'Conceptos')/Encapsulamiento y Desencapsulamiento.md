
[[TCP_IP]]

---
 
 >[!note] **Encapsulamiento**:
 > Es el proceso descendente en el dispositivo de origen. Los datos bajan desde la capa de aplicación hacia la capa física y, en cada paso, se les agregan cabeceras y colas de control (como "sobres dentro de sobres").

>[!note] Desencapsulamiento
>Es el proceso ascendente en el equipo de destino. La información sube por las capas y se le van despojando las cabeceras añadidas tras validar su integridad y procedencia

## 1. El Proceso de [Encapsulamiento y Desencapsulamiento] y Desencapsulamiento (0:00 - 19:42)

El profesor inicia la clase demostrando cómo viaja la información desde el dispositivo origen hasta el destino a través de la arquitectura [[TCP_IP]], atravesando las distintas capas y transformando su [PDU] (Unidad de Datos del Protocolo).

Tanto en origen como destino, se ejecutan las cuatro capas de la arquitectura TCP/IP. y En dispositivos intermedios: Host a Red (capa 1 y 2 del OSI) e Interred (capa 3 del OSI).![[{92AC963B-B5BB-43CA-AC6D-7C81C0D93C26}.png]]

- **En el Origen (Encapsulamiento):** 
	- La [Capa de Aplicación]  inicia la comunicacion y genera los datos.
	- Estos descienden a la [Capa de Transporte] segmenta y encapsula (se les agrega cabecera [TCP] o UDP formando un [Segmento]), 
	- luego a la [Capa de Internet] (se agrega cabecera [IP] formando un [Paquete]) 
	- y finalmente a la [Capa Host a red] encapsual la trama (se agrega cabecera (eth) y cola (CRC)  formando una [Trama]), para ser enviados como [Bits] al medio físico.
	- ![[{549F74AC-570A-4901-946E-4863C2C6C778}.png]]
>[!note] **[[Encapsulamiento y Desencapsulamiento| Encapsulamiento]]**: Es el proceso descendente en el dispositivo de origen. Los datos bajan desde la capa de aplicación hacia la capa física y, en cada paso, se les agregan cabeceras y colas de control (como "sobres dentro de sobres").



- **En Dispositivos Intermedios ([Router]):**
> [!question] **Pregunta en clase:** El profesor preguntó: _"¿Qué funciones de capas cumple un Router: Capa 1, Capa 2, Capa 3 o todas?"_ 
> **Respuesta:** Varios alumnos dudaron, pero la respuesta correcta es que un [[Router]] es un dispositivo de **Capa 3** (Capa de Red), lo que significa que asume obligatoriamente las funciones de su capa máxima y de todas las inferiores (Capa 1 y Capa 2). Recibe bits, desencapsula la trama, lee la dirección IP del paquete para consultar su [Tabla de Encaminamiento] y vuelve a encapsular para enviarlo por la interfaz correspondiente.
    
- **En el Destino (Desencapsulamiento):** 
	- Bits llegan a la capa de Host a Red del destino.
	- En la capa de intrared (en osi la de enlace), se interpreta la trama y se verifica el CRC (código de redundancia cíclica). La placa revisa la [[Dirección MAC]] y verifica errores mediante el cálculo del [CRC] (Código de Redundancia Cíclica).
		- Si correcto, se procesa y pasa a la capa de Interred.
		- Si incorrecto, se descarta sin avisar
	- Capa de Interred,  verifica la IP destino y desencapsula el segmento.
	- Capa de transporte tcp
	- capa de aplicaco
> [!danger] **Cuidado con el descarte de tramas:** Un alumno preguntó si se avisa al origen cuando el [CRC] da error. El profesor aclaró que no. La tecnología [[IEE 802.3 (Ethernet)]] es de _"máximo esfuerzo"_; si la trama está corrupta, simplemente **se descarta sin avisar**. Será responsabilidad de las capas superiores (como el protocolo [TCP]) solicitar la retransmisión.

![[{15F568FC-3DA7-4719-B9B6-F10D82E6033D}.png]]


> [!note] Definición: Unidades de Datos Cada capa maneja un tipo diferente de [PDU] (Unidad de Datos del Protocolo). La Capa de Transporte maneja el [Segmento], la Capa de Internet maneja el [Paquete], y la Capa de Enlace construye la [Trama].



# observaciones:
• Encapsulamiento: Descendente por capas, desde datos hasta bits.
• Desencapsulamiento: Ascendente por capas, desde bits hasta datos.
• En el modelo OSI, la comunicación se da entre capas homólogas (la capa de transporte del origen se comunica con la capa de transporte del destino), pero no se comunican de manera directa sino, que se comunican entre capas adyacentes (descendiendo en la jerarquía de capas)
• Cada capa maneja un tipo de dato distinto y habla un protocolo distinto