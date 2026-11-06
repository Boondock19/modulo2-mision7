import pytest

from demanda.config import cargar_config
from demanda.logica import estimar


def test_entrada_normal():
    assert estimar([10.0, 20.0, 30.0], factor=1.1) == pytest.approx(22.0)


def test_entrada_vacia():
    with pytest.raises(ValueError, match="no hay ventas"):
        estimar([], factor=1.1)


def test_ventas_negativas():
    with pytest.raises(ValueError, match="negativo"):
        estimar([10.0, -1.0], factor=1.1)


def test_parametro_invalido_texto():
    with pytest.raises(ValueError, match="factor"):
        cargar_config(["--factor", "abc"], {})