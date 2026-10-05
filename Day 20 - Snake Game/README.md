# Day 20: Snake Game

## Folder structure

```text
Day 20 - Snake Game/
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── README.md
├── lessons/
│   └── snake_setup_and_movement.py
└── versions/
    └── main_before_slicing.py
```

## Final project

The final Snake Game keeps the original four-file project structure:

```text
main.py
snake.py
food.py
scoreboard.py
```

The project logic has not been rewritten.

Only explanatory comments were added.

## Earlier code

### `lessons/snake_setup_and_movement.py`

Contains the earlier procedural snake-building code from the original `main.py`.

It shows the progression from:

1. manually creating three Turtle segments
2. creating the segments with a loop
3. storing the segments in a list
4. moving the snake from the tail toward the head

### `versions/main_before_slicing.py`

Preserves the earlier tail-collision technique that checks every segment and skips the head manually.

The final `main.py` uses list slicing instead.

# Lessons learned

## 1. Building a larger project with multiple files

Day 20 separates the Snake Game into different responsibilities.

### `main.py`

Controls the overall game.

It creates:

```python
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
```

and manages the game loop and collision detection.

### `snake.py`

Contains the `Snake` class.

It manages the snake segments and movement.

### `food.py`

Contains the `Food` class.

It controls the food appearance and random position.

### `scoreboard.py`

Contains the `ScoreBoard` class.

It manages the score display and game-over message.

This keeps each part of the game in its own file.

## 2. Screen animation with `tracer()` and `update()`

The screen uses:

```python
screen.tracer(0)
```

This turns off automatic animation updates.

Inside the game loop:

```python
screen.update()
```

refreshes the screen manually.

This makes the snake movement appear smoother because the program controls exactly when the frame is redrawn.

## 3. Slowing down a game loop

The project uses:

```python
time.sleep(0.1)
```

This pauses the loop briefly between frames.

Without the pause, the snake would move too quickly.

## 4. Creating several Turtle objects

A snake is not one Turtle object.

It is a list of several Turtle objects.

The original lesson begins with three starting positions:

```python
STARTING_POSITIONS = [
    (0, 0),
    (-20, 0),
    (-40, 0)
]
```

The Snake class creates one segment for every position.

## 5. Storing objects inside a list

The Snake object stores all segments in:

```python
self.segments
```

Every item in that list is a Turtle object.

The first segment becomes:

```python
self.head
```

This makes it easier to control the head separately from the rest of the body.

## 6. Moving the snake body

The snake cannot move every segment forward independently.

Instead, the last segment moves to the position of the segment in front of it.

The loop starts from the back:

```python
for seg_num in range(len(self.segments) - 1, 0, -1):
```

Then it reads the previous segment's coordinates:

```python
new_x = self.segments[seg_num - 1].xcor()
new_y = self.segments[seg_num - 1].ycor()
```

and moves the current segment there:

```python
self.segments[seg_num].goto(new_x, new_y)
```

Finally, the head moves forward.

This creates the snake-following movement.

## 7. Constants

The Snake file defines values such as:

```python
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
```

These values are reused by the movement methods.

This avoids repeating the same numbers throughout the class.

## 8. Preventing the snake from reversing direction

The snake should not immediately turn into itself.

For example:

```python
def up(self):
    if self.head.heading() != DOWN:
        self.head.setheading(UP)
```

The snake can move up only when it is not currently moving down.

The same idea is used for the other three directions.

## 9. Keyboard controls with object methods

The final project connects keys directly to Snake methods:

```python
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
```

These are methods belonging to the `snake` object.

The function references are passed without parentheses.

## 10. Class inheritance

Day 20 introduces inheritance in the project.

The Food class is defined as:

```python
class Food(Turtle):
```

and the ScoreBoard class is:

```python
class ScoreBoard(Turtle):
```

This means both classes inherit behavior from Turtle.

They can directly use Turtle methods such as:

```python
shape()
penup()
color()
goto()
write()
hideturtle()
```

