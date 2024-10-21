import requests
import json
import socket
from API_KEYS import api_key

User_IP = socket.gethostbyname(socket.gethostname())
print(User_IP)

City_inp = input("Please enter a city name: ")
State_inp = input("Please enter a state initial: ")
Zip_code = input("Please enter a zip code: ")

response1 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={City_inp},{State_inp},{Zip_code}&limit=1&appid={api_key}")
data2 = response1.json()

User_location1 = data2[0]['lat']
User_location2 = data2[0]['lon']

response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?units=imperial&lat={User_location1}&lon={User_location2}&appid={api_key}")
#response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?units=imperial&lat={User_location1}&lon={User_location2}&appid={api_key}")
data = response.json()


JSON_data = {
    "location_data": data2,
    "weather_data": data
}


with open('WeatherAPI_Output.json', 'w') as file:
    json.dump(JSON_data, file, indent=4)

'''
import requests
from geopy import Nominatim
#from Geopy_Locator import *
from API_KEYS import *
from geopy import Nominatim
#from Geopy_Locator import WeatherLocation
import json
#api_key = "ac4759706d906841a39f9c7d4cceb73d"
def WeatherLocation():
    geolocator = Nominatim(user_agent="WeatherAPI")
    User_location = geolocator.geocode(City_inp)
    return User_location

City_inp = input("Please enter a city name: ")
State_inp = input("Please enter a state initial: ")
Zip_code = input("Please enter a zip code: ")
response1 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={City_inp},{State_inp},{Zip_code}&limit=1&appid={api_key}")
data2 = response1.json()

print(WeatherLocation())

print(json.dumps(data2, indent=4))

file = open('WeatherAPI Output.txt', 'w')
'''
print(data2)

User_location1 = data2[0]['lat']
User_location2 = data2[0]['lon']

#response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units=imperial&lat={User_location1}&lon={User_location2}&appid={api_key}")
response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?units=imperial&lat={User_location1}&lon={User_location2}&appid={api_key}")
data = response.json()

#print(data)
print(json.dumps(data, indent=4))
file.write(json.dumps(data2, indent=4) + '\n')
file.write(json.dumps(data, indent=4))
file.close()