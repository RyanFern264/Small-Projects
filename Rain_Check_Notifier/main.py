import requests
import os

api_key = os.environ.get("OWM_api_key")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

lat = os.environ.get("lat")
lon = os.environ.get("lon")

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt":5
}

weather_api_call = requests.get(OWM_Endpoint, params=weather_params)
weather_api_call.raise_for_status()
weather_data = weather_api_call.json()

will_rain = False
for hour in weather_data["list"]:
    if hour["weather"][0]["id"] < 700:
        will_rain = True
print("bring an umbrella")