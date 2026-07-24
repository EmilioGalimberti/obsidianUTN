padre: [[Agotamiento de IPv4]]

Para mitigar la crisis temporalmente, se implementó un rango de direcciones que no se pueden enrutar en la Internet pública.

- **[[Direccionamiento Privado]] (RFC 1918):** 
	- Sólo se pueden utilizar DENTRO de una empresa u organización
	- Estas direcciones no son visibles desde Internet, lo que proporciona una capa adicional de seguridad
	- si se necesita acceder a Internet desde la empresa, se requiere la traducción de direcciones (NAT). Las direcciones privadas suelen pertenecer al rango de la clase C, con direcciones comunes como 192.168.0.0 o 192.168.1.0

> [!question] Pregunta a la clase: Cantidad de Redes Privadas El profesor evaluó a los alumnos sobre cuántas direcciones de red privadas existen por clase:
> 
> 1** red Clase A (la `10.0.0.0/8`).
> **16** de Clase B (desde `172.16.0.0` hasta `172.31.0.0`) 
> **256** de Clase C (desde `192.168.0.0` hasta `192.168.255.0`).
> 
> ![[{7711C366-A3CF-43A6-9A99-C95503BE83D8}.png]]