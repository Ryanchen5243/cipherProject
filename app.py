# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods = ["GET","POST"])
def results():
    if request.method == "POST":
        user_message = request.form["original_message"]
        enc_message = model.caesar_cipher(user_message)

        return render_template('results.html', user_message=user_message, enc_message=enc_message)
    else:
        return "Error"

