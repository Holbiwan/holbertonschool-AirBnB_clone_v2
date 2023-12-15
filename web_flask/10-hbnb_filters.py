#!/usr/bin/python3
"""
Start a Flask application on localhost"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)

def teardown_appcontext(exc=None):
    """
    Called on teardown of app contexts,
    for more info on contexts visit
    -> http://flask.pocoo.org/docs/1.0/appcontext/
    Storage.close() closes the SQL scoped session or reloads file storage.
    """
    storage.close()

app.teardown_appcontext(teardown_appcontext)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Checking input data using templating
    """
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda x: x.name)

    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
