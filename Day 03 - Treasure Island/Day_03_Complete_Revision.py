"""
Day 3: Control Flow and Logical Operators

Topics covered:
1. if and else statements
2. Comparison operators
3. The difference between = and ==
4. The modulo operator
5. Nested if statements
6. if, elif, and else
7. Multiple independent if statements
8. Logical operators: and, or, and not
9. Rollercoaster ticket challenge
10. Even or odd challenge
11. BMI classification challenge
12. Pizza order challenge
13. Treasure Island project

Run this file from the main course folder with:

    python "Day 03 - Treasure Island/Day_03_Complete_Revision.py"
"""


# ============================================================
# LESSON 1: BASIC IF AND ELSE
# ============================================================

print("=== Lesson 1: Basic if and else ===")

height = int(input("What is your height in centimetres?\n"))

# The rider must be at least 120 cm tall.
if height >= 120:
    print("You can ride the rollercoaster.")
else:
    print("You must grow taller before you can ride.")


# ============================================================
# LESSON 2: COMPARISON OPERATORS
# ============================================================

print("\n=== Lesson 2: Comparison Operators ===")

# >   Greater than
# <   Less than
# >=  Greater than or equal to
# <=  Less than or equal to
# ==  Equal to
# !=  Not equal to
#
# = assigns a value to a variable.
# == compares two values.

example_age = 18

print(example_age > 12)
print(example_age < 12)
print(example_age >= 18)
print(example_age <= 18)
print(example_age == 18)
print(example_age != 18)


# ============================================================
# CODING CHALLENGE 1: EVEN OR ODD
# ============================================================

print("\n=== Coding Challenge 1: Even or Odd ===")

number_to_check = int(input("Enter a whole number:\n"))

# % returns the remainder after division.
# An even number leaves a remainder of 0 when divided by 2.
if number_to_check % 2 == 0:
    print(f"{number_to_check} is even.")
else:
    print(f"{number_to_check} is odd.")


# ============================================================
# LESSON 3: NESTED IF STATEMENTS
# ============================================================

print("\n=== Lesson 3: Nested if Statements ===")

rider_height = int(input("What is your height in centimetres?\n"))

if rider_height >= 120:
    print("You can ride the rollercoaster.")

    rider_age = int(input("What is your age?\n"))

    if rider_age <= 12:
        print("Your ticket costs $5.")
    elif rider_age <= 18:
        print("Your ticket costs $7.")
    else:
        print("Your ticket costs $12.")
else:
    print("You must grow taller before you can ride.")


# ============================================================
# CODING CHALLENGE 2: BMI CLASSIFICATION
# ============================================================

print("\n=== Coding Challenge 2: BMI Classification ===")

weight = float(input("Enter your weight in kilograms:\n"))
height_in_metres = float(input("Enter your height in metres:\n"))

bmi = weight / (height_in_metres ** 2)

if bmi >= 25:
    bmi_category = "overweight"
elif bmi >= 18.5:
    bmi_category = "normal weight"
else:
    bmi_category = "underweight"

print(f"Your BMI is {bmi:.2f}.")
print(f"Your BMI category is {bmi_category}.")


# ============================================================
# LESSON 4: MULTIPLE INDEPENDENT IF STATEMENTS
# ============================================================

print("\n=== Lesson 4: Multiple if Statements ===")

visitor_height = int(input("What is your height in centimetres?\n"))
bill = 0

if visitor_height >= 120:
    print("You can ride the rollercoaster.")

    visitor_age = int(input("What is your age?\n"))

    if visitor_age <= 12:
        bill = 5
        print("Child tickets cost $5.")
    elif visitor_age <= 18:
        bill = 7
        print("Youth tickets cost $7.")
    else:
        bill = 12
        print("Adult tickets cost $12.")

    wants_photo = input(
        "Would you like a photo? Type 'y' for yes or 'n' for no.\n"
    ).lower()

    # This is a separate if statement because the photo is optional
    # for every eligible rider.
    if wants_photo == "y":
        bill += 3

    print(f"Your final bill is ${bill}.")
else:
    print("You must grow taller before you can ride.")


# ============================================================
# CODING CHALLENGE 3: PYTHON PIZZA DELIVERY
# ============================================================

print("\n=== Coding Challenge 3: Python Pizza Delivery ===")

print("Welcome to Python Pizza Deliveries!")

