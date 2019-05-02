from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateTimeField, validators, SelectField ,PasswordField

class AddEventForm(FlaskForm):
    description = StringField('Description of Event:', [validators.Length(min=4, max=25)])
    organizer = SelectField('Organizer', coerce=int)
    submit = SubmitField('Add Event')
    location = StringField('Location of Event:', [validators.Length(min=4, max=25)])
    start_date = StringField('Start date of Event:', [validators.Length(min=4, max=25)])
    end_date = StringField('End date of Event:', [validators.Length(min=4, max=25)])

class SignUpForm(FlaskForm):
    username=StringField('Username: ',[validators.DataRequired(),validators.Length(min=6,max=16)])
    email=StringField("Email: ",[validators.DataRequired()])
    # phonenumber=StringField("Phone Number: ")
    password_hash=StringField("Password: ",[validators.DataRequired()])
    # starttime=DateField("Time", format='%Y-%m-%d')
    submit=SubmitField('Create' )

class LoginForm(FlaskForm):
    email=StringField("Email: ",[validators.DataRequired()])
    password_hash=PasswordField("Password: ",[validators.DataRequired()])
    # starttime=DateField("Time", format='%Y-%m-%d')
    submit=SubmitField('Login' )


