from flask import Flask, render_template, request
import sys

#app = Flask(__name__, template_folder="/home/jeimer398/Documents/HackBU/Spring2018/HackBU2018/site")

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder="../HackBU2018/site")

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/contact.php')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])





if __name__ == "__main__":
    app.run(debug=True)
