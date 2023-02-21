from collections import defaultdict, Counter

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()
# meu_texto = meu_texto.split()
print(meu_texto)

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1
print(aparicoes)

class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)

aparicoes2 = Counter()
for palavra in meu_texto.split():
    aparicoes2[palavra] += 1
print(aparicoes2)

aparicoes3 = Counter(meu_texto.split())
print(aparicoes3)