# Day 10: Functions with Outputs
#
# Topics included:
# 1. Returning values from functions
# 2. Saving a returned value in a variable
# 3. Using one function inside another function
# 4. Returning early when input is invalid
# 5. Docstrings
# 6. Storing functions inside a dictionary
# 7. Leap Year coding challenge
# 8. Calculator final project
#
# The Leap Year challenge and Calculator project are kept exactly
# as written in the original Day 10 file.


# ============================================================
# LESSON 1: A FUNCTION WITH OUTPUT
# ============================================================

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("yaHyA", "MoUlaRAD"))


# ============================================================
# LESSON 2: USING ONE FUNCTION INSIDE ANOTHER
# ============================================================

def function_1(text):
    return text + text


def function_2(text):
    return text.title()


out_put = function_2(function_1("hello"))
print(out_put)


# ============================================================
# LESSON 3: RETURNING EARLY
# ============================================================

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(
    format_name(
        input("What is your first name?"),
        input("What is your last name")
    )
)


# ============================================================
# CODING CHALLENGE: LEAP YEAR
# ============================================================

#coding challenge Leap year: 

# def is_leap_year(year):
#     if year % 4 == 0 :
#         if year % 100 == 0: 
#             if year % 400 == 0:
#                 return True
#             else: 
#                 return False
#         else:
#             return True
#     else:
#         return False
        
# print(is_leap_year(int(input("What is the year you want to check: "))))


# ============================================================
# LESSON 4: DOCSTRINGS
# ============================================================

def format_name(f_name, l_name):
    """Take a first and last name and format it to return
    the title case version of the name."""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGela", "YU")
length = len(formatted_name)

print(formatted_name)
print(length)


# ============================================================
# DAY 10 REVISION NOTES
# ============================================================

# return sends a value back to the place where the function
# was called.
#
# Example:
#
# def add(n1, n2):
#     return n1 + n2
#
# result = add(2, 3)
#
# The returned value can be:
#
# 1. Printed directly.
# 2. Saved inside a variable.
# 3. Passed into another function.
#
# A function can stop early with return:
#
# if f_name == "" or l_name == "":
#     return "You did not provide valid inputs"
#
# A docstring is written immediately after the function
# definition using triple quotation marks.
#
# Functions can be stored as dictionary values:
#
# operations = {
#     "+": add,
#     "-": subtract,
# }
#
# The selected function can then be called:
#
# operations["+"](2, 3)
#
# In the Calculator project, the result from one calculation
# can become the first number of the next calculation.


# ============================================================
# DAY 10 FINAL PROJECT: CALCULATOR
# ============================================================

#Day 10 Final project


# def add(n1, n2):
#     return n1 + n2

# my_favourite_operation = add #assign function as value on a variable then call it with its inputs

# print(my_favourite_operation(2, 3))

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
# print(operations["*"](4, 8))

#my version: 
import art

def calculator(n1, n2, op):
    if op == "+": 
        result = operations["+"](n1, n2)
        print(f"{n1} {op} {n2} = {result}")
        return result
    elif op == "-": 
        result = operations["-"](n1, n2)
        print(f"{n1} {op} {n2} = {result}")
        return result
    elif op == "*": 
        result = operations["*"](n1, n2)
        print(f"{n1} {op} {n2} = {result}")
        return result
    elif op == "/": 
        result = operations["/"](n1, n2)
        print(f"{n1} {op} {n2} = {result}")
        return result
    else: 
        print("Please Enter a valid operation")

continue_calculation = True 
while continue_calculation == True:
    print(art.logo)
    first_number = float(input("What's the first number?: "))
    print("+ \n- \n* \n/")
    operation = input("Pick an operation: ")
    next_number = float(input("What's the next number ?: "))
    result = calculator(n1 = first_number ,n2= next_number ,op= operation)
    more_calculation = True
    while more_calculation: 
        other_operation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:").lower()
        if other_operation == "y": 
            print("+ \n- \n* \n/")
            operation = input("Pick an operation: ")
            next_number = float(input("What's the next number ?: "))
            result = calculator(n1 = result ,n2= next_number ,op= operation)
        elif other_operation == "n":
            print("\n" * 18)    
            more_calculation = False

#Angela's version
import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations["*"](4, 8))


def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
