import requests

pet_id = 646
url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
response = requests.get(url)
print(response.json())
