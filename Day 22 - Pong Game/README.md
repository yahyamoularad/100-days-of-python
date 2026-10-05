# Day 22: Pong Game

## Folder structure

```text
Day 22 - Pong Game/
├── main.py
├── paddle.py
├── ball.py
├── scoreboard.py
└── README.md
```

## Final project

Day 22 contains a complete Pong game split across four Python files.

The original project structure is preserved:

```text
main.py
paddle.py
ball.py
scoreboard.py
```

There were no separate commented code versions in the uploaded Day 22 files, so no additional version files were created.

# Lessons learned

## 1. Breaking a project into steps

The Day 22 main file starts with the project plan:

```text
1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses
8. Keep score
```

This is an important programming habit.

Instead of trying to build the entire game at once, the project is divided into smaller problems.

## 2. Multiple classes with different responsibilities

The project uses three classes:

```python
Paddle
Ball
Scoreboard
```

Each class has one main responsibility.

### Paddle

Controls paddle appearance and vertical movement.

### Ball

Controls movement, bouncing, speed, and resetting.

### Scoreboard

Stores and displays the score.

This makes the program easier to understand than putting everything inside `main.py`.

## 3. Class inheritance

All three classes inherit from Turtle:

```python
class Paddle(Turtle)
class Ball(Turtle)
class Scoreboard(Turtle)
```

This allows the classes to directly use Turtle methods.

For example:

```python
self.goto(...)
self.color(...)
self.shape(...)
self.write(...)
```

## 4. Calling the parent constructor

Each class uses:

```python
super().__init__()
```

This initializes the inherited Turtle behavior before adding the class-specific configuration.

## 5. Creating objects with different starting positions

The Paddle constructor receives a position:

```python
def __init__(self, position):
```

The main program can therefore create two Paddle objects from the same class:

```python
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
```

The same class is reused for both players.

## 6. Object state

Each object stores its own state.

The Ball stores:

```python
self.x_move
self.y_move
self.move_speed
```

The Scoreboard stores:

```python
self.l_score
self.r_score
```

These values belong to each object and can change while the game runs.

## 7. Moving the paddles

The Paddle class calculates a new y-coordinate.

Moving up:

```python
new_y = self.ycor() + 20
self.goto(self.xcor(), new_y)
```

Moving down:

```python
new_y = self.ycor() - 20
self.goto(self.xcor(), new_y)
```

The x-coordinate stays unchanged.

Only the y-coordinate changes.

## 8. Keyboard controls for two players

The right paddle uses:

```python
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
```

The left paddle uses:

```python
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
```

This allows two players to control different Paddle objects.

## 9. Manual screen updates

The screen uses:

```python
screen.tracer(0)
```

and the game loop uses:

```python
screen.update()
```

This gives the program control over when frames are drawn.

## 10. Ball movement using x and y values

The Ball stores:

```python
self.x_move = 10
self.y_move = 10
```

Every time `move()` runs:

```python
new_x = self.xcor() + self.x_move
new_y = self.ycor() + self.y_move
self.goto(new_x, new_y)
```

The ball therefore moves diagonally.

## 11. Bouncing from the top and bottom walls

The main program checks:

```python
if ball.ycor() > 280 or ball.ycor() < -280:
```

When the ball reaches the top or bottom, it calls:

```python
ball.bounce_y()
```

Inside the Ball class:

```python
self.y_move *= -1
```

Multiplying by `-1` reverses the vertical direction.

For example:

```text
10 becomes -10
-10 becomes 10
```

## 12. Bouncing from a paddle

The program uses:

```python
ball.distance(r_paddle)
```

and:

```python
ball.distance(l_paddle)
```

to check whether the ball is close enough to a paddle.

It also checks the ball x-coordinate so the correct side is detected.

When a collision occurs:

```python
ball.bounce_x()
```

runs.

## 13. Horizontal bounce

The Ball class uses:

```python
self.x_move *= -1
```

This reverses the ball's horizontal direction.

A ball moving right begins moving left.

A ball moving left begins moving right.

## 14. Making the game progressively faster

Inside `bounce_x()`:

```python
self.move_speed *= 0.9
```

The main loop sleeps for:

```python
time.sleep(ball.move_speed)
```

Because `move_speed` becomes smaller after a paddle collision, the pause becomes shorter.

That makes the ball appear to move faster.

## 15. Detecting a missed ball

The program checks whether the ball has moved beyond the right side:

```python
if ball.xcor() > 380:
```

or beyond the left side:

```python
if ball.xcor() < -380:
```

This means one of the paddles missed the ball.

## 16. Resetting the ball

After a missed ball:

```python
ball.reset_position()
```

runs.

The Ball class:

```python
self.goto(0, 0)
self.move_speed = 0.1
self.bounce_x()
```

This:

1. returns the ball to the center
2. resets the speed
3. sends it toward the opposite player

## 17. Score keeping for two players

The Scoreboard stores:

```python
self.l_score = 0
self.r_score = 0
```

The left score increases with:

```python
self.l_score += 1
```

and the right score increases with:

```python
self.r_score += 1
```

## 18. Redrawing the scoreboard

Before writing the latest score:

```python
self.clear()
```

removes the previous text.

The scores are then drawn at two positions:

```python
self.goto(-100, 200)
self.goto(100, 200)
```

This produces a left score and a right score.

## 19. Using object methods from another file

The main program coordinates the objects:

```python
ball.move()
ball.bounce_y()
ball.bounce_x()
ball.reset_position()

scoreboard.l_point()
scoreboard.r_point()

r_paddle.go_up()
l_paddle.go_down()
```

This is another example of separating responsibilities between objects.

## 20. Game loop

The project uses:

```python
game_is_on = True

while game_is_on:
```

The loop repeatedly:

```text
waits
updates the screen
moves the ball
checks wall collision
checks paddle collision
checks misses
updates scores
```

This is the core game loop.

## Day 22 progression

```text
create screen
      ↓
create Paddle class
      ↓
create two Paddle objects
      ↓
add keyboard controls
      ↓
create Ball class
      ↓
move ball
      ↓
bounce from walls
      ↓
bounce from paddles
      ↓
detect missed ball
      ↓
reset ball
      ↓
create Scoreboard
      ↓
track both players' scores
```

## Running the project

From the root of the `100-days-of-python` repository:

```bash
python "Day 22 - Pong Game/main.py"
```

## Controls

Right paddle:

```text
Up Arrow
Down Arrow
```

Left paddle:

```text
W
S
```

## Dependencies

Day 22 only uses Python standard-library modules:

```text
turtle
time
```

No external package installation is required.
