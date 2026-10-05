# Day 23: Turtle Crossing

## Folder structure

```text
Day 23 - Turtle Crossing/
├── main.py
├── player.py
├── car_manager.py
├── scoreboard.py
└── README.md
```

## Final project

Day 23 contains the Turtle Crossing capstone-style game.

The original final project structure is preserved:

```text
main.py
player.py
car_manager.py
scoreboard.py
```

There were no separate commented solution versions in the uploaded Day 23 files, so no additional version files were created.

# Project structure

## `main.py`

Controls the overall game.

It creates:

```python
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
```

It also manages:

```text
keyboard input
game loop
car creation
car movement
collision detection
successful crossings
level progression
```

## `player.py`

Contains the `Player` class.

The player:

```text
starts at the bottom
faces upward
moves forward
returns to the start
detects the finish line
```

## `car_manager.py`

Contains the `CarManager` class.

It manages all car Turtle objects.

## `scoreboard.py`

Contains the `Scoreboard` class.

It displays the current level and the GAME OVER message.

# Lessons learned

## 1. Breaking a game into separate classes

Day 23 uses three main classes:

```python
Player
CarManager
Scoreboard
```

Each class is responsible for one part of the game.

This keeps `main.py` focused on the game flow.

## 2. Class inheritance

The `Player` class inherits from Turtle:

```python
class Player(Turtle):
```

and the `Scoreboard` class also inherits from Turtle:

```python
class Scoreboard(Turtle):
```

They call:

```python
super().__init__()
```

to initialize the parent Turtle class.

## 3. Constants

The Player file defines:

```python
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
```

The CarManager file defines:

```python
COLORS
STARTING_MOVE_DISTANCE
MOVE_INCREMENT
```

The Scoreboard defines:

```python
FONT
```

These values are stored once and reused throughout the project.

## 4. Starting position

The Player uses:

```python
self.goto(STARTING_POSITION)
```

to return to the starting point.

The player starts near the bottom edge of the screen.

## 5. Setting Turtle direction

The Player constructor uses:

```python
self.setheading(90)
```

A heading of 90 degrees points upward.

This allows:

```python
self.forward(MOVE_DISTANCE)
```

to move the player toward the finish line.

## 6. Keyboard input

The game listens for keyboard events:

```python
screen.listen()
```

and connects the `w` key to:

```python
player.go_up
```

with:

```python
screen.onkey(player.go_up, "w")
```

The method is passed without parentheses because it should run only when the key is pressed.

## 7. Random car creation

The CarManager does not create a car on every game-loop iteration.

It generates:

```python
random_chance = random.randint(1, 6)
```

and creates a car only when:

```python
random_chance == 1
```

This produces cars at irregular intervals.

## 8. Creating Turtle objects dynamically

When a car is created:

```python
new_car = Turtle("square")
```

The program configures that Turtle as a car.

It changes its size:

```python
new_car.shapesize(stretch_wid=1, stretch_len=2)
```

This makes the Turtle shape wider than it is tall.

## 9. Random car colors

The project stores colors in:

```python
COLORS
```

and selects one with:

```python
random.choice(COLORS)
```

Every newly generated car can therefore have a different color.

## 10. Random y positions

Cars are positioned with:

```python
random_y = random.randint(-250, 250)
```

and:

```python
new_car.goto(300, random_y)
```

The x-coordinate starts the car on the right side of the screen.

The random y-coordinate places it at a different height.

## 11. Storing many objects in a list

CarManager keeps all car objects in:

```python
self.all_cars = []
```

Every new car is added with:

```python
self.all_cars.append(new_car)
```

The game can then work with all existing cars.

## 12. Moving all cars

The method:

```python
move_cars()
```

loops through:

```python
self.all_cars
```

and moves each car:

```python
car.backward(self.car_speed)
```

All cars use the current CarManager speed.

## 13. Object state

CarManager stores:

```python
self.car_speed
```

Scoreboard stores:

```python
self.level
```

These values change as the game progresses.

This is another practical example of objects maintaining state.

## 14. Increasing game difficulty

When the player successfully crosses the road:

```python
car_manager.level_up()
```

runs.

The method changes:

```python
self.car_speed += MOVE_INCREMENT
```

This makes the cars move faster at higher levels.

## 15. Game loop

The main game uses:

```python
game_is_on = True
```

and:

```python
while game_is_on:
```

Every loop:

```text
waits briefly
updates the screen
tries to create a new car
moves all cars
checks collisions
checks the finish line
```

## 16. Manual screen updates

The project uses:

```python
screen.tracer(0)
```

to disable automatic updates.

Inside the loop:

```python
screen.update()
```

redraws the screen manually.

This gives the program more control over the animation.

## 17. Controlling game speed

The game loop uses:

```python
time.sleep(0.1)
```

This adds a short pause between screen updates.

Without it, the cars would move too quickly.

## 18. Collision detection

The main file checks every car:

```python
for car in car_manager.all_cars:
```

and measures the distance from the player:

```python
car.distance(player)
```

A collision occurs when:

```python
car.distance(player) < 20
```

The game then sets:

```python
game_is_on = False
```

and displays:

```python
scoreboard.game_over()
```

## 19. Detecting the finish line

The Player class contains:

```python
is_at_finish_line()
```

It checks:

```python
self.ycor() > FINISH_LINE_Y
```

and returns:

```python
True
```

or:

```python
False
```

This allows the main program to ask the Player object whether it crossed the road.

## 20. Resetting the player

After a successful crossing:

```python
player.go_to_start()
```

returns the Turtle to:

```python
STARTING_POSITION
```

The player can then start the next level.

## 21. Increasing the level

A successful crossing also runs:

```python
scoreboard.increase_level()
```

The Scoreboard changes:

```python
self.level += 1
```

and redraws the displayed level.

## 22. Clearing text before rewriting it

The Scoreboard uses:

```python
self.clear()
```

before writing the new level.

Without clearing, new text would be drawn on top of the previous text.

## 23. Coordinating several objects

The main file does not contain all game functionality itself.

Instead it asks the objects to perform their responsibilities:

```python
car_manager.create_car()
car_manager.move_cars()

player.is_at_finish_line()
player.go_to_start()

car_manager.level_up()

scoreboard.increase_level()
scoreboard.game_over()
```

This continues the Object-Oriented Programming approach from the previous days.

## 24. Increasing difficulty through state

Day 23 demonstrates a simple game difficulty system.

The game does not need a completely different car algorithm for each level.

Instead, one value changes:

```python
self.car_speed
```

As that value increases, the same movement code becomes more difficult for the player.

## Day 23 progression

```text
create the Player
       ↓
move Player with keyboard input
       ↓
create CarManager
       ↓
generate cars randomly
       ↓
move all cars
       ↓
detect collision
       ↓
detect finish line
       ↓
reset player
       ↓
increase car speed
       ↓
create Scoreboard
       ↓
increase level
       ↓
display GAME OVER
```

## Running the project

From the root of the `100-days-of-python` repository:

```bash
python "Day 23 - Turtle Crossing/main.py"
```

## Controls

```text
W = move forward
```

## Dependencies

Day 23 uses only Python standard-library modules:

```text
turtle
random
time
```

No external package installation is required.
