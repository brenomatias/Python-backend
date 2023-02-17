# url = "bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
url = ' '

#sanitização dados
url = url.strip()

#validaçao url
if url == '':
    raise ValueError('Url vazia')

# Separa base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
print(indice_parametro)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:] #pega ultimo parametro
else:
    valor = url_parametros[indice_valor:indice_e_comercial] # pega parametros que tem '&' até o valor do parametro

print(indice_valor)
print(valor)