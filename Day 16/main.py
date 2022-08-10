from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:    
    items = menu.get_items()
    order = input(f"What would you like? {items}: ").lower()

    if order == "off":
        print("Shutting down... Goodbye.")
        exit
    elif order == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        order_item = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(order_item) and money_machine.make_payment(order_item.cost):
                coffee_machine.make_coffee(order_item)

