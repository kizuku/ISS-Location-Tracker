from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('welcome.html')

@app.route('/user-interface')
def interface():
    return render_template('user-interface.html')

if __name__ == '__main__':
    app.run(debug=True)
