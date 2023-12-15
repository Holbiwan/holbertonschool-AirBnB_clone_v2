#!/usr/bin/python3
"""Start a flask web application on localhost"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Display a HTML page of state"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """show id for the states"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state,
                                   id=True)
    return render_template('9-states.html')


@app.teardown_appcontext
def remove_session(exception):
    """closing storage"""
    storage.close()
