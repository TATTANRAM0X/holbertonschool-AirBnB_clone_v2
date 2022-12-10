#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_route(text):
    """ display “C ” followed by the value of the text variable """
    newText = text.replace('_', ' ')
    return 'C {}'.format(escape(newText))


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    newText = text.replace('_', ' ')
    return 'Python {}'.format(escape(newText))


@app.route("/number/<int:n>", strict_slashes=False)
def number_Route(n):
    return '{} is a number'. format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
