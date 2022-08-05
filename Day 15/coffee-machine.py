from menu import MENU, resources

order = input("What would you like? (Espresso/Latte/Capuccino): ").lower()

def turn_off():
    exit

    
def generate_report():
    for ingredient in resources:
        measurement = resources[ingredient]
        if ingredient == "water" or ingredient == "milk":
            measurement = f"{measurement}ml"
        elif ingredient == "coffee":
            measurement = f"{measurement}g"
        elif ingredient == "money":
            measurement = f"${measurement}"
            
        resources[ingredient]
        print(f"{ingredient.title()}: {measurement}")


        
def check_resources(drink):
    drink_cost = MENU[drink]["ingredients"]
    for ingredient in drink_cost:    
        if drink_cost[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True
    
    
def take_resources(drink):    
    drink_cost = MENU[drink]["ingredients"]
    for ingredient in drink_cost:
        print(ingredient)
        resources[ingredient] -= drink_cost[ingredient]

def add_coins():
    sum_money = 0
    keep_adding = True    
    
    coin_value= {
        "quarter": 0.25,
        "dime": 0.10,
        "nickels": 0.05,
        "penny": 0.01                
    }
        
    while keep_adding:
        coin_inserted = input("Insert a coin (Quarter, Dime, Nickel, Penny): ").lower()
        amount_inserted = int(input(f"How many {coin_inserted} did you insert?: ").lower())
        sum_money += coin_value[coin_inserted] * amount_inserted
        
        print(f"Balance: {sum_money}")
        keep_inserting = input("Do you want to keep inserting? Type 'y' or 'n': ").lower()
        
        if keep_inserting == 'y':
            keep_adding = True
        elif keep_inserting == 'n':
            keep_adding = False
            return sum_money
  
def process_coins(drink):
    money = add_coins()
    drink_cost = MENU[drink]["cost"]
    if money == drink_cost:
        print("No change")
    elif money > drink_cost:
        print("Change to be given")
    elif money < drink_cost:
        print("Sorry, that is not enough money. Money refunded.")
    
        
    
        
        
process_coins(order)
#def process_coin()
    



