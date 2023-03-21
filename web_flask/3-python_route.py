#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask

# Define host and port variables
HOST = '0.0.0.0'
PORT = '5000'

# Create Flask app instance
app = Flask(__name__)


# Define routes
@app.route('/', strict_slashes=False)
def index():
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Displays “C” followed by the value of the text variable"""
    return f'C {text.replace("_", " ")}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """Displays “Python” followed by the value of the text variable"""
    return f'Python {text.replace("_", " ")}'


# Run app
if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
