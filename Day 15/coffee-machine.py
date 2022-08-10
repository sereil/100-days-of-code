from tabnanny import check
from tkinter import OFF
from menu import MENU, resources
from os import system

def clear():
    system("cls")

def turn_off_machine():
    print("Goodbye.")
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
    print(f"Here is your {drink}. Enjoy!")

def store_coins(money):
    if "money" in resources.keys():
        resources["money"] += money
    else:
        resources.update({"money": money})
        
        
def add_coins():
    sum_money = 0
    keep_adding = True    
    
    coin_value= {
        "quarter": 0.25,
        "dime": 0.10,
        "nickel": 0.05,
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
    drink_cost = MENU[drink]["cost"]
    print(f"Please insert ${drink_cost}")
    money = add_coins()
    
    if money == drink_cost:
        store_coins(drink)
    elif money > drink_cost:
        difference = money - drink_cost
        difference = round(difference,2)
        print(f"Here's ${difference} dollars in change.")
        store_coins(drink_cost)
    elif money < drink_cost:
        print("Sorry, that is not enough money. Money refunded.")
        return False    
    return True
    
def turn_on_machine():
    generate_report()
    #Just in case someone ever looks at this and is confused why there's an infinite loop.
    print("Type 'off' if you wish to turn off the machine.")
    order = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    clear()
    
    if order == "off":
        turn_off_machine()
    elif order == "report":
        generate_report()
    else:
        if not check_resources(order):
            turn_on_machine()
        else:
            if process_coins(order):
                take_resources(order)
                turn_on_machine()
        

turn_on_machine()



