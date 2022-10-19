# import requests


# #https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
# #One Call 3.0 Subscription is not free anymore, using 4 DAY forecast instead:
# #https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={API key}
# API_KEY = '42d9785b1d32c20726f87ea8c66d0d06'
# MY_LAT = 45.476543
# MY_LONG = -75.701271

# OWM_Endpoint="https://api.openweathermap.org/data/2.5/onecall?"

# parameters ={
#     'lat':MY_LAT,
#     'lon':MY_LONG,
#     'appid':API_KEY    
# }

# response = requests.get(url=OWM_Endpoint, params=parameters)
# response.raise_for_status()
# data =response.json()

# print(data)


import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
  body='Hi there with environment tokens!',
  from_='+13143508974',
  to='+18199685073'
)

print(message.sid)