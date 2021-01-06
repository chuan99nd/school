from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    f = open("index.html")
    content = f.read()
    return content

