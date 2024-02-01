import requests
from datetime import datetime

username = "parthbathia"
token = "S0n1que243wdfdsf54efcds4d"

url = "https://pixe.la/v1/users"
user_params = {
    "token": token,
    "username": "parthbathia",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=url, json=user_params)
print(response.text)

graph_endpoint = f"{url}/{username}/graphs"
graph_config = {
    "id": "graph1",
    "name": "code commits",
    "unit": "commit",
    "type": "int",
    "color": "kuro",
    "timezone": "Asia/Kolkata"
}
headers = {
    "X-USER-TOKEN": token
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

pixel_endpoint = f"{url}/{username}/graphs/graph1"
pixel_config = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "2"
}
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
update_endpoint = f"{url}/{username}/graphs/graph1/20240201"
update_config = {
    "quantity": "2"
}
response = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(response.text)

delete_endpoint = f"{url}/{username}/graphs/graph1/20240201"
response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
