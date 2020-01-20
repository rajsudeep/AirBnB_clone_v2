#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ Says hello """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Says HBNB """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
