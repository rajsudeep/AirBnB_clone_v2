#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """ Says hello """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Says HBNB """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display C followed by text """
    return "C " + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ Display Python followed by text """
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Display integer """
    return "%d is a number" % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Display number in template """
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_o_or_e(n):
    """ Display o or e statement in template """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
