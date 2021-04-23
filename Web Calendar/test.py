import requests

BASE = 'http://127.0.0.1:5000'

response = requests.post(BASE + '/event', {"event": "Video conference", "date": "2021-03-01"})
print(response.json())
