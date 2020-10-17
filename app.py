# import flask framework
from flask import Flask

# create a flask app instance
app = Flask(__name__)

# GET / handler
@app.route("/")
def index():
    return "Hello, World!"