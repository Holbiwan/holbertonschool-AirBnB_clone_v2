#!/usr/bin/python3
"""Script to start a Flask app on localhost."""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)

@app.teardown_appcontext
def appcontext_teardown(exc=None):
    """Called on teardown of app contexts."""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def conditional_templating():
    """Checking input data using templating."""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
