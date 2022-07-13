import requests
import os


MY_LAT = os.environ.get("lat")
MY_LNG = os.environ.get("lng")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": "afce4b31a81950a80a5cad9db6637ba2",
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
data = response.json()
print(data)

# import time
# from twilio.rest import Client
# import random
#
# account_sid = "ACb2b6cc6288147430b835198ca7500126"
# auth_token = 'b77a51468978c2f61d64c6afa1e63163'
# client = Client(account_sid, auth_token)
# for X in range(10):
#     message = client.messages \
#         .create(
#         body=f"Mitul potty {random.randint(1, 10)}",
#         from_='+15185030691',
#         to='+919501545441'
#     )
#     print(message.status)
#     time.sleep(30)
