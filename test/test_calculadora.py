# tests/test_calculadora.py

import unittest
from src.main import calculadora

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora(2, 3, '+'), 5)

    def test_subtracao(self):
        self.assertEqual(calculadora(5, 2, '-'), 3)

    def test_multiplicacao(self):
        self.assertEqual(calculadora(3, 4, '*'), 12)

    def test_divisao(self):
        self.assertEqual(calculadora(10, 2, '/'), 5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            calculadora(10, 0, '/')

    def test_operacao_invalida(self):
        with self.assertRaises(ValueError):
            calculadora(10, 2, '%')

    def test_soma_negativos(self):
        self.assertEqual(calculadora(-1, -1, '+'), -2)

    def test_subtracao_negativos(self):
        self.assertEqual(calculadora(-5, -2, '-'), -3)

    def test_multiplicacao_negativos(self):
        self.assertEqual(calculadora(-3, -4, '*'), 12)

    def test_divisao_negativos(self):
        self.assertEqual(calculadora(-10, -2, '/'), 5)

    def test_soma_com_zero(self):
        self.assertEqual(calculadora(0, 5, '+'), 5)

    def test_subtracao_com_zero(self):
        self.assertEqual(calculadora(5, 0, '-'), 5)

    def test_divisao_com_zero(self):
        self.assertEqual(calculadora(0, 1, '/'), 0)

if __name__ == '__main__':
    unittest.main()
