idades = [14, 30, 31, 23, 10]

for i in range(len(idades)):
    print(i, idades[i])

print(enumerate(idades))

print('Posiçõesa array {}'.format(list(range(len(idades))))) # com list força a geração dos valores
print('Enumerate {}'.format(list(enumerate(idades))))

for valor in enumerate(idades):
    print(valor)

# Quando utilizamos o enumerate, ele faz a enumeração dos valores automaticamente
for i, idade in enumerate(idades):
    print(i, idade)

for i, idade in enumerate(idades): #unpacking da tupla
    print(i, 'x', idade)

usuarios = [
    ('Guilherme', 34, 1981),
    ('Daniela', 31, 1985),
    ('Paulo', 32, 1986)
]

# desempacotarmos essas nossas tuplas buscando apenas um elemento
for nome, idade, nascimento in usuarios:
    print(nome)

for nome, _, _ in usuarios:
    print(nome)

for nome, _, nascimento in usuarios:
    print(nome, nascimento)