#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=None):
    """ Display state """
    state = None
    states = storage.all(state)
    if not id:
        state_list = list(states.values())
    else:
        if ("State." + id) in states.keys():
            state = states["State." + id]
    return render_template('9-states.html', **locals())


@app.teardown_appcontext
def close(self):
    """ Close app """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
