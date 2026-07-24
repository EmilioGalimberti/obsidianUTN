**[[Token Ring (IEEE 802.5)]]**: (Redes de Anillo Lógico) Método lógico de transmisión estructurado en anillo. Es determinístico y libre de colisiones. Consiste en hacer circular un testigo llamado **[Token]** por la red. Únicamente la máquina que posee dicho token en su poder tiene el derecho a insertar datos en el medio físico
![[{7407E1FE-11BD-4E1E-9629-D3B2795BCFA1}.png|518]]
En esta configuración, los datos circulan en una única dirección, formando un círculo a través de las estaciones conectadas

* Proceso de transmisión: Cuando una estación recibe el token y no tiene datos, lo pasa a la siguiente. Si tiene datos, convierte el token en una trama (le agg datos, agg mac origen y mac destino) y la lanza al medio de transmisión.

* Verificación de destino: Cada estación verifica si la trama está dirigida a ella por medio de la dirección MAC. Si no es el caso, la trama sigue su curso; si es correcto, la estación procesa la trama y envía un acuse de recibo al origen.

* Token como permiso: El token actúa como un permiso para enviar datos, permitiendo que solo una máquina transmita a la vez y evitando colisiones.
* Método determinístico: Garantiza que las máquinas podrán transmitir datos, pero se considera lento en comparación con otras tecnologías.
* Recorrido completo de la trama: La trama completa da una vuelta desde el origen hasta el destino, y luego se genera un nuevo token para habilitar la transmisión desde otras estaciones.
---
Es logico en anillo como la foto de arriba pero es fisica en estrella

> [!note] En una topología en estrella, 
>un switch actúa como un puente, permitiendo que los datos se transmitan secuencialmente de un dispositivo a otro. Cada estación transmite en su turno, y la inteligencia para realizar el puente entre dispositivos radica en el concentrador central

![[{FDC101C5-8550-4FD4-834B-70C9677CEB2F}.png]]