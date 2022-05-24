#importando a classe db do objeto app
from app import db

#criando a classe que representa a tabela campaign_set
class Ad(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "ad"

    #atributos que se referem ao campos da tabela
    ad_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ad_set_id = db.Column(db.Integer, db.ForeignKey('ad_set.ad_set_id'))
    campaign_creative = db.Column(db.String)
    cta_link = db.Column(db.String)
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.agency_id'))


    #buscando as relações de chave estrangeiras nas tabelas equivalentes
    ad_set = db.relationship('Ad_Set', back_populates='ad', foreign_keys='Ad.ad_set_id')
    
    agency = db.relationship('Agency', back_populates='ad', foreign_keys='Ad.agency_id')

    #método construtor
    def __init__(self, name, ad_set_id, campaign_creative, cta_link, agency_id):
        self.name = name
        self.ad_set_id = ad_set_id
        self.campaign_creative = campaign_creative
        self.cta_link = cta_link
        self.agency_id = agency_id

    #método de representação
    def __repr__(self):
        return "<Ad %r>" % self.name

    