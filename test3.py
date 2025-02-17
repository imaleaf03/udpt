import requests

url = "http://localhost:5000/set"
data = {"key": "user1", "value": "admin"}

response = requests.post(url, json=data)
print(response.json())  # In phản hồi từ server
response = requests.get("http://localhost:5000/get/username")
print(response.json())  # Output: {"key": "username", "value": "admin"}
