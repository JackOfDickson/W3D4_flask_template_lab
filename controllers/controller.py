from flask import render_template, request
from app import app
from models.event_calendar import event_list, add_new_event
from models.event import Event

@app.route('/home')
def index():
    return render_template('index.html', title="home", events=event_list)

@app.route('/home', methods=['POST'])
def add_event():
    event_name = request.form["event-name"]
    event_date = request.form["event-date"]
    event_description = request.form["description"]
    number_of_guests = 30
    event_location = "yes"
    new_event = Event(event_date, event_name, number_of_guests, event_location, event_description)
    add_new_event(new_event)

    return render_template('index.html', title="home", events=event_list)