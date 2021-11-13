#importando as bibliotecas FLASK
from flask import Flask, render_template, request

from app import app, db

from werkzeug.exceptions import abort

from app.models.formcampaignset import CampaignSetForm
from app.models.campaignset import Campaign_Set
from app.models.campaign import Campaign
from app.models.campaignobjective import Campaign_Objective
from app.models.adset import Ad_Set




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


@app.route('/campaignsetcreate', methods=['GET', 'POST'])
def campaignsetcreate():
    form = CampaignSetForm()
    if request.method == 'POST':
        return render_template('campaignsetcreate.html', form=form)
        # if form.validate_on_submit():
        #     name = form.name.data
        #     campset = Campaign_Set(name)
        #     db.session.add(campset)
        #     db.session.commit()
        
        # return render_template('index.html')
    
    if request.method == 'GET':
        return render_template('index.html', form=form)
       
    


@app.route('/campaign/<campaign_id>')
def campaign(campaign_id):
    campaign = Campaign.query.filter_by(Campaign_id=campaign_id).first()
    adsets = Ad_Set.query.filter_by(Campaign_Id=campaign_id).all()
    return render_template('campaign.html', campaign=campaign, adsets=adsets)








    # if request.method == 'POST':
    #     name = request.form['name']
        
    #     if not name:
    #         flash('Por favor, escolha um nome para o CampaignSet')
    #     else:
    #         campaignset = Campaign_Set(name=name)
    #         db.session.add(campaignset)
    #         db.session.commit()
    #         # campaignsetnew = Campaign_Set.query.order_by(campaignset.id).last()
    #         return redirect(url_for('index'))