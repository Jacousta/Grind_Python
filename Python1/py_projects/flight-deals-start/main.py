import requests
import datetime as dt

API_ID = "obEuEnNLRR2VK3h-DvKcVMDcq3OpoP6a"
flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"

sheet_endpoint = "https://api.sheety.co/760a8d91b2f084d8b882a7c8883af212/flightDeals/prices"

key_header = {
    "apikey": API_ID
}

today = dt.datetime.now()
six_months = today + dt.timedelta(days=180)
today_date = dt.datetime.now().date().strftime("%d/%m/%Y")
six_months_date = six_months.date().strftime("%d/%m/%Y")

sheet = requests.get(url=sheet_endpoint)

for x in range(len(sheet.json()["prices"])):

    flight_search_params = {
        "fly_from": "DEL",
        "fly_to": f"{sheet.json()['prices'][x + 2]['iataCode']}",
        "date_from": f"{today_date}",
        "date_to": f"{six_months_date}",
        "nights_in_dst_from": 7,
        "nights_in_dst_to": 28,
        "flight_type": "round",
        "one_for_city": 1,
        "max_stopovers": 0,
        "curr": "INR"
    }

    response = requests.get(url=flight_search_endpoint, headers=key_header, params=flight_search_params)
    try:
        data = response.json()["data"][0]
        price = data["price"]
        origin_city = data["route"][0]["cityFrom"]
        origin_airport = data["route"][0]["flyFrom"]
        destination_city = data["route"][0]["cityTo"]
        destination_airport = data["route"][0]["flyTo"]
        out_date = data["route"][0]["local_departure"].split("T")[0]
        print(f"{destination_city}: ₹{price}")
    except IndexError:
        print(f"No flights found")

# print(response.json()["data"][0])
# price=data["price"],
# origin_city=data["route"][0]["cityFrom"],
# origin_airport=data["route"][0]["flyFrom"],
# destination_city=data["route"][0]["cityTo"],
# destination_airport=data["route"][0]["flyTo"],
# out_date=data["route"][0]["local_departure"].split("T")[0],
# return_date=data["route"][1]["local_departure"].split("T")[0]


# for x in range(len(sheet.json()["prices"])):
#     sheet_put_endpoint = f"https://api.sheety.co/760a8d91b2f084d8b882a7c8883af212/flightDeals/prices/{x+2}"
#     CITY_NAME = sheet.json()["prices"][x]["city"]
#     # print(sheet_update.json()["prices"][0]["iataCode"])
#     # print(sheet_update.json()["prices"][x]["lowestPrice"])
#
#     flight_data = {
#         "term": f"{CITY_NAME}",
#         "location_types": "city"
#     }
#
#     response = requests.get(url=flight_search_endpoint, headers=key_header, params=flight_data)
#     code = response.json()["locations"][0]["code"]
#
#     code_update = {
#         "price": {
#             "iataCode": f"{code}"
#         }
#     }
#
#     update = requests.put(url=sheet_put_endpoint, json=code_update)
#     print(update.text)
