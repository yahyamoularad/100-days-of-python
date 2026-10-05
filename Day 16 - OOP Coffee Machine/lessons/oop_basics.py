# Day 16: Object-Oriented Programming Basics
#
# This file contains the lesson examples from the original
# Day16-start.py file, now uncommented and organized.
#
# Topics:
# - Procedural programming compared with OOP
# - Classes as blueprints
# - Objects created from classes
# - Attributes
# - Methods
# - Importing classes
# - Turtle example
# - PrettyTable example


# ============================================================
# LESSON 1: PROCEDURAL PROGRAMMING VS OOP
# ============================================================

# Procedural programming organizes a program around procedures
# and functions.
#
# Object-Oriented Programming organizes a program around objects.
#
# Example model:
#
# waiter
#
# What it has: attributes
#     is_holding_plate = True
#     tables_responsible = [4, 5, 6]
#
# What it does: methods
#     take_order(table, order)
#     take_payment(amount)
#
# A class is a blueprint.
# We can create many objects from the same class.
#
# Class names use PascalCase.
#
# Basic syntax:
#
# object = Class()


# ============================================================
# LESSON 2: CREATING AN OBJECT, FIRST IMPORT STYLE
# ============================================================

import turtle

timmy = turtle.Turtle()

# turtle is the imported module.
# Turtle is the class.
# timmy is an object created from the Turtle class.


# ============================================================
# LESSON 3: CREATING OBJECTS, SECOND IMPORT STYLE
# ============================================================

from turtle import Turtle, Screen

timmy = Turtle()

print(timmy)

# Methods are called with:
#
# object.method()

timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)


# ============================================================
# LESSON 4: ACCESSING OBJECT ATTRIBUTES
# ============================================================

my_screen = Screen()

# Attributes are accessed with:
#
# object.attribute

print(my_screen.canvheight)


# ============================================================
# LESSON 5: CALLING OBJECT METHODS
# ============================================================

# A method belongs to an object.
#
# Syntax:
#
# object.method()

my_screen.exitonclick()


# ============================================================
# LESSON 6: PRETTYTABLE OBJECTS
# ============================================================

from prettytable import PrettyTable

table = PrettyTable()

table.add_column(
    "Pokemon Name",
    ["Pikachu", "Squirtle", "Charmander"]
)

table.add_column(
    "Type",
    ["Electric", "Water", "Fire"]
)

# align is an attribute of the table object.
table.align = "l"

print(table.align)
