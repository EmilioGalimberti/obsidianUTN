PADRE:  CAPA 3

El Router o enrutador : Es un equipo intermediario encargado de unir, separar o dividir redes y subredes. Su función principal es enrutar y encaminar paquetes de información, decidiendo el camino a tomar gracias a mapas de enrutamiento

Si el switch es el jefe de la oficina, el **Router** es el cartero que conoce todas las rutas de la ciudad. Es el intermediario crítico que interconecta redes distintas.

Para entenderlo, piensen en la **analogía del domicilio**: Tu IP es tu dirección (Calle Pepito 1234). El Router es el que tiene los **mapas**. Él no es el dueño del mensaje ni el destinatario final; es un intermediario que mira la dirección de destino y dice: _"Ah, querés ir a la red de Finanzas, tomá la avenida de la derecha"_ o _"¿Vas para China? Salí por la interfaz de Internet"_.

> [!question] **Pregunta en clase:** El profesor preguntó: _"¿Qué funciones de capas cumple un Router: Capa 1, Capa 2, Capa 3 o todas?"_ 
> **Respuesta:** Varios alumnos dudaron, pero la respuesta correcta es que un [Router] es un dispositivo de **Capa 3** (Capa de Red), lo que significa que asume obligatoriamente las funciones de su capa máxima y de todas las inferiores (Capa 1 y Capa 2). Recibe bits, desencapsula la trama, lee la dirección IP del paquete para consultar su [Tabla de Encaminamiento] y vuelve a encapsular para enviarlo por la interfaz correspondiente.