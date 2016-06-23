from flask import render_template
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

@app.route('/interface/<name>')
def interface():
    return render_template('interface.html', name)

if __name__ == '__main__':
    app.run(debug=True)
