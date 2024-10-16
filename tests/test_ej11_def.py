import pytest
from src.ej11_def import resultado

def test_resultado():
    assert resultado(1) == 2
    assert resultado(2) == 4.5
    assert resultado(3) == 8.0
    assert resultado(4) == 12.5
    assert resultado(5) == 18.0