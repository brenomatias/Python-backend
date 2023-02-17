from abc import ABCMeta, abstractmethod
from functools import total_ordering

class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita(self, valor):
        self._saldo += valor
    
    @abstractmethod
    def passa_o_mes(self, valor):
        pass
    
    def __str__(self):
        return '[Codigo {} Saldo {}]'.format(self._codigo, self._saldo)

class ContaCorrente(Conta):
    def passa_o_mes(self, valor = 2):
        self._saldo -= valor

class ContaPoupanca(Conta):
    def passa_o_mes(self, valor = 3):
        self._saldo *= 1.01
        self._saldo -= valor

conta16 = ContaCorrente(16)
conta16.deposita(1000)
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
print(conta17)

contas = [conta16, conta17]

# polimorfismo
for conta in contas:
    conta.passa_o_mes()

for conta in contas:
    print(conta)


# métodos abstratos
#  se você tem um método que você quer definir na sua classe mãe e que todo mundo seja forçado a implementar, coloque um @abstractmethod nela, defina ela como uma classe abstrata através da meta classe ABCmeta

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita(self, valor):
        self._saldo += valor
    
    def __str__(self):
        return '[Codigo {} Saldo {}]'.format(self._codigo, self._saldo)
    
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo
    

conta1 = ContaSalario(15)
print(conta1)
print('############')

contas = [conta16, conta17, conta1]

