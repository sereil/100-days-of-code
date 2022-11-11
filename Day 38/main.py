import requests
from datetime import datetime
import os


GENDER = "male"
WEIGHT_KG = 0
HEIGHT_CM = 0
AGE = 0


APP_ID = "675ca335"
API_KEY = "09a89362305fe346fc2ccbb8aff3a99c"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
WORKOUTS_SHEETS_ENDPOINT = "https://api.sheety.co/44287064d8fb2ae5de177ed1d8b62793/myWorkouts/workouts"

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}


query = input("Tell me which exercise you did: ")

exercise_params = {
    "query":query,
    "gender":GENDER,
    "weight_kg":WEIGHT_KG,
    "height_cm":HEIGHT_CM,
    "age":AGE
        
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
result = response.json()["exercises"]

e_name = result[0]["name"]
e_calories = result[0]["nf_calories"]
e_duration = result[0]["duration_min"]

today = datetime.now()

fToday = today.strftime("%d/%m/%Y")

workout_params = {
    "workout": {
        "date":fToday,
        "time":"20:00",
        "exercise":e_name,
        "duration":e_duration,
        "calories":e_calories
    }
}

gsheet_r = requests.post(url=WORKOUTS_SHEETS_ENDPOINT, json=workout_params)

print(gsheet_r)