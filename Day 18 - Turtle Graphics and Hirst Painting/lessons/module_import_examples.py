# Day 18 - Importing Modules, Packages, and Aliases
#
# These are the import styles demonstrated in the original lesson.
#
# Keep only one Turtle import style active at a time when experimenting.


# 1st way
import turtle

tim = turtle.Turtle()


# 2nd way
from turtle import Turtle

# from    -> keyword
# turtle  -> module name
# import  -> keyword
# Turtle  -> item imported from the module

tim = Turtle()


# 3rd way
from turtle import *

# * means everything from the module.


# Aliasing a module
import turtle as t

tim = t.Turtle()


# Installing a new package was demonstrated with:
#
# pip install heroes

import heroes

print(heroes.gen())
