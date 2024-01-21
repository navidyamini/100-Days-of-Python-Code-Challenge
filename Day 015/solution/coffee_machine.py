from data import MENU, resources, COINS_VALUE
from art import logo


def print_report(resources_dic):
    print(f"\nWater: {resources_dic['water']}")
    print(f"Milk: {resources_dic['milk']}")
    print(f"Coffee: {resources_dic['coffee']}")
    print(f"Money: ${resources_dic['money']}\n")
    return


def check_resources(order, resources_dic):
    """Returns True when order can be made, False if ingredients are insufficient."""
    water_needed = MENU[order]['ingredients']['water']
    coffee_needed = MENU[order]['ingredients']['coffee']
    # it is possible to write this part with for loop, think about it.
    if resources_dic['water'] < water_needed:
        print("Sorry there is not enough water 😞.")
        return False
    elif resources_dic['coffee'] < coffee_needed:
        print("Sorry there is not enough coffee 😞.")
        return False
    elif order != 'espresso':
        milk_needed = MENU[order]['ingredients']['milk']
        if resources_dic['milk'] < milk_needed:
            print("Sorry there is not enough milk 😞.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins 🪙.")
    total = int(input("How many quarters? ")) * COINS_VALUE['quarters']
    total += int(input("How many dimes? ")) * COINS_VALUE['dimes']
    total += int(input("How many nickles? ")) * COINS_VALUE['nickles']
    total += int(input("How many pennies? ")) * COINS_VALUE['pennies']
    return total


def check_transaction(order, money):
    """Return True when the payment is accepted, or False if money is insufficient."""
    money_needed = MENU[order]['cost']
    if money < money_needed:
        print("Sorry that's not enough money 😞. Money refunded 🪙.")
        return False, 0
    elif money == money_needed:
        return True, money_needed
    else:
        change = round(money - money_needed, 2)
        print(f"Here is ${change} dollars in change 🪙.")
        return True, money_needed


def make_coffee(order, resource):
    """Deduct the required ingredients from the resources."""
    resource["water"] -= MENU[order]['ingredients']['water']
    resource["coffee"] -= MENU[order]['ingredients']['coffee']
    if order != 'espresso':
        resource["milk"] -= MENU[order]['ingredients']['milk']
    print(f"Here is your {order}☕️. Enjoy!")
    return resource


def coffee_machine():
    print(logo)
    is_on = True
    machine_resources = resources
    machine_resources['money'] = 0
    while is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == 'off':
            is_on = False
        elif order == 'report':
            print_report(machine_resources)
        else:
            sufficient_resources = check_resources(order, machine_resources)
            if sufficient_resources:
                money = process_coins()
                enough_money, money_added = check_transaction(order, money)
                if enough_money:
                    machine_resources['money'] += money_added
                    machine_resources = make_coffee(order, machine_resources)


coffee_machine()
