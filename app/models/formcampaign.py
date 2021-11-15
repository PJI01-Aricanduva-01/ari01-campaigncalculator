from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired

class CampaignForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    campaignobjective = IntegerField('objective', validators=[DataRequired()])