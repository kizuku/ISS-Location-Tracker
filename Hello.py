from flask import render_template
from flask import Flask, request

app = Flask(__name__, static_url_path='/templates/')

@app.route('/')
def hello():
    return "Hello!"

@app.route('/interface')
def interface():
    return app.send_static_file('interface.html')

if __name__ == '__main__':
    app.run(debug=True)
