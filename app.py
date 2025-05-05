from flask import Flask, request, jsonify
from flask_cors import CORS
import backend
app = Flask(__name__)
CORS(app)

@app.route('/stations', methods=['GET'])
def get_all_station():
    country = str(request.args.get('country'))
    stations = backend.get_stations(country)
    return jsonify(stations)

@app.route('/get_countries', methods=['GET'])
def get_countries():
    countries = backend.get_countries()
    return jsonify(countries)

@app.route('/get_schedule_for_one_station', methods=['GET'])
def get_schedule_for_one_station():
    code_station = str(request.args.get('code_station'))
    date = str(request.args.get('date'))
    schedule = backend.get_schedule_for_one_station(code_station, date)
    return jsonify(schedule)

@app.route('/get_schedule_between_stations', methods=['GET'])
def get_schedule_between_stations():
    start_code_station = str(request.args.get('start_code_station'))
    end_code_station = str(request.args.get('end_code_station'))
    date = str(request.args.get('date'))
    schedule = backend.get_schedule_between_stations(start_code_station, end_code_station, date)
    return jsonify(schedule)

if __name__ == '__main__':
    app.run(debug=True)
