import os
import requests
import json
from flask import Flask, render_template, request, jsonify
from API_KEYS import api_key  # Ensure this file contains your actual API key

app = Flask(__name__)
application = app

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('Weathepro.html')

@app.route('/get_weather', methods=['GET', 'POST'])
def get_weather():
    if request.method == 'POST':
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zip')
    else:
        city = request.args.get('city')
        state = request.args.get('state')
        zip_code = request.args.get('zip')

    # Geolocation API request
    geo_response = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{zip_code}&limit=1&appid={api_key}"
    )
    geo_data = geo_response.json()

    # Check if geolocation data is found
    if geo_data:
        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']

        # Weather data API request
        weather_response = requests.get(
            f"https://api.openweathermap.org/data/3.0/onecall?units=imperial&lat={lat}&lon={lon}&appid={api_key}"
        )
        weather_data = weather_response.json()

        combined_data = {
            "location_data": geo_data,
            "weather_data": weather_data
        }

        # Save JSON data to the file
        output_file_path = os.path.join(app.static_folder, 'WeatherAPI_Output.json')
        if not os.path.exists(app.static_folder):
            os.makedirs(app.static_folder)

        with open(output_file_path, 'w') as json_file:
            json.dump(combined_data, json_file, indent=4)

        return jsonify(combined_data)  # Return combined data as JSON

    return jsonify({"error": "Location not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

'''
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    message = 'It works!\n'
    version = 'Python %s\n' % sys.version.split()[0]
    response = '\n'.join([message, version])
    return [response.encode()]
'''