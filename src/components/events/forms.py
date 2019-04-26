from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField, validators, SelectField 

class AddEventForm(FlaskForm):
    description = StringField('Description of Event:', [validators.Length(min=4, max=25)])
    organizer = SelectField('Organizer', coerce=int)
    submit = SubmitField('Add Event')
    location = StringField('Location of Event:', [validators.Length(min=4, max=25)])
    start_date = StringField('Start date of Event:', [validators.Length(min=4, max=25)])
    end_date = StringField('End date of Event:', [validators.Length(min=4, max=25)])




