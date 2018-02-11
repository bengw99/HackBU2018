from flask import Flask, render_template, request
import sys
from auth import *

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder="../HackBU2018/site")

@app.route("/", methods = ["GET", "POST"])
def home():
    print(request.method, request.method == "POST")
    if request.method == "POST":
        start_auth()
    return render_template("index.html")

@app.route('/contact.php')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])





if __name__ == "__main__":
    app.run(debug=True)
