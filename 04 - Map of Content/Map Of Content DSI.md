


# Parcial 2
![[DSI-P2-MapaMental.excalidraw]]

## Practico
```dataview
TABLE type AS "Practico", status AS "Estado"
FROM  "03 - Permanent Notes"
WHERE subject = "DSI" AND exam = "PARCIAL2" and type = "PRACTICO"
SORT unit ASC, type DESC
```
## TEO
### fleeting Notes
```dataview
TABLE type AS "Teórico", unit AS "Unidad", status AS "Estado"
FROM "3ro/dsi/P2/Fleeting notes"
WHERE subject = "DSI" AND exam = "PARCIAL2" and type = "TEO"
SORT unit ASC, type DESC
```

### Permanet Notes
```dataview
TABLE type AS "Teórico", unit AS "Unidad", status AS "Estado"
FROM  "03 - Permanent Notes"
WHERE subject = "DSI" AND exam = "PARCIAL2" and type = "TEO"
SORT unit ASC, type DESC
```



# Recomendaciones PRACTICAS
🚀 Consejos Generales para el Examen

- **Comprensión del Problema:** Antes de escribir una sola línea, lee y entiende el enunciado completo. Si no entiendes alguna palabra, pregunta. Es clave que puedas explicar el "corazón" del sistema en pocas palabras para identificar correctamente los dominios y las transacciones más importantes.
- **Organización:** Usa **hojas separadas para cada vista** (Funcional, Subdominios, Global, Detallada, Despliegue). Esto no solo te ayuda a mantener el orden y la consistencia entre las vistas, sino que también facilita la corrección.
- **Consistencia y Trazabilidad:** Mantenga una trazabilidad y consistencia claras entre todas las vistas. Lo que defina en una vista debe reflejarse coherentemente en las siguientes