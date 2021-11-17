from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, DateField
from wtforms.validators import DataRequired

class AdsetForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    date_start = DateField('date_start', validators=[DataRequired()])
    date_end = DateField('date_end', validators=[DataRequired()])
    public = StringField('public', validators=[DataRequired()])
    budget = StringField('budget', validators=[DataRequired()])
