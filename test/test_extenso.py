import pytest
from main import calculadora  # Importa a função calculadora do main.py

def test_soma():
    resultado = calculadora(10, 5, "+")
    assert resultado == 15

def test_subtracao():
    resultado = calculadora(10, 5, "-")
    assert resultado == 5

def test_multiplicacao():
    resultado = calculadora(10, 5, "*")
    assert resultado == 50

def test_divisao():
    resultado = calculadora(10, 5, "/")
    assert resultado == 2

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        calculadora(10, 0, "/")

def test_entrada_invalida():
    with pytest.raises(ValueError):
        calculadora(10, 5, "invalid_operation")
