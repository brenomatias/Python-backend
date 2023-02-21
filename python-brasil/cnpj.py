from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.cnpj_eh_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("Tamanho cnpj inválido")
    
    def __str__(self):
        return self.format_cnpj
    
    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            raise ValueError("CNPJ inválid")

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)