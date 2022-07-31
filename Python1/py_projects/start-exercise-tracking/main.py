import requests
import datetime as dt

api_key = "43c24ed228d4a9e99ad15ec124bef7ad"
app_id = "e341e1b8"

exersice_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/760a8d91b2f084d8b882a7c8883af212/tracking/workouts"
sheet_update = "https://api.sheety.co/760a8d91b2f084d8b882a7c8883af212/tracking/workouts/2"

today = dt.datetime.now()
date = today.strftime("%x")
time = today.strftime("%X")

workout_text = input()

exersice_config_header = {
    "x-app-id": app_id,
    "x-app-key": api_key
}

exercise_config = {
    "query": f"{workout_text}"
}
sheet_config_header = {
    "Authorization": "Bearer wafjkaenfj3JWANJfndAIUW"
}

response = requests.post(url=exersice_endpoint, json=exercise_config, headers=exersice_config_header)
workout_data = response.json()["exercises"]

for x in range(len(workout_data)):
    user_input = workout_data[x]["user_input"]
    duration_min = workout_data[x]["duration_min"]
    nf_calories = workout_data[x]["nf_calories"]
    workout_update = {
        "workout": {
            "date": f"{date}",
            "time": f"{time}",
            "exercise": f"{user_input}",
            "duration": f"{duration_min}",
            "calories": f"{nf_calories}",
        }
    }
    response_create = requests.post(sheet_endpoint, json=workout_update, headers=sheet_config_header)
    print(response_create.text)
