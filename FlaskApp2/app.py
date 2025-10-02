#! /usr/bin/env python3
# Author: SWilliams
# Description: This script will demo
"""
    Docstring:
"""
from flask import Flask

from application import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


