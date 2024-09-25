import unittest
from src.main import calcular

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calcular(2, 3, '+'), 5)

    def test_subtracao(self):
        self.assertEqual(calcular(5, 3, '-'), 2)

    def test_multiplicacao(self):
        self.assertEqual(calcular(2, 3, '*'), 6)

    def test_divisao(self):
        self.assertEqual(calcular(6, 3, '/'), 2)

    def test_operacao_invalida(self):
        with self.assertRaises(ValueError):
            calcular(1, 1, '%')

if __name__ == "__main__":
    unittest.main()
