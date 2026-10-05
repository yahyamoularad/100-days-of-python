# Day 19: Higher Order Functions and Function Arguments
#
# This lesson keeps the executable code from the original Day 19 file.
# No new Python keyword or function has been added.


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, func):
    # func is passed without parentheses because the function itself
    # is being given to calculator.
    return func(n1, n2)


# Positional Arguments
#
# This example was written as lesson structure only in the original file:
#
# def my_function(a, b, c):
#     # Do this with a
#     # Then do this with b
#     # Finally do this with c
#
# my_function(1, 2, 3)
#
# The values are matched according to their positions.


# Keyword Arguments
#
# This example was also written as lesson structure only:
#
# def my_function(a, b, c):
#     # Do this with a
#     # Then do this with b
#     # Finally do this with c
#
# my_function(c=3, a=1, b=2)
#
# Here the argument names decide which value goes to each parameter.
