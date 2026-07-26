"""
Day 1: Working with Variables in Python

Topics covered:
1. Printing text with print()
2. Creating strings
3. Printing text on multiple lines with \n
4. Joining strings with +
5. Getting user input with input()
6. Storing information in variables
7. Counting characters with len()
8. Building the Band Name Generator project

Run this file from the terminal with:

    python Day_01_Complete_Revision.py
"""


# ============================================================
# LESSON 1: PRINTING TEXT
# ============================================================

print("=== Lesson 1: Printing Text ===")

# Text written inside quotation marks is called a string.
print("Hello World!")


# ============================================================
# LESSON 2: NEW LINES
# ============================================================

print("\n=== Lesson 2: New Lines ===")

# \n starts a new line inside a string.
print("Hello World!\nHello World!\nHello World!")


# ============================================================
# LESSON 3: STRING CONCATENATION
# ============================================================

print("\n=== Lesson 3: Joining Strings ===")

# The + operator joins strings together.
# Spaces must be added manually when concatenating strings.
first_name = "Yahya"
last_name = "Moularad"

print(first_name + " " + last_name)


# ============================================================
# LESSON 4: USER INPUT
# ============================================================

print("\n=== Lesson 4: User Input ===")

# input() pauses the program and waits for the user to type.
# The value returned by input() is stored in the variable user_name.
user_name = input("What is your name?\n")

print("Hello " + user_name + "!")


# ============================================================
# CODING CHALLENGE 1: COUNT THE CHARACTERS
# ============================================================

print("\n=== Coding Challenge: Name Length ===")

# len() returns the number of characters in a string.
# Spaces are also counted as characters.
name_to_measure = input("Enter a name and I will count its characters:\n")
name_length = len(name_to_measure)

print("The number of characters is:")
print(name_length)


# A shorter version of the same challenge would be:
#
# print(len(input("What is your name?\n")))
#
# The version using variables is easier to read, understand, and debug.


# ============================================================
# DAY 1 PROJECT: BAND NAME GENERATOR
# ============================================================

print("\n=== Day 1 Project: Band Name Generator ===")

print("Welcome to the Band Name Generator.")

city_name = input("What is the name of the city you grew up in?\n")
pet_name = input("What is your pet's name?\n")

band_name = city_name + " " + pet_name

print("Your band name could be " + band_name + ".")


# ============================================================
# DAY 1 REVISION NOTES
# ============================================================

# print() displays information on the screen.
# input() collects text entered by the user.
# A variable stores a value so it can be reused later.
# len() counts the characters in a string.
# + joins strings together.
# \n creates a new line.
#
# Good variable names describe the information they contain:
#
# Good:
#     city_name
#     pet_name
#     name_length
#
# Less clear:
#     c
#     p
#     x
