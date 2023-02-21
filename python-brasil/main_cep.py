import requests
from cep_API import BuscaEndereco

cep = 35164237
obejto_cep = BuscaEndereco(cep)
print(obejto_cep)

r = requests.get("https://viacep.com.br/ws/{cep}/json/")
print(r)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text

result = obejto_cep.acessa_via_cep()
# print(type(result.text))

# print(type(result.json()))

# print(result.json())
# print(result.json()['cep'])
# print(result.json()['bairro'])
print(result)