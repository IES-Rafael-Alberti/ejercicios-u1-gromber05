import pytest

from src.ej05_def2 import calcula_precio

def test_calcula_precio():
    assert calcula_precio(10, 0.21) == 12.1