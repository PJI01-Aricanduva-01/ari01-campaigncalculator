from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    rpassword = PasswordField("rpassword", validators=[DataRequired()])
    agency = SelectField('agency_id', coerce=int, validators=[DataRequired()])

 
