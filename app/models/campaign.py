#importando a classe db do objeto app
from app import db

from datetime import datetime

#criando a classe que representa a tabela campaign_set
class Campaign(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "campaign"

    #atributos que se referem ao campos da tabela
    campaign_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    campaign_set_id = db.Column(db.Integer, db.ForeignKey('campaign_set.campaign_set_id'))
    date_creation = db.Column(db.DateTime)
    campaign_objective_id = db.Column(db.Integer, db.ForeignKey('campaign_objective.campaign_objective_id'))
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.agency_id'))

    #buscando as relações de chave estrangeiras nas tabelas equivalentes
    campaign_set = db.relationship('Campaign_Set', back_populates='campaign', foreign_keys='Campaign.campaign_set_id')

    ad_set = db.relationship('Ad_Set', back_populates='campaign', primaryjoin='Campaign.campaign_id==Ad_Set.campaign_id', cascade='all, delete-orphan')
    
    campaign_objective = db.relationship('Campaign_Objective', foreign_keys=campaign_objective_id)

    agency = db.relationship('Agency', back_populates='campaign', foreign_keys='Campaign.agency_id')


    #método construtor
    def __init__(self, name, campaign_set_id, campaign_objective_id, agency_id):
        self.name = name
        self.campaign_set_id = campaign_set_id
        self.campaign_objective_id = campaign_objective_id
        self.date_creation = datetime.now()
        self.agency_id = agency_id

    #método de representação
    def __repr__(self):
        return "<Campaign %r>" % self.name

    