#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from user_manager import UserManager
from notification_manager import NotificationManager
from datetime import date
from dateutil.relativedelta import relativedelta
import os
from twilio.rest import Client


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

user_manager = UserManager() 

ORIGIN_CITY_IATA = "YYZ"

TWIL_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWIL_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])        
       
        
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

today = date.today()
fToday = today.strftime("%d/%m/%Y")
tomorrow = today + relativedelta(days=+1)
fTomorrow = tomorrow.strftime("%d/%m/%Y")

sixmonths = today + relativedelta(months=+6)       
fSixmonths = sixmonths.strftime("%d/%m/%Y")



for destination in sheet_data:
    flight = flight_search.search(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=fTomorrow,
        to_time=fSixmonths
    )
    if (flight.price < destination["lowestPrice"]):
        nm = NotificationManager()
        message=f"Low price alert! Only ${flight.price}CAD to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."        
        nm.send_notification(message)        
        
    



