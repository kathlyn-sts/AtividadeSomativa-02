import pytest

def test_soma():
    with pytest.raises(SystemExit):
        calculadora("10", "5", "+")

def test_subtracao():
    with pytest.raises(SystemExit):
        calculadora("10", "5", "-")

def test_multiplicacao():
    with pytest.raises(SystemExit):
        calculadora("10", "5", "*")

def test_divisao():
    with pytest.raises(SystemExit):
        calculadora("10", "5", "/")

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        calculadora("10", "0", "/")

def test_entrada_invalida():
    with pytest.raises(ValueError):
        calculadora("dez", "5", "+")  # "dez" é inválido
