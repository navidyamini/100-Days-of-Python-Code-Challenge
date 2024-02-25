import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# api_key = "*************"
api_key = os.environ.get("API_KEY")
account_sid = "*************"
# auth_token = "*************"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "appid": api_key,
    "lat": 53.349804,
    "lon": -6.260310,
    "cnt": 4,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            from_='+*************',
            body="It's going to rain today. Remember to take an umbrella ☂️ with you.",
            to='+*************'
        )
    print(message.status)
