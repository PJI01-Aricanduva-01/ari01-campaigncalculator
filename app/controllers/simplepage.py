
from flask import Blueprint, redirect, url_for, render_template, request, flash, session, jsonify
from flask_login import login_user, logout_user
from app.models.user import *
from app.models.login import LoginForm
from app.models.formuser import UserForm
from app.models.agency import *
from app.models.formagency import *
from app.models.credential import Credential
from app.models.campaignset import Campaign_Set
from app.models.campaign import Campaign
from app.models.adset import Ad_Set
from app import db

simplepage = Blueprint('simplepage', __name__, static_folder="static", template_folder="templates")



@simplepage.route('/register/', methods=["GET", "POST"])
def register():

    form = UserForm()
    form.agency.choices = [(g.agency_id, g.name) for g in Agency.query.all()]
      
    if form.validate_on_submit():
        objective = form.agency.data
        name = form.username.data
        password = form.password.data
        rpassword = form.rpassword.data
        agency_set_id = Agency.query.filter_by(agency_id=objective).first()
        newuser = User.query.filter_by(agency_id=agency_set_id.agency_id).first()

        if not newuser:
            credential = Credential("Responsavel", 1)
            print(credential)
            db.session.add(credential)
            db.session.commit()

        else:
             credential = Credential("convidado", 0)
             db.session.add(credential)
             db.session.commit()
             print(credential)

        if password != rpassword:
            flash('Digite a mesma senha') 
            return redirect(url_for('simplepage.register'))

        #credential_id = Credential.query.filter_by(credential_id=credential).first()
        reg = User(name, agency_set_id.agency_id, password, credential.credential_id)
        db.session.add(reg)
        db.session.commit()
            
        
        return redirect(url_for('simplepage.login'))

    return render_template('register.html', form=form)


@simplepage.route('/addagency', methods=["GET", "POST"])
def addagency():

    form = AgencyForm()

    if form.validate_on_submit():
        objective1 = form.newagency.data
        addagency = Agency(objective1)
        db.session.add(addagency)
        db.session.commit()
        return redirect(url_for('simplepage.register'))
    
    return render_template('newagency.html', form=form)


@simplepage.route('/login', methods=["GET", "POST"])
def login():
    if "user" in session:
        return redirect(url_for('index'))    
    
    else:
        form = LoginForm()

        if form.validate_on_submit():
            name = form.username.data
            pwd = form.password.data
            #user = User.query.get(form.name.data)
            user = User.query.filter_by(name=name).first()
            #agencyid = User.query.filter_by(agency_id=agency_id).first
        

            if not user or not user.verify_password(pwd):
                flash("invalid login")
                return render_template('loginpage.html', form=form)

            login_user(user)
            session["user"] = name, user.agency_id, user.credential_id
            return redirect(url_for('index'))
    
        return render_template('loginpage.html', form=form)


@simplepage.route('/useragency', methods=["GET", "POST"])
def useragency():

    if "user" in session:
        form = AgencyFormChoices()
        form.user_id.choices = [(g.credential_id, g.name) for g in User.query.filter_by(agency_id=session["user"][1]).all()]

        user_choice = form.user_id.data
        permissao = form.permissao.data
        if user_choice and permissao == "permitir":
            credential = Credential.query.filter_by(credential_id=user_choice).first()
            if credential.name  == "Responsavel":
                flash('Não tem permissão para essa ação')
                return redirect(url_for('index'))    
            credential.name = "User"
            db.session.commit()
            credential.habilitie_01 = True
        
            db.session.commit()
            return redirect(url_for("index"))
        
        if user_choice and permissao == "negar":
            credential = Credential.query.filter_by(credential_id=user_choice).first()
            if credential.name  == "Responsavel":
                flash('Não tem permissão para essa ação')
                return redirect(url_for('index'))
            credential.name = "Convidado"
            db.session.commit()
            credential.habilitie_01 = False
            db.session.commit()
            return redirect(url_for("index"))

        return render_template('useragency.html', form=form)
    else:
        return redirect(url_for("simplepage.login"))


@simplepage.route('/logout')
def logout():
    session.pop("user", None)
    logout_user()
    return redirect(url_for('simplepage.login'))


@simplepage.route('/apiexterna')
def apiexterna():
    agency_check = session['user'][1]
    print(agency_check)
    camp_set_info = Campaign_Set.query.filter_by(agency_id=agency_check).all()
    camp_info = Campaign.query.filter_by(agency_id=agency_check).all()
    ad_info = Ad_Set.query.filter_by(agency_id=agency_check).all()
    
    x = 0
    camp_set_name = []
    camp_name = []
    adname_j = []
    adpublic = []
    adbudget = []
    date_start = []
    date_end = []
    apiex = {}
    total = 0
    
    while(True): #Criação do objeto Json. 
        camp_name.append(camp_info[x].name)
        camp_set_name.append(camp_set_info[x].name)
        adname_j.append(ad_info[x].name)
        date_start.append(ad_info[x].date_start)
        date_end.append(ad_info[x].date_end)
        adpublic.append(ad_info[x].public)
        adbudget.append(ad_info[x].total_budget)
        total = total + adbudget[x]
        x = x + 1
        if x == len(camp_set_info):
            apiex['1 - Campanha'] = camp_name
            apiex['2 - Campanha Name'] = camp_set_name
            apiex['3 - Ad name'] = adname_j
            apiex['4 - Publico Alvo'] = adpublic
            apiex['5 - Data de Inicio'] = date_start
            apiex['6 - Data de Termino'] = date_end
            apiex['7 - Budget por campanha'] = adbudget
            apiex['8 - Total'] = total
            break

    '''api = camp_set_info[0].name'''
    return jsonify(apiex) #Transformando o dicionario em Json.