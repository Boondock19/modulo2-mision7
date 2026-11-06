Proyecto heredado. Ejecutar `python app.py`. Debéis identificar sus limitaciones y convertirlo en un paquete profesional. El fichero ventas.csv se entrega para pruebas. No modifiquéis la carpeta original: trabajad en vuestro repositorio.

# Estimador de demanda

Estima la demanda de un producto a partir de sus ventas recientes:

```text
demanda = media de las ventas × factor
```

Es la versión profesionalizada del proyecto heredado de la Misión 7. El script original, `app.py`, se conserva sin cambios en esta carpeta como referencia.

## Requisitos

- Python 3.10 o superior (el curso recomienda 3.11)
- Git

El programa solo usa la biblioteca estándar de Python. `requirements.txt` instala las herramientas de desarrollo: pytest y Ruff.

## Instalación desde cero

Clona el repositorio y entra en la carpeta del proyecto:

```bash
git clone https://github.com/Boondock19/modulo2-mision7.git
cd modulo2-mision7/03_Starter/proyecto_heredado
```

Crea y activa el entorno virtual:

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

```powershell
# Windows (PowerShell)
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Con el entorno activado, instala las dependencias y el proyecto:

```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

En VS Code, selecciona el intérprete con `Python: Select Interpreter` → `.venv`.

## Uso

```bash
demanda                            # usa ventas.csv y el factor 1.1
demanda ruta/a/ventas.csv          # usa otro archivo
demanda ruta/a/ventas.csv --factor 1.5
demanda --help
```

Con el archivo incluido, el resultado esperado es:

```text
Demanda prevista: 22.00
```

## Configuración

Cada valor se toma de la primera fuente que lo defina: argumento, variable de entorno o valor por defecto.

| Valor | Argumento | Variable de entorno | Por defecto |
|---|---|---|---|
| Archivo CSV | `archivo` | `DEMANDA_CSV` | `ventas.csv` de esta carpeta |
| Multiplicador | `--factor` | `DEMANDA_FACTOR` | `1.1` |

Para definir una variable en la sesión actual:

```bash
export DEMANDA_FACTOR=1.5            # macOS / Linux
```

```powershell
$env:DEMANDA_FACTOR = "1.5"          # Windows (PowerShell)
```

El programa no carga archivos `.env` automáticamente.

## Formato del archivo

El CSV debe estar en UTF-8, usar coma como separador y tener una columna `ventas`. Puede tener más columnas. Los decimales se escriben con punto:

```csv
mes,ventas
enero,10
febrero,20.5
```

El programa termina con un mensaje de error y código de salida 1 si:

- el archivo no se puede leer o no tiene la columna `ventas`
- no hay datos
- hay valores vacíos, no numéricos, no finitos (`nan`, `inf`) o negativos
- una fila tiene más valores que columnas, por ejemplo por usar coma decimal
- el factor no es un número positivo

## Calidad

```bash
python -m pytest -q
ruff check .
ruff format --check .
```

## Estructura

```text
src/demanda/
├── logica.py    # cálculo y validación, sin archivos ni print
├── datos.py     # lectura del CSV
├── config.py    # argumentos y variables de entorno
└── cli.py       # punto de entrada y mensajes al usuario
tests/           # pruebas con pytest
ventas.csv       # datos de ejemplo
app.py           # script heredado original, sin cambios
```

Consulta también [`diagnostico.md`](diagnostico.md) y [`evidencias.md`](evidencias.md).
