#!/usr/bin/python3
"""
Flask web application listening on 0.0.0.0 port 5000
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown():
    storage.close(self)


@app.route('/states_list')
def state_list():
    return render_template('7-states_list.html', state=list(storage.all(State).values()))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
