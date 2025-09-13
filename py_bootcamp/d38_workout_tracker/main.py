import requests
import os
from datetime import datetime
from dotenv import load_dotenv, dotenv_values

load_dotenv()

HOST_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
ROW_ENDPOINT = "https://api.sheety.co/0c3d02b0bdfba07c66219692a0efa461/workoutTracking/workouts"

headers_nutri = {
    "x-app-id": os.getenv('APP_ID'),
    "x-app-key": os.getenv('API_KEY')
}

params_nutri = {} 
params_nutri["query"] = input("Which exercises have you done today?: ")

response = requests.post(url = HOST_URL, json = params_nutri, headers = headers_nutri)
result = response.json()
# print(result)

# json results
for entry in result["exercises"]:
    duration = entry["duration_min"]
    exercise = entry["name"]
    calories = entry["nf_calories"]
    print(f"{duration} mins - {exercise} - {calories} calories")

current_date = datetime.today().strftime("%d/%m/%Y")
current_time = datetime.today().strftime("%H:%M:%S")

# POST data to Google Sheets using Sheety
params_sheety = {
    "workout":{
        "date": current_date,
        "time": current_time, 
        "exercise": exercise,
        "duration": int(duration),
        "calories": int(calories)
    }
}

response_sheety = requests.post(url = ROW_ENDPOINT, json = params_sheety)
print(response_sheety.text)