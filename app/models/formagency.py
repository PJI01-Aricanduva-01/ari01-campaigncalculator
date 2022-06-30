from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField
from wtforms.validators import DataRequired, InputRequired


class AgencyForm(FlaskForm):
    newagency = StringField("newagency", validators=[DataRequired()])
 

class AgencyFormChoices(FlaskForm):
    user_id = SelectField('user_id', coerce=int, validators=[DataRequired()])
    permissao = RadioField("permissao", choices=[('permitir', 'Permitir'), ('negar', 'Negar')], default="negar", coerce=str)