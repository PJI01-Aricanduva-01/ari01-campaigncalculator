#importando as bibliotecas FLASK
from flask import Flask
from flask_login import LoginManager

#importando as bibliotecas do ORM SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

#criando a instância da aplicação Flask no objeto app
app = Flask(__name__)

#configurando o app Flask a partir de config.py
app.config.from_object('config')

#criando a instância do Banco de Dados SQLAlchemy no objeto db
db = SQLAlchemy(app)

#criando a intância login
lm = LoginManager(app)


#importando os controllers 
from app.controllers import default


