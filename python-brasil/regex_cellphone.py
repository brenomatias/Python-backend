import re

padrao_molde = "(xx)aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto do numero 2126451234 2126451255"
resposta = re.findall(padrao, texto)
print(resposta)