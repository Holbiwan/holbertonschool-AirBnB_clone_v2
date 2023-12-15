#!/usr/bin/python3
"""Starts a Flask application on localhost"""

from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Check input data using a template"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(exception):
    """After each request remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
