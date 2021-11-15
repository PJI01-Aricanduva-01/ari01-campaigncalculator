#importando as bibliotecas FLASK
from flask import Flask, render_template, request
from wtforms.validators import DataRequired 

#importando as dependencias da própria aplicação
from app import app, db

#importando dependencias de tratamento de erros
from werkzeug.exceptions import abort

#importando os models
from app.models.formcampaignset import CampaignSetForm
from app.models.formcampaign import CampaignForm
from app.models.campaignset import Campaign_Set
from app.models.campaign import Campaign
from app.models.campaignobjective import Campaign_Objective
from app.models.adset import Ad_Set



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



#criação da rota para detalhe de campaingset
@app.route('/campaignset/<campaignset_id>') #rota para campaignset passando o id clicado como parametro
def campaignset(campaignset_id):
    campaignset = Campaign_Set.query.filter_by(campaign_set_id=campaignset_id).first() #consulta campaignset no banco de dados usando o id passado como filtro
    campaigns = Campaign.query.filter_by(campaign_set_id=campaignset_id).all() #consulta as campanhas no banco de dados usando o id do campset clicado como filtro
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
        campaignsets = Campaign_Set.query.all() #consulta dos campsets no banco para montagem do template index
        return render_template('index.html', campsets=campaignsets) #chamada do template index

    else:
        return render_template('campaignsetcreate.html', form=form) #no caso de metodo GET (usuário acessou a página de criação), chamada do template campaignsetcreate
       

@app.route('/campaigncreate/<campaignset_id>', methods=['GET', 'POST'])
def campaigncreate(campaignset_id):
    form = CampaignForm()

    if form.validate_on_submit():
        name = form.name.data
        objective = form.campaignobjective.data
        camp = Campaign(name, campaignset_id,objective)
        db.session.add(camp)
        db.session.commit()
        campaignset = Campaign_Set.query.filter_by(campaign_set_id=campaignset_id).first() #consulta campaignset no banco de dados usando o id passado como filtro
        campaigns = Campaign.query.filter_by(campaign_set_id=campaignset_id).all() #consulta as campanhas no banco de dados usando o id do campset clicado como filtro
        return render_template('campaignset.html', campaignset=campaignset, campaigns=campaigns) #chamada para o template campaignset

    else:
        campaignset = Campaign_Set.query.filter_by(campaign_set_id=campaignset_id).first()
        return render_template('campaigncreate.html', form=form, campset=campaignset)

        

#rota para a tela detalhes de campanha
@app.route('/campaign/<campaign_id>') #rota para tela de campanha
def campaign(campaign_id):
    campaign = Campaign.query.filter_by(Campaign_id=campaign_id).first() #consulta dos detalhes de campanha
    adsets = Ad_Set.query.filter_by(Campaign_Id=campaign_id).all() #consulta dos conjuntos de anuncio
    return render_template('campaign.html', campaign=campaign, adsets=adsets) #chamada do template campaign








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