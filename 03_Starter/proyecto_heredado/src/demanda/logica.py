"""Reglas de negocio: no leen archivos ni imprimen nada."""

import math
from collections.abc import Sequence


def estimar(ventas: Sequence[float], factor: float = 1.1) -> float:
    """Devuelve la media de las ventas multiplicada por el factor."""
    if not math.isfinite(factor) or factor <= 0:
        raise ValueError(f"El factor debe ser un número positivo: {factor}")
    if not ventas:
        raise ValueError("no hay ventas con las que estimar la demanda")

    for valor in ventas:
        if not math.isfinite(valor):
            raise ValueError(f"Hay un valor de ventas no finito: {valor}")
        if valor < 0:
            raise ValueError(f"Hay un valor de ventas negativo: {valor}")

    return sum(ventas) / len(ventas) * factor
