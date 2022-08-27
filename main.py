import requests
import os
import pandas as pd
from twilio.rest import Client

# twilio info
twilio_phone_number = '+15739203384'
account_sid = 'ACf39abe6372c09aea416fb39b3791705c'
auth_token = os.environ.get(AUTH_TOKEN)

# API info
weather_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get(API_KEY)
parameters = {
    "lat": 33.248348,
    "lon": -8.516350,
    'exclude': 'current,minutely,daily',
    "appid": api_key,
}
response = requests.get(weather_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
hourly_forecast = data['hourly']
df = pd.DataFrame(hourly_forecast)
df = df.loc[0:11]
weather_df = df.weather
bring_umbrella = False
for i in range(0, len(weather_df)):
    if weather_df[i][0]['id'] <= 700:
        bring_umbrella = True
if bring_umbrella:
    print("it's raining")
# Setting up twilio client
if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☂️ ",
        from_=twilio_phone_number,
        to='your phone number'
    )
    print(message.status)


