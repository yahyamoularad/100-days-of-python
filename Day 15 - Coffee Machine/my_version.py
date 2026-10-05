# Day 15: Coffee Machine
# My original version
#
# This file is your original Day 15 version, uncommented.
# The program logic is preserved as you wrote it.
# Comments have been added only to make the structure easier to revise.
#
# ------------------------------------------------------------
# MENU AND STARTING RESOURCES
# ------------------------------------------------------------
# My version :
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
}
money = 0.0
resources["money"] = 0

# ------------------------------------------------------------
# CHECK RESOURCES
# ------------------------------------------------------------
# Checks the current machine resources before continuing.

def check_resources():
    if resources["water"] < MENU["espresso"]["ingredients"]["water"] or resources["water"] < MENU["latte"]["ingredients"]["water"] or resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
        return print("Sorry there is not enough water.")
    elif resources["milk"] < MENU["latte"]["ingredients"]["milk"] or resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
        return print("Sorry there is not enough milk.")
    elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"] or resources["coffee"] < MENU["latte"]["ingredients"]["coffee"] or resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
        return print("Sorry there is not enough coffee.")


# ------------------------------------------------------------
# PROCESS COINS
# ------------------------------------------------------------
# Calculates the inserted coin value and returns the result
# based on the selected drink.

def process_coins(q,d,n,p,variant):
    money = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
    if variant == "espresso":
        return money - 1.5
    elif variant == "latte":
        return money - 2.5
    elif variant == "cappuccino":
        return money - 3.0
    
    


# ------------------------------------------------------------
# MAIN MACHINE LOOP
# ------------------------------------------------------------
# Keeps the coffee machine running until the user enters "off".

is_on = True 
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}ml")
        print(f"Money: {resources["money"]}$")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        check_resources()
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: ")) 
        nickles = int(input("how many nickles?: "))  
        pennies = int(input("how many pennies?: "))
        money = process_coins(q=quarters,d=dimes,n=nickles,p=pennies,variant=choice)

        if choice == "espresso":
            if money < MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:    
                print(f"Here is ${money:.2f} in change.")
                print("Here is your espresso ☕️. Enjoy!")
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                resources["money"] += MENU["espresso"]["cost"]
        elif choice == "latte":
            if money < MENU["latte"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${money:.2f} in change.")
                print("Here is your latte ☕️. Enjoy!")
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["money"] += MENU["latte"]["cost"]
        elif choice == "cappuccino":
            if money < MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${money:.2f} in change.")
                print("Here is your cappuccino ☕️. Enjoy!")
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["money"] += MENU["cappuccino"]["cost"]
