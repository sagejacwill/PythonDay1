#! /usr/bin/env python3
# Author: SWilliams
# Description: A Flask App
"""
    Docstring:
"""

from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_from_flask():
    return 'Hello from Flask'

@app.route('/sky', methods=['GET'])
def hello_grads():
    return 'Hello Sky Grads'

@app.route('/get/text', methods=['GET'])
def get_text():
    return Response("Hello from Flask, using an explicit Response Object")

@app.route('/post/text', methods=['GET'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response(f"You posted{data_sent} to the Flask app", mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)


