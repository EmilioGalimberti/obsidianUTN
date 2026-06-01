El **Modelo de Referencia OSI**, creado por la Organización Internacional de Normalización en 1980, es un **marco conceptual** para los **protocolos de red**. Se estructura en capas, cada una con funciones específicas, y se utiliza como referencia en el estudio de la arquitectura TCP/IP. Al referirse a dispositivos o protocolos, se utiliza la terminología "dispositivo de capa X", vinculando así el dispositivo a una capa específica del modelo.

Las **capas** están **interconectadas** de manera **adyacente**, y cada capa **ofrece servicios a la capa superior** mientras **utiliza los servicios** **de la capa inferior**. Por ejemplo, cuando se describe un router como un dispositivo de capa 3, significa que realiza funciones de las capas 1, 2 y 3, indicando la capa más alta que abarca. En resumen, un dispositivo no solo cumple las funciones de su capa designada, sino también de las capas inferiores

> [!danger] **Error de concepto frecuente** Un dispositivo clasificado en una capa superior asume obligatoriamente las funciones de las capas inferiores. Por ejemplo, un [Router] (Capa 3) también realiza funciones de Capa 2 y Capa 1, no solo de la suya propia.
![[{6F1BA90D-079F-4DF5-A4B5-B71E405CC195}.png]]



hijo:
* [[CAPA DE ENLACE DE DATOS]]