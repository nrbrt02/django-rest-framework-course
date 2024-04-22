import requests

# # endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_responce = requests.get(endpoint, json=({"Name":"Mwiseneza"}))

print(get_responce.json())
# print(get_responce.json()['message'])
# print(get_responce.text)
# print(get_responce.status_code)
