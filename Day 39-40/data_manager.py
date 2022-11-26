import requests
from flight_search import FlightSearch
from pprint import pprint

SHEETY_ENDPOINT =  "https://api.sheety.co/58abbfdbd2d6afb2cca4f68b947bffea/flightDeals/prices"


class DataManager:
    
    def __init__(self) -> None:
        self.destination_data = self.get_destination_data()                
    
    
    def get_destination_data(self):        
        sheet_data = requests.get(url=SHEETY_ENDPOINT)
        self.destination_data = sheet_data.json()["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        fs = FlightSearch()
        
        for city in self.destination_data:
            print(city["city"])
            new_data = {
                "price": {
                    "iataCode": fs.get_iata_code(city["city"].upper())
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
            
    def update_lowest_prices(self):
        fs = FlightSearch()
        for destination in self.destination_data:
            fs.search(home_airport="YYZ",destination_airport=destination["iataCode"])
        