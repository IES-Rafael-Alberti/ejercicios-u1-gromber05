import pytest

from src.ej05_def2 import calcula_precio

def test_calcula_precio():
    assert calcula_precio(10, 0.21) == "El precio con iva ha sido un total de 12.1 y el iva añadido ha sido un total de 2.1"