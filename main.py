import requests
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


LAT = "22.485161"
LNG = "88.357430"
account_sid = "ACf1c88379cd26f8670c4f73ce33887367"
auth_token = "04c9a744206ac9493764ea6cf3edfbec"
api_key = "652c2e4a51301f5407bbaa8357bee637"
OWM_ENDPOINT_ONECALL = "https://api.openweathermap.org/data/2.5/onecall"
OWM_WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    "lon": LNG,
    "lat": LAT,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
res = requests.get(OWM_ENDPOINT_ONECALL, params=parameters)
res.raise_for_status()
weather_data = res.json()
hourly_slice = weather_data["hourly"][:12]
rain = False
for hour in hourly_slice:
    condition = (hour["weather"][0]["id"])
    if condition < 700:
        rain = True
    else:
        rain = False
# print(hourly_data)
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Carry an umbrella with you today.",
        from_="+12707705695",
        to="+919330609602"
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="No need to carry an umbrella today.",
        from_="+12707705695",
        to="+919330609602"
    )
    print(message.status)
