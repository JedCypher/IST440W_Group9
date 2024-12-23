import os
import requests
import json
from flask import Flask, render_template, request, jsonify
from API_KEYS import api_key

app = Flask(__name__)
application = app

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('Weathepro.html')
@app.route('/weathermap')
def weathermap():
    return render_template('Weathermap.html')

@app.route('/get_weather', methods=['post'])
def get_weather():
    city = request.form.get('city')
    state_in = request.form.get('state')
    zip_code = request.form.get('zip')


    response1 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state_in},{zip_code}&limit=1&appid={api_key}")
    data2 = response1.json()


    if data2:
        User_location1 = data2[0]['lat']
        User_location2 = data2[0]['lon']



    # response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=imperial&lat={User_location1}&lon={User_location2}&appid={api_key}")
        weather_response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?units=imperial&lat={User_location1}&lon={User_location2}&appid={api_key}")
        weather_data = weather_response.json()

        combined_data = {
            "location_data": data2,
            "weather_data": weather_data
        }

        weatherpro_output = os.path.join(app.static_folder, 'WeatherAPI_Output.json')


        os.makedirs(app.static_folder, exist_ok=True)


        with open(weatherpro_output, 'w') as json_file: json.dump(combined_data, json_file, indent=4)

        return jsonify(combined_data)


if __name__ == '__main__':
    app.run(debug=True)

