from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class AgencyForm(FlaskForm):
    newagency = StringField("newagency", validators=[DataRequired()])
    
 