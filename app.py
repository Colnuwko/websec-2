from flask import Flask, render_template, request, jsonify
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
    event = bool(request.args.get('event'))
    schedule = backend.get_schedule_for_one_station()
    return jsonify(schedule)
if __name__ == '__main__':
    app.run(debug=True)
