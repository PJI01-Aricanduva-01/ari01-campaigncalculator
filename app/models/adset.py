#importando a classe db do objeto app
from app import db

#criando a classe que representa a tabela campaign_set
class Ad_Set(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "ad_set"

    #atributos que se referem ao campos da tabela
    ad_set_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.campaign_id'))
    date_start = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)
    public = db.Column(db.String)
    budget = db.Column(db.Integer)

    #buscando as relações de chave estrangeiras nas tabelas equivalentes
    campaign = db.relationship('Campaign', foreign_keys=campaign_id)

    #método construtor
    def __init__(self, name, campaign_set_id, campaign_objective_id):
        self.name = name
        self.campaign_id = campaign_set_id

    #método de representação
    def __repr__(self):
        return "<Add_Set %r>" % self.name

    