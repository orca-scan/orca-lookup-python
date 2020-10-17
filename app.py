# import flask framework
from flask import Flask
from flask import request

# create a flask app instance
app = Flask(__name__)

# GET / handler
@app.route("/")
def index():
    barcode = request.args.get("barcode")
    return barcode