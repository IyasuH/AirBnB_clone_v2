#!/usr/bin/python3
"""
Python script that starts a Flask web application
listening on 0.0.0.0 on port 5000
"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ returns Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """retunrs HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def C_fun(text):
    """returns C followed by the value of text variable"""
    txt = ""
    for i in range(len(text)):
        if text[i] == '_':
            txt = txt + ' '
        else:
            txt = txt + text[i]
    return 'C %s' % txt


@app.route('/python/')
@app.route('/python/<text2>')
def python_cool(text2="is cool"):
    """returns Python followed by the alue of the text variable
    the default value of text is is cool"""
    txt = ""
    for i in range(len(text2)):
        if text2[i] == '_':
            txt = txt + ' '
        else:
            txt = txt + text2[i]
    return 'Python %s' % txt


@app.route('/number/<int:n>')
def number_di(n):
    """display n is a number only if n is an integer"""
    return '%s is a number' % n


@app.route('/number_template/<int:n>')
def number_temp(n):
    """display HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_oddEven(n):
    """display HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
