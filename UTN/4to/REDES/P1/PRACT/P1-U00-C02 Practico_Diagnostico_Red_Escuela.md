---
tags: [redes, practico, diagnostico, VLAN, 802.1Q, UTN]
aliases: [Práctico Diagnóstico Red, Diagnóstico Escuela]
date: 2026-04-27
---

# 🖧 Práctico: Diagnóstico y Diseño de Red Escolar

> [!info] Contexto del ejercicio
> Se nos contrata para diseñar e implementar la red de una escuela desde cero, usando equipamiento donado y un presupuesto fijo. El objetivo es cumplir todos los requisitos del cliente de forma eficiente y quedarnos con la mayor ganancia posible.

---


> [!important] Concepto clave
> **VLAN (Virtual LAN)** = separación **lógica** de redes a nivel de software, aunque estén en la misma infraestructura física.

#### ¿Qué es IEEE 802.1Q?
El protocolo **IEEE 802.1Q** es el encargado de ponerle una **"etiqueta"** invisible a cada paquete de datos para identificar a qué VLAN pertenece. Un router/switch que soporta este protocolo puede leer esas etiquetas, separar el tráfico y decidir quién puede comunicarse con quién.

#### Tipos de Conexión en una Red con VLANs

| Tipo | Entre quiénes | Qué lleva |
|---|---|---|
| **Enlace Troncal (Trunk)** | Dos equipos "inteligentes" (ej. Router ↔ Switch Administrable) | Todas las VLANs **con etiquetas** |
| **Puerto de Acceso (Access)** | Equipo inteligente → dispositivo final | **Una sola VLAN**, sin etiqueta |

**Estrategia clave:** Los switches No Administrables se conectan a un **Puerto de Acceso** del router. Todo lo enchufado en ese switch pertenece automáticamente a esa VLAN, sin necesidad de configuración en el switch.

---

### 6. Listas de Control de Acceso (ACL)

Son **reglas de software** que se configuran en el Router 802.1Q para controlar qué redes pueden comunicarse entre sí. El router actúa como guardia de seguridad:

- `"Prohibir que la VLAN 20 (Estudiantes) acceda a la IP de la Impresora"`
- `"Prohibir que cualquier VLAN (excepto la 30) acceda a las IPs de los Servidores"`

---

### 7. Topología Resultante: Árbol (Estrella Extendida)

> [!success] Topología identificada
> El diseño de la red escolar corresponde a una **topología en Árbol** (también llamada Estrella Extendida o Topología Jerárquica).

**¿Por qué?**
- Las **"hojas"** (estrella local): Las PCs de cada aula se conectan a su switch local → forman una estrella.
- Las **"ramas" y el "tronco"** (jerarquía): Los switches de las aulas no se conectan directamente entre sí ni a Internet. Sus cables van hacia un nivel superior (Sala Técnica → Cuarto Técnico → Router).

**Ventaja:** Si un switch de un aula falla, solo esa aula pierde conexión. El resto de la escuela sigue funcionando.

---

## 🏫 El Ejercicio: Escuela con Red desde Cero

### Requisitos del Cliente

- [x] 1. Acceso a internet en toda la organización
- [x] 2. Conectar todos los HOSTs a la red
- [x] 3. Proteger los servidores (acceso restringido)
- [x] 4. Cada aula debe tener **mínimo 5 máquinas** (1 profesor + 4 alumnos)
- [x] 5. Servidores y área de administración IT en la **misma red**
- [x] 6. Todas las aulas **separadas** del resto de las redes
- [x] 7. Impresora disponible para todos **salvo estudiantes**
- [x] 8. AP (WiFi) **solo para el personal** de la institución

---

## 🧮 Fase 1: Análisis y Presupuesto

### Cálculo de Computadoras (Hosts)

| Área | Detalle | Cantidad |
|---|---|---|
| **Aulas (x3)** | 1 prof + 4 alumnos = 5 por aula | 15 PCs |
| **Secretaría** | 2 máquinas | 2 PCs |
| **Sala Operativa** | 2 devs + 1 compartida (2 admins en turnos) | 3 PCs |
| **TOTAL NECESARIO** | | **20 PCs** |
| **Disponibles (donadas)** | | 17 PCs |
| **A COMPRAR** | | **3 PCs** |

### Presupuesto Total Asignado

| Ítem | Cantidad | Precio Unit. | Total |
|---|---|---|---|
| Switches de 12p (No admin) | 5 | $200.000 | $1.000.000 |
| Switches 8p (Admin) | 2 | $15.000 | $30.000 |
| Routers sin 802.1Q | 2 | $350.000 | $700.000 |
| Router con 802.1Q | 1 | $450.000 | $450.000 |
| PCs | 5 | $650.000 | $3.250.000 |
| Access Point | 1 | $50.000 | $50.000 |
| ISP (contratación) | 1 | $150.000 | $150.000 |
| **TOTAL** | | | **$5.630.000** |

