# Day 18 - Turtle Challenge 1: Draw a Square
#
# This code is uncommented from the original Day18-start.py file.

from turtle import Turtle, Screen

tim = Turtle()

# These examples were also present in the lesson:
# tim.shape("turtle")
# tim.color("red")
# tim.forward(100)
# tim.right(90)

# A square has four equal sides and four 90-degree turns.
for _ in range(4):
    tim.forward(100)
    tim.left(90)

screen = Screen()
screen.exitonclick()
