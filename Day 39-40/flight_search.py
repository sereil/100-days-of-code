import requests
import sys

from flight_data import FlightData

from pprint import pprint


TEQUILA_API_KEY = "Fq9BtiGbxBrfIfPMf2S374a3BSWy1KFy"
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_LOCATION = f"{TEQUILA_ENDPOINT}/locations/query/"
TEQUILA_SEARCH = f"{TEQUILA_ENDPOINT}/v2/search"

HEADER ={
        "apikey":TEQUILA_API_KEY            
        }

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.iata_codes = {}
        pass
    
    def get_iata_code(self,city_name):
        locations_query = ""
        
        
        params = {            
            "term":city_name,
            "locale":"en-US",
            "location_types":"airport"
        }
        response = requests.get(url=TEQUILA_LOCATION, params=params, headers=HEADER)
        data = response.json()["locations"]
       
        for airport in data:
            currCity = airport["city"]["name"]
            if(currCity.upper() == city_name):
                return airport["code"]
        #pprint(response.json()["locations"][1]["code"])

    def update_lowest_price(self):
        pass
        
    def search(self, home_airport, destination_airport, from_time, to_time):
        #MTL = YUL, OTT = YOW, TORONTO = YYZ
    
        search_params = {
            "fly_from":home_airport,
            "fly_to":destination_airport,
            "date_from":from_time,
            "date_to":to_time,
            "max_stopovers":2,
            "curr":"CAD"
        }
        response = requests.get(url=TEQUILA_SEARCH, params=search_params, headers=HEADER)
        data = response.json()["data"]
        lowest_price = sys.float_info.max
        lowest_price_flight = None
        try:
            for flight in data:
                if (lowest_price > float(flight["price"])):
                    lowest_price = float(flight["price"])
                    lowest_price_flight = flight            
            
            fd = FlightData(
                price=lowest_price,
                origin_city=lowest_price_flight["cityFrom"],
                origin_airport=lowest_price_flight["flyFrom"],
                destination_city=lowest_price_flight["cityTo"],
                destination_airport=lowest_price_flight["flyTo"],
                out_date=lowest_price_flight["local_departure"].split("T")[0],
                return_date=lowest_price_flight["local_departure"].split("T")[0],
                stop_overs=len(lowest_price_flight["route"]) -1,
                via_city= [layover["cityTo"]  for layover in lowest_price_flight["route"] if len(lowest_price_flight["route"]) > 1]
            )
            print(f"{fd.destination_city}: ${fd.price}(CAD)")
            if fd.stop_overs >= 1:
                layovers = " ".join(fd.via_city)
                print(f"You have {fd.stop_overs} layovers. You leave from {fd.origin_city} and have stops in {layovers}")
            return fd            
        except:
            print(f"No flight was found from {home_airport} to {destination_airport}")
            return None
        
        
        #print(f"{lowest_price_flight['cityTo']}: ${lowest_price}(CAD)")
        
