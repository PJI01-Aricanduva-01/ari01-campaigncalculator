#importando as bibliotecas FLASK
from flask import Flask

#importando as bibliotecas do ORM SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

#criando a instância da aplicação Flask no objeto app
app = Flask(__name__)

#configurando o app Flask a partir de config.py
app.config.from_object('config')

#criando a instância do Banco de Dados SQLAlchemy no objeto db
db = SQLAlchemy(app)

#importando os controllers 
from app.controllers import default

#registrando a BluePrint dragndropupload
from app.controllers.dragndropupload import dragndropupload
app.register_blueprint(dragndropupload, url_prefix="/upload")


