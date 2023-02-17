usuarios = [
    ('Guilherme', 34, 1981),
    ('Daniela', 31, 1985),
    ('Paulo', 32, 1986)
]

idades = [14, 30, 31, 23, 10]
print(sorted(idades))
print(sorted(idades, reverse = True))

idades.sort() # sort() altera a lista original
print(idades)