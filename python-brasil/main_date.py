from datetime import datetime, timedelta
from datas_br import DatasBr

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_da_semana())

hoje = datetime.today()
hoje_formatada = hoje.strftime("%Y")
print(hoje)
print(hoje_formatada)

hoje_formatada = hoje.strftime("%d/%m/%Y")
print(hoje_formatada)

hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")
print(hoje_formatada)

print('data {}'.format(cadastro))

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1)
print(hoje - amanha)

hoje = DatasBr()
print(hoje.tempo_cadastro())