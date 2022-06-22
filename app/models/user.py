#importando a classe db do objeto app
from app import db, lm
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.credential import *

@lm.user_loader
def get_user(id):
    return User.query.filter_by(user_id=id).first()
#criando a classe que representa a tabela campaign_set
class User(db.Model, UserMixin):
    #atributo que se refere ao nome real da tabela no bando de dados
    __tablename__ = "user"

    #atributos que se referem ao campos da tabela
    user_id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String)
    agency_id = db.Column(db.Integer, db.ForeignKey('agency.agency_id'))
    date_create = db.Column(db.DateTime)
    Password = db.Column(db.String)
    credential_id = db.Column(db.Integer, db.ForeignKey('credential.credential_id'))

    #buscando as relações de chave estrangeiras nas tabelas equivalentes
    agency = db.relationship('Agency', back_populates='user', foreign_keys='User.agency_id')
    
    credential = db.relationship('Credential', back_populates='user', foreign_keys='User.credential_id')


    #método get para utilização da biblioteca Flask-login.login()
    def get_id(self):
        return (self.user_id)

    #método construtor
    def __init__(self, name, agency_id, Password, credential_id):
        self.name = name
        self.agency_id = agency_id
        self.date_create = datetime.now()
        self.Password = generate_password_hash(Password)
        self.credential_id = credential_id

    
    def verify_password(self, pwd):
        return check_password_hash(self.Password, pwd)

    #método de representação
    def __repr__(self):
        return "<User %r>" % self.name

    