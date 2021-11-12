#script utilizado para popular a tabela Campaign_Objectives

#não possui utilidade

#guardado apenas para documentação


from app.models.campaignobjective import Campaign_Objective

from app import db

class copopulate():
    names = ['Reconhecimento da Marca',
             'Alcance',
             'Tráfego',
             'Engajamento',
             'Instalação do Aplicativo',
             'Visualizações do Vídeo',
             'Geração de Cadastros'
             'Mensagens',
             'Conversões',
             'Vendas do Catálogo',
             'Tráfego para Estabelecimento']

    def testit(self):
        for i in self.names:
            objective = Campaign_Objective(i)
            print(objective)

    def doit(self):
        for i in self.names:
            objective = Campaign_Objective(i)
            db.session.add(objective)
            db.session.commit()