#! /usr/bin/env python3
# Author: SWilliams
# Description: A Flask App
"""
    Docstring:
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_from_flask():
    return 'Hello from Flask'

@app.route('/sky', methods=['GET'])
def hello_grads():
    return 'Hello Sky Grads'

if __name__ == '__main__':
    app.run(debug=True)

