import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'History Wto',
    'price': 67
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())

