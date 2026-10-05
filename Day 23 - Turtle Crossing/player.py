# Day 23: Player class
#
# Player inherits from Turtle.
#
# Responsibilities:
# - start at the bottom of the screen
# - face upward
# - move forward when the user presses "w"
# - return to the start after reaching the finish line
# - report whether the finish line has been reached
#
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Create a turtle player that starts at the bottom of the screen 
# and listen for the "Up" keypress to move the turtle north. 
# If you get stuck, check the video walkthrough in Step 3.

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False