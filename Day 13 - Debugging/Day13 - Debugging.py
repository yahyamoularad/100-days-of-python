# =============================================================================
# DAY 13 - DEBUGGING
# HOW TO FIND AND FIX ERRORS IN PYTHON
# =============================================================================
#
# Day 13 does not have a final project. It teaches a debugging process that
# can be used with every Python program.
#
# MAIN LESSONS
# 1. Describe the problem before changing the code.
# 2. Reproduce the bug consistently.
# 3. Play computer and trace each line manually.
# 4. Read error messages and red underlines carefully.
# 5. Use print() to inspect values.
# 6. Use a debugger and breakpoints.
# 7. Test edge cases and boundary values.
# 8. Fix one problem at a time.
#
# The code from the original Day13.py file is preserved below. Explanations
# and debugging notes were added as comments.
# =============================================================================


# =============================================================================
# LESSON 1: DESCRIBE THE PROBLEM
# =============================================================================
#
# Before fixing a bug, answer three questions:
#
# 1. What is the code doing?
# 2. What is the code supposed to do?
# 3. What assumption is incorrect?
#
# range(start, stop) includes start but excludes stop.
#
# range(1, 20) produces 1 through 19, so i never becomes 20.
# range(1, 21) produces 1 through 20, so the condition i == 20 can be True.
#
# # Debugging 

# def my_function():
#     for i in range(1, 21): #it was range(1, 20)
#         if i == 20:
#             print("You got it !")
# my_function()

# # Describe the Problem - Write your answers as comments: 
# # 1. What is the for loop doing? 
# # 2. When is the function meant to print "You got it"? 
# # 3. What are your assumptions about the value of i ?


# =============================================================================
# LESSON 2: REPRODUCE THE BUG
# =============================================================================
#
# Some bugs appear only with certain random values. Reproducing a bug means
# finding the exact input or random result that causes the problem.
#
# This list contains six elements, so its valid indexes are:
#
# 0, 1, 2, 3, 4, 5
#
# randint() includes both endpoints.
#
# randint(1, len(dice_images) - 1) becomes randint(1, 5).
# It is valid, but index 0 is never selected, so "❶" never appears.
#
# randint(0, 5) is also valid and can select all six images. The comment
# saying that it causes an index error does not match the current code.
#
# A real out-of-range bug would happen if dice_num could become 6.
#
# Reproduce the bug 
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, len(dice_images) -1)
# print(dice_images[dice_num])

# #other version : 
# from random import randint
# dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) # Index out of range error
# print(dice_images[dice_num])


# =============================================================================
# LESSON 3: PLAY COMPUTER AND EVALUATE EACH LINE
# =============================================================================
#
# "Play computer" means following the program manually in execution order.
# Write down the value of each variable and whether every condition is True
# or False.
#
# Important boundary values for this example are 1980, 1981, 1993, and 1994.
#
# Current behavior:
#
# 1980 or earlier:
#     Neither condition is True, so nothing is printed.
#
# 1981 through 1993:
#     The first condition is True, so "You are a millennial." is printed.
#
# 1994 or later:
#     The elif condition year >= 1994 is True, so "You are a Gen Z." prints.
#
# The old comment about 1994 producing no output does not match the current
# condition because the current code uses >= 1994.
#
# Play Computer and evaluate each line 
# year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:   # when we enter 1994 the program ends without display
#     print("You are a Gen Z.")


# =============================================================================
# LESSON 4: FIX ERRORS AND WATCH RED UNDERLINES
# =============================================================================
#
# int() can convert text such as "15" to an integer.
# It cannot convert text such as "fifteen", so Python raises ValueError.
#
# try:
#     Python attempts to run the code.
#
# except ValueError:
#     Python runs this block only when a ValueError occurs.
#
# The current example gives the user one extra attempt. If the second input
# is also invalid, another ValueError occurs because it is outside a loop.
#
# Fixing Errors and Watching for Red Underlines 
# The errors : when the user enters a string instead of integer the program displays ValueError

# try: 
#     age = int(input("How old are you?"))
# except ValueError: 
#     print("You have typed in an invalid number. Please try again with a numerical response such as 15.")
#     age = int(input("How old are you?"))

# if age > 18: 
#     print(f"You can drive at age {age}.")


