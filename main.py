import os
import requests
from twilio.rest import Client

account_sid =  os.environ.get("ACCOUNT_SID")
auth_token =  os.environ.get("AUTH_TOKEN")
api_key =  os.environ.get("MY_KEY")
MY_LAT =  os.environ.get("MY_LAT")
MY_LNG = os.environ.get("MY_LNG")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()


weather_id_list = [
    element["weather"][0]["id"]
    for element
    in data["list"]
    if element["weather"][0]["id"] < 700
]
if weather_id_list:
    print(weather_id_list)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_= os.environ.get("MY_FROM"),
        body="It's going to rain today. Remember to bring an ☂️",
        to=" os.environ.get("MY_TO"),
    )

    print(message.status)




