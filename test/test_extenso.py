import unittest
from src.main import calculadora  # Verifique se o caminho está correto

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(calculadora(2, 3, '+'), 5)

    def test_subtracao(self):
        self.assertEqual(calculadora(5, 2, '-'), 3)

if __name__ == '__main__':
    unittest.main()
