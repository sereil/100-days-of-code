import requests
from datetime import datetime

USERNAME = "sereilvp"
TOKEN = "QazWsx@3Edc"
pixela_endpoint = f"https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph1_endpoint = f"{graph_endpoint}/graph1"
user_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"        
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_config = {
    "id":"graph1",
    "name":"Study Graph",
    "unit":"Hours",
    "type":"float",
    "color":"sora"    
}



headers = {
    "X-USER-TOKEN":TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

yesterday = datetime(year=2022, month =11, day = 8)

graph_pixel = {
    "date":yesterday.strftime("%Y%m%d"),
    "quantity":"0.001"
    #"optionalData":{"Comment":"Currently doing this for 100 days of code so time is not accurate."} #  Doesn't work
}

# response = requests.post(url=graph1_endpoint, json=graph_pixel, headers=headers)
# print(response.text)

'''Update Yesterday'''
response = requests.put(url=f"{graph1_endpoint}/{yesterday.strftime('%Y%m%d')}", json={'quantity':'2'}, headers=headers)
print(response.text)

'''Delete Yesterday'''
response = requests.delete(url=f"{graph1_endpoint}/{yesterday.strftime('%Y%m%d')}",headers=headers)
print(response.text)