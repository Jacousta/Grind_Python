import requests
from datetime import datetime

parameters = {
    "token": "padkaejfjkad",
    "username": "chirag01",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response_pixela = requests.post(url="https://pixe.la/v1/users",json=parameters)
# print(response_pixela.text)
graph_config = {
    "id": "randyorton",
    "name": "graph1",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

graph_auth = {
    "X-USER-TOKEN": "padkaejfjkad"
}

# graph_response = requests.post(url="https://pixe.la/v1/users/chirag01/graphs", json=graph_config, headers=graph_auth)
# print(graph_response.text)

today = datetime(day=12,month=7,year=2022)
pixel_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity":"100"

}

pixel = requests.delete(url="https://pixe.la/v1/users/chirag01/graphs/randyorton/20220712", headers=graph_auth)
print(pixel.text)

# graph_update_json = {
#     "name":"graph1",
#     "timezone":"Asia/Tokyo",
#
# }
#
# graph_update = requests.put(url="https://pixe.la/v1/users/chirag01/graphs/randyorton",headers=graph_auth,)
# print(graph_update.text)
