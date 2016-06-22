from flask import render_template

@app.route('/')

app = Flask(__name__)

def hello():
    return render_template('interface.html', name=name)
