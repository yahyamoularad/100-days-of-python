# Day 14: Higher Lower Game

## Project files

```text
Day 14 - Higher Lower Game/
├── main.py
├── art.py
├── game_data.py
├── my_first_version.py
├── my_simplified_version.py
├── chatgpt_version.py
└── README.md
```

`main.py` is the final Day 14 project version.

The other three Python files preserve the earlier versions from the original Day 14 work so they can be reviewed separately without mixing several programs inside one file.

## Run the final project

From the main `100-days-of-python` repository:

```bash
python "Day 14 - Higher Lower Game/main.py"
```

## Lessons learned

### 1. Splitting a project into multiple Python files

Day 14 uses three main project files:

- `main.py` contains the game logic.
- `art.py` contains `logo` and `vs`.
- `game_data.py` contains the account data.

The imports used in the final project are:

```python
from art import logo, vs
from game_data import data
import random
```

This keeps the main program focused on the game logic.

### 2. A list can contain dictionaries

`game_data.py` stores many dictionaries inside the `data` list.

Each account has keys such as:

```python
"name"
"follower_count"
"description"
"country"
```

A value is accessed with its key:

```python
account["name"]
account["follower_count"]
```

### 3. Choosing random data

The game selects an account with:

```python
random.choice(data)
```

The returned value is one dictionary from the `data` list.

### 4. Functions can receive dictionaries

The final project passes one account dictionary into:

```python
format_data(account)
```

The function reads the account values and returns formatted text.

### 5. Functions can return Boolean results

`check_answer()` compares two follower counts and returns the result of a comparison such as:

```python
user_guess == "a"
```

That result is either `True` or `False`.

### 6. Keeping game state between rounds

The game starts with an `account_b`.

Inside the loop:

```python
account_a = account_b
account_b = random.choice(data)
```

This means the previous B becomes the next A.

That is how one account stays on screen after a correct answer.

### 7. Avoiding the same comparison

The project checks:

```python
if account_a == account_b:
    account_b = random.choice(data)
```

This reduces the chance of comparing an account with itself.

### 8. Repeating a game with a Boolean variable

The game uses:

```python
game_should_continue = True
```

and:

```python
while game_should_continue:
```

A wrong answer changes it to:

```python
game_should_continue = False
```

which ends the loop.

### 9. Score keeping

The score begins at:

```python
score = 0
```

and increases after a correct answer:

```python
score += 1
```

The score is preserved between rounds because it is created before the `while` loop.

### 10. Breaking a larger problem into smaller pieces

The final project separates two responsibilities into functions:

```python
format_data()
check_answer()
```

This makes the main game loop easier to read because formatting and answer checking are handled separately.

## Version progression

### `my_first_version.py`

The first version builds the game step by step and contains repeated display code.

### `my_simplified_version.py`

The repeated display work is moved into a `game()` function.

### `chatgpt_version.py`

The display and answer logic are separated into dedicated functions.

### `main.py`

The final course version uses:

```python
format_data()
check_answer()
```

and a single main `while` loop.

This progression shows how the same program can become easier to understand when repeated responsibilities are separated.
