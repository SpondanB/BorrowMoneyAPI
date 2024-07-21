import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"likes": 1234, "name": "Hello Youtube", "views": 20345})
print(response.json())

input()

response = requests.get(BASE + "video/1")
print(response.json())