# =============================================================================
# LESSON 5: CHECK = AND ==
# =============================================================================
#
# A single equals sign assigns a value:
#
# word_per_page = 10
#
# A double equals sign compares two values:
#
# word_per_page == 10
#
# A comparison returns True or False. It does not save the value.
#
# The original bug used == where assignment with = was required.
# The current line correctly uses =.
#
# Printing intermediate values helps confirm that the program received the
# values expected by the programmer.
#
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))  # it was == instead of = 
# print(word_per_page)
# total_words = pages * word_per_page 
# print(f"{total_words} = {pages} * {word_per_page} ")
# print(total_words)


# =============================================================================
# LESSON 6: USE A DEBUGGER
# =============================================================================
#
# A debugger pauses a program and lets you inspect it one line at a time.
#
# Important debugger tools:
#
# Breakpoint:
#     A marker where the program should pause.
#
# Step over:
#     Execute the current line without entering called functions.
#
# Step into:
#     Enter a function and inspect its instructions.
#
# Step out:
#     Finish the current function and return to the caller.
#
# Variables panel:
#     Displays the current value of each variable.
#
# In mutate():
#
# 1. b_list begins as an empty list.
# 2. Each item is multiplied by 2.
# 3. A random number from 1 to 3 is added.
# 4. maths.add() adds the original item again.
# 5. The result is appended to b_list.
#
# Because random.randint() is used, the output can change on each run.
#
# Pycharm Debugger "How it works ?"
# import maths
# import random

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3)
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)


# mutate([1, 2, 3, 5, 8, 13])


# =============================================================================
# LESSON 7: DEBUG THE LEAP-YEAR FUNCTION
# =============================================================================
#
# Leap-year rules:
#
# 1. A year divisible by 4 is normally a leap year.
# 2. A year divisible by 100 is normally not a leap year.
# 3. A year divisible by 400 is a leap year.
#
# The current code uses 4000 instead of 400:
#
# year % 4000 == 0
#
# This is a logic error. The code runs, but it returns an incorrect result
# for some years.
#
# Example:
# 2000 is divisible by 400 and is a leap year.
# It is not divisible by 4000, so the current code incorrectly returns False.
#
# Exercice debugging
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0: #error it should be modulo 400
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


# =============================================================================
# LESSON 8: DEBUG FIZZBUZZ
# =============================================================================
#
# Expected rules:
#
# Multiples of both 3 and 5 print "FizzBuzz".
# Multiples of only 3 print "Fizz".
# Multiples of only 5 print "Buzz".
# All other numbers print the number.
#
# The current code contains four logic problems.
#
# PROBLEM 1: SEPARATE if STATEMENTS
#
# All three if statements are checked independently.
# For number 15, the program prints "FizzBuzz", "Fizz", and "Buzz".
# An if / elif / elif / else chain is normally used when only one result
# should be printed.
#
# PROBLEM 2: THE else BELONGS ONLY TO THE LAST if
#
# The else is connected only to:
#
# if number % 5 == 0:
#
# Therefore, a number such as 3 prints "Fizz" and then also prints [3].
#
# PROBLEM 3: print([number]) PRINTS A LIST
#
# [number] creates a list containing the number. For 7, it prints [7]
# instead of 7.
#
# PROBLEM 4: print(fizz_buzz(50)) PRINTS None
#
# fizz_buzz() prints its results but has no explicit return statement.
# A function without an explicit return statement returns None.
# The outer print() therefore displays None after the loop finishes.
#
# The code below is preserved exactly as it appeared in Day13.py.
#
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])
print(fizz_buzz(50))

#Corrected version:
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# =============================================================================
# DAY 13 DEBUGGING TIPS
# =============================================================================
#
# 1. Read the complete error message.
#
# 2. Start with the final line of the traceback, then find the mentioned line
#    in your file.
#
# 3. Explain what the code should do before changing it.
#
# 4. Reproduce the problem with the same input.
#
# 5. Test boundaries such as 0, 1, the first item, the last item, minimum
#    values, and maximum values.
#
# 6. Print important variables:
#
#    print(variable)
#
# 7. Inspect data types:
#
#    print(type(variable))
#
# 8. Check assignment and comparison:
#
#    =   assigns a value
#    ==  compares two values
#
# 9. Check indentation carefully.
#
# 10. Check which if statement an else belongs to.
#
# 11. Remember that list indexes begin at 0.
#
# 12. Remember that range() excludes its stop value.
#
# 13. Use a breakpoint and inspect variables one line at a time.
#
# 14. Change one thing at a time, then run the program again.
#
# 15. Code can contain logic errors even when it runs without exceptions.
#
# 16. Ask someone else to review the code when you are stuck.
#
# 17. Take a short break and return with fresh attention.
#
# 18. Search the exact error message or consult the documentation.
# =============================================================================
