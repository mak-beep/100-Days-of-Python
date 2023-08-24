import requests
import os
from dotenv import load_dotenv
import datetime
from requests.auth import HTTPBasicAuth

load_dotenv()

# Task 1 : Identify Exercise information from the user input
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("API_KEY")
}
parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": os.environ.get("GENDER"),
    "age": os.environ.get("AGE"),
    "weight_kg": os.environ.get("WEIGHT_KG"),
    "height_cm": os.environ.get("HEIGHT_CM")
}

response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=headers)
response.raise_for_status()
exercises = response.json()["exercises"]
# print(exercises)

# Task 2 : Upload to Google Sheet
bearer_auth = {
    "Authorization": f"Bearer {os.environ.get('AUTH_TOKEN')}"
}
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

info = {
    "workout": {
        "date": datetime.datetime.now().strftime("%d/%m/%Y"),
        "time": datetime.datetime.now().strftime("%H:%M:%S")
    }
}
# response = requests.post(url=SHEETY_ENDPOINT, json=params)
# print(response.json())

for exercise in exercises:
    info["workout"]["exercise"] = exercise.get("name").title()
    info["workout"]["duration"] = exercise.get("duration_min")
    info["workout"]["calories"] = exercise.get("nf_calories")
    response = requests.post(url=SHEETY_ENDPOINT, json=info, headers=bearer_auth)
    response.raise_for_status()