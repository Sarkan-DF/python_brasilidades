from datetime import datetime,timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_datas()

    def mes_cadastro(self):
        meses_do_ano = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
                        "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        mes_cadastro = self.momento_cadastro.month -1
        return meses_do_ano[mes_cadastro]

    def dia_semana_cadastro(self):
        dias_semana = ["Segunda","Terça","Quarta","Quinta","Sexta","Sadado","Domingo",]
        dias_semana_cadastro = self.momento_cadastro.weekday()
        return dias_semana[dias_semana_cadastro]

    def format_datas(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y")
        return data_formatada

    def tempo_de_cadastro(self):
        tempo_de_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_de_cadastro