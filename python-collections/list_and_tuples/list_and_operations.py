idades_list = [30, 12, 15, 15, 15,]
list2 = [2, 3, 5]

for value in idades_list:
    print(value)

idades_list.append(13)
idades_list.remove(30)
list2.clear()
print('Tamanho da lista {}'.format(len(idades_list)))

for idade in idades_list:
    print(idade)

for i in idades_list:
    idades_list.remove(15)

print(idades_list)

print(28 in idades_list)

# in, usado bastante para quando queremos filtrar alguma coisa.
if 18 in idades_list:
    print(idades_list[18])
else:
    print('Este numero nao esta na lista')

# inserir um item, que é o item x, na posição desejada.
idades_list.insert(1, 10)

# que estende a lista adicionando todos os itens desse iterável
idades_list.extend([25, 10])

idades_ano_que_vem = []
for idade in idades_list:
    idades_ano_que_vem.append(idade+1)


# list comprehension
idades_ano_que_vem = [(idade+1) for idade in idades_list]
maior_que_21 = [(idade) for idade in idades_list if idade > 21]

def proximo_ano(idade):
    return idade+1

maior_que_21_ano_que_vem = [proximo_ano(idade) for idade in idades_list if idade > 21]
print(maior_que_21_ano_que_vem)