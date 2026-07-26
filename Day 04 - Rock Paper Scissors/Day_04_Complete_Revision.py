"""
Day 4: Randomisation and Python Lists

Topics covered:
1. Importing Python modules
2. Importing a custom module
3. random.randint()
4. random.random()
5. random.uniform()
6. Python lists
7. List indexing
8. Changing and adding list items
9. Nested lists
10. Heads or Tails challenge
11. Banker Roulette challenge
12. Rock Paper Scissors project

Keep this file and my_module.py in the same folder.

Run this file from the main course folder with:

    python "Day 04 - Rock Paper Scissors/Day_04_Complete_Revision.py"
"""

import random
import my_module


# ============================================================
# LESSON 1: IMPORTING MODULES
# ============================================================

print("=== Lesson 1: Importing Modules ===")

# random is a module included with Python.
# my_module is a module stored in the same folder as this file.
print(f"My favourite number is {my_module.my_favourite_number}.")


# ============================================================
# LESSON 2: RANDOM INTEGERS
# ============================================================

print("\n=== Lesson 2: Random Integers ===")

# randint(a, b) includes both a and b.
random_integer = random.randint(1, 10)

print(f"Random integer from 1 to 10: {random_integer}")


# ============================================================
# LESSON 3: RANDOM FLOATING-POINT NUMBERS
# ============================================================

print("\n=== Lesson 3: Random Floats ===")

# random() returns a float where:
#     0.0 <= number < 1.0
random_number_zero_to_one = random.random()
print(
    "Random number from 0 up to, but not including, 1: "
    f"{random_number_zero_to_one}"
)

# Multiplying changes the possible range.
random_number_zero_to_ten = random.random() * 10
print(
    "Random number from 0 up to, but not including, 10: "
    f"{random_number_zero_to_ten}"
)

# uniform(a, b) returns a random float between a and b.
random_float = random.uniform(1, 10)
print(f"Random float from 1 to 10: {random_float}")


# ============================================================
# CODING CHALLENGE 1: HEADS OR TAILS
# ============================================================

print("\n=== Coding Challenge 1: Heads or Tails ===")

coin_result = random.randint(0, 1)

if coin_result == 0:
    print("Heads")
else:
    print("Tails")


# ============================================================
# LESSON 4: PYTHON LISTS
# ============================================================

print("\n=== Lesson 4: Python Lists ===")

fruits = ["Cherry", "Apple", "Pear"]

# List indexing starts at 0.
print(fruits[0])

# Negative indexing starts from the end.
print(fruits[-1])

# Replace an existing item.
fruits[2] = "Banana"

# Add a new item to the end.
fruits.append("Peach")

print(fruits)


# ============================================================
# LESSON 5: LIST LENGTH AND VALID INDEXES
# ============================================================

print("\n=== Lesson 5: List Length and Indexes ===")

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

number_of_friends = len(friends)

print(f"There are {number_of_friends} friends.")

# The final valid index is always length minus 1.
last_friend = friends[number_of_friends - 1]
print(f"The final friend is {last_friend}.")


# ============================================================
# CODING CHALLENGE 2: BANKER ROULETTE
# ============================================================

print("\n=== Coding Challenge 2: Banker Roulette ===")

# random.choice() selects one item directly from a sequence.
friend_paying = random.choice(friends)

print(f"{friend_paying} is going to buy the meal today.")


# The same challenge can also be solved using a random index:
#
# random_index = random.randint(0, len(friends) - 1)
# friend_paying = friends[random_index]
# print(f"{friend_paying} is going to buy the meal today.")


# ============================================================
# LESSON 6: NESTED LISTS
# ============================================================

print("\n=== Lesson 6: Nested Lists ===")

fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]

vegetables = [
    "Spinach",
    "Kale",
    "Tomatoes",
    "Celery",
    "Potatoes",
]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

# First list inside dirty_dozen
print(dirty_dozen[0])

# Second list inside dirty_dozen
print(dirty_dozen[1])

# Item at index 1 from the first inner list
print(dirty_dozen[0][1])

# Item at index 1 from the second inner list
print(dirty_dozen[1][1])


# ============================================================
# DAY 4 PROJECT: ROCK PAPER SCISSORS
# ============================================================

print("\n=== Day 4 Project: Rock Paper Scissors ===")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]
choice_names = ["Rock", "Paper", "Scissors"]

user_choice = int(
    input(
        "What do you choose?\n"
        "Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"
    )
)

computer_choice = random.randint(0, 2)

# Validate the user's choice before using it as a list index.
if user_choice < 0 or user_choice > 2:
    print("You entered an invalid number. You lose.")
else:
    print(f"\nYou chose {choice_names[user_choice]}:")
    print(game_images[user_choice])

    print(f"Computer chose {choice_names[computer_choice]}:")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It is a draw.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win.")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose.")
    elif user_choice > computer_choice:
        print("You win.")
    else:
        print("You lose.")


# ============================================================
# DAY 4 REVISION NOTES
# ============================================================

# A module is a Python file containing reusable code.
#
# Import a built-in or custom module with:
#
#     import module_name
#
# Access something inside it with:
#
#     module_name.variable_name
#     module_name.function_name()
#
# Common random functions:
#
#     random.randint(a, b)
#     random.random()
#     random.uniform(a, b)
#     random.choice(sequence)
#
# Lists store multiple values in one ordered collection.
#
#     items = ["first", "second", "third"]
#
# List indexes begin at 0:
#
#     items[0]
#
# A negative index counts from the end:
#
#     items[-1]
#
# Change a list item:
#
#     items[1] = "new value"
#
# Add an item:
#
#     items.append("another value")
#
# The final valid index is:
#
#     len(items) - 1
#
# A nested list contains one or more lists:
#
#     nested = [first_list, second_list]
#
# Access an inner value with two indexes:
#
#     nested[list_index][item_index]
#
# Validate a number before using it as a list index.
