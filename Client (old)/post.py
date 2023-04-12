from requests import post
import json

url = "http://localhost:8080"
path = "/api/users"

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

data = json.dumps({
    'name': 'test123',
    'username': 'taha',
    'password': 'mtaha1387'
})

response = post(url + path, headers=headers, data=data)

print(response.text)