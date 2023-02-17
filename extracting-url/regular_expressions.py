endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco) # search: buscar um padrão dentro da string (extrair)
if busca:
    cep = busca.group()
    print(cep)

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url) # match: verifica se a STRING INTEIRA bate com o padrão

if not match:
    raise ValueError('A url não é valida')
