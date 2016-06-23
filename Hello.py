from flask import render_template
from flask import Flask, request

app = Flask(__name__, static_url_path='')

@app.route('/')
def hello():
    return app.send_static_file('welcome.html')
#    return "Hello!"

#@app.route('/interface')
#def interface():
#    return app.send_static_file('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)
