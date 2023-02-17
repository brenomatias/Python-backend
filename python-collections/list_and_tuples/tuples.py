guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

conta_do_gui = (15, 1000)

def deposita(conta):
    novo_saldo = conta[1] + 100
    codigo = conta[0]
    return (codigo, novo_saldo)

conta_do_gui = deposita(conta_do_gui)
print(conta_do_gui)

usuarios = [guilherme, daniela]
usuarios.append(('Paulo', 30, 1984))
print(usuarios)