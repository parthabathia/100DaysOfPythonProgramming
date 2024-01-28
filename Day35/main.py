import requests
import os
from twilio.rest import Client

ACCOUNT_SID = "your_account"
AUTH_TOKEN = "auth_token"
MY_LAT = 41.445049
MY_LONG = -74.420021
OWM_api_key = "api_key"
API_endpoint_forecast = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": OWM_api_key,
    "units": "metric",
    "cnt": 4
}
API_endpoint_weather = "https://api.openweathermap.org/data/2.5/weather"

response = requests.get(url=API_endpoint_forecast, params=params)
response.raise_for_status()
weather_data = response.json()

need_umbrella = False
for data in weather_data['list']:
    if data['weather'][0]['id'] < 700:
        need_umbrella = True

if need_umbrella:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Bring an umbrella",
        from_='temp_number',
        to='your_number'
    )
    print(message.status)
