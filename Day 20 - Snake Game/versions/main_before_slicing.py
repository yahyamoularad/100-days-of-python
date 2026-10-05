# Day 20: Snake Game
# Alternative version before using list slicing
#
# This version preserves the earlier tail-collision approach
# from the original Day 20 file.
#
# Instead of looping over:
#
# snake.segments[1:]
#
# it loops over every segment and explicitly skips the head.
#
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food. 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with wall.             # In Angela's x and y are equal to 280 and -280 (there is little gap in my case that's why i have choosen 300 and -300 ) 
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:  
        game_is_on = False
        scoreboard.game_over()

    # # Detect collision with tail.   #Before Slicing technique
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

    # Detect collision with tail. Before using slicing.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()