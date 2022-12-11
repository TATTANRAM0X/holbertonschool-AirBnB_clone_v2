#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
import os

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ Removes the current SQLAlquemy session """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def states_route():
    """ Display a HTML page """
    states = [state for state in storage.all(State).values()]
    cities = [city for city in list(storage.all(City).values())]
    amenities = [amenity for amenity in storage.all(Amenity).values()]
    return render_template(
            '10-hbnb_filters.html',
            states=states,
            cities=cities,
            amenities=amenities)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)