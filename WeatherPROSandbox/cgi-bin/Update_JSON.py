import cgi
import requests
import json
import os
import sys
sys.path.append(r'C:---File Path to Where You Installed the Folder---')
# Example: sys.path.append(r'C:\Users\arben\PyCharmProjects\WeatherPROSandbox')

from API_KEYS import api_key


form = cgi.FieldStorage()
city = form.getvalue('city')
state = form.getvalue('state')
zip_code = form.getvalue('zip')



response1 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{zip_code}&limit=1&appid={api_key}")
data2 = response1.json()

if data2 and len(data2) > 0:
    User_location1 = data2[0]['lat']
    User_location2 = data2[0]['lon']


    #response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=imperial&lat={User_location1}&lon={User_location2}&appid={api_key}")
    response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?units=imperial&lat={User_location1}&lon={User_location2}&appid={api_key}")
    weather_data = response.json()


    merge_weather_data = {
        "location_data": data2,
        "weather_data": weather_data
    }




    with open('WeatherAPI_Output.json', 'w') as file:
        json.dump(merge_weather_data, file, indent=4)

    print("<HTML>")
    print("Location: /Weathepro.html\n")



else:
    print("<HTML>")
    print("<html><body><h1>Error: Location data not found. Please try again.</h1></body></html>")

print('<html><head><meta http-equiv="refresh" content="0; url=/Weathepro.html" /></head></html>')


