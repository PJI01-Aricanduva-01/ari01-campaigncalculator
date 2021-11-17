#importando a classe db do objeto app
from app import db

#criando a classe que representa a tabela campaign_set
class AdObject(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "ad"

    #atributos que se referem ao campos da tabela
    ad_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ad_set_id = db.Column(db.Integer, db.ForeignKey('ad_set.ad_set_id'))
    campaign_creative = db.Column(db.String)
    cta_link = db.Column(db.String)


    #buscando as relações de chave estrangeiras nas tabelas equivalentes
    ad_set = db.relationship('Ad_Set', foreign_keys=ad_set_id)

    #método construtor
    def __init__(self, name, ad_set_id, campaign_creative, cta_link):
        self.name = name
        self.ad_set_id = ad_set_id
        self.campaign_creative = campaign_creative
        self.cta_link = cta_link

    #método de representação
    def __repr__(self):
        return "<Ad %r>" % self.name

    