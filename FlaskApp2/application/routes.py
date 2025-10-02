#! /usr/bin/env python3
# Author: SWilliams
# Description: This script will demo
"""
    Docstring:
"""

from flask import render_template
from . import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/words')
def template_words():
    words = []
    fh_in = open(r"/Users/swi081/PycharmProjects/Python QA/Demos/words", mode="rt")
    for word in fh_in:
        if "town" in word:
            words.append(word)
    return render_template('words.html', words=words)
