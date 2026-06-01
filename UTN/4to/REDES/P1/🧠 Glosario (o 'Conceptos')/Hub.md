## 3. [[Hub]] o Concentrador (24:53 - 28:55)
![[{AF57CC6F-98EF-41A3-99D3-074F6FBA636C} 1.png]]

Dispositivo que permite conectar varias computadoras o formar una red, aunque actualmente ha sido reemplazado por switches más económicos y genéricos

*funciones principales*
- **Nivel operativo:** Dispositivo netamente de [Capa 1] (Física). No tiene inteligencia.
- **Función:** Conocido como "repetidor multipuerto". Centraliza el cableado de una red una [Topología en Estrella] física. Recibe la señal por un puerto y la reenvía o repite por **todos** los demás puertos, 
- Si interconectamos varios hubs, se extendiende el tamaño del [[Dominio de Colisión]].
- Conocido como repetidor multipuerto, regenera la señal recibida y la envía por todos los puertos, excepto por donde ingresó, elevando su potencia para permitir mayor alcance.

*caracteristicas:*
* Conecta eléctricamente todos los cables que llegan a él.
* Carece de inteligencia, no procesa ni interpreta la señal, simplemente la repite
* Permite la conexión/desconexión de computadoras sin interrumpir la red.

*Modo de Operación:*

> [!question] **Pregunta en clase:** _"¿En qué modo opera un Hub: Simplex, Half-Duplex o Full-Duplex?"_ 
> **Respuesta de los alumnos validada por el profesor:** Opera en [Half-Duplex] o (Semi-dúplex), ya que un equipo puede transmitir o recibir, pero no ambas cosas simultáneamente. Por esto, los equipos conectados a un Hub están obligados a usar el método de acceso [[CSMA_CD]] para lidiar con las colisiones.
