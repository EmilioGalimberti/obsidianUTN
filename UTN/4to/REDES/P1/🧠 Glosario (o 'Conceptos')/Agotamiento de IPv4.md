padre: [[DIRECCIONAMIENTO]]

## 1. El Problema: [[Agotamiento de IPv4]] y la Asignación [Classful]

El profesor inicia la clase planteando el problema central: las direcciones **[[IPv4]]** se agotaron mucho antes de lo previsto.

- **Causas del [[Agotamiento de IPv4]]:** 
	- El crecimiento exponencial de Internet, (causa principal)
	- Gran cantidad de “dispositivos” que requieren una dirección IP
	- las conexiones de banda ancha "siempre activas" y la proliferación masiva de dispositivos por usuario.
- **El Error Estructural ([Classful]):** El diseño original asignaba direcciones en bloques enteros de clase (A, B o C). Este método no utiliza eficazmente las direcciones disponibles y ha llevado a la necesidad de IPv6 para abordar la creciente demanda de direcciones IP.



### ASIGNACIÓN DE DIRECCIONES IPV4 POR CLASES [Classful]
Classful: significa que se asignan una clase entera de direcciones IP cada vez que una empresa u organización necesitaba direccionar sus dispositivos sin importar la necesidad real de la empresa.
> [!danger] El Derroche Estructural de las Clases El profesor demostró este fallo con un ejemplo matemático crítico: si una empresa necesitaba 500 direcciones, una red de Clase C (254 IPs) no era suficiente. Por ende, se le entregaba una red entera de Clase B, la cual otorga 65.534 direcciones. Esto generaba un desperdicio masivo e irrecuperable de más de 65.000 direcciones **[[IPv4]]** públicas en una sola empresa.

* Empresa A (30 puestos de trabajo): Clase C, por lo que hay un derroche de 254 - 30 de direcciones. Se derrochan 224 direcciones IP.
* Empresa B (100 puestos de trabajo): Clase C, por lo que hay un derroche de 254 - 100 de direcciones. Se derrochan 154 direcciones IP.
* Empresa C (500 puestos de trabajo): Clase B, por lo que hay un derroche de 65534 - 500 de direcciones. Se derrochan 65034 direcciones IP.
* ![[{4DD77B09-0682-4D0C-BB9B-4D68B6CA5C8A}.png]]












## Soluciones Al agotamiento:
1. [[Direccionamiento privado]]: acá hacemos traducción de direcciones de red.
2. Traducción de direcciones de red. [[NAT]]
3. [[CIDR]]: Enrutamiento entre dominios sin clases. Método de asignación de direcciones IP que mejora la eficiencia del enrutamiento de datos en Internet
4. [[VLSM]] (Máscaras de subred de longitud variable)
5. Protocolo IPv6

Los primeros cuatro ítems fueron decididos por más de la mitad de la comunidad de internet. Internet se dividió en dos bandos, aquellos que querían que siguieran viviendo el protocolo IPv4, y el bando del protocolo IPv6.


>[!question] TODOS ESTAS SOLUCIONES SE USAN?
>* se usa la traduccion de direcciones para ips privadas, por lo tanto tmb se usa el direccionamiento privado
>* y las direcciones publicas son asignadas con CIDR y van de la mano con VLSM

## 3. ADMINISTRACIÓN DE DIRECCIONES IP: [IANA] y [RIR]
El control y distribución de direcciones IP públicas se usa para evitar duplicados a través de:

### IANA (Internet Assigned Number Authority):
- **[IANA]**: Autoridad mundial que distribuye grandes bloques de IPs.

Se encarga de distribuir partes del espacio global de direcciones IP y números de sistemas autónomos a Registros Regionales de Internet. Garantiza que no haya direcciones IP públicas idénticas. IANA asigna direcciones IP a Registros Regionales de Internet, y estos registros las distribuyen a proveedores de servicios de Internet (ISP) y empresas.
### RIR (Regional Internet Registry)
- **[RIR] (Registro Regional de Internet)**: Organismos continentales (como **[LACNIC]** para Latinoamérica) que reciben los bloques de la IANA y los reparten a los Proveedores de Servicios de Internet (**[ISP]**).
![[{ED6D85BE-E7AE-40BF-8772-D8CF028318E4}.png]]
RIR es **responsable de distribuir bloques de direcciones IP a sus miembros** y registrar estas asignaciones. Recibe bloques de direcciones y números de sistemas autónomos de IANA y luego los asigna a ISPs (proveedores de servicio de internet ) y estos a su vez a organizaciones en su región. Además, administra números de sistemas autónomos para garantizar una jerarquía en el enrutamiento de Internet.

Internet se divide en áreas y cada área es un sistema autónomo. Cada sistema autónomo tiene un número que es único e irrepetible
# ---
hijos:

[[Direccionamiento Privado]]
[[NAT]]
[[CIDR]]
[[VLSM]]