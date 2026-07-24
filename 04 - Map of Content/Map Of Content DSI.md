


# Parcial 2
## Practico

## TEO
### fleeting Notes
```dataview
TABLE type AS "Teórico", unit AS "Unidad", status AS "Estado"
FROM "01 - Fleeting Notes"
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
