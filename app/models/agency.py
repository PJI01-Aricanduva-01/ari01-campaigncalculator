#importando a classe db do objeto app
from app import db

from datetime import datetime

#criando a classe que representa a tabela campaign_set
class Agency(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "agency"

    #atributos que se referem ao campos da tabela
    agency_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date_create = db.Column(db.DateTime)

    #buscando as relações de chave estrangeiras nas tabelas equivalentes

    campaign_set = db.relationship('Campaign_Set', back_populates='agency', primaryjoin='Agency.agency_id==Campaign_Set.agency_id')
    campaign = db.relationship('Campaign', back_populates='agency', primaryjoin='Agency.agency_id==Campaign.agency_id')
    ad_set = db.relationship('Ad_Set', back_populates='agency', primaryjoin='Agency.agency_id==Ad_Set.agency_id')
    ad = db.relationship('Ad', back_populates='agency', primaryjoin='Agency.agency_id==Ad.agency_id')

    user = db.relationship('User', back_populates='agency', primaryjoin='Agency.agency_id==User.agency_id')

    
    
    #método construtor
    def __init__(self, name):
        self.name = name
        self.date_create = datetime.now()

    #método de representação
    def __repr__(self):
        return "<Agency %r>" % self.name
