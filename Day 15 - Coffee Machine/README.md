# Day 15: Coffee Machine

## Folder structure

```text
Day 15 - Coffee Machine/
├── main.py
├── my_version.py
├── Coffee_Machine_Program_Requirements.pdf
└── README.md
```

## Files

### `main.py`

This is the final Day 15 Coffee Machine project version.

The project structure and logic are preserved. Explanatory comments were added around the existing sections.

### `my_version.py`

This is the original personal solution, uncommented so it can be reviewed separately from the final version.

Its purpose is to preserve the learning progression from the first attempt to the final solution.

### `Coffee_Machine_Program_Requirements.pdf`

The original project requirements are included for reference.

## Project requirements

The program is expected to:

1. Repeatedly ask the user what drink they want.
2. Turn off when the user enters `off`.
3. Print the current resources when the user enters `report`.
4. Check whether enough ingredients are available.
5. Ask the user to insert coins.
6. Check whether the transaction is successful.
7. Return change when necessary.
8. Deduct ingredients after making a drink.
9. Track the money earned by the machine.

## Lessons learned

### 1. Working with nested dictionaries

The menu is stored as a dictionary containing other dictionaries.

Example:

```python
MENU["latte"]["ingredients"]["water"]
```

This accesses the amount of water required for a latte.

The same structure stores the drink cost:

```python
MENU["latte"]["cost"]
```

### 2. Using dictionaries to represent program state

The machine resources are stored in one dictionary:

```python
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
```

The values change as drinks are made.

For example:

```python
resources[item] -= order_ingredients[item]
```

This updates the machine after consuming an ingredient.

### 3. Breaking a larger program into functions

The final project separates responsibilities into functions:

```python
is_resource_sufficient()
process_coins()
is_transaction_successful()
make_coffee()
```

Each function handles one part of the coffee machine.

This makes the main loop easier to read.

### 4. Functions with parameters

Some functions receive information from the main program.

Example:

```python
is_resource_sufficient(order_ingredients)
```

The function does not need to know which drink was chosen. It only needs the ingredient dictionary passed to it.

### 5. Functions with return values

Functions can send results back to the caller.

Examples:

```python
return True
return False
return total
```

The program can then use those returned values inside `if` statements.

### 6. Looping through a dictionary

The project uses:

```python
for item in order_ingredients:
```

This allows the same resource-checking and deduction logic to work for different drinks.

### 7. Using Boolean values to control a program

The coffee machine begins with:

```python
is_on = True
```

The main loop continues with:

```python
while is_on:
```

When the user enters:

```text
off
```

the program changes:

```python
is_on = False
```

and the machine stops.

### 8. Keeping track of profit

The final project uses:

```python
profit = 0
```

When a transaction succeeds:

```python
profit += drink_cost
```

The value remains available for the next order and appears in the report.

### 9. Using `global`

`profit` is created outside the transaction function.

Inside `is_transaction_successful()`, the program uses:

```python
global profit
```

so that the function can update the same `profit` variable.

### 10. Processing several coin types

The project calculates the total value of quarters, dimes, nickels, and pennies.

Example:

```python
total = int(input("how many quarters?: ")) * 0.25
total += int(input("how many dimes?: ")) * 0.1
```

This demonstrates accumulating values into one variable.

### 11. Rounding monetary values

Change is calculated with:

```python
round(money_received - drink_cost, 2)
```

This keeps the displayed change to two decimal places.

### 12. Reusing the same program logic for several drinks

Instead of writing completely separate programs for espresso, latte, and cappuccino, the final version selects:

```python
drink = MENU[choice]
```

The same functions then operate on the selected drink.

This is one of the main improvements compared with the first version.

## Running the final project

From the main `100-days-of-python` repository:

```bash
python "Day 15 - Coffee Machine/main.py"
```

## Running the original version

```bash
python "Day 15 - Coffee Machine/my_version.py"
```

## GitHub

Only source files and useful documentation should be committed. Files such as `__pycache__/` and `.pyc` files should remain ignored.
