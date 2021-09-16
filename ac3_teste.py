import unittest
from ac3 import Calculadora

class PrimoTeste(unittest.TestCase):

    def teste_soma(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(20, 4, 'soma')
        self.assertEqual(24, resultado)

    def teste_subtracao(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(5, 2, 'subtracao')
        self.assertEqual(3, resultado)

    def teste_multiplicacao(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(7, 7, 'multiplicacao')
        self.assertEqual(49, resultado)

    def teste_divisao(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(100, 10, 'divisao')
        self.assertEqual(10, resultado)

    def teste_deve_retornar_0_caso_operador_invalido(self):
        calculadora = Calculadora()
        resultado = calculadora.calcular(2, 6, 'erro')
        self.assertEqual(0, resultado)
    
if __name__ == '__main__':
    unittest.main()
