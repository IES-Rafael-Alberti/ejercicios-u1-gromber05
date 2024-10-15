import pytest
from src.ej01_def import saludo

def test_saludo():
    assert saludo("Juan") == 'Hola, Juan.'