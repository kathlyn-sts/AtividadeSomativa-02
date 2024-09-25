import pytest
from src.main import adicionar, subtrair, multiplicar, dividir

def test_adicionar():
    assert adicionar(1, 1) == 2
    assert adicionar(-1, 1) == 0
    assert adicionar(1.5, 2.5) == 4.0

def test_subtrair():
    assert subtrair(2, 1) == 1
    assert subtrair(0, 5) == -5

def test_multiplicar():
    assert multiplicar(3, 3) == 9
    assert multiplicar(-1, 5) == -5

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3
    with pytest.raises(ValueError):
        dividir(10, 0)
