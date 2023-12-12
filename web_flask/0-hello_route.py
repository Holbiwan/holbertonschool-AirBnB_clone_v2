#!/usr/bin/python3
"""Start a Flask web application on localhost"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display a message when making a request to root"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    """run app flask"""
    app.run(host='0.0.0.0', port=5000)
