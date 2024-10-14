import pytest 

from src.ej04_def2 import grados_celsius

def test_grados_celsius():
    assert grados_celsius(10) == 50.0
    assert grados_celsius(20) == 68.0