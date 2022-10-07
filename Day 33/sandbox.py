import requests
import pandas


response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.content)

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude,latitude)

print(iss_position)
