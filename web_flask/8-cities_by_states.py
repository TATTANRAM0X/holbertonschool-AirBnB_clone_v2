#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
import os

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ removes the current SQLAlchemy Session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_state():
    """ displays a HTML page """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = [city for city in list(storage.all(City).values())]
        states = [state for state in storage.all(State).values()]
        return render_template(
            "8-cities_by_states.html",
            states=states,
            cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
