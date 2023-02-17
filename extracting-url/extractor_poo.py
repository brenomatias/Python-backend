import re

class UrlExtractor():
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def __str__(self):
        return self.url + '\n' + 'Parametros: ' + self.get_url_parametros() + '\n' + 'URL Base: ' + self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other.url

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else: 
            return ''
    
    def valida_url(self):
        if not self.url:
            raise ValueError('Url vazia')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")
    
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) +1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def __len__(self):
        return len(self.url)
    


url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
extrator_url = UrlExtractor(url)
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)
print('O tamanho da URL: ', len(extrator_url)) # se a classe nao tiver o metodo __len__ nao é possivel fazer len(extractor_url)

print(extrator_url)

extrator_url2 = UrlExtractor(url)

print(extrator_url == extrator_url2) # comparaçao de objetos (__eq__)

print(id(extrator_url)) # registro de memória do objeto (identidade do obejto)

# is x ==

# Desafio
Valor_dolar = 5.5
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')

if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_conversao = int(quantidade)/ Valor_dolar
    print('O valor de R$' + quantidade + ' reais é igual a $' + str(valor_conversao) + 'dolares')
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_conversao = int(quantidade) * Valor_dolar
    print(' O valor de $' + quantidade + 'dolares é igual a R$' + str(valor_conversao) + 'reais')
else:
    print(f'Cambio de {moeda_origem} para {moeda_destino} não está disponível')