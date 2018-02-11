from flask import Flask, render_template, request
import sys
from auth import *

app = Flask(__name__, template_folder="../HackBU2018/site")

@app.route("/", methods = ["GET", "POST"])
def home():
    print(request.method, request.method == "POST")
    if request.method == "POST":
        start_auth()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
