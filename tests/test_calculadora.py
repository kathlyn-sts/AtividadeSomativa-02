import unittest
from calculadora import calculadora  # Certifique-se de que o módulo está importado corretamente

class TestCalculadora(unittest.TestCase):
    
    def test_soma(self):
        self.assertEqual(calculadora('Usuário', '+', 2, 3), 5)
    
    def test_subtracao(self):
        self.assertEqual(calculadora('Usuário', '-', 5, 3), 2)
    
    def test_multiplicacao(self):
        self.assertEqual(calculadora('Usuário', '*', 2, 3), 6)
    
    def test_divisao(self):
        self.assertEqual(calculadora('Usuário', '/', 6, 3), 2)
    
    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculadora('Usuário', '/', 1, 0)

    def test_operacao_invalida(self):
        with self.assertRaises(ValueError):
            calculadora('Usuário', '%', 1, 1)

if __name__ == '__main__':
    unittest.main()
