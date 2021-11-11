#importando a classe db do objeto app
from app import db

#criando a classe que representa a tabela campaign_set
class Campaign_Objective(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "campaign_objective"

    #atributos que se referem ao campos da tabela
    campaign_objective_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    #método construtor
    def __init__(self, name):
        self.name = name

    #método de representação
    def __repr__(self):
        return "<Campaign_Objective %r>" % self.name

    