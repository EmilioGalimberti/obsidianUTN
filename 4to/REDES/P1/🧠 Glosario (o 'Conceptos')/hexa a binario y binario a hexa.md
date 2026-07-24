**2. Repaso del Sistema Binario (4:48 - 13:24)**

El profesor inició la clase recordando cómo funciona el sistema de numeración posicional de base 2, ya que es la base indispensable para comprender las direcciones IP.

Repasó los valores posicionales de los 8 bits de un byte (1, 2, 4, 8, 16, 32, 64, 128)

![[{BCD028FD-1FC2-42E8-84F7-44CF934E859A}.png]]

ejemplo: (vemos las posiciones donde esta prendido sumamos ese numero)

00110010 → hexa →32+16+2=50

01000011= 64+2+1= 67

11111111=255

---

explicacion de hexa a decimal→

- **El número 120 (Ejemplo principal):** El profesor utilizó este número para mostrar el procedimiento paso a paso basándose en los valores de un byte (128, 64, 32, 16, 8, 4, 2, 1). Lo explicó de la siguiente forma:
    - **128:** Como es mayor que 120, ese bit queda apagado (0).
    - **64:** Como es menor, se enciende el bit (1) y se lo resta: 120 - 64 = 56.
        - 01
    - **32:** Como es menor que 56, se enciende el bit (1) y se lo resta: 56 - 32 = 24.
        - 011
    - **16:** Como es menor que 24, se enciende el bit (1) y se lo resta: 24 - 16 = 8.
        - 0111
    - **8:** Como es igual a 8, se enciende el bit (1) y la resta 8 - 8 da 0.
        - 01111
    - **4, 2 y 1:** Al haber llegado a 0, las posiciones restantes quedan apagadas (0).
    - Finalmente, comprobó el cálculo sumando los valores de los bits encendidos (64 + 32 + 16 + 8 = 120).
        - 01111000