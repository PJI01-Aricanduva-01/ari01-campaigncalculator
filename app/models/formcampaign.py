from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField
from wtforms.validators import DataRequired


class CampaignForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    # campaignobjective = IntegerField('objective', validators=[DataRequired()])
    campaignobjective = SelectField('campaign_objective_id', coerce=int, validators=[DataRequired()])