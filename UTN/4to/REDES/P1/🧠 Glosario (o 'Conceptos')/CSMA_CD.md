1. **[[CSMA_CD]]  Acceso Múltiple con Sensibilidad de Portadora y Detección de Colisiones)**: Es el protocolo dinámico usado en la [Ethernet Clásica] (redes alambradas, redes de área local (LAN)). El dispositivo "escucha" el canal; si está libre, transmite. Si dos equipos transmiten simultáneamente, sus señales chocan produciendo una **Colisión**. Al detectar el choque, dejan de enviar datos, lanzan una **Señal de Atasco** y esperan un tiempo aleatorio antes de reintent
   ![[{CB6F97A3-D1BF-4BFF-A23F-903B28EF9570}.png|508]]
	* Dispositivos y Ubicación de Lógica CSMA/CD:
		* Lógica implementada en la NIC (placa de red) y en el SWITCH (dispositivos de capa 2 - capa de enlace).
	* Limitaciones:
		* Funciona mejor en redes alámbricas, como en el caso de cable UTP.
		* No es adecuado para redes inalámbricas, ya que no pueden detectar colisiones.
	* Manejo de Errores:
		* Después de 16 intentos sin éxito, se detiene el intento y se informa de un error.