import os 
from flask import Flask
from flask import request

app = Flask(__name__, static_url_path='')

@app.route('/')
def html():
    return app.send_static_file('Interface.html')


