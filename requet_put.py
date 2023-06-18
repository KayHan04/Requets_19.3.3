import requests
import json

username = 'Vega'

url = (f"https://petstore.swagger.io/#/user/updateUser'{username}"),

headers = {
    'accept': 'application/json',
    'auth_key': 'key',
    'Content-Type': 'application/json'}

data = {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}

response = requests.put(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())
