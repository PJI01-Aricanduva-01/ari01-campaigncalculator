from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, DateField
from wtforms.validators import DataRequired

class AdForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    campaign_creative = StringField('campaign_creative', validators=[DataRequired()])
    cta_link = StringField('cta_link', validators=[DataRequired()])
