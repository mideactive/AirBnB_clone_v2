#!/usr/bin/python3
"""A script that starts a flask app"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_web():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_web1():
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
