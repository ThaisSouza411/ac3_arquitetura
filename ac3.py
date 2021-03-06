from abc import ABC, abstractmethod

class Calculadora():

    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if operacao == None:
            return 0
        else:
            resultado = operacao.executar(valor1, valor2)
            return resultado

class OperacaoFabrica:
    def criar(self, operador):
        if(operador == 'soma'):
            return Soma()
        elif (operador == 'subtracao'):
            return Subtracao()
        elif(operador == 'divisao'):
            return Divisao()
        elif(operador == 'multiplicacao'):
            return Multiplicacao()

class Operacao(ABC):
    @abstractmethod
    def executar(self, valor1, valor2):
        pass

class Soma(Operacao):
    def executar(self, valor1, valor2):
        return valor1 + valor2
    
class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 - valor2

class Multiplicacao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 * valor2

class Divisao(Operacao):
    def executar(self, valor1, valor2):
        return valor1 / valor2
