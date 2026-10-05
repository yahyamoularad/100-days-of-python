# Day 19: Turtle Race

## Folder structure

```text
Day 19 - Turtle Race/
├── main.py
├── README.md
└── lessons/
    ├── event_listeners.py
    ├── higher_order_functions.py
    └── etch_a_sketch.py
```

## Final project

`main.py` contains the final Turtle Race project.

The final project structure and logic are preserved from the original Day 19 file.

## Lesson files

### `event_listeners.py`

Demonstrates how Turtle can react to keyboard input.

### `higher_order_functions.py`

Demonstrates passing a function as an argument and reviews positional and keyword arguments.

### `etch_a_sketch.py`

Contains the Day 19 Etch-A-Sketch coding challenge.

# Lessons learned

## 1. Event listeners

Turtle can react to keyboard input.

The screen first needs to listen:

```python
screen.listen()
```

Then a key can be connected to a function:

```python
screen.onkey(key="space", fun=move_forward)
```

The important detail is that the function is passed without parentheses:

```python
fun=move_forward
```

not:

```python
fun=move_forward()
```

The function should run only when the event happens.

## 2. Higher-order functions

A function can receive another function as an argument.

The lesson uses:

```python
def calculator(n1, n2, func):
    return func(n1, n2)
```

`func` represents a function such as:

```python
add
subtract
multiply
divide
```

This introduces the idea that functions can be passed around like other values.

## 3. Positional arguments

With:

```python
my_function(1, 2, 3)
```

the first value goes to `a`, the second to `b`, and the third to `c`.

The order matters.

## 4. Keyword arguments

With:

```python
my_function(c=3, a=1, b=2)
```

the values are connected to parameters by name.

The order no longer needs to match the parameter order.

## 5. Building keyboard controls

The Etch-A-Sketch challenge connects several keys to different functions:

```python
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
```

This turns several small functions into an interactive program.

## 6. Reading and changing Turtle heading

The Etch-A-Sketch challenge reads the current direction with:

```python
tim.heading()
```

and changes it with:

```python
tim.setheading(new_heading)
```

For example:

```python
new_heading = tim.heading() + 10
tim.setheading(new_heading)
```

turns the Turtle left.

Subtracting 10 turns it right.

## 7. Clearing and resetting Turtle

The `clear()` function uses:

```python
tim.clear()
tim.penup()
tim.home()
tim.pendown()
```

This:

1. clears the drawing
2. lifts the pen
3. returns the Turtle to the home position
4. puts the pen down again

## 8. Instances

The Day 19 notes explain that different Turtle objects are different instances of the same class.

For example, Timmy and Tommy can both be Turtle objects while having different positions, colors, and behavior.

Each object can have its own state.

## 9. Object state

An object's current data is its state.

For a Turtle, state can include things such as:

```text
position
heading
color
```

Two Turtle instances can therefore behave independently even though both were created from the same `Turtle` class.

## 10. Turtle coordinate system

The Turtle Race uses screen coordinates.

The screen is created with:

```python
screen.setup(width=500, height=400)
```

Turtles are positioned with:

```python
new_turtle.goto(x=-230, y=y_positions[turtle_index])
```

The x-coordinate controls left and right position.

The y-coordinate controls vertical position.

## 11. Lists can contain objects

The final project creates:

```python
all_turtles = []
```

Each new Turtle object is added with:

```python
all_turtles.append(new_turtle)
```

The program can then loop through all Turtle instances:

```python
for turtle in all_turtles:
```

This is another practical example of storing objects inside a list.

## 12. Creating several objects with a loop

The race creates six Turtle instances:

```python
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
```

Each Turtle receives a different color and y-position from:

```python
colors
y_positions
```

using the same index.

## 13. User input from the Turtle window

The race gets the user's bet with:

```python
screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
)
```

This returns the user's text input.

## 14. Boolean state controlling a game loop

The race begins with:

```python
is_race_on = False
```

If the user entered a bet:

```python
if user_bet:
    is_race_on = True
```

The race then continues with:

```python
while is_race_on:
```

When one Turtle crosses the finish line:

```python
is_race_on = False
```

and the loop stops.

## 15. Random movement

Each Turtle moves by a random distance:

```python
rand_distance = random.randint(0, 10)
turtle.forward(rand_distance)
```

Because every Turtle gets a different random movement on each loop, the winner is unpredictable.

## 16. Detecting the winner

The race checks the x-coordinate:

```python
if turtle.xcor() > 230:
```

When a Turtle moves past x = 230, the race ends.

Its color is read with:

```python
winning_color = turtle.pencolor()
```

## 17. Comparing the result with the user's bet

The winner's color is compared with:

```python
user_bet
```

If they match, the player wins.

Otherwise, the player loses.

## 18. Day 19 progression

The day builds toward the Turtle Race in several stages:

```text
keyboard event listening
        ↓
passing functions as arguments
        ↓
interactive Etch-A-Sketch controls
        ↓
understanding object instances and state
        ↓
using Turtle coordinates
        ↓
creating and racing multiple Turtle objects
```

This is the main progression of Day 19.

## Running the final project

From the root of the `100-days-of-python` repository:

```bash
python "Day 19 - Turtle Race/main.py"
```

## Running the lessons

Event listener example:

```bash
python "Day 19 - Turtle Race/lessons/event_listeners.py"
```

Higher-order function example:

```bash
python "Day 19 - Turtle Race/lessons/higher_order_functions.py"
```

Etch-A-Sketch:

```bash
python "Day 19 - Turtle Race/lessons/etch_a_sketch.py"
```

## Dependencies

Day 19 only uses Python's built-in Turtle and Random modules.

No external package installation is required.
