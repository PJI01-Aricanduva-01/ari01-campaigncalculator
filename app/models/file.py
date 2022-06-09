#importando a classe db do objeto app
from app import db

from datetime import datetime

#criando a classe que representa a tabela campaign_set
class File(db.Model):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "file"

    #atributos que se referem ao campos da tabela
    file_id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String)
    file_url = db.Column(db.String)
    file_extention = db.Column(db.String)
    deleted = db.Column(db.Boolean)
    ad_id = db.Column(db.Integer, db.ForeignKey('ad.ad_id'))
    date_created = db.Column(db.DateTime)


    #buscando as relações de chave estrangeiras nas tabelas equivalentes
    ad = db.relationship('Ad', back_populates='file', foreign_keys='File.ad_id')

    #método construtor
    def __init__(self, file_name, file_url, file_extention, ad_id):
        self.file_name = file_name
        self.file_url = file_url
        self.file_extention = file_extention
        self.deleted = 0
        self.date_created = datetime.now()
        self.ad_id = ad_id
        

    #método de representação
    def __repr__(self):
        return "<File %r>" % self.name

    