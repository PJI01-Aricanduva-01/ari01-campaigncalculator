#importando as bibliotecas FLASK
from flask import Flask, render_template, request

#importando biblioteca para captura de log
from datetime import datetime

from app import app

@app.route('/index')
@app.route('/')

def index():
    return render_template('index.html')


@app.route('/campaignset/<campset_id>')
def campset(campset_id):
    campaign = ['alcance', 'tráfego']
    return render_template('campaignset.html', campset_id=campset_id, campaign=campaign) 