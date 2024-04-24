import requests

endpoint = "http://localhost:8000/api/products/3/delete/"


get_response = requests.delete(endpoint)

# print(get_responce.json())
print(get_response.status_code,get_response.status_code==204 )
# print(get_responce.json()['message'])
# print(get_responce.text)
# print(get_responce.status_code)
