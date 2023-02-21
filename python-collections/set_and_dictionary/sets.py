usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]
assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

print(set(assistiram))

print(set([4,1,2,3,1]))

for usuario in set(assistiram):
    print(usuario)

# para sets, extend() = | 'ou' (união dos conjuntos)
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
assistiram2 = usuarios_data_science | usuarios_machine_learning
print(assistiram2)

# intersecção dos conjuntos.
assistiram3 = usuarios_machine_learning & usuarios_data_science
print(assistiram3)

# quem está no usuario_data_science mas não está no Machine Learning.
assistiram4 = usuarios_data_science - usuarios_machine_learning
print(assistiram4)

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
print(15 in fez_ds_mas_nao_fez_ml)

usuarios = {1,3,5,12,55,24,15}
usuarios.add(156) #nao é append -> append adiciona no final, e sets nao tem ordem
print(usuarios)

usuarios = frozenset(usuarios)
print(type(usuarios))

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
print(set(meu_texto.split('')))