import requests

endpoint = "http://localhost:8000/api/products/4/update/"

data = {
    'title': 'History 30000',
    'price': 9
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())

