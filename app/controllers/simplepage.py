from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_login import login_user, logout_user
from app.models.user import User
from app.models.login import LoginForm

simplepage = Blueprint('simplepage', __name__, static_folder="static", template_folder="templates")



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
