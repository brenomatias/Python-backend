import re

padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)
print(resposta.group())

padrao_email = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto_email = "aaabbbcc rodrigo123@gmail.com.br"
resposta_email = re.search(padrao_email, texto_email)
print(resposta_email.group())

padrao_email_brasileiro = "\w{5,50}@[a-z]{3,10}.com.br"
texto_email_br = "aaabbbcc rodrigo123@gmail.com.br ccbbbaaa"
resposta_email_br = re.search(padrao_email_brasileiro, texto_email_br)
print(resposta_email_br.group())