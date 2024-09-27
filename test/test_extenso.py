import pytest
from src.main import calculadora

def test_soma(monkeypatch):
    inputs = iter(["TestUser", "+", "10", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        calculadora()

def test_subtracao(monkeypatch):
    inputs = iter(["TestUser", "-", "10", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        calculadora()

def test_multiplicacao(monkeypatch):
    inputs = iter(["TestUser", "*", "10", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        calculadora()

def test_divisao(monkeypatch):
    inputs = iter(["TestUser", "/", "10", "5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(SystemExit):
        calculadora()

def test_divisao_por_zero(monkeypatch):
    inputs = iter(["TestUser", "/", "10", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(ZeroDivisionError):
        calculadora()

def test_entrada_invalida(monkeypatch):
    inputs = iter(["TestUser", "+", "dez", "5"]) 
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    with pytest.raises(ValueError):
        calculadora()
