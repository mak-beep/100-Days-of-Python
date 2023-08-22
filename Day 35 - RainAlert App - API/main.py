import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

# openweathermap
# ventusky.com

# apilist.fun
api_key = os.environ.get("api_key")
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 7.889097,
    "lon": -72.496689,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_sliced_data = weather_data["hourly"][:12]
print(weather_sliced_data)
will_rain = False

for hour_data in weather_sliced_data:
    if hour_data["weather"][0]["main"] == "Rain":
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Its going to rain today. Remember to bring an Umbrella.",
        from_= os.environ.get("from_phone"),
        to = os.environ.get("to_phone")
    )
    print(message.status)

