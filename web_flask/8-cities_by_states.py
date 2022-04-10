#!/usr/bin/python3
"""
Start a Flask web application on 0.0.0.0 port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """to remove current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states')
def city_state():
    """cities by states"""
    state = list(storage.all(State).values())
    #for stat in state:
    return render_template('8-cities_by_states.html', state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
