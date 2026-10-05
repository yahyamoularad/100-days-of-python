# Day 20: Building the Snake Step by Step
#
# This file contains the earlier procedural code from the original
# Day 20 main file, now uncommented and organized.
#
# It shows the progression from manually creating snake segments
# to creating them with a loop and then moving them as one snake.

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# tracer(0) turns off automatic screen updates.
screen.tracer(0)


# ============================================================
# FIRST IDEA: CREATE EACH SEGMENT MANUALLY
# ============================================================

# Easy Way:
#
# segment_1 = Turtle("square")
# segment_1.color("white")
#
# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)


# ============================================================
# BETTER WAY: CREATE SEGMENTS WITH A LOOP
# ============================================================

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


# ============================================================
# MOVE THE SNAKE
# ============================================================

game_is_on = True

while game_is_on:
    # Manually refresh the screen.
    screen.update()

    # Slow down the loop so the movement is visible.
    time.sleep(0.1)

    # Move from the last segment toward the first.
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    # The first segment is the head.
    segments[0].forward(20)

    # This turn was also part of the original lesson example.
    segments[0].left(90)

screen.exitonclick()
