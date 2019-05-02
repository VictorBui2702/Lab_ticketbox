from flask import Blueprint, render_template
from flask import Flask, render_template, flash, redirect, url_for,request

from flask_login import UserMixin, LoginManager,login_user,logout_user, current_user, login_required
from flask import request
from flask import session

from werkzeug.security import generate_password_hash, check_password_hash

events_blueprint = Blueprint('event',
    __name__,
    template_folder='../../templates/events')


from src.components.events.forms import AddEventForm, SignUpForm, LoginForm
from src.models.user import User 
from src.models.event import Event
from src import db


@events_blueprint.route('/add', methods=['POST', 'GET'])
def add():
    form = AddEventForm()
    form.organizer.choices = [(u.id, u.username) for u in User.query.all() ]
    if form.validate_on_submit():
        e = Event(description=form.description.data, organizer_id=form.organizer.data)
        db.session.add(e)
        db.session.commit()
    return render_template("add_event.html", form=form)


@events_blueprint.route('/signup',methods=['POST','GET'])
def signup():
    form=SignUpForm()
    if request.method == 'POST':
        u=User(email=form.email.data,password_hash=generate_password_hash(form.password_hash.data))
        print("username")
        db.session.add(u)
        db.session.commit()
        flash("Your account has been successfully created")
        print('*******', u.id)
        return redirect('/')
    return render_template('signup.html',form=form)  



@events_blueprint.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if request.method == 'POST':
        email=form.email.data
        password=form.password_hash.data
        user=User.query.filter_by(email=email).first()
        if user is not None and check_password_hash(user.password_hash,password):
            login_user(user)
            session['username'] = user.username
            
 #user here being the user object you have queried
            print(user.username)
    return render_template('home.html', form=form)


# @events_blueprint.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     del session['username']
#     return redirect('/')



        

