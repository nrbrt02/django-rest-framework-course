import requests

# # endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_responce = requests.post(endpoint, json=({"title": "ABC 123", "content": "Hello world"}))

print(get_responce.json())
# print(get_responce.json()['message'])
# print(get_responce.text)
# print(get_responce.status_code)
