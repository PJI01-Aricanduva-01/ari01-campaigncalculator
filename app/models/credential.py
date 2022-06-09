#importando a classe db do objeto app
from app import db

#criando a classe que representa a tabela campaign_set
class Credential(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "credential"

    #atributos que se referem ao campos da tabela
    credential_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    habilitie_01 = db.Column(db.Bit)
    habilitie_02 = db.Column(db.Bit)
    habilitie_03 = db.Column(db.Bit)

    
    #método construtor
    def __init__(self, credential_id, name, habilitie_01, habilitie_02, habilitie_03):
        self.credential_id = credential_id
        self.name = name
        self.habilitie_01 = habilitie_01
        self.habilitie_02 = habilitie_02
        self.habilitie_03 = habilitie_03


    #método de representação
    def __repr__(self):
        return "<Credential %r>" % self.name
