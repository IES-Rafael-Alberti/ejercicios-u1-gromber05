import pytest
from src.ej11_def import resultado

def test_resultado():
    assert resultado(1) == "El resultado es: 2.0"
    assert resultado(2) == "El resultado es: 4.5"
    assert resultado(3) == "El resultado es: 8.0"
    assert resultado(4) == "El resultado es: 12.5"
    assert resultado(5) == "El resultado es: 18.0"