### Gasto Real (Lo que realmente compramos)

| Ítem | Precio |
|---|---|
| 3 PCs | $1.950.000 |
| 1 Router 802.1Q | $450.000 |
| 2 Switches Administrables 8p | $30.000 |
| 2 Switches de 12p (No admin) | $400.000 |
| 1 Access Point | $50.000 |
| ISP | $150.000 |
| **TOTAL GASTADO** | **$3.030.000** |

### 💰 Ganancia Final

$$\$5.630.000 - \$3.030.000 = \$2.600.000$$

---

## 🗺️ Fase 2: Diseño Lógico — VLANs

Se crean 3 redes virtuales (VLANs) en el Router 802.1Q:

| VLAN | Nombre | Equipos incluidos |
|---|---|---|
| **VLAN 10** | Gestión / Staff | Secretarias + Profesores (1 por aula) + AP (WiFi) |
| **VLAN 20** | Estudiantes | 4 PCs de alumnos por aula (12 en total) |
| **VLAN 30** | Administración IT | Sala Operativa + 3 Servidores |

> [!warning] La "trampa" del ejercicio
> Si conectás las 5 PCs de un aula al **mismo switch No Administrable**, ¡no podés separarlas por VLAN! La PC del profesor y las de los alumnos quedarían en la misma red. La solución es tirar cables separados para el profesor hacia un **Switch Administrable**.

---

## 🏗️ Fase 3: Diseño Físico — Ubicación de Equipos

### ¿Por qué no poner switches en las aulas?

> [!danger] Problema eléctrico
> El documento advierte que cada espacio tiene su propia llave térmica. Si el aula se vacía y se corta la luz, el switch dentro del aula se apaga. Si ese switch conectaba a otras salas, **toda la red cae**. Por eso, todo el equipamiento central va en el Cuarto Técnico o Sala Técnica (que tienen aire acondicionado y energía estable).

### Distribución por Sala

```
INTERNET (ISP)
     |
[Nube / ISP]  ← en Sala Técnica
     |
[Router Viejo sin 802.1Q]  ← en Sala Técnica (Router de Borde)
     |
[Router IEEE 802.1Q]  ← en Cuarto Técnico (Router Principal)
     |
[Switch Administrable 1 - 8p]  ← en Cuarto Técnico
     |         |           |
[Switch Adm 2] [PC Op.1] [PC Op.2] [PC Op.3]  [→ Switch No Admin Extra]
(Sala Técnica)                                  (Sala Administrativa)
```

#### Cuarto Técnico
- Router IEEE 802.1Q (cerebro de la red)
- Switch Administrable 1 (8 puertos) — el que la escuela ya tenía

#### Sala Técnica
- Router Viejo sin 802.1Q (Router de Borde — recibe el ISP)
- Switch Administrable 2 (8 puertos) — comprado nuevo
- Bloque de Switches No Administrables (para alumnos)
- 3 Servidores (Web, Correo, Archivos)

#### Sala Administrativa
- Switch No Administrable "extra" (de los sobrantes de la compra)
- 2 PCs de secretarias
- Impresora de red
- Access Point (WiFi)

---

## 🔌 Fase 4: Conexiones Puerto a Puerto

### Switch Administrable 1 — Cuarto Técnico (8p)

| Puerto | Tipo | Conexión |
|---|---|---|
| 1 | Troncal | → Router IEEE 802.1Q |
| 2 | Troncal | → Switch Administrable 2 (Sala Técnica) |
| 3 | VLAN 30 | PC Operativa 1 |
| 4 | VLAN 30 | PC Operativa 2 |
| 5 | VLAN 30 | PC Operativa 3 |
| 6 | VLAN 10 | → Switch No Admin extra (Sala Administrativa) |
| 7 | Libre | — |
| 8 | Libre | — |

### Switch No Administrable "Extra" — Sala Administrativa

Al conectarlo al Puerto 6 (VLAN 10) del Switch Adm. 1, **todo lo enchufado aquí pertenece automáticamente a la VLAN 10**.

| Puerto | Dispositivo |
|---|---|
| 1 | PC Secretaria 1 |
| 2 | PC Secretaria 2 |
| 3 | Impresora de red |
| 4 | Access Point (AP) |

### Switch Administrable 2 — Sala Técnica (8p)

