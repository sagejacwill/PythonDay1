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

