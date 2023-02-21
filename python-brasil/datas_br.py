from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
    
    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março", "abril",
            "maio", "junho", "julho", "agosto",
            "setembro", "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month-1
        print(mes_cadastro)
        return meses_do_ano[mes_cadastro]
    
    def dia_da_semana(self):
        dias_da_semana = [
            "segunda", "terça", "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        dia_cadastro = self.momento_cadastro.weekday()
        print(dia_cadastro)
        return dias_da_semana[dia_cadastro]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def __str__(self):
        return self.format_data()
    
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro