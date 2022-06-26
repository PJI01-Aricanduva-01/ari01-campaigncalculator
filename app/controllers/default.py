#importando as bibliotecas FLASK
from flask import render_template, redirect, url_for, session, flash

#importando as dependencias da própria aplicação
from app import app, db


#importando os models
from app.models.agency import Agency
from app.models.formcampaignset import CampaignSetForm
from app.models.campaignset import Campaign_Set
from app.models.campaign import Campaign
from app.models.formcampaign import CampaignForm
from app.models.campaignobjective import Campaign_Objective
from app.models.adset import Ad_Set
from app.models.formadset import AdsetForm
from app.models.ad import Ad
from app.models.formad import AdForm
from app.models.fuction import permitir


from app.controllers.simplepage import simplepage


app.register_blueprint(simplepage)


#criação da rota para index
@app.route('/index') #rota para index
@app.route('/') #mesma rota para /
def index():
    if "user" in session: #verificar se o usuario está logado na aplicação
        per = permitir(session["user"][2])
        if per == 0:
            #agency = Agency.query.filter_by(agency_id=1).first()
            fil = session["user"][1]
            campaignsets = Campaign_Set.query.filter_by(agency_id=fil).all() #faz um filtro de acordo com a agencia da pessoa.
            #campaignsets = Campaign_Set.query.all() #consulta no banco de dados para trazer as CampSets
            return render_template('index.html', campsets=campaignsets) #chamada do template index
        else:
            flash("Você não tem permissão do Responsável da agencia para acessa as campanhas. \n Entre em contato com Responsável")
            return redirect(url_for("simplepage.logout"))
    else:
        return redirect(url_for("simplepage.login"))


@app.route('/sobre')
@app.route('/about')
def about():
    return render_template('about.html') 


#criação da rota para detalhe de campaingset
@app.route('/campaignset/<campaignset_id>') #rota para campaignset passando o id clicado como parametro
def campaignset(campaignset_id):
    if "user" in session:
        campaignset = Campaign_Set.query.filter_by(campaign_set_id=campaignset_id).first() #consulta campaignset no banco de dados usando o id passado como filtro
        campaigns = Campaign.query.filter_by(campaign_set_id=campaignset_id).all() #consulta as campanhas no banco de dados usando o id do campset clicado como filtro
        # campobj = Campaign_Objective.query.filter_by(campaign_objective_id=camp) - Fazer Link com objetivos
        if campaignset.agency_id == session["user"][1]: #verifica se o usuario pode acessa essa campanha.    
            return render_template('campaignset.html', campaignset=campaignset, campaigns=campaigns) #chamada para o template campaignset
        else:
            flash("Acesso negado")
            return redirect(url_for('index'))
    else:
        return redirect(url_for('simplepage.login'))


#rota para tela de criação de campaignset
@app.route('/campaignsetcreate', methods=['GET', 'POST']) #rota para o campaignset com permissão de métodos GET e POST para o retorno do formulário
def campaignsetcreate():
    if "user" in session:
        form = CampaignSetForm() #criação do objeto formulário

        if form.validate_on_submit(): #verificação dos dados pelo usuário. No evento de clique Submit, o wtforms recupera os dados e faz a verificação atravez desse métoro
            name = form.name.data
            agency = session["user"][1] #recuperação do campo name do formulário e atribuição à variável
            campset = Campaign_Set(name, agency) #criação de uma instancia do model Campaign_Set com passagem do name como parametro
            db.session.add(campset) #sqlalchemy criação de session com o objeto campset como parametro
            db.session.commit() #sqlachemy commit da session. sqlalchemy escreve no banco os dados do model
            return redirect(url_for('index'))

        else:
            return render_template('campaignsetcreate.html', form=form) #no caso de metodo GET (usuário acessou a página de criação), chamada do template campaignsetcreate
    else:
        return redirect(url_for('simplepage.login'))

@app.route('/campaignsetremove/<campset_id>', methods=['GET', 'POST'])
def campaignsetremove(campset_id):
    if "user" in session:
        campset = Campaign_Set.query.filter_by(campaign_set_id=campset_id).first()
        if campset.agency_id == session["user"][1]:        
            db.session.delete(campset)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            flash("Acesso negado")
            return redirect(url_for('index'))

    else:
        return redirect(url_for('simplepage.login'))


#rota para a tela detalhes de campanha
@app.route('/campaign/<campaign_id>') #rota para tela de campanha
def campaign(campaign_id):
    if "user" in session:
        campaign = Campaign.query.filter_by(campaign_id=campaign_id).first() #consulta dos detalhes de campanha
        campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first()
        adsets = Ad_Set.query.filter_by(campaign_id=campaign_id) #consulta dos conjuntos de anuncio
        if campaign.agency_id == session["user"][1]:
            return render_template('campaign.html', campaign=campaign, campset=campaign_set, adset=adsets) #chamada do template campaign
        
        else:
            flash("Acesso negado")
            return redirect(url_for("index"))    
    else:
        return redirect(url_for("simplepage.login"))

@app.route('/campaigncreate/<campaignset_id>', methods=['GET', 'POST'])
def campaigncreate(campaignset_id):
    if "user" in session:
        form = CampaignForm()
        form.campaignobjective.choices = [(g.campaign_objective_id, g.name) for g in Campaign_Objective.query.all()]


        if form.validate_on_submit():
            name = form.name.data
            objective = form.campaignobjective.data
            agency = session["user"][1]
            camp = Campaign(name, campaignset_id, objective, agency)
            db.session.add(camp)
            db.session.commit()
            return redirect(url_for('campaignset', campaignset_id=campaignset_id))
            
        else:
            campaignset = Campaign_Set.query.filter_by(campaign_set_id=campaignset_id).first()
            campaignobj = Campaign_Objective.query.all()
            return render_template('campaigncreate.html', form=form, campset=campaignset, campobj=campaignobj)
    else:
        return redirect(url_for("simplepage.login"))


@app.route('/campaignremove/<campaignId>', methods=['GET', 'POST'])
def campaignremove(campaignId):
    if "user" in session:
        campaign = Campaign.query.filter_by(campaign_id=campaignId).first()
        campSetId = campaign.campaign_set_id

        if campaign.agency_id == session["user"][1]: 
            db.session.delete(campaign)
            db.session.commit()
            return redirect(url_for('campaignset', campaignset_id=campSetId))
        else:
            flash("Acesso negado")
            return redirect(url_for("index"))

    else:
        return redirect(url_for('simplepage.login'))



@app.route('/adset/<adset_id>')
def adset(adset_id):
    if "user" in session:
        adset = Ad_Set.query.filter_by(ad_set_id=adset_id).first()
        campaign = Campaign.query.filter_by(campaign_id=adset.campaign_id).first() #consulta dos detalhes de campanha
        campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first()
        ad = Ad.query.filter_by(ad_set_id=adset_id)
        if adset.agency_id == session["user"][1]:
            return render_template('adset.html', adset=adset, ad=ad, campaign=campaign, campset=campaign_set)

        else:
            flash('Acesso negado')
            return redirect(url_for('index'))
    else:
        return redirect(url_for("simplepage.login"))


@app.route('/adsetcreate/<campaign_id>', methods=['GET', 'POST'])
def adsetcreate(campaign_id):
    if "user" in session:
        form = AdsetForm()

        if form.validate_on_submit():
            name = form.name.data
            date_start = form.date_start.data
            date_end = form.date_end.data
            public = form.public.data
            budget = form.budget.data
            agency = session["user"][1]
            adset = Ad_Set(name, campaign_id, date_start, date_end, public, budget, agency)
            db.session.add(adset)
            db.session.commit()
            return redirect(url_for('campaign', campaign_id=campaign_id))

        else:
            campaign = Campaign.query.filter_by(campaign_id=campaign_id).first() #consulta dos detalhes de campanha
            campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first()
            adset = Ad_Set.query.filter_by(campaign_id=campaign_id).all() #consulta dos conjuntos de anuncio
            return render_template('adsetcreate.html', form=form, campaign=campaign, campset=campaign_set, adset=adset)
    else:
        return redirect(url_for("simplepage.login"))


@app.route('/adsetremove/<adset_id>', methods=['GET', 'POST'])
def adsetremove(adset_id):
    if "user" in session:
        adset = Ad_Set.query.filter_by(ad_set_id=adset_id).first()
        campaign_id = adset.campaign_id
        if adset.agency_id == session["user"][1]:
            db.session.delete(adset)
            db.session.commit()
            return redirect(url_for('campaign', campaign_id=campaign_id))
        else:
            flash("Acesso negado")
            return redirect(url_for("index"))

    else:
        return redirect(url_for('simplepage.login'))


@app.route('/ad/<ad_id>', methods=['GET', 'POST'])
def ad(ad_id):
    if "user" in session:
        ad = Ad.query.filter_by(ad_id=ad_id)
        adset = Ad_Set.query.filter_by(ad_set_id=ad.ad_set_id).first()
        campaign = Campaign.query.filter_by(campaign_id=adset.campaign_id).first()
        campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first() #consulta dos detalhes de campanha
        ad = Ad.query.filter_by(ad_set_id=adset.adset_id)
        if ad.agency_id == session["user"][1]:
            return render_template('adcreate.html', campaign=campaign, campset=campaign_set, adset=adset, ad=ad)
        else:
            flash("Acesso negado")
            return redirect(url_for('index'))

    else:
        return redirect(url_for('simplepage.login'))


@app.route('/adcreate/<adset_id>', methods=['GET', 'POST'])
def adcreate(adset_id):
    if "user" in session:
        form = AdForm()

        if form.validate_on_submit():
            name = form.name.data
            campaign_creative = form.campaign_creative.data
            cta_link = form.cta_link.data
            agency = session["user"][1]
            ad = Ad(name, adset_id, campaign_creative, cta_link, agency)
            db.session.add(ad)
            db.session.commit()
            return redirect(url_for('adset', adset_id=adset_id))

        else:
            adset = Ad_Set.query.filter_by(ad_set_id=adset_id).first()
            campaign = Campaign.query.filter_by(campaign_id=adset.campaign_id).first()
            campaign_set = Campaign_Set.query.filter_by(campaign_set_id=campaign.campaign_set_id).first() #consulta dos detalhes de campanha
            ad = Ad.query.filter_by(ad_set_id=adset_id)
            return render_template('adcreate.html', form=form, campaign=campaign, campset=campaign_set, adset=adset, ad=ad)
    
    else:
        return redirect(url_for('simplepage.login'))


@app.route('/adremove/<ad_id>', methods=['GET', 'POST'])
def adremove(ad_id):
    if "session" in session:
        ad = Ad.query.filter_by(ad_id=ad_id).first()
        adset_id = ad.ad_set_id
        if ad.agency_id == session["user"][1]:
            db.session.delete(ad)
            db.session.commit()
            return redirect(url_for('adset', adset_id=adset_id))
        else:
            flash("Acesso negado")
            return redirect(url_for('index'))
    
    else:
        return redirect(url_for('simplepage.login'))


@app.route('/campsetreport/<campset_id>')
def campsetreport(campset_id):
    if "user" in session:
        campset = Campaign_Set.query.filter_by(campaign_set_id=campset_id).first()

        campaign = db.session.query(Campaign, Ad_Set, Ad).\
            filter(Campaign.campaign_set_id==campset_id).\
            outerjoin(Campaign_Set.campaign).\
            outerjoin(Campaign.ad_set).\
            outerjoin(Ad_Set.ad).\
            order_by(Campaign.campaign_id)
        
        if campset.agency_id == session["user"][1]:
            return render_template('campsetreport.html', campset=campset, campaign=campaign)
        
        else:
            flash("Acesso negado")
            return redirect(url_for('index'))
    
    else:
        return redirect(url_for('simplepage.login'))    

