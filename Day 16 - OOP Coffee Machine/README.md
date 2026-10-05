# Day 16: Object-Oriented Programming Coffee Machine

## Folder structure

```text
Day 16 - OOP Coffee Machine/
├── main.py
├── coffee_maker.py
├── menu.py
├── money_machine.py
├── lessons/
│   └── oop_basics.py
├── Coffee_Machine_Classes_Documentation.pdf
├── requirements.txt
└── README.md
```

## Final project

The final Coffee Machine project keeps the original four-file structure:

```text
main.py
coffee_maker.py
menu.py
money_machine.py
```

`main.py` coordinates objects created from the three main classes.

## Lesson examples

The commented examples from `Day16-start.py` were moved into:

```text
lessons/oop_basics.py
```

They were uncommented and organized without replacing them with newer concepts.

The lesson file contains the original ideas about:

- procedural programming compared with Object-Oriented Programming
- classes as blueprints
- objects
- attributes
- methods
- two ways of importing Turtle
- accessing object attributes
- calling object methods
- using PrettyTable

## Lessons learned

### 1. Procedural programming compared with OOP

Before Day 16, most programs were organized around variables, functions, loops, and conditions.

Object-Oriented Programming introduces another way to organize a program by grouping related data and behavior into objects.

The waiter example from the lesson separates:

```text
Attributes: what the object has
Methods:    what the object does
```

For example, a waiter could have:

```python
is_holding_plate = True
tables_responsible = [4, 5, 6]
```

and methods such as:

```python
take_order()
take_payment()
```

### 2. A class is a blueprint

A class describes what objects of that type contain and what they can do.

The lesson uses:

```python
timmy = Turtle()
```

`Turtle` is the class.

`timmy` is an object created from that class.

The same class can be used to create many different objects.

### 3. Class names use PascalCase

Examples from Day 16 include:

```python
Turtle
Screen
PrettyTable
MenuItem
Menu
CoffeeMaker
MoneyMachine
```

### 4. Accessing attributes

An attribute stores data belonging to an object.

The syntax learned is:

```python
object.attribute
```

For example:

```python
my_screen.canvheight
```

In the Coffee Machine project:

```python
drink.cost
drink.ingredients
order.name
```

are also attributes.

### 5. Calling methods

A method is a function associated with an object.

The syntax is:

```python
object.method()
```

Examples from the lessons:

```python
timmy.shape("turtle")
timmy.forward(100)
my_screen.exitonclick()
```

Examples from the Coffee Machine:

```python
menu.get_items()
coffee_maker.report()
money_machine.report()
menu.find_drink(choice)
coffee_maker.make_coffee(drink)
```

### 6. Creating objects from classes

The final project creates three main objects:

```python
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
```

Each object has its own responsibility.

### 7. The `__init__` method

The supplied Day 16 classes use `__init__` to set the starting attributes of new objects.

For example, `CoffeeMaker` creates:

```python
self.resources
```

and `MoneyMachine` creates:

```python
self.profit
self.money_received
```

### 8. Understanding `self`

Inside a class, `self` refers to the current object.

For example:

```python
self.resources
```

means the resources belonging to a particular `CoffeeMaker` object.

Similarly:

```python
self.profit
```

belongs to a `MoneyMachine` object.

### 9. Objects can contain other objects

The `Menu` object contains a list of `MenuItem` objects.

Each `MenuItem` contains attributes such as:

```python
name
cost
ingredients
```

This means the program can work with a drink as one object instead of passing separate values everywhere.

### 10. Methods can receive objects

The class documentation shows that:

```python
is_resource_sufficient(drink)
```

receives a `MenuItem` object.

The method can then access:

```python
drink.ingredients
```

The same idea appears in:

```python
make_coffee(order)
```

where the `order` is also a `MenuItem`.

### 11. Separating responsibilities between classes

The final project separates the Coffee Machine into different responsibilities.

#### `Menu`

Responsible for available drinks.

Important methods:

```python
get_items()
find_drink()
```

#### `CoffeeMaker`

Responsible for ingredients and making drinks.

Important methods:

```python
report()
is_resource_sufficient()
make_coffee()
```

#### `MoneyMachine`

Responsible for payment.

Important methods:

```python
report()
process_coins()
make_payment()
```

This is a major difference from the procedural Day 15 project, where most state and functions were kept together in one file.

### 12. `main.py` coordinates the objects

The main program does not contain all of the internal details.

Instead, it asks the objects to perform work:

```python
options = menu.get_items()
drink = menu.find_drink(choice)
coffee_maker.is_resource_sufficient(drink)
money_machine.make_payment(drink.cost)
coffee_maker.make_coffee(drink)
```

This makes `main.py` responsible for the overall program flow while the classes handle their own responsibilities.

### 13. Importing classes from other files

The final project imports classes with:

```python
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
```

This allows the project to be divided into several Python files instead of putting every class in `main.py`.

## Class documentation

`Coffee_Machine_Classes_Documentation.pdf` is included as the original reference for the classes and their methods.

It documents:

- `MenuItem`
- `Menu`
- `CoffeeMaker`
- `MoneyMachine`

## Running the final project

From the root of the `100-days-of-python` repository:

```bash
python "Day 16 - OOP Coffee Machine/main.py"
```

## Running the lesson examples

The PrettyTable lesson requires the `prettytable` package.

Install the project dependency inside the virtual environment:

```bash
pip install -r "Day 16 - OOP Coffee Machine/requirements.txt"
```

Then run:

```bash
python "Day 16 - OOP Coffee Machine/lessons/oop_basics.py"
```

The Turtle section opens a graphical window. Close the Turtle window to allow the script to continue to the PrettyTable example.

## Day 15 compared with Day 16

Day 15 implemented the Coffee Machine procedurally with dictionaries and functions.

Day 16 reorganizes the same type of program using objects.

Instead of directly managing all resources and payments in the main file, Day 16 creates objects such as:

```python
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
```

The main program then interacts with those objects through their methods.

That transition is the central lesson of Day 16.
