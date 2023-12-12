#!/usr/bin/python3
"""Start a flask web application on localhost"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Display HBNB"""
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def text_C(text):
    """Display “C ” followed by the value of the text variable """
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
