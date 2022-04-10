#!/usr/bin/python3
"""
Start a Flask web application on 0.0.0.0 port 5000
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    """to remove current SQLAlchemy Session"""
    storage.close()


@app.route('/states')
def state_list():
    """cities by states"""
    state = list(storage.all(State).values())
    return render_template('9-states.html', x=3, stat=state)


@app.route('/states/<n>')
def staes_id(n):
    """sate objects found with <id>"""
    state = list(storage.all(State).values())
    for stat in state:
        x = 1
        if n == stat.id:
            x = 2
            return render_template('9-states.html', x=2, stat=stat)
    if x == 1:
        return render_template('9-states.html', x=1, stat=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
