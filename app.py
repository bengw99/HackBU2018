from flask import Flask, render_template, request, redirect
import sys
import json
from auth import *
from scraper import *

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder="../HackBU2018/site")

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/contact.php')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/preauth/')
def preauth():
    auther = make_auther()
    auth_url = auther.get_auth_url()
    return redirect(auth_url)

@app.route('/email/', defaults={'path': ''})
def postauth(path):
    code = request.args.get('code')
    messages = scrape(code)
    print("\n\n")
    print(json.dumps(messages, indent=1))
    return json.dumps(messages)

if __name__ == "__main__":
    app.run(debug=True)
