import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Updated Title",
    "price": 150.00
}

get_responce = requests.put(endpoint, json=data)

print(get_responce.json())
# print(get_responce.json()['message'])
# print(get_responce.text)
# print(get_responce.status_code)
