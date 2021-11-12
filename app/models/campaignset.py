#importando a classe db do objeto app
from app import db

#criando a classe que representa a tabela campaign_set
class Campaign_Set(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "campaign_set"

    #atributos que se referem ao campos da tabela
    campaign_set_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date_creation = db.Column(db.DateTime)

    #método construtor
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Campaign_Set %r>" % self.name

    