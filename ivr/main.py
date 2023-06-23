import requests
import json

url = "https://stream-backend-preprod-pub.voicese.in/sv/justdial/v1/generate_token/"

headers = {"Content-Type": "application/json", "Authorization": "Api-Key BlCszf5LFnkABwiKCtuZsogiJb0GMycu0G6HPzUD"}

data = {
	"user_id": "9164186611",
	"name": "vivek",
	"amount": "145.66",
	"language": "hindi"
}

response = requests.post(url, headers=headers, json=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())
