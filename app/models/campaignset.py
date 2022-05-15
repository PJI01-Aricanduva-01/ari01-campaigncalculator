#importando a classe db do objeto app
from app import db

from datetime import datetime

#criando a classe que representa a tabela campaign_set
class Campaign_Set(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "campaign_set"

    #atributos que se referem ao campos da tabela
    campaign_set_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    date_creation = db.Column(db.DateTime)
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.agency_id'))

    campaign = db.relationship('Campaign', back_populates='campaign_set', primaryjoin='Campaign_Set.campaign_set_id==Campaign.campaign_set_id', cascade='all, delete-orphan')
    agency = db.relationship('Agency', back_populates='campaign_set', foreign_keys='Campaign_Set.agency_id')

    #método construtor
    def __init__(self, name, agency_id):
        self.name = name
        self.date_creation = datetime.now()
        self.agency_id = agency_id

    def __repr__(self):
        return "<Campaign_Set %r>" % self.name

    