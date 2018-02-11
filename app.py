from flask import Flask, render_template, request, redirect
import sys
from auth import *
from scraper import *

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder="../HackBU2018/site")

@app.route("/")
def home():
    print("home")
    return render_template("index.html")

@app.route('/contact.php')
def static_from_root():
    print("static")
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/preauth/')
def preauth():
    print("PREAUTH being called")
    auther = make_auther()
    auth_url = auther.get_auth_url()
    return redirect(auth_url)

@app.route('/email/', defaults={'path': ''})
def postauth(path):
    code = request.args.get('code')
    print("------POSTAUTH-----")
    print("CODE = " + code)
    messages = scrape(code)
    print("---------------CHECK HERE FOR MESSAGES: " + messages)
    return messages

if __name__ == "__main__":
    app.run(debug=True)
