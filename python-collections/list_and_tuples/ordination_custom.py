from operator import attrgetter
from list_polimorfism import ContaSalario 

conta_do_guilherme = ContaSalario(17)
conta_da_dani = ContaSalario(190)
conta_do_pedro = ContaSalario(3)

contas = [ conta_do_guilherme, conta_da_dani, conta_do_pedro]

for conta in contas:
    print(conta)

conta_da_dani.deposita(1000)
conta_do_guilherme.deposita(1000)
conta_do_pedro.deposita(1)

    
def extrai_saldo(conta):
    return conta._saldo

# ordenamento customizado (quebra encapsulamento)
for conta in sorted(contas, key=extrai_saldo):
    print(conta)

# nao precisa criar a funçao extrai_saldo (quebra encapsulamento)
for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)

print('#####')
# aqui só é possivel porque o metodo de comparaçao __lt__ foi criado na classe 'ContaSalario'
for conta in sorted(contas):
    print(conta)

# desempatar pelo critério 'id' (codigo)
for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
    print(conta)