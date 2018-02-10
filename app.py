from flask import Flask, render_template, request
import sys

app = Flask(__name__, template_folder="/home/jeimer398/Documents/HackBU/Spring2018/HackBU2018/site")

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
