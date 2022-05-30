from flask import Blueprint, render_template, flash
from flask_login import login_user
from app import lm
from app.models.user import User
from app.models.login import LoginForm

simplepage = Blueprint('simplepage', __name__, static_folder="static", template_folder="templates")


@lm.user_loader
def load_user(user_id):
    return User.query.filter_by(user_id=user_id).first


@simplepage.route('/simplepage')
@simplepage.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user and user.Password == form.data.password:    
            login_user()
            flash("Logged in")
        else:
            flash("Invalid login")
    else:
        print(form.errors)
    return render_template("loginpage.html", form=form)

