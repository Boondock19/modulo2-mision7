"""Configuración. Prioridad: argumentos > variables de entorno > valores por defecto."""

import argparse
import os
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

# Se calcula desde este archivo para no depender de la carpeta de ejecución.
ARCHIVO_POR_DEFECTO = Path(__file__).resolve().parents[2] / "ventas.csv"
FACTOR_POR_DEFECTO = 1.1


@dataclass(frozen=True)
class Config:
    archivo: Path
    factor: float


def cargar_config(
    argv: Sequence[str] | None = None,
    entorno: Mapping[str, str] = os.environ,
) -> Config:
    parser = argparse.ArgumentParser(
        prog="demanda",
        description="Estima la demanda de un producto a partir de sus ventas.",
    )
    parser.add_argument(
        "archivo",
        nargs="?",
        help="CSV con una columna 'ventas' (o variable DEMANDA_CSV)",
    )
    parser.add_argument(
        "--factor",
        help=(
            "multiplicador aplicado a la media (o variable DEMANDA_FACTOR; "
            f"por defecto, {FACTOR_POR_DEFECTO})"
        ),
    )
    argumentos = parser.parse_args(argv)

    # "or" hace que una variable definida pero vacía cuente como no definida.
    archivo = argumentos.archivo or entorno.get("DEMANDA_CSV") or ARCHIVO_POR_DEFECTO
    factor = argumentos.factor or entorno.get("DEMANDA_FACTOR") or FACTOR_POR_DEFECTO

    try:
        factor = float(factor)
    except ValueError:
        raise ValueError(f"El factor debe ser un número: {factor!r}") from None

    return Config(archivo=Path(archivo), factor=factor)
