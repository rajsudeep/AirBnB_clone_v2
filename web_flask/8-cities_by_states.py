#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_id():
    """ Display state and city list """
    state_list = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=state_list)


@app.teardown_appcontext
def close(self):
    """ Close app """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
