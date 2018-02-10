from flask import Flask
import sys

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def display():
    return "Working"

if __name__ == "__main__":
    app.run(debug=True)
