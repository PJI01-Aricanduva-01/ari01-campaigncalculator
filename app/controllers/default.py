#importando as bibliotecas FLASK
from flask import Flask, render_template, request, url_for, flash, redirect
import os, datetime

from werkzeug.exceptions import abort

from app.models.campaignset import Campaign_Set
from app.models.campaign import Campaign
from app.models.campaignobjective import Campaign_Objective
from app.models.adset import Ad_Set

#importando biblioteca para captura de log
from datetime import datetime

from app import app, db


@app.route('/index')
@app.route('/')
def index():
    campaignsets = Campaign_Set.query.all()
    return render_template('index.html', campsets=campaignsets)


@app.route('/campaignset/<campaignset_id>')
def campaignset(campaignset_id):
    campaignset = Campaign_Set.query.filter_by(campaign_set_id=campaignset_id).first()
    campaigns = Campaign.query.filter_by(campaign_set_id=campaignset_id).all()
    return render_template('campaignset.html', campaignset=campaignset, campaigns=campaigns)

@app.route('/campaignset/createcampaignset', methods=('GET', 'POST'))
def campaignsetcreate():
    return render_template('campaignsetcreate.html')

@app.route('/campaign/<campaign_id>')
def campaign(campaign_id):
    campaign = Campaign.query.filter_by(Campaign_id=campaign_id).first()
    adsets = Ad_Set.query.filter_by(Campaign_Id=campaign_id).all()
    return render_template('campaign.html', campaign=campaign, adsets=adsets)