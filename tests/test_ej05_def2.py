import pytest

from src.ej05_def2 import calcula_precio

def test_calcula_precio():
    assert calcula_precio(10, 0.21) == "El precio final del artículo con IVA (21%) es 12.1€."
    assert calcula_precio(15, 0.21) == "El precio final del artículo con IVA (21%) es 18.15€."
    assert calcula_precio(10, 10.00) == "El precio final del artículo con IVA (21%) es 12.1€."
    assert calcula_precio(10, 0.34) == "El precio final del artículo con IVA (34%) es 13.4€."
    assert calcula_precio(15, 0.51) == "El precio final del artículo con IVA (51%) es 22.65€."
    