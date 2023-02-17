class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return '[Codigo {} saldo {}]'.format(self.codigo, self.saldo)
    

def deposita_para_todos(contas):
    for conta in contas:
        conta.deposita(100)

conta_gui = ContaCorrente(2)
conta_gui.deposita(200)
print(conta_gui)

conta_dani = ContaCorrente(153)
conta_dani.deposita(1000)


contas = [conta_gui, conta_dani]

print(contas)

# print de um objeto especifico retorna a representaçao de string (__str__) dele
for conta in contas:
    print(conta)

deposita_para_todos(contas)
print(contas[0], contas[1])

    