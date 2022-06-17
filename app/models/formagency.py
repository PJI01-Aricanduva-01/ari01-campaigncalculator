from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class AgencyForm(FlaskForm):
    newagency = StringField("newagency", validators=[DataRequired()])
    permitir = BooleanField("permitir")
    negar =  BooleanField("negar")
    
 