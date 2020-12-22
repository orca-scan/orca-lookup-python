# orca-lookup-python

This open source project is a an example of [how to scan barcodes using a smartphone](https://orcascan.com/mobile) and [present data from your system](https://orcascan.com/docs/api/lookup-url) using [Python](https://www.python.org/) and the [flask](https://github.com/pallets/flask) framework.

**How it works:**

1. A user [scans a barcode](https://orcascan.com/mobile) using their smartphone
2. Orca Scan sends a HTTP GET request to your endpoint with `?barcode=value`
3. Your system queries a database or internal API for a `barcode` match
4. Your system returns the data in JSON format with keys matching column names
5. The [Orca Scan mobile](https://orcascan.com/mobile) app presents that data to the user

*If the mobile user has [update permission](https://orcascan.com/docs/getting-started/adding-users#selecting-user-permissions) and saves the data, it will saved to your Orca sheet.*

## Install

First ensure you have [Python](https://www.python.org/downloads/) installed:

```bash
# should return 3.7 or higher
python3 --version
```

Then execute the following:

```bash
# download this example code
git clone https://github.com/orca-scan/orca-lookup-python.git

# go into the new directory
cd orca-lookup-python

# create virtual environment and activate it
python3 -m venv orca && source ./orca/bin/activate

# upgrade pip to latest version
pip install --upgrade pip

# install dependencies
pip install -r requirements.txt
```

## Run

```bash
# activate virtual environment
source ./orca/bin/activate

# start the project
flask run
```

Visit [http://localhost:5000?barcode=4S3BMHB68B3286050](http://localhost:5000?barcode=4S3BMHB68B3286050) to see the following:

```json
{
    "VIN": "4S3BMHB68B3286050",
    "Make": "SUBARU",
    "Model": "Legacy",
    "Manufacturer Name": "FUJI HEAVY INDUSTRIES U.S.A",
    "Vehicle Type": "PASSENGER CAR",
    "Year": 1992
}
```

## How this example works

This [example](app.py) uses the [flask](https://github.com/pallets/flask) framework:

```python
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
```

## Troubleshooting

If you run into any issues not listed here, please [open a ticket](https://github.com/orca-scan/orca-lookup-python/issues).

## Examples in other langauges
* [orca-lookup-node](https://github.com/orca-scan/orca-lookup-node)
* [orca-lookup-dotnet](https://github.com/orca-scan/orca-lookup-dotnet)
* [orca-lookup-go](https://github.com/orca-scan/orca-lookup-go)
* [orca-lookup-php](https://github.com/orca-scan/orca-lookup-php)
* [orca-lookup-java](https://github.com/orca-scan/orca-lookup-java)

## History

For change-log, check [releases](https://github.com/orca-scan/orca-lookup-python/releases).

## License

Licensed under [MIT License](LICENSE) &copy; [Orca Scan](https://orcascan.com)
