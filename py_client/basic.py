import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={
    "title": "ABC",
    "content": "Danh",
})

# print(get_response.text)
print(get_response.json())
