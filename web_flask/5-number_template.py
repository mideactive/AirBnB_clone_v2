#!/usr/bin/python3
"""
A script that start a fask web app
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text
variable (replace underscore _ symbols with a space )
/python/(<text>): display “Python ”, followed by the value of
the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def web():
    """print string"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def web1():
    """print string"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """print variable"""
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/<text>', defaults={'text': 'Cool'}, strict_slashes=False)
@app.route('/python/<text>', defaults={'text': 'Cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p_route(text):
    """print variable"""
    return 'Python {}'.format(escape(text.replace('_', ' ')))


@app.route('/nuber/<int:n>', strict_slashes=False)
def n_route(n):
    """print only int"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def t_route(n):
    """print template"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
