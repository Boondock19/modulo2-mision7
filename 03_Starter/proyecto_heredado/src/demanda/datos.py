"""Lectura del archivo de ventas."""

import csv
from pathlib import Path

COLUMNA_VENTAS = "ventas"


def leer_ventas(ruta: Path) -> list[float]:
    """Devuelve los valores de la columna de ventas de un CSV."""
    # utf-8-sig también acepta el BOM que añade Excel al guardar en UTF-8.
    with open(ruta, encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if COLUMNA_VENTAS not in (lector.fieldnames or []):
            raise ValueError(f"{ruta} no tiene la columna '{COLUMNA_VENTAS}'")

        ventas = []
        for fila in lector:
            if None in fila:
                raise ValueError(
                    f"línea {lector.line_num}: hay más valores que columnas "
                    "(¿se usó coma decimal?)"
                )
            texto = fila[COLUMNA_VENTAS]
            try:
                ventas.append(float(texto))
            except (TypeError, ValueError):
                raise ValueError(
                    f"línea {lector.line_num}: valor de ventas no numérico: {texto!r}"
                ) from None
    return ventas
