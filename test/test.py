import unittest
from src.main import calculadora

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora(2, 3, '+'), 5)

    def test_subtracao(self):
        self.assertEqual(calculadora(10, 5, '-'), 5)

    def test_multiplicacao(self):
        self.assertEqual(calculadora(4, 3, '*'), 12)

    def test_divisao(self):
        self.assertEqual(calculadora(10, 2, '/'), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            calculadora(10, 0, '/')

    def test_operacao_invalida(self):
        with self.assertRaises(ValueError):
            calculadora(10, 5, '%')

if __name__ == '__main__':
    unittest.main()
