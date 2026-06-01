## 2. Tarjeta de Interfaz de Red o [[NIC]] (19:42 - 24:53)
![[{E72D3A0C-85EF-4F3E-9F05-AF28AD55EA3B}.png]]
- es esencial para la comunicación entre dispositivos en una red. Sinónimos incluyen adaptador de red, placa de red, y tarjeta de interfaz de red.
-
funciones principales:

- **Definición:** Es el adaptador que brinda acceso físico al medio de comunicación. dependiendo del método de acceso al medio ([[IEE 802.3 (Ethernet)]] para alámbricos y 802.11 para inalámbricos)
- **Ubicación lógica:** Opera en la [Capa 1] (Física) y la [Capa 2] ([[CAPA DE ENLACE DE DATOS]]) del [[Modelo OSI]].
- Cada placa de red posee una [[Dirección MAC]] unica(almacenada en la ROM)
- **Funcionamiento:** Trabaja de forma autónoma analizando la [[Dirección MAC | MAC destino]]  de las tramas que llegan para saber si las procesa o las descarta.
- Detecta y verifica errores en las tramas mediante el algoritmo de código de redundancia cíclica.

operacion:
* Recibe un paquete de la capa de red, lo encapsula en una trama y lo envía al medio de comunicación.
* El protocolo de capa de enlace está implementado en la NIC (802.3 – 802.11)


**Tipos:** 
	- Existen diferentes tipos según el medio (Cable UTP, [Fibra Óptica], inálambricas para [Wi-Fi]), ya que deben adaptar la información a la naturaleza física del canal.
