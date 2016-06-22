import os 
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return render_template('interface.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host = '0.0.0.0', port=port)
