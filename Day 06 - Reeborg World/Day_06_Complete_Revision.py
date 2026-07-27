"""
Day 6: Python Functions, while Loops, and Reeborg's World

Topics covered:
1. Defining and calling functions
2. Why functions are useful
3. for loops compared with while loops
4. while conditions
5. Using not in a while condition
6. Avoiding infinite loops
7. Creating turn_right() in Reeborg's World
8. Hurdle challenges 1 to 4
9. Maze challenge using the right-hand rule

Important:
The first lessons in this file run in normal Python.

The Reeborg solutions use special commands such as move(),
turn_left(), wall_in_front(), and at_goal(). Those commands exist
only inside Reeborg's World, so the Reeborg code is stored as
multi-line strings for revision and copying.

Run this file from the main course folder with:

    python "Day 06 - Reeborg World/Day_06_Complete_Revision.py"
"""


# ============================================================
# LESSON 1: DEFINING AND CALLING A FUNCTION
# ============================================================

print("=== Lesson 1: Functions ===")


def greet():
    """Print a simple greeting."""
    print("Hello")
    print("Bye!")


# Defining a function does not run it.
# The function runs only when it is called.
greet()


# ============================================================
# LESSON 2: WHY FUNCTIONS ARE USEFUL
# ============================================================

print("\n=== Lesson 2: Reusing Functions ===")


def print_separator():
    """Print a separator line."""
    print("=" * 40)


print_separator()
print("Functions prevent repeated code.")
print_separator()


# ============================================================
# LESSON 3: FOR LOOPS AND WHILE LOOPS
# ============================================================

print("\n=== Lesson 3: for Compared with while ===")

# A for loop is useful when the number of repetitions is known.
print("for loop:")

for number in range(1, 4):
    print(number)

# A while loop is useful when repetition depends on a condition.
print("while loop:")

count = 1

while count <= 3:
    print(count)
    count += 1


# ============================================================
# LESSON 4: HOW A WHILE LOOP WORKS
# ============================================================

print("\n=== Lesson 4: while Conditions ===")

steps_remaining = 3

while steps_remaining > 0:
    print(f"Steps remaining: {steps_remaining}")
    steps_remaining -= 1

print("The while loop has finished.")


# ============================================================
# LESSON 5: USING not WITH while
# ============================================================

print("\n=== Lesson 5: while not ===")

goal_reached = False
moves = 0

while not goal_reached:
    moves += 1
    print(f"Move {moves}")

    if moves == 3:
        goal_reached = True

print("Goal reached.")


# ============================================================
# LESSON 6: AVOIDING INFINITE LOOPS
# ============================================================

print("\n=== Lesson 6: Avoiding Infinite Loops ===")

attempts = 0

while attempts < 3:
    print(f"Attempt {attempts + 1}")
    attempts += 1

# The variable affecting the condition must eventually change.
# Otherwise, the loop may run forever.


# ============================================================
# REEBORG REFERENCE: AVAILABLE COMMANDS
# ============================================================

REEBORG_REFERENCE = r'''
Common Reeborg commands:

    move()
    turn_left()

Common Reeborg conditions:

    at_goal()
    front_is_clear()
    wall_in_front()
    right_is_clear()
    wall_on_right()

Reeborg does not provide turn_right(), so we create it by
turning left three times.
'''


# ============================================================
# REEBORG HELPER FUNCTIONS
# ============================================================

REEBORG_HELPER_FUNCTIONS = r'''
def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()
'''


# ============================================================
# HURDLE 1: FIXED NUMBER OF HURDLES
# ============================================================

HURDLE_1_SOLUTION = r'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# The course world contains exactly six hurdles.
for _ in range(6):
    jump()
'''


# ============================================================
# HURDLE 2: UNKNOWN NUMBER OF HURDLES
# ============================================================

HURDLE_2_SOLUTION = r'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    jump()
'''


# ============================================================
# HURDLE 3: HURDLES APPEAR IN DIFFERENT POSITIONS
# ============================================================

HURDLE_3_SOLUTION = r'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
'''


# ============================================================
# HURDLE 4: HURDLES HAVE DIFFERENT HEIGHTS
# ============================================================

HURDLE_4_SOLUTION = r'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    # Begin climbing the left side of the hurdle.
    turn_left()

    # Continue upward until the robot reaches the top.
    while wall_on_right():
        move()

    # Move across the top of the hurdle.
    turn_right()
    move()

    # Face downward on the other side.
    turn_right()

    # Continue downward until the ground blocks the robot.
    while front_is_clear():
        move()

    # Face forward again.
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
'''


# ============================================================
# DAY 6 PROJECT: MAZE
# ============================================================

MAZE_SOLUTION = r'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Move forward until the robot first reaches a wall.
while front_is_clear():
    move()

# Turn so the robot begins following the wall on its right.
turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
'''


# ============================================================
# DAY 6 REVISION NOTES
# ============================================================

# Define a function:
#
#     def function_name():
#         code
#
# Call a function:
#
#     function_name()
#
# Use a for loop when the number of repetitions is known:
#
#     for _ in range(6):
#         jump()
#
# Use a while loop when repetition depends on a condition:
#
#     while not at_goal():
#         move()
#
# Boolean helper functions must be called with parentheses:
#
#     at_goal()
#     wall_in_front()
#     front_is_clear()
#
# Correct:
#
#     if wall_in_front():
#
# Incorrect:
#
#     if wall_in_front:
#
# Use if, elif, and else when only one action should happen.
#
# The maze follows the right-hand rule:
#
#     1. Prefer turning right.
#     2. Otherwise move forward.
#     3. Otherwise turn left.
#
# Reeborg code cannot run in a normal Python terminal because
# commands such as move() and turn_left() are supplied by the
# Reeborg website, not by standard Python.


# ============================================================
# DISPLAY INFORMATION
# ============================================================

print("\n=== Reeborg Revision Code ===")
print(
    "The Reeborg solutions are stored inside this file as "
    "multi-line strings."
)
print(
    "Open the file in VS Code and copy the required solution "
    "into Reeborg's World."
)
