import pytest
from src.ej02_def import horario

def test_horario():
    assert horario(10, 10) == 100
    assert horario(5, 10) == 50
    assert horario(5, 5) == 25
    assert horario(7, 8) == 56
    assert horario(4, 7) == 28