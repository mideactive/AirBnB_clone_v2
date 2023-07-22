#!/usr/bin/python3
"""
A script that starts a flask app and display path variable
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_web():
    """display Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_web1():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display content of a variable"""
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/<text>', strict_slashes=False)
def p_route(text):
    """display content of a variable"""
    return 'Python {}'.format(escape(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