| Puerto | Tipo | Conexión |
|---|---|---|
| 1 | Troncal | ← Switch Administrable 1 (Cuarto Técnico) |
| 2 | VLAN 30 | Servidor Web |
| 3 | VLAN 30 | Servidor Correo |
| 4 | VLAN 30 | Servidor Archivos |
| 5 | VLAN 10 | PC Profesor Aula 1 |
| 6 | VLAN 10 | PC Profesor Aula 2 |
| 7 | VLAN 10 | PC Profesor Aula 3 |
| 8 | VLAN 20 | → Bloque de Switches de Alumnos |

### Bloque de Switches de Alumnos — Sala Técnica

- Los switches No Administrables se conectan **en cascada (Daisy-chain)** entre sí.
- Un solo cable sale del grupo hacia el Puerto 8 (VLAN 20) del Switch Adm. 2.
- Las 12 PCs de alumnos (4 por aula) se enchufan a los puertos libres de estos switches.

> [!tip] Por qué cascada y no directa
> En lugar de gastar 3 bocas del switch administrable para los 3 switches de alumnos, los conectamos entre sí (daisy-chain) y sacamos **un solo cable** hacia el switch administrable. Ahorramos puertos y simplificamos el diseño.

---

## 📶 Fase 5: Configuración del Access Point (AP)

El documento pide explícitamente una lista de configuración para el AP.

| Parámetro | Valor / Configuración |
|---|---|
| **SSID** | `WiFi_Personal_Escuela` (nombre que no invite a alumnos) |
| **Seguridad** | WPA2-PSK o WPA3 con contraseña robusta. Ocultar SSID es recomendable. |
| **VLAN Asignada** | VLAN 10 (misma red que secretarias y profesores) |
| **Modo DHCP** | **Bridge/Puente** — el AP no reparte IPs; las IPs las asigna el Router 802.1Q |

> [!note] ¿Por qué modo Bridge?
> Si el AP funciona en modo Router, crea su propia sub-red y los dispositivos WiFi quedarían aislados del resto del personal. En modo Bridge/Puente, los dispositivos WiFi reciben IP directamente del Router 802.1Q como si estuvieran conectados por cable.

---

## ❓ ¿Por qué funciona todo aunque el Router Viejo no entiende VLANs?

> [!success] Respuesta: el Router 802.1Q es el "Traductor"
> Cada router tiene una tarea específica y **no necesitan entenderse entre sí a nivel VLAN**.

**División de responsabilidades:**

| Router | Trabajo | ¿Entiende 802.1Q? |
|---|---|---|
| **Router Interno (802.1Q)** | "Cerebro interno". Gestiona todas las VLANs de la escuela. Hacia adentro usa **Trunks**. | ✅ Sí |
| **Router de Borde (Viejo)** | Solo se comunica con el ISP. No le interesan las VLANs internas. | ❌ No (y no necesita) |

**El cable que une ambos routers es una conexión de acceso normal** (no un trunk). El Router 802.1Q le quita la etiqueta VLAN al paquete antes de pasárselo al Router Viejo.

### Flujo de un paquete: Alumno → Google

```
1. PC alumno envía dato
2. Switch Administrable le pone etiqueta "VLAN 20"
3. Dato llega al Router 802.1Q
4. Router 802.1Q: "Esto va a Internet" → le QUITA la etiqueta VLAN 20
5. Le pasa el paquete "limpio" al Router Viejo
6. Router Viejo lo manda a Internet → Google responde
7. Router 802.1Q recibe la respuesta y le VUELVE A PONER la etiqueta VLAN 20
8. Lo envía directo a la PC del alumno ✅
```

---

## ✅ Checklist Final de Requisitos

| # | Requisito | Estado | Cómo se cumplió |
|---|---|---|---|
| 1 | Internet en toda la organización | ✅ Cumplido | ISP → Router Viejo → Router 802.1Q → red interna |
| 2 | Conectar todos los HOSTs | ✅ Cumplido | 20 PCs conectadas (hay que recordar poner la 4ª PC de alumno en cada aula) |
| 3 | Servidores con acceso restringido | ✅ Cumplido | VLAN 30 + ACLs en Router 802.1Q |
| 4 | Mínimo 5 máquinas por aula | ✅ Cumplido | 1 prof (VLAN 10) + 4 alumnos (VLAN 20) = 5 |
| 5 | Servidores + IT en la misma red | ✅ Cumplido | Ambos en VLAN 30 |
| 6 | Aulas separadas del resto | ✅ Cumplido | VLAN 20 dedicada exclusivamente a alumnos |
| 7 | Impresora para todos salvo alumnos | ✅ Cumplido | Impresora en Switch de Sala Administrativa (VLAN 10) |
| 8 | WiFi solo para personal | ✅ Cumplido | AP conectado a VLAN 10, WPA2/WPA3 con contraseña |

---

## 🔗 Notas Relacionadas


---

#redes #practico #diagnostico #VLAN #802.1Q #switches #router #topologia
