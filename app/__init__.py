import os

from flask import Flask

app = Flask(__import__)

@app.route("/")
def hello_world():
    return "<p>hello, world!</p>"


