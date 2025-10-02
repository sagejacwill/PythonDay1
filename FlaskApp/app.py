#! /usr/bin/env python3
# Author: SWilliams
# Description: A Flask App
"""
    Docstring:
"""

from flask import Flask, Response, request, render_template, url_for

app = Flask(__name__)

"""
@app.route('/', methods=['GET'])
def hello_from_flask():
    return 'Hello from Flask'
"""

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

@app.route('/dynamic/<string:word>')
def get_word(word):
    return word

@app.route('/square/<int:number>')
def get_square(number):
    return f"{number} squared is {number**2}"

@app.route('/hello/<string:name>')
def say_hello(name):
    return f"Hello {name.title()}!"

@app.route("/index/<name>/<int:iq>")
def index(name, iq):
    url = url_for("get_text")
    return f"""
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <title>Sample - Flask routes</title>
     </head>
     <body>
         <h1>Name Page</h1>
         <p>Hello {name}!</p>
         <p>Your IQ is {iq}!</p>
         <hr>
         <a href="{url}">Welcome</a>
     </body>
     </html>
     """

if __name__ == '__main__':
    app.run(debug=True)
