import requests
from datetime import datetime
import os

APP_ID = os.environ["NUTRI_APP_ID"]
API_KEY = os.environ["NUTRI_API_KEY"]
NUTRITIONIX_ENDPOINT = os.environ["NUTRITIONIX_ENDPOINT"]
WEIGHT_KG = 78
HEIGHT_CM = 172
AGE = 20
SHETTY_ENDPOINT = os.environ["SHETTY_ENDPOINT"]
SHETTY_USERNAME = os.environ["SHETTY_USERNAME"]
SHETTY_PASSWORD = os.environ["password_shetty"]
AUTH = os.environ["Authorization"]

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exercise_text = input("Tell me which exercises you did: ")
parameters = {
    "query": exercise_text,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=header, json=parameters)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")
for exercise in result['exercises']:
    sheet_input = {
        "sheet1": {
            "date": today_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

shetty_header = {
    "Authorization": AUTH
}
reponse = requests.post(url=SHETTY_ENDPOINT, json=sheet_input, auth=(SHETTY_USERNAME, SHETTY_PASSWORD), headers=shetty_header)
print(reponse.text)

