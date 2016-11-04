from csv_reader import CSVReader
from application import Application
from decorators import check_rate_limit
from flask import Flask, request,abort,make_response
from config import config
import json
app = Flask(__name__)
utils = Application()

@app.route("/")
def main():
    return "Welcome!"

@app.route("/getCityHotels",methods=['POST'])
@check_rate_limit('api_key')
def get_hotels():
    try:
        request_body = json.loads(request.data)
        city_id = request_body.get('city_id')
        sort_type_value = request_body.get('sort_type')
        meta_data = utils.get_city_hotels(city_id,sort_type=sort_type_value)
        format_data = utils.format_data(meta_data,config.CSV_DATA.headers)
        response = json.dumps(format_data)
        return response
    except KeyError:
        response = "Key not found for {}".format(city_id)
        abort(make_response(str(response), 404))
    except Exception as e:
        response = e.args
        abort(make_response(str(response), 400))

if __name__ == "__main__":
    config.CSV_DATA = CSVReader()  # reads CSV while while starting the server
    app.run()