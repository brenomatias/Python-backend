from bytebank import Funcionario

'''
lucas = Funcionario('Lucas', '13/03/2000', 1000)
print(lucas.idade())
print(lucas)
'''
def test_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste1 = Funcionario('Teste', '13/03/1999', 2000)
    print(f'Teste = {funcionario_teste1.idade()}')


test_idade()

ana = Funcionario("Ana", "13/12/2000", 100000)
print(ana.calcular_bonus())