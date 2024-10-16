import pytest
from src.ej01_def import saludo

def test_saludo():
    assert saludo("Juan") == 'Hola, Juan.'
    assert saludo("Hector") == 'Hola, Hector.'
    assert saludo("Jesús") == 'Hola, Jesús.'
    assert saludo("David") == 'Hola, David.'
    assert saludo("Diego") == 'Hola, Diego.'