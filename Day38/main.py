import requests
from datetime import datetime

NUTRI_API_KEY = "your_key"
NUTRI_APP_ID = "your_id"

SHEETY_TOKEN = "<your_token>"

GENDER = "your gender"
WEIGHT = "your weight in int"
HEIGHT = "your height in int"
AGE = "your age in int"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
query = input("Which exercises did you do today? ")

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY
}

parameters = {
    "query": query,
    "gender": GENDER,
    # "weight": WEIGHT,
    # "height": HEIGHT,
    "age": AGE
}
date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
data = response.json()['exercises']

sheety_endpoint = "https://api.sheety.co/<your_file>/myWorkouts/workouts"
sheety_header = {
    "Authorization" : "Bearer <your_token>"
}
for row in data:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": current_time,
            "exercise": row['user_input'],
            "duration": row['duration_min'],
            "calories": row['nf_calories']
        }
    }
    response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_header)
    print(response.text)
