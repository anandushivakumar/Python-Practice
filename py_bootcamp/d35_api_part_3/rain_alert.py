import requests
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

# 129b616b2748b4b2f1896c37603ff518
API_ID = os.getenv('API_ID')
MY_LAT = 25.20
MY_LON = 55.29

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_ID,
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status()
data = response.json()
#print(data)

# check weather data for the next 12 hours and primt temp and ask to bring umbrella if temperature is above 35C
for entry in data["list"]:
    max_temp = entry["main"]["temp_max"]
    max_temp_c = max_temp - 273.15
    weather_id = entry["weather"][0]["id"]
    print(f"Max temperature: {max_temp_c} C")
    print(f"Weather ID: {weather_id}")
    if weather_id == 800 and max_temp_c > 30:
        print("Bring an umbrella")
        break
    else:
        print("Don't bring an umbrella")
        break
