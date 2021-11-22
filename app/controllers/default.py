#importando as bibliotecas FLASK
from flask import render_template, redirect, url_for

#importando as dependencias da própria aplicação
from app import app, db

#importando os models
from app.models.formcampaignset import CampaignSetForm
from app.models.campaignset import Campaign_Set
from app.models.campaign import Campaign
from app.models.formcampaign import CampaignForm
from app.models.campaignobjective import Campaign_Objective
from app.models.adset import Ad_Set
from app.models.formadset import AdsetForm
from app.models.ad import Ad
from app.models.formad import AdForm



#criação da rota para index
@app.route('/index') #rota para index
@app.route('/') #mesma rota para /
def index():
    campaignsets = Campaign_Set.query.all() #consulta no banco de dados para trazer as CampSets
    return render_template('index.html', campsets=campaignsets) #chamada do template index

@app.route('/sobre')
@app.route('/about')
def about():
    return render_template('about.html') 



@app.route('/sobre')
@app.route('/about')
def about():
    return render_template('about.html')



#criação da rota para detalhe de campaingset
@app.route('/campaignset/<campaignset_id>') #rota para campaignset passando o id clicado como parametro
def campaignset(campaignset_id):
    campaignset = Campaign_Set.query.filter_by(campaign_set_id=campaignset_id).first() #consulta campaignset no banco de dados usando o id passado como filtro
    campaigns = Campaign.query.filter_by(campaign_set_id=campaignset_id).all() #consulta as campanhas no banco de dados usando o id do campset clicado como filtro
    # campobj = Campaign_Objective.query.filter_by(campaign_objective_id=camp) - Fazer Link com objetivos
    return render_template('campaignset.html', campaignset=campaignset, campaigns=campaigns) #chamada para o template campaignset


#rota para tela de criação de campaignset
@app.route('/campaignsetcreate', methods=['GET', 'POST']) #rota para o campaignset com permissão de métodos GET e POST para o retorno do formulário
def campaignsetcreate():
    form = CampaignSetForm() #criação do objeto formulário

    if form.validate_on_submit(): #verificação dos dados pelo usuário. No evento de clique Submit, o wtforms recupera os dados e faz a verificação atravez desse métoro
        name = form.name.data #recuperação do campo name do formulário e atribuição à variável
        campset = Campaign_Set(name) #criação de uma instancia do model Campaign_Set com passagem do name como parametro
        db.session.add(campset) #sqlalchemy criação de session com o objeto campset como parametro
        db.session.commit() #sqlachemy commit da session. sqlalchemy escreve no banco os dados do model
        return redirect(url_for('/'))

    else:
        return render_template('campaignsetcreate.html', form=form) #no caso de metodo GET (usuário acessou a página de criação), chamada do template campaignsetcreate
               

#rota para a tela detalhes de campanha
@app.route('/campaign/<campaign_id>') #rota para tela de campanha
def campaign(campaign_id):
    campaign = Campaign.query.filter_by(campaign_id=campaign_id).first() #consulta dos detalhes de campanha
    campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first()
    campaign_objective = Campaign_Objective.query.filter_by(campaign_objective_id=campaign.campaign_objective_id).first()
    adsets = Ad_Set.query.filter_by(campaign_id=campaign_id) #consulta dos conjuntos de anuncio
    return render_template('campaign.html', campaign=campaign, campset=campaign_set, campobj=campaign_objective, adsets=adsets) #chamada do template campaign


@app.route('/campaigncreate/<campaignset_id>', methods=['GET', 'POST'])
def campaigncreate(campaignset_id):
    form = CampaignForm()
    form.campaignobjective.choices = [(g.campaign_objective_id, g.name) for g in Campaign_Objective.query.all()]


    if form.validate_on_submit():
        name = form.name.data
        objective = form.campaignobjective.data
        camp = Campaign(name, campaignset_id, objective)
        db.session.add(camp)
        db.session.commit()
        return redirect(url_for('campaignset', campaignset_id=campaignset_id))
        
    else:
        campaignset = Campaign_Set.query.filter_by(campaign_set_id=campaignset_id).first()
        campaignobj = Campaign_Objective.query.all()
        return render_template('campaigncreate.html', form=form, campset=campaignset, campobj=campaignobj)


@app.route('/adset/<adset_id>')
def adset(adset_id):
    adset = Ad_Set.query.filter_by(ad_set_id=adset_id).first()
    campaign = Campaign.query.filter_by(campaign_id=adset.campaign_id).first() #consulta dos detalhes de campanha
    campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first()
    ad = Ad.query.filter_by(ad_set_id=adset_id)
    return render_template('adset.html', adset=adset, ad=ad, campaign=campaign, campset=campaign_set)


@app.route('/adsetcreate/<campaign_id>', methods=['GET', 'POST'])
def adsetcreate(campaign_id):
    form = AdsetForm()

    if form.validate_on_submit():
        name = form.name.data
        date_start = form.date_start.data
        date_end = form.date_end.data
        public = form.public.data
        budget = form.budget.data
        adset = Ad_Set(name, campaign_id, date_start, date_end, public, budget)
        db.session.add(adset)
        db.session.commit()
        return redirect(url_for('campaign', campaign_id=campaign_id))

    else:
        campaign = Campaign.query.filter_by(campaign_id=campaign_id).first() #consulta dos detalhes de campanha
        campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first()
        adset = Ad_Set.query.filter_by(campaign_id=campaign_id).all() #consulta dos conjuntos de anuncio
        return render_template('adsetcreate.html', form=form, campaign=campaign, campset=campaign_set, adset=adset)


@app.route('/ad/<ad_id>', methods=['GET', 'POST'])
def ad(ad_id):

    ad = Ad.query.filter_by(ad_id=ad_id)
    adset = Ad_Set.query.filter_by(ad_set_id=ad.ad_set_id).first()
    campaign = Campaign.query.filter_by(campaign_id=adset.campaign_id).first()
    campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first() #consulta dos detalhes de campanha
    ad = Ad.query.filter_by(ad_set_id=adset.adset_id)
    return render_template('adcreate.html', form=form, campaign=campaign, campset=campaign_set, adset=adset, ad=ad)


@app.route('/adcreate/<adset_id>', methods=['GET', 'POST'])
def adcreate(adset_id):
    form = AdForm()

    if form.validate_on_submit():
        name = form.name.data
        campaign_creative = form.campaign_creative.data
        cta_link = form.cta_link.data
        ad = Ad(name, adset_id, campaign_creative, cta_link)
        db.session.add(ad)
        db.session.commit()
        return redirect(url_for('adset', adset_id=adset_id))

    else:
        adset = Ad_Set.query.filter_by(ad_set_id=adset_id).first()
        campaign = Campaign.query.filter_by(campaign_id=adset.campaign_id).first()
        campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first() #consulta dos detalhes de campanha
        ad = Ad.query.filter_by(ad_set_id=adset_id)
        return render_template('adcreate.html', form=form, campaign=campaign, campset=campaign_set, adset=adset, ad=ad)