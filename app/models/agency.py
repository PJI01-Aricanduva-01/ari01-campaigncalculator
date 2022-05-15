#importando a classe db do objeto app
from app import db

#criando a classe que representa a tabela campaign_set
class Agency(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "agency"

    #atributos que se referem ao campos da tabela
    agency_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date_create = db.Column(db.DataTime)

    
    #método construtor
    def __init__(self, agency_id, name, date_create):
        self.agency_id = agency_id
        self.name = name
        self.date_create = date_create

    #método de representação
    def __repr__(self):
        return "<Agency %r>" % self.name
