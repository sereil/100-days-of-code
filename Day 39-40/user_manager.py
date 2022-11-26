import requests
SHEETY_ENDPOINT =  "https://api.sheety.co/58abbfdbd2d6afb2cca4f68b947bffea/flightDeals/users"

class UserManager:
    def __init__(self) -> None:
        self.gather_user_info()
        
    
    def get_user_data(self):
        pass
    
    def gather_user_info(self):
        print("Welcome to Séreil's Flight Club!\r\nWe find the best flight deals for you.")
        is_new = input("Are you a new user? y/n \r\n").lower()
        if(is_new == 'y'):
            first_name = input("What is your first name?\r\n")
            last_name = input("What is your last name?\r\n")
            email = input("What is your email?\r\n")

            new_user = {
                "user":{
                    "firstName":first_name,
                    "lastName":last_name,
                    "email":email                    
                }                
            }
            
            requests.post(url=SHEETY_ENDPOINT, json=new_user)

            print("You're in the club!")
    

        
