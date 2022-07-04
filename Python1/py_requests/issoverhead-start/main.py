from config import *
import time
import requests

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response_iss = requests.get("http://api.open-notify.org/iss-now.json")

response.raise_for_status()

ist_hour = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
ist_min = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[1]) + 30
ist_hour_set = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0]) + 5
ist_min_set = int(response.json()["results"]["sunset"].split("T")[1].split(":")[1]) + 30
while True:
    time.sleep(60)
    if iss_near(response_iss) and night_checker(ist_hour_set, ist_min_set, ist_hour, ist_min):
        send_email()
