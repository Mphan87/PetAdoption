from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()],)
    species = StringField("Species")
    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)
    age =  IntegerField("Age",validators=[Optional(), NumberRange(min=0, max=30)],)
    notes = StringField("Notes",validators=[Optional(), Length(min=10)],)

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()],)
    notes = StringField("Notes",validators=[Optional(), Length(min=10)],)
    available = BooleanField("Still Available?") 
