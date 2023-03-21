#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return 'HBNB'


@app.route('/about')
def about():
    """Returns an about page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Returns a contact page"""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)


