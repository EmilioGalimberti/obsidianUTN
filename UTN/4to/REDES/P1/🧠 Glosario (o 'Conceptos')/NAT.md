padre: [[Agotamiento de IPv4]]

###  [[NAT]] **(Network Address Translation)**
La traducción de direcciones es necesaria cuando se comunica con Internet desde una empresa. La dirección privada (origen) se convierte en direccion pública (origen) al salir de la empresa, y al entrar desde Internet, la dirección pública (destino) se reemplaza por la dirección privada( destino) en los paquetes. Esto lo gestiona el [[router]], que mantiene tablas de traducción. 

Sin embargo, esta traducción es lenta y puede convertirse en un cuello de botella, ya que todo el proceso debe realizarse en el router

> [!danger] Trampa de Diseño: El Cuello de Botella del [[NAT]] El profesor enfatizó que el proceso de traducción que hace el **[[Router]]** (reemplazar la dirección origen privada por la pública y mantener registros en tablas) es computacionalmente **"muy lento"**. Esto convierte al router en un cuello de botella crítico para el tráfico de la red empresarial.

![[{BF3F2E12-4972-4241-9A09-2985BBA70F7B} 1.png|375]]

>[!question] hace falta traduccion si se quiere comunicar entre ellas sin salir a internet?
>NO HACE FALTA
