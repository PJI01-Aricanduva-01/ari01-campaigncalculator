#importando as bibliotecas FLASK
from flask import Flask, render_template, request

from app.models.campaignset import Campaign_Set
from app.models.campaign import Campaign
from app.models.campaignobjective import Campaign_Objective

#importando biblioteca para captura de log
from datetime import datetime

from app import app, db


@app.route('/index')
@app.route('/')
def index():
    campaignsets = Campaign_Set.query.order_by(Campaign_Set.campaign_set_id).all()
    return render_template('index.html', campsets=campaignsets)


@app.route('/campaignset/<campaignset_id>')
def campaignset(campaignset_id):
    campaignset = Campaign_Set.query.filter_by(campaign_set_id=campaignset_id)
    campaigns = Campaign.query.filter_by(campaign_set_id=campaignset_id).all()
    return render_template('campaignset.html', campaignsets=campaignset, campaigns=campaigns)