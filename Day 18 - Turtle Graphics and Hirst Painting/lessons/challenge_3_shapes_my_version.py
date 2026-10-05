# Day 18 - Turtle Challenge 3: Different Shapes
# My original version
#
# This code is uncommented from Day18-start.py.

import turtle as t

tim = t.Turtle()

# Triangle
for _ in range(3):
    tim.color("cyan")
    tim.forward(100)
    tim.right(120)

# Square
for _ in range(4):
    tim.color("blue")
    tim.forward(100)
    tim.right(90)

# Pentagon
for _ in range(5):
    tim.color("red")
    tim.forward(100)
    tim.right(72)

# Hexagon
for _ in range(6):
    tim.color("darkkhaki")
    tim.forward(100)
    tim.right(60)

# Heptagon
for _ in range(7):
    tim.color("darkslateblue")
    tim.forward(100)
    tim.right(51.43)

# Octagon
for _ in range(8):
    tim.color("darkseagreen")
    tim.forward(100)
    tim.right(45)

# Nonagon
for _ in range(9):
    tim.color("darkorange")
    tim.forward(100)
    tim.right(40)

# Decagon
for _ in range(10):
    tim.color("darkmagenta")
    tim.forward(100)
    tim.right(36)

screen = t.Screen()
screen.exitonclick()
