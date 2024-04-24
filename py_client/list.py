import requests

endpoint = "http://localhost:8000/api/products/"



get_responce = requests.get(endpoint)

print(get_responce.json())
# print(get_responce.json()['message'])
# print(get_responce.text)
# print(get_responce.status_code)
