#!/usr/bin/python3
"""
A script that starts a flask web application
and display content of path's variable
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_web():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_web1():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p_route(text):
    return 'Python {}'.format(escape(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def n_route(n):
    return '{} is a number'.format(n)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
