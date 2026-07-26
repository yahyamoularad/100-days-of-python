"""
Day 2: Understanding Data Types and Manipulating Strings

Topics covered:
1. String subscripting
2. Strings, integers, floats, and booleans
3. Checking data types with type()
4. Type conversion
5. Mathematical operators
6. Operator precedence
7. BMI coding challenge
8. Rounding numbers
9. Assignment operators
10. f-strings
11. Tip Calculator project

Run this file from the main course folder with:

    python "Day 02 - Tip Calculator/Day_02_Complete_Revision.py"
"""


# ============================================================
# LESSON 1: STRING SUBSCRIPTING
# ============================================================

print("=== Lesson 1: String Subscripting ===")

word = "Hello"

# Indexing starts at 0.
print(word[0])   # H
print(word[4])   # o

# A negative index counts backward from the end.
print(word[-1])  # o


# ============================================================
# LESSON 2: PYTHON DATA TYPES
# ============================================================

print("\n=== Lesson 2: Data Types ===")

# String: text inside quotation marks
text_value = "123"

# Integer: a whole number
integer_value = 123

# Float: a number with a decimal point
float_value = 3.14159

# Boolean: either True or False
boolean_value = True

print(text_value)
print(integer_value)
print(float_value)
print(boolean_value)

# Underscores make large integers easier to read.
large_number = 123_456_789
print(large_number)


# ============================================================
# LESSON 3: STRINGS VERSUS NUMBERS
# ============================================================

print("\n=== Lesson 3: Strings Versus Numbers ===")

# These values are strings, so + joins them.
print("123" + "345")  # 123345

# These values are integers, so + adds them.
print(123 + 345)      # 468


# ============================================================
# LESSON 4: CHECKING DATA TYPES
# ============================================================

print("\n=== Lesson 4: Checking Data Types ===")

print(type("Python"))
print(type(100))
print(type(3.14))
print(type(False))


# ============================================================
# LESSON 5: TYPE CONVERSION
# ============================================================

print("\n=== Lesson 5: Type Conversion ===")

# int() converts a compatible value to an integer.
first_number = int("123")
second_number = int("456")
print(first_number + second_number)

# str() converts a value to a string.
age = 21
print("My age is " + str(age) + ".")

# float() converts a compatible value to a decimal number.
decimal_number = float("12.5")
print(decimal_number)

# Common conversion functions:
# int()
# float()
# str()
# bool()


# ============================================================
# CODING CHALLENGE 1: COUNT NAME CHARACTERS
# ============================================================

print("\n=== Coding Challenge 1: Name Length ===")

user_name = input("Enter your name:\n")
name_length = len(user_name)

# name_length is an integer, so str() is required when using +.
print("Number of letters in your name: " + str(name_length))


# ============================================================
# LESSON 6: MATHEMATICAL OPERATORS
# ============================================================

print("\n=== Lesson 6: Mathematical Operators ===")

print(7 + 3)   # Addition
print(7 - 3)   # Subtraction
print(7 * 3)   # Multiplication
print(7 / 3)   # Division, always returns a float
print(7 // 3)  # Floor division
print(7 % 3)   # Modulo, returns the remainder
print(7 ** 3)  # Exponentiation


# ============================================================
# LESSON 7: OPERATOR PRECEDENCE
# ============================================================

print("\n=== Lesson 7: Operator Precedence ===")

# Python follows this general order:
# 1. Parentheses
# 2. Exponents
# 3. Multiplication, division, floor division, and modulo
# 4. Addition and subtraction
#
# Operations with the same priority are normally evaluated
# from left to right.

first_result = 3 * 3 + 3 / 3 - 3
second_result = 3 * (3 + 3) / 3 - 3

print(first_result)
print(second_result)


# ============================================================
# CODING CHALLENGE 2: BMI CALCULATOR
# ============================================================

print("\n=== Coding Challenge 2: BMI Calculator ===")

height = float(input("Enter your height in metres:\n"))
weight = float(input("Enter your weight in kilograms:\n"))

bmi = weight / (height ** 2)

print(f"Your exact BMI is {bmi}.")
print(f"Your BMI rounded to the nearest whole number is {round(bmi)}.")
print(f"Your BMI rounded to two decimal places is {bmi:.2f}.")


# ============================================================
# LESSON 8: NUMBER MANIPULATION
# ============================================================

print("\n=== Lesson 8: Number Manipulation ===")

example_number = 24.806

print(int(example_number))       # Removes the decimal part
print(round(example_number))     # Rounds to the nearest integer
print(round(example_number, 2))  # Rounds to two decimal places
print(f"{example_number:.2f}")   # Displays exactly two decimal places


# ============================================================
# LESSON 9: ASSIGNMENT OPERATORS
# ============================================================

print("\n=== Lesson 9: Assignment Operators ===")

score = 0
print(score)

score += 1
print(score)

score -= 1
print(score)

score += 10
score *= 2
score /= 4

print(score)

# Common assignment operators:
# +=
# -=
# *=
# /=


# ============================================================
# LESSON 10: F-STRINGS
# ============================================================

print("\n=== Lesson 10: f-Strings ===")

player_score = 10
player_height = 1.80
is_winning = True

print(
    f"Your score is {player_score}, "
    f"your height is {player_height} metres, "
    f"and your winning status is {is_winning}."
)


# ============================================================
# DAY 2 PROJECT: TIP CALCULATOR
# ============================================================

print("\n=== Day 2 Project: Tip Calculator ===")

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15?\n")
)
number_of_people = int(input("How many people will split the bill?\n"))

tip_as_decimal = tip_percentage / 100
tip_amount = bill * tip_as_decimal
bill_with_tip = bill + tip_amount
amount_per_person = bill_with_tip / number_of_people

# :.2f ensures that money always displays two decimal places.
print(f"Each person should pay: ${amount_per_person:.2f}")


# ============================================================
# DAY 2 REVISION NOTES
# ============================================================

# A string contains text.
# An integer is a whole number.
# A float contains a decimal point.
# A boolean is either True or False.
#
# type() tells you the data type of a value.
# int(), float(), str(), and bool() convert data types.
# / returns a float, while // performs floor division.
# % returns the remainder of a division.
# ** raises a number to a power.
# round(number, digits) rounds a number.
# f-strings make it easier to combine values and text.
#
# Descriptive variable names improve readability:
#
# Good:
#     tip_percentage
#     number_of_people
#     amount_per_person
#
# Less clear:
#     t
#     n
#     x
