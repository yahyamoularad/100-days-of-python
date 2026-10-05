# Day 22: Paddle class
#
# Paddle inherits from Turtle.
# Each Paddle object:
# - has a stretched square shape
# - starts at a supplied position
# - can move up
# - can move down
#
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20 
        self.goto(self.xcor(), new_y)
        

    def go_down(self):
        new_y = self.ycor() - 20 
        self.goto(self.xcor(), new_y)