# Day 19: Turtle Event Listeners
#
# This code is uncommented from the original Day 19 file.
#
# screen.listen() allows the Screen to listen for keyboard input.
# screen.onkey() connects a key press to a function.

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


# The Screen must listen before keyboard events can be detected.
screen.listen()

# Pressing the space key calls move_forward.
# The function is passed without parentheses.
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
