from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

print(logo)
is_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ").lower()
    if order == 'off':
        is_on = False
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        sufficient_resources = coffee_maker.is_resource_sufficient(drink)
        if sufficient_resources:
            enough_money = money_machine.make_payment(drink.cost)
            if enough_money:
                coffee_maker.make_coffee(drink)
