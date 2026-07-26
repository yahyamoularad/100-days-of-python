"""
Day 5: Python Loops

Topics covered:
1. for loops with lists
2. Indentation inside loops
3. Calculating totals manually
4. Finding the maximum value manually
5. Using range()
6. Gauss's sum from 1 to 100
7. FizzBuzz challenge
8. Easy password generator
9. Hard password generator

Run this file from the main course folder with:

    python "Day 05 - Password Generator/Day_05_Complete_Revision.py"
"""

import random


# ============================================================
# LESSON 1: FOR LOOPS WITH LISTS
# ============================================================

print("=== Lesson 1: for Loops with Lists ===")

fruits = ["Apple", "Peach", "Pear"]

# On each loop, fruit receives one item from the fruits list.
for fruit in fruits:
    print(fruit)
    print(f"{fruit} pie")

# This line is outside the loop because it is not indented.
print("The fruit loop has finished.")


# ============================================================
# LESSON 2: CALCULATING A TOTAL
# ============================================================

print("\n=== Lesson 2: Calculating a Total ===")

student_scores = [
    150,
    142,
    185,
    120,
    171,
    184,
    149,
    24,
    59,
    68,
    199,
    78,
    65,
    89,
    86,
    55,
    91,
    64,
    89,
]

# Python can calculate the total directly with sum().
total_using_sum = sum(student_scores)
print(f"Total using sum(): {total_using_sum}")

# The same calculation can be written manually with a loop.
manual_total = 0

for score in student_scores:
    manual_total += score

print(f"Total calculated manually: {manual_total}")


# Avoid using a variable named sum:
#
#     sum = 0
#
# That name would replace access to Python's built-in sum() function
# inside the current program. A name such as manual_total is clearer.


# ============================================================
# LESSON 3: FINDING THE HIGHEST VALUE
# ============================================================

print("\n=== Lesson 3: Finding the Highest Value ===")

# Python can find the largest value directly with max().
highest_using_max = max(student_scores)
print(f"Highest score using max(): {highest_using_max}")

# Manual version using a loop:
highest_score = student_scores[0]

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"Highest score calculated manually: {highest_score}")


# Starting with student_scores[0] is safer than always starting at 0.
# It still works if the list contains only negative values.


# ============================================================
# LESSON 4: USING RANGE()
# ============================================================

print("\n=== Lesson 4: range() ===")

# range(start, stop) includes start but excludes stop.
for number in range(1, 6):
    print(number)

# This prints:
# 1
# 2
# 3
# 4
# 5


# range(start, stop, step) can use a custom step.
print("Counting by 2:")

for number in range(2, 11, 2):
    print(number)


# ============================================================
# CODING CHALLENGE 1: GAUSS'S SUM
# ============================================================

print("\n=== Coding Challenge 1: Sum from 1 to 100 ===")

gauss_total = 0

# The stop value must be 101 because 101 is excluded.
for number in range(1, 101):
    gauss_total += number

print(f"The sum of the numbers from 1 to 100 is {gauss_total}.")


# The mathematical formula for this sum is:
#
#     n * (n + 1) / 2
#
# For n = 100:
#
#     100 * 101 / 2 = 5050


# ============================================================
# CODING CHALLENGE 2: FIZZBUZZ
# ============================================================

print("\n=== Coding Challenge 2: FizzBuzz ===")

for number in range(1, 101):
    # Check divisibility by both 3 and 5 first.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# The order matters.
#
# If divisibility by 3 were checked first, then 15 would print
# "Fizz" and Python would never reach the "FizzBuzz" condition.


# ============================================================
# DAY 5 PROJECT: PYPASSWORD GENERATOR
# ============================================================

print("\n=== Day 5 Project: PyPassword Generator ===")

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")

number_of_letters = int(
    input("How many letters would you like in your password?\n")
)
number_of_symbols = int(
    input("How many symbols would you like?\n")
)
number_of_numbers = int(
    input("How many numbers would you like?\n")
)


# ============================================================
# PROJECT VERSION 1: EASY LEVEL
# ============================================================

print("\n--- Easy password ---")

# The easy version keeps all character types grouped together.
easy_password = ""

for _ in range(number_of_letters):
    easy_password += random.choice(letters)

for _ in range(number_of_symbols):
    easy_password += random.choice(symbols)

for _ in range(number_of_numbers):
    easy_password += random.choice(numbers)

print(f"Easy password: {easy_password}")


# The variable name _ means that the loop number itself is not used.
#
# This:
#
#     for _ in range(3):
#
# means:
#
#     Repeat the indented code three times.


# ============================================================
# PROJECT VERSION 2: HARD LEVEL
# ============================================================

print("\n--- Hard password ---")

# The hard version first stores each character in a list.
password_characters = []

for _ in range(number_of_letters):
    password_characters.append(random.choice(letters))

for _ in range(number_of_symbols):
    password_characters.append(random.choice(symbols))

for _ in range(number_of_numbers):
    password_characters.append(random.choice(numbers))

print(f"Before shuffling: {password_characters}")

# shuffle() changes the order of the original list.
random.shuffle(password_characters)

print(f"After shuffling:  {password_characters}")

# Join the list items into one string.
hard_password = ""

for character in password_characters:
    hard_password += character

print(f"Your generated password is: {hard_password}")


# A shorter way to combine the characters would be:
#
#     hard_password = "".join(password_characters)
#
# The loop version is kept here because loops are the main Day 5 lesson.


# ============================================================
# DAY 5 REVISION NOTES
# ============================================================

# A for loop repeats code for every item in a sequence:
#
#     for item in items:
#         print(item)
#
# Indented code belongs to the loop.
# Non-indented code runs after the loop.
#
# range(start, stop) includes start but excludes stop.
#
#     range(1, 6)
#
# produces:
#
#     1, 2, 3, 4, 5
#
# range(start, stop, step) changes the increment:
#
#     range(2, 11, 2)
#
# produces:
#
#     2, 4, 6, 8, 10
#
# Useful list operations from this project:
#
#     random.choice(items)
#     items.append(value)
#     random.shuffle(items)
#     "".join(items)
#
# random.choice() returns one random item.
# append() adds one item to the end of a list.
# shuffle() changes the order of a list in place.
# join() combines strings from a list into one string.
#
# FizzBuzz must check divisibility by both 3 and 5 first.
#
# Use descriptive variable names:
#
# Good:
#     number_of_letters
#     password_characters
#     highest_score
#
# Less clear:
#     nr_letters
#     chars
#     x
