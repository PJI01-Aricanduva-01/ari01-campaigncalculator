#importando a classe db do objeto app
from app import db

from datetime import datetime

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
    total_budget = db.Column(db.Numeric, db.Computed('budget * (date_end - date_start.day)'))
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.agency_id'))
    

    #buscando as relações de chave estrangeiras nas tabelas equivalentes
    campaign = db.relationship('Campaign', back_populates='ad_set', foreign_keys='Ad_Set.campaign_id')
    
    agency = db.relationship('Agency', back_populates='ad_set', foreign_keys='Ad_Set.agency_id')

    ad = db.relationship('Ad', back_populates='ad_set', primaryjoin='Ad_Set.ad_set_id==Ad.ad_set_id', cascade='all, delete-orphan')

    #método construtor
    def __init__(self, name, campaign_id, date_start, date_end, public, budget, agency_id):
        self.name = name
        self.campaign_id = campaign_id
        self.date_start = date_start
        self.date_end = date_end
        self.public = public
        self.budget = budget        
        self.agency_id = agency_id

    #método de representação
    def __repr__(self):
        return "<Add_Set %r>" % self.name

    