## 11. Calling the parent constructor with `super()`

Because Food and ScoreBoard inherit from Turtle, their constructors call:

```python
super().__init__()
```

This runs the Turtle constructor first.

After that, the subclass can configure the inherited Turtle object.

## 12. Food as a specialized Turtle

The Food constructor changes the inherited Turtle:

```python
self.shape("circle")
self.penup()
self.shapesize(stretch_len=0.5, stretch_wid=0.5)
self.color("blue")
self.speed("fastest")
```

Then:

```python
self.refresh()
```

moves the food to a random position.

This demonstrates inheritance by taking a general Turtle and specializing it into Food.

## 13. Random positions

The food position is generated with:

```python
random_x = random.randint(-280, 280)
random_y = random.randint(-280, 280)
```

Then:

```python
self.goto(random_x, random_y)
```

moves the Food object.

Whenever the snake eats the food:

```python
food.refresh()
```

places it somewhere else.

## 14. Detecting collision with food

The main program checks:

```python
if snake.head.distance(food) < 15:
```

`distance()` measures the distance between the snake head and the food.

If the distance becomes small enough, the program considers the food eaten.

Then:

```python
food.refresh()
snake.extend()
scoreboard.increase_score()
```

runs.

## 15. Extending the snake

When food is eaten:

```python
snake.extend()
```

calls:

```python
self.add_segment(self.segments[-1].position())
```

A new segment is created at the position of the final existing segment.

## 16. Score keeping

The ScoreBoard starts with:

```python
self.score = 0
```

When food is eaten:

```python
self.score += 1
```

The old text is removed with:

```python
self.clear()
```

and the score is written again:

```python
self.update_scoreboard()
```

## 17. Detecting wall collision

The project reads the snake head coordinates with:

```python
snake.head.xcor()
snake.head.ycor()
```

The original final version checks whether those values move outside the chosen game boundaries.

When that happens:

```python
game_is_on = False
scoreboard.game_over()
```

ends the game loop and displays the game-over message.

## 18. Detecting tail collision

The final version uses list slicing:

```python
snake.segments[1:]
```

This creates a view of the snake segments excluding the head.

The program then checks:

```python
for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
```

If the head gets too close to any body segment, the game ends.

## 19. List slicing

This is one of the important Day 20 concepts.

Given:

```python
snake.segments
```

the slice:

```python
snake.segments[1:]
```

means:

```text
start at index 1
continue to the end
```

Because the head is at index 0, this conveniently skips it.

## 20. Earlier tail-collision method

Before using slicing, the program looped through every segment:

```python
for segment in snake.segments:
```

and manually skipped the head:

```python
if segment == snake.head:
    pass
```

The slicing version is shorter because the head is excluded before the loop begins.

Both versions are preserved in this folder.

## 21. Game state with a Boolean variable

The main game loop uses:

```python
game_is_on = True
```

and:

```python
while game_is_on:
```

Collisions change:

```python
game_is_on = False
```

which ends the game.

## Day 20 progression

The day develops the game in stages:

```text
create snake segments manually
        ↓
create segments with a loop
        ↓
make the segments follow each other
        ↓
move snake code into a Snake class
        ↓
add keyboard controls
        ↓
create Food using inheritance
        ↓
detect food collisions
        ↓
extend the snake
        ↓
create ScoreBoard using inheritance
        ↓
detect wall collisions
        ↓
detect tail collisions
        ↓
use slicing to simplify tail collision
```

## Running the final project

From the root of the `100-days-of-python` repository:

```bash
python "Day 20 - Snake Game/main.py"
```

## Running the earlier lesson

```bash
python "Day 20 - Snake Game/lessons/snake_setup_and_movement.py"
```

## Running the pre-slicing version

```bash
python "Day 20 - Snake Game/versions/main_before_slicing.py"
```

## Dependencies

Day 20 uses only Python standard-library modules:

```text
turtle
random
time
```

No external package installation is required.
