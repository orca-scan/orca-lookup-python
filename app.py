# import flask framework
from flask import Flask
from flask import request
from flask import jsonify

# create a flask app instance
app = Flask(__name__)

# GET / handler
@app.route("/")
def index():

    # get the incoming barcode sent from Orca Scan (scanned by a user)
    barcode = request.args.get("barcode")

    # TODO: query a database or API to retrieve some data based on barcode value
    data = {
        "VIN": barcode,
        "Make": "SUBARU",
        "Model": "Legacy",
        "Manufacturer Name": "FUJI HEAVY INDUSTRIES U.S.A",
        "Vehicle Type": "PASSENGER CAR",
        "Year": 1992
    }

    # return data in JSON format (property names must match Orca column names)
    return jsonify(data) 
