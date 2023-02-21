from cpf_cnpj import Documento

exemplo_cpf = "11800778651"
documento_cpf = Documento.cria_documento(exemplo_cpf)
exemplo_cnpj = "35379838000112"
documento_cnpj = Documento.cria_documento(exemplo_cnpj)

print(documento_cpf)
print(documento_cnpj)