
from flask import Blueprint, redirect, url_for, render_template, request, flash, session
from flask_login import login_user, logout_user
from app.models.formagency import AgencyForm
from app.models.user import User
from app.models.login import LoginForm
from app.models.formuser import UserForm
from app.models.agency import *
from app.models.formagency import AgencyForm
from app.models.credential import Credential
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
        

            if not user and user.Password != pwd:
                flash("invalid login")
                return render_template('loginpage.html', form=form)

            login_user(user)
            session["user"] = name, user.agency_id, user.credential_id
            return redirect(url_for('index'))
    
        return render_template('loginpage.html', form=form)


@simplepage.route('/useragency', methods=["GET", "POST"])
def useragency():

    if "user" in session:
        form = AgencyForm()
        form.user_id.choices = [(g.credential_id, g.name) for g in User.query.filter_by(agency_id=session["user"][1]).all()]

        user_choice = form.user_id.data
        permissao = form.permissao.data
        if user_choice and permissao == "permitir":
            credential = Credential.query.filter_by(credential_id=user_choice).first()
            if credential.name  == "Responsavel" or credential.name == "User":
                flash('Não tem permissão para essa ação')
                return redirect(url_for('index'))    
            credential.name = "User"
            db.session.commit()
            credential.habilitie_01 = True
        
            db.session.commit()
            return redirect(url_for("index"))
        
        if user_choice and permissao == "negar":
            credential = Credential.query.filter_by(credential_id=user_choice).first()
            if credential.name  == "Responsavel" or credential.name == "User":
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

