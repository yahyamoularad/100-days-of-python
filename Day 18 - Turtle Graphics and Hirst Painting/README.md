# Day 18: Turtle Graphics and Hirst Painting

## Folder structure

```text
Day 18 - Turtle Graphics and Hirst Painting/
├── main.py
├── README.md
├── requirements.txt
├── lessons/
│   ├── challenge_1_square.py
│   ├── module_import_examples.py
│   ├── challenge_2_dashed_line.py
│   ├── challenge_3_shapes_my_version.py
│   ├── challenge_3_shapes_angela_version.py
│   ├── challenge_4_random_walk.py
│   ├── random_rgb_walk.py
│   └── challenge_5_spirograph.py
└── versions/
    ├── my_hirst_painting.py
    ├── angela_solution.py
    └── color_extraction.py
```

## Final project

`main.py` is the final Hirst Painting project version.

Its original drawing structure is preserved.

The final program:

1. creates a Turtle
2. enables 0 to 255 RGB colour mode
3. lifts the pen
4. hides the Turtle
5. moves to a starting position
6. draws 100 dots
7. uses a random colour for every dot
8. moves to the next row after every 10 dots

## Preserved versions

### `versions/my_hirst_painting.py`

Your original Hirst Painting implementation, uncommented.

### `versions/angela_solution.py`

The supplied `solution_day18.py`, preserved separately.

### `versions/color_extraction.py`

The original Colorgram example used to extract RGB colours from an image.

The image used by the original code was not uploaded, so this file requires the original `image.jpg` before it can run successfully.

# Lessons learned

## 1. Turtle Graphics

Day 18 expands the use of the Turtle module.

A Turtle object is created with:

```python
tim = t.Turtle()
```

The Turtle can then be controlled with methods such as:

```python
tim.forward(100)
tim.left(90)
tim.right(90)
tim.circle(100)
```

## 2. Turtle screen

A Turtle program keeps its window open with:

```python
screen = t.Screen()
screen.exitonclick()
```

The drawing remains visible until the window is clicked.

## 3. Using loops for repeated drawing

The first challenge draws a square with:

```python
for _ in range(4):
    tim.forward(100)
    tim.left(90)
```

Instead of writing the same movement four times, the loop repeats the drawing instructions.

## 4. Importing modules in different ways

The lesson demonstrates several import styles.

Import the module:

```python
import turtle
```

Import one item:

```python
from turtle import Turtle
```

Import everything:

```python
from turtle import *
```

Import with an alias:

```python
import turtle as t
```

The alias makes repeated module references shorter.

## 5. Installing external packages

The lesson demonstrates that external packages can be installed with `pip`.

Example from the lesson:

```text
pip install heroes
```

and then imported with:

```python
import heroes
```

## 6. Pen control

The dashed-line challenge uses:

```python
tim.penup()
tim.pendown()
```

When the pen is up, Turtle moves without drawing.

When the pen is down, movement draws a line.

## 7. Drawing regular polygons

For a regular polygon, the turning angle used in the Angela version is:

```python
angle = 360 / num_sides
```

A triangle uses 3 sides, a square 4, a pentagon 5, and so on.

The same `draw_shape()` function can therefore draw several polygons.

## 8. Random choices

Day 18 uses:

```python
random.choice(colours)
```

to select a random colour.

The Random Walk also uses:

```python
random.choice(directions)
```

to select one of:

```python
[0, 90, 180, 270]
```

## 9. Turtle heading

The Turtle direction can be changed with:

```python
tim.setheading(...)
```

The Random Walk uses fixed headings.

The Spirograph uses:

```python
tim.heading()
```

to read the current heading before adding the next angle.

## 10. Changing line thickness and drawing speed

The Random Walk uses:

```python
tim.pensize(15)
tim.speed("fastest")
```

This changes the appearance and speed of the drawing.

## 11. Tuples

The lesson introduces tuples with:

```python
my_tuple = (1, 3, 8)
```

A tuple is immutable, which means its values cannot be changed directly.

The lesson also notes that it can be converted to a list with:

```python
list(my_tuple)
```

## 12. RGB colours

The Turtle colour mode is changed with:

```python
t.colormode(255)
```

An RGB colour is represented by a tuple:

```python
(r, g, b)
```

Each value is generated between 0 and 255:

```python
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
```

The result can then be used as a Turtle colour.

## 13. Functions for reusable drawing logic

The lesson introduces reusable drawing functions such as:

```python
draw_shape(num_sides)
random_color()
draw_spirograph(size_of_gap)
```

Instead of repeating drawing logic, the program gives the repeated operation a function name.

## 14. Building a Spirograph

The Spirograph repeatedly draws circles.

After every circle, the heading changes:

```python
tim.setheading(tim.heading() + size_of_gap)
```

The number of circles is calculated with:

```python
int(360 / size_of_gap)
```

This allows the drawing to cover a full rotation.

## 15. Extracting colours from an image

The Hirst project includes an earlier Colorgram step:

```python
colors = colorgram.extract(..., 30)
```

Each extracted colour provides RGB values.

The original code then builds tuples:

```python
new_color = (r, g, b)
```

and stores them inside:

```python
rgb_colors
```

The final project no longer needs Colorgram while running because the extracted colour tuples are already stored in `color_list`.

## 16. The Hirst Painting grid

The final project draws:

```python
number_of_dots = 100
```

The loop creates one dot at a time.

After every 10 dots:

```python
if dot_count % 10 == 0:
```

the Turtle moves up one row and returns to the left side.

This produces a 10 by 10 grid.

## 17. Modulo in a graphical program

The modulo operator is used to determine when one row is complete:

```python
dot_count % 10 == 0
```

This is a practical use of `%` beyond the earlier even-or-odd exercises.

## 18. Separating experimentation from the final project

Day 18 contains many small drawing experiments before the final Hirst Painting.

Keeping each challenge in `lessons/` makes it possible to revise each concept separately while keeping `main.py` focused on the final project.

## Running the final project

From the repository root:

```bash
python "Day 18 - Turtle Graphics and Hirst Painting/main.py"
```

## External packages

The final Hirst Painting does not need an external package beyond Python's Turtle and Random modules.

Some lesson or version files use external packages.

Install them with:

```bash
pip install -r "Day 18 - Turtle Graphics and Hirst Painting/requirements.txt"
```

The `color_extraction.py` file also needs the original image file used in the lesson.
