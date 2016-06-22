import os 
from flask import Flask
from flask import url_for, redirect

app = Flask(__name__)

@app.route("/")
def html():
    return redirect(url_for('static', filename='Interface.html'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
