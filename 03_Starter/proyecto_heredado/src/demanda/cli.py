"""Punto de entrada: conecta configuración, datos y lógica, y muestra el resultado."""

import csv
import sys
from collections.abc import Sequence

from demanda.config import cargar_config
from demanda.datos import leer_ventas
from demanda.logica import estimar


def main(argv: Sequence[str] | None = None) -> int:
    try:
        config = cargar_config(argv)
        demanda = estimar(leer_ventas(config.archivo), config.factor)
    except OSError as error:
        print(
            f"Error: no se pudo leer {error.filename}: {error.strerror}",
            file=sys.stderr,
        )
        return 1
    except (ValueError, csv.Error) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(f"Demanda prevista: {demanda:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
