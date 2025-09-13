import requests
from datetime import datetime

USER = "busa01"
TOKEN = "b8a4d0a5-e0d7-4c0f-b5d4-f8d1f7f5f4a6"
GRAPH_ID = "testgraph1"

pixela_url = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}

# response = requests.post(url=pixela_url, json=user_params)
# print(response.text)

# creating a graph definition
# graph_endpoint = f"{pixela_url}/{USER}/graphs"

# graph_params = {
#     "id": "testgraph1",
#     "name": "Sleep Graph", 
#     "unit": "hours",
#     "type": "int",
#     "color": "kuro"
# }

# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url = graph_endpoint, json = graph_params, headers = headers)
# print(response.text)

# printing a pixel to the graph
# graph_enpoint = f"{pixela_url}/{USER}/graphs/{GRAPH_ID}"

# today = datetime.today()


# pixel_params = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "9",
# }

# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_enpoint, json=pixel_params, headers=headers)
# print(response.text)

# PUT METHOD - updating a pixel
# day = datetime(year=2025, month = 9, day = 9)
# pixel_endpoint = f"{pixela_url}/{USER}/graphs/{GRAPH_ID}/{day.strftime('%Y%m%d')}"

# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# pixel_params = {
#     "quantity": "5"
# }

# response = requests.put(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# DELTE method - deleting a pixel
day = datetime(year=2025, month = 9, day = 9)
pixel_endpoint = f"{pixela_url}/{USER}/graphs/{GRAPH_ID}/{day.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.delete(url = pixel_endpoint, headers = headers)
print(response.text)