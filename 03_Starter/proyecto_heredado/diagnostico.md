# Diagnóstico del proyecto heredado

Con el `ventas.csv` entregado y desde su propia carpeta, `python app.py` funciona y muestra `Demanda prevista: 22.0`. Los problemas aparecen al cambiar los datos del csv.

Los fallos se reprodujeron con Python 3.14.6 sobre el `app.py` original.

## Fallos encontrados

| # | Síntoma | Causa | Corrección |
|---|---|---|---|
| 1 | No hay ningún tipo de validación de los datos de entrada en el CSV ni sobre la función de estimar | `estimar()` y `ejecutar()` usan los datos sin comprobarlos | Validaciones en `datos.py` y `logica.py` |
| 2 | Código sin modularizar | `ejecutar()` mezcla lectura, cálculo e impresión en un solo archivo | Módulos `datos`, `logica`, `config` y `cli` |
| 3 | README en formato `.txt` | Es texto plano, sin títulos, listas ni bloques de código | `README.md` con instalación, uso y configuración |

## Problemas de diseño y mantenimiento

| # | Problema | Evidencia | Corrección |
|---|---|---|---|
| 4 | El factor `1.1` está fijo y sin explicar | Lectura del código, `app.py:8` | `--factor` y `DEMANDA_FACTOR`, con validación |
| 5 | Codificación del archivo sin definir | Lectura del código, `app.py:11` | Abrir con `utf-8-sig`, que también acepta el BOM de Excel |
| 6 | Código sin pasar Ruff | `ruff check --isolated`: `F401` (`os` sin usar) e `I001` (imports sin ordenar) | Quitar el import y mantener Ruff en el proyecto nuevo |
| 7 | Sin pruebas | No existe ningún test | Cuatro pruebas de pytest en `tests/` |
| 8 | Sin `requirements.txt`, `.gitignore` ni instrucciones de instalación | Contenido de la carpeta original | Añadidos en esta carpeta |
