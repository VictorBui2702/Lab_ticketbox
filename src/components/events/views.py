from flask import Blueprint, render_template

events_blueprint = Blueprint('event',
    __name__,
    template_folder='../../templates/events')


from src.components.events.forms import AddEventForm
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

@events_blueprint.route('/list')
def list():
    return "Here are all the events"