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

@app.route('/states_list', strict_slashes=False)
def conditional_templating(n=None):
    """Check input data using a template."""
    return render_template('7-states_list.html', states=storage.all("State"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

