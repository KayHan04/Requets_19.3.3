import requests

url = 'https://petstore.swagger.io/v2/user'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

data = {
    "id": 6461,
    "username": "Vega",
    "firstName": "boba",
    "lastName": "biba",
    "email": "876@.ru",
    "password": "09867567",
    "phone": "893756",
    "userStatus": 0
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())