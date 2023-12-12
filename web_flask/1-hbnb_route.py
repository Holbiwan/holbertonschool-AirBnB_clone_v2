#!/usr/bin/python3
"""Start a flask web application on localhost
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bhnb():
    """Display message Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display message HBNB!"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
