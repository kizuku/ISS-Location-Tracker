import os 
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('interface.html')

if __name__ == '__main__':
    app.run()
