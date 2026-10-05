# Day 18 - Turtle Challenge 2: Dashed Line
#
# This code is uncommented from the original Day18-start.py file.

import turtle as t

tim = t.Turtle()

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = t.Screen()
screen.exitonclick()
