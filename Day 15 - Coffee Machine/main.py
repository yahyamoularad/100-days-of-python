# Day 15: Coffee Machine
# Final project version
#
# This file keeps Angela's final project structure and logic.
# Only explanatory comments have been added.
#
# Main concepts used:
# - Nested dictionaries
# - Functions with parameters
# - Functions with return values
# - while loops
# - for loops
# - if / elif / else
# - Boolean values
# - global variables
# - round()
# - Updating dictionary values
#
# ------------------------------------------------------------
# 1. MENU DATA
# ------------------------------------------------------------
# MENU stores every drink.
# Each drink contains:
# - ingredients needed
# - cost of the drink
#
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

# ------------------------------------------------------------
# 2. MACHINE RESOURCES
# ------------------------------------------------------------
# resources stores the current amount of water, milk, and coffee.
# These values decrease whenever a drink is made.

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# ------------------------------------------------------------
# 3. MACHINE PROFIT
# ------------------------------------------------------------
# profit stores the money earned from successful transactions.

profit = 0

# ------------------------------------------------------------
# 4. CHECK AVAILABLE RESOURCES
# ------------------------------------------------------------
# This function receives the ingredient dictionary for the selected drink.
# It checks each ingredient against the machine resources.

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# ------------------------------------------------------------
# 5. PROCESS COINS
# ------------------------------------------------------------
# This function asks how many coins were inserted
# and returns their total monetary value.

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins. ")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# ------------------------------------------------------------
# 6. CHECK THE TRANSACTION
# ------------------------------------------------------------
# This function compares the money received with the drink cost.
# If payment is sufficient, it calculates change and adds the cost
# of the drink to profit.

def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# ------------------------------------------------------------
# 7. MAKE THE COFFEE
# ------------------------------------------------------------
# This function deducts the selected drink ingredients
# from the machine resources.

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


# ------------------------------------------------------------
# 8. MAIN MACHINE LOOP
# ------------------------------------------------------------
# The machine keeps asking for another order while is_on is True.
# "off" stops the program.
# "report" prints the current resources and profit.
# Otherwise, the selected drink is processed.

is_on = True

while is_on: 
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else: 
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])