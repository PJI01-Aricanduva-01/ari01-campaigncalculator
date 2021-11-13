from flask_wtf import FlaskForm
from wtforms import Form, StringField
from wtforms.validators import DataRequired

class CampaignSetForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])



