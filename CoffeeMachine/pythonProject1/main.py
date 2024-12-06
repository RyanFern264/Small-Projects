from itertools import filterfalse
from platform import machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def user_choice(choice):
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if handle_resources(choice):
            handle_money(choice)
        return True
    elif choice == "report":
        print_report()
        return True
    elif choice == "off":
        return False
    else:
        print("Please enter a valid option")
        return True

def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")

def handle_resources(choice):
    sufficient_resources = True
    for item in MENU[choice]["ingredients"]:
        if resources[item] < MENU[choice]["ingredients"][item]:
            print(f"Sorry, theres not enough {item}")
            sufficient_resources = False
    if sufficient_resources:
        for item in MENU[choice]["ingredients"]:
            resources[item] -= MENU[choice]["ingredients"][item]
    return sufficient_resources

def handle_money(choice):
    print(f"A {choice} costs ${MENU[choice]['cost']}")
    print("Please insert coins.")
    total_inserted = int(input("How many quarters?: ")) * 0.25
    total_inserted += int(input("How many dimes?: ")) * 0.1
    total_inserted += int(input("How many niggles?: ")) * 0.05
    total_inserted += int(input("How many pennies?: ")) * 0.01
    cost_of_item = float(MENU[choice]["cost"])
    print(f"You inserted ${total_inserted}")
    if total_inserted < cost_of_item:
        print("You didn't insert enough coinz. Broke nigga detected. This incident has been logged.")
        handle_money(choice)
    elif total_inserted >= cost_of_item:
        change = total_inserted - cost_of_item
        resources["money"] += cost_of_item
        print(f"Your change is ${change}")
        print(f"Here is your {choice}. Enjoy! ")

machine_power = True
print("いらっしゃいませ!")
while machine_power:
    menu_choice = input("What would you like? (espresso/latte/cappuccino): ")
    machine_powered = user_choice(menu_choice)
    if not machine_powered:
        machine_power = False


'''
sections that were improved after watching solution:
    RESOURCE HANDLING
    water_cost = MENU[choice]["ingredients"]["water"]
    sufficient_resources = True
    if resources["water"] < water_cost:
        print("Sorry, there's not enough water")
        sufficient_resources = False
    elif resources["water"] >= water_cost:
        resources["water"] -= water_cost

    try:
        milk_cost = MENU[choice]["ingredients"]["milk"]
        if resources["milk"] < milk_cost:
            print("Sorry, there's not enough milk")
            sufficient_resources = False
        elif resources["milk"] >= milk_cost:
            resources["milk"] -= milk_cost
    except KeyError:
        pass

    coffee_cost = MENU[choice]["ingredients"]["coffee"]
    if resources["coffee"] < coffee_cost:
        print("Sorry, there's not enough coffee")
        sufficient_resources = False
    elif resources["coffee"] >= coffee_cost:
        resources["coffee"] -= coffee_cost
    return sufficient_resources
    
    COST HANDLING
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many niggles?: "))
    pennies = int(input("How many pennies?: "))
    total_inserted = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
'''