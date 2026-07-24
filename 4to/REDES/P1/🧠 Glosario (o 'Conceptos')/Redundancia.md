l Planteo Inicial:** El profesor propuso la situación donde el Switch 1 estaba conectado en cascada al Switch 2, y este a su vez al Switch 3 (donde se encontraba alojado el servidor principal).
- ![[{7A45C5BB-94F9-4467-81B4-00BA919EFD05}.png]]
-  Si se interrumpe el enlace entre el switch 1 y el switch 2, las máquinas A y B no podrán comunicarse con la máquina C y el servidor. Sin embargo, A y B seguirán siendo capaces de comunicarse entre sí, dividiendo la red en dos partes
	- Para evitar esta situación, se establece redundancia conectando el switch 2 y el switch 3. Si un enlace falla, el tráfico se redirige automáticamente por el otro enlace hacia el destino.
	- ![[{18D4BD4A-0BA9-4F4A-BB3D-C00DB3EFEE63}.png]]
- **Conclusión del ejemplo:** La redundancia es costosa físicamente porque se desperdician puertos en los dispositivos, pero es fundamental ya que brinda fiabilidad y tolerancia a fallos, previniendo que se interrumpan los servicios si un cable se daña