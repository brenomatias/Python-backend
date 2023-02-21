aparicoes = {
    'Guilherme': 1,
    'cachorro': 2,
    'nome': 2,
    'vindo': 1
}

print(aparicoes['Guilherme'])

#  eu quero pegar a chave "xpto", se não estiver lá dentro a chave "xpto", devolva zero ('not found')
print(aparicoes.get('xpto', 'not found'))

aparicoes = dict(Guilherme = 2, cachorro = 1)

#adicionar valor dicionario
aparicoes['Carlos'] = 3
print(aparicoes)

# alterar valor dicionario
aparicoes['Carlos'] = 5
print(aparicoes)

# remover elemento
del aparicoes['Carlos']

# in funciona para buscar nas chaves e não nos valore
'cachorro' in aparicoes

# esse iterável retorna o quê? As chaves e não os valores
# in padrao busca nas chaves
for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

1 in aparicoes.values()

for elemento in aparicoes.keys():
    print(elemento, aparicoes[elemento])

# um item é uma dupla
for elemento in aparicoes.items():
    print(elemento)

# desempacotar de uma vez só
for chave, valor in aparicoes.items():
    print(chave, '=', valor)

# lit comprhension
print(['palavra = {}'.format(chave) for chave in aparicoes])