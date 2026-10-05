# Day 18 - Tuples and Random RGB Colours
#
# This code is uncommented from Day18-start.py.
#
# Tuple example from the lesson:
#
# my_tuple = (1, 3, 8)
# my_tuple[2]
#
# Tuples are immutable.
# The lesson also mentioned converting a tuple to a list:
#
# list(my_tuple)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)

    return random_color


directions = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
