from flask import Flask, render_template, request, redirect
import sys
import json
from auth import *
from scraper import *
from batchrate import *

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
# MUSC CONVERT MESSAGES TO DATA TYPE 
    batch_rate(messages)
    json_string = json.dumps([ob.__dict__ for ob in messages])
#    return json_string
    print("\n\n")
    print(json_string);
    print("\n\n")
    return render_template('output.html', reviews = json_string)

if __name__ == "__main__":
    app.run(debug=True)
