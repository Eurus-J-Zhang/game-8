from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import TextArea

# Here is for Prolific ID and gender and age
class DemographicInfo(FlaskForm):
    id = StringField('Prolific ID', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('M','Male'),('F','Female'),('O','Others')], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=80)])

eleven_point_scale = [(str(i), f'Opt{i}') for i in range(11)]

# Here is the first emotion check
class EmotionForm(FlaskForm):
    emo_choice = RadioField('Emotion choice', choices=[('joy', 'Joy'), ('despair', 'Despair'), ('rage', 'Rage')], validators=[DataRequired()])
    feedback = StringField('',validators=[DataRequired()],widget=TextArea())