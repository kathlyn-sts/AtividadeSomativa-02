import pytest
from src.calculadora import calculadora  # Ajuste para refletir o caminho correto

class TestCalculadora:

    def test_soma(self):
        assert calculadora('Usuário', '+', 2, 3) == 5
    
    def test_subtracao(self):
        assert calculadora('Usuário', '-', 5, 3) == 2
    
    def test_multiplicacao(self):
        assert calculadora('Usuário', '*', 2, 3) == 6
    
    def test_divisao(self):
        assert calculadora('Usuário', '/', 6, 3) == 2
    
    def test_divisao_por_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculadora('Usuário', '/', 1, 0)

    def test_operacao_invalida(self):
        with pytest.raises(ValueError):
            calculadora('Usuário', '%', 1, 1)
