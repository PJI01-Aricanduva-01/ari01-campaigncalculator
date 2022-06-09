from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_login import login_user, logout_user
from app.models.user import User
from app.models.login import LoginForm
from app.models.formuser import UserForm
from app.models.agency import *
from app import db

simplepage = Blueprint('simplepage', __name__, static_folder="static", template_folder="templates")


@simplepage.route('/register/', methods=["GET", "POST"])
def register():

    form = UserForm()
    
    if form.validate_on_submit():
        agency = request.form ['agency']
        credential_id = 1
        name = form.username.data
        password = form.password.data
        rpassword = form.rpassword.data
        agency_set_id = Agency.query.filter_by(name=agency).first()
    
        if not agency_set_id:
            flash('Agencia Invalida')
            return redirect(url_for('simplepage.register'))
            
        if password != rpassword:
            flash('Digite a mesma senha') 
            return redirect(url_for('simplepage.register'))
        
        reg = User(name, agency_set_id.agency_id, password, credential_id)
        print(reg)
        db.session.add(reg)
        db.session.commit()
        
        
        return redirect(url_for('simplepage.login'))

    return render_template('register.html', form=form)


@simplepage.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data
        #user = User.query.get(form.name.data)
        user = User.query.filter_by(name=name).first()

        if not user or not user.verify_password(pwd):
            flash("invalid login")
            return render_template('loginpage.html', form=form)

        login_user(user)
        flash("login in")
        return redirect(url_for('loginpage'))
    
    return render_template('loginpage.html', form=form)


@simplepage.route('/logout')
def logout():
    logout_user()
    return render_template('loginpage.html')

