import os 
from flask import Flask
from flask import url_for, render_template
import Interface.html

app = Flask(__name__)

@app.route("/")
def html():
    return render_template(url_for("static", filename="Interface.html"))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
