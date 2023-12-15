#!/usr/bin/python3
"""Start a Flask application on localhost."""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(exc=None):
    """Called on teardown of app contexts.

    After each request: remove the current SQLAlchemy session.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a list of states and their cities"""

    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=sorted(states))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
