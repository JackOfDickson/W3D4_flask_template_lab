from flask import render_template
from app import app
from models.event_calendar import event_list

@app.route('/home')
def index():
    return render_template('index.html', title="home", events=event_list)