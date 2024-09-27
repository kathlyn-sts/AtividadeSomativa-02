import unittest
from src.main import calculadora  # Certifique-se de que o caminho está correto

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora(1, 2, '+'), 3)

    def test_subtracao(self):
        self.assertEqual(calculadora(5, 2, '-'), 3)

    def test_multiplicacao(self):
        self.assertEqual(calculadora(3, 2, '*'), 6)

    def test_divisao(self):
        self.assertEqual(calculadora(6, 2, '/'), 3)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            calculadora(5, 0, '/')

    def test_operacao_invalida(self):
        with self.assertRaises(ValueError):
            calculadora(5, 2, '%')

if __name__ == '__main__':
    unittest.main()
