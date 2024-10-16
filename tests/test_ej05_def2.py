import pytest

from src.ej05_def2 import calcula_precio

def test_calcula_precio():
    assert calcula_precio(10, 0.21) == 12.1
    assert calcula_precio(15, 0.21) == 18.15
    assert calcula_precio(10, 10.00) == 12.1
    assert calcula_precio(10, 0.34) == 13.4
    assert calcula_precio(15, 0.51) == 22.65