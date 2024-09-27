import pytest

# Testes diretos da função calculadora
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

# Teste para simular entrada inválida
def test_entrada_invalida(monkeypatch):
    inputs = iter(["TestUser", "+", "dez", "5"])  # "dez" é inválido
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with pytest.raises(ValueError):
        calculadora()
