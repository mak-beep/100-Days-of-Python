import requests
from datetime import datetime

USERNAME = "mak"
TOKEN = "jsjhgfjgd6yhsdfg"
GRAPH = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPH,
    "name": "Programming Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_parameters, headers=headers)
# print(response.text)

today = datetime.now()
# today = datetime(year=2023, month=8, day=22)
# print(today.strftime("%Y%m%d"))
value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

value_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code, Today? ")
}

response = requests.post(url=value_endpoint, json=value_parameters, headers=headers)
print(response.text)

# Updating a value
update_value_parameters = {
    "quantity": "56"
}
date = today.strftime('%Y%m%d')
update_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{date}"

# response = requests.put(url=update_value_endpoint, json=update_value_parameters, headers=headers)
# print(response.text)

# Deleting a value

# response = requests.delete(url=update_value_endpoint, headers=headers)
# print(response.text)
