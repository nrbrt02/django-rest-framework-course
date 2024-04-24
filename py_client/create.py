import requests

endpoint = "http://localhost:8000/api/products/"


data = {
    'title': 'Amandazi menshi', 
    'content': 'From the bakery this is to mean ko nshojye'
}
get_responce = requests.post(endpoint, json=data)

print(get_responce.json())
# print(get_responce.json()['message'])
# print(get_responce.text)
# print(get_responce.status_code)