pizza_size = input("What size pizza would you like? S, M, or L:\n").upper()
wants_pepperoni = input("Would you like pepperoni? Y or N:\n").upper()
wants_extra_cheese = input("Would you like extra cheese? Y or N:\n").upper()

pizza_bill = 0
valid_size = True

if pizza_size == "S":
    pizza_bill = 15
elif pizza_size == "M":
    pizza_bill = 20
elif pizza_size == "L":
    pizza_bill = 25
else:
    valid_size = False
    print("You entered an invalid pizza size.")

if valid_size:
    if wants_pepperoni == "Y":
        if pizza_size == "S":
            pizza_bill += 2
        else:
            pizza_bill += 3

    if wants_extra_cheese == "Y":
        pizza_bill += 1

    print(f"Your final pizza bill is ${pizza_bill}.")


# ============================================================
# LESSON 5: LOGICAL OPERATORS
# ============================================================

print("\n=== Lesson 5: Logical Operators ===")

# and is True only when both conditions are True.
# or is True when at least one condition is True.
# not reverses a Boolean value.

temperature = 24
is_sunny = True

print(temperature > 20 and is_sunny)
print(temperature < 10 or is_sunny)
print(not is_sunny)


# ============================================================
# CODING CHALLENGE 4: ROLLERCOASTER WITH A FREE-RIDE RULE
# ============================================================

print("\n=== Coding Challenge 4: Rollercoaster Final Version ===")

customer_height = int(input("What is your height in centimetres?\n"))
final_bill = 0

if customer_height >= 120:
    print("You can ride the rollercoaster.")

    customer_age = int(input("What is your age?\n"))

    if customer_age <= 12:
        final_bill = 5
        print("Child tickets cost $5.")
    elif customer_age <= 18:
        final_bill = 7
        print("Youth tickets cost $7.")
    elif 45 <= customer_age <= 55:
        final_bill = 0
        print("Your ride is free today.")
    else:
        final_bill = 12
        print("Adult tickets cost $12.")

    customer_wants_photo = input(
        "Would you like a photo? Type 'y' for yes or 'n' for no.\n"
    ).lower()

    if customer_wants_photo == "y":
        final_bill += 3

    print(f"Your final bill is ${final_bill}.")
else:
    print("You must grow taller before you can ride.")


# ============================================================
# DAY 3 PROJECT: TREASURE ISLAND
# ============================================================

print("\n=== Day 3 Project: Treasure Island ===")

print(
    """
          __________
         /\\____;;___\\
        | /         /
        `. ())oo() .
         |\\(%()*^^()^\\
        %| |-%-------|
       % \\ | %  ))   |
       %  \\|%________|
    """
)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_choice = input(
    'You are at a crossroads. Type "left" or "right".\n'
).lower()

if first_choice == "left":
    second_choice = input(
        'You have reached a lake. Type "wait" for a boat or "swim" across.\n'
    ).lower()

    if second_choice == "wait":
        third_choice = input(
            "You reach a house with three doors. "
            'Choose "red", "yellow", or "blue".\n'
        ).lower()

        if third_choice == "red":
            print("The room is full of fire. Game over.")
        elif third_choice == "yellow":
            print("You found the treasure. You win!")
        elif third_choice == "blue":
            print("You enter a room full of beasts. Game over.")
        else:
            print("That door does not exist. Game over.")
    elif second_choice == "swim":
        print("You are attacked by an angry trout. Game over.")
    else:
        print("That is not a valid choice. Game over.")
elif first_choice == "right":
    print("You fall into a hole. Game over.")
else:
    print("That is not a valid direction. Game over.")


# ============================================================
# DAY 3 REVISION NOTES
# ============================================================

# if runs code only when its condition is True.
# else runs when the preceding condition is False.
# elif checks another condition when earlier conditions were False.
#
# Nested conditionals are if statements inside other if statements.
#
# Use multiple independent if statements when more than one action
# may need to happen.
#
# = assigns a value.
# == checks whether two values are equal.
# != checks whether two values are different.
# % returns the remainder after division.
#
# Logical operators:
#     A and B
#     A or B
#     not A
#
# String methods such as lower() return a new string.
# Save the returned value or call the method directly on input():
#
# Correct:
#     choice = input("Choose: ").lower()
#
# Also correct:
#     choice = input("Choose: ")
#     choice = choice.lower()
#
# Incorrect:
#     choice = input("Choose: ")
#     choice.lower()
#
# The incorrect version does not replace the original value.
