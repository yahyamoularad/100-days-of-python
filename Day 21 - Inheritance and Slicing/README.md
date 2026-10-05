# Day 21: Inheritance and Slicing

## Folder structure

```text
Day 21 - Inheritance and Slicing/
├── main.py
├── README.md
└── lessons/
    ├── class_inheritance.py
    └── list_and_tuple_slicing.py
```

## Important note

The uploaded Day 21 file does not contain a separate new final project.

Its own note says:

```text
Go back to day 20 for the remaining parts of the snake game
```

For that reason, no new Snake Game implementation was invented or copied into this folder.

The completed Snake Game remains in Day 20.

Day 21 focuses on:

1. class inheritance
2. list and tuple slicing

# Lessons learned

## 1. Class inheritance

Inheritance allows one class to receive attributes and methods from another class.

The example uses:

```python
class Animal:
```

as the parent class and:

```python
class Fish(Animal):
```

as the child class.

## 2. Parent and child classes

In this example:

```text
Animal
  ↑
Fish
```

`Animal` is the parent.

`Fish` is the child.

The child can reuse behavior from the parent.

## 3. Calling the parent constructor

The Fish constructor contains:

```python
super().__init__()
```

This calls the constructor of `Animal`.

The Animal constructor creates:

```python
self.num_eyes = 2
```

so a Fish object receives that inherited attribute.

## 4. Inheriting methods

Animal defines:

```python
def breathe(self):
    print("Inhale, exhale.")
```

Fish inherits that behavior.

## 5. Extending an inherited method

Fish defines:

```python
def breathe(self):
    super().breathe()
    print("doing this underwater.")
```

`super().breathe()` runs the parent implementation first.

Fish then adds its own behavior.

## 6. Child-specific methods

Fish also defines:

```python
def swim(self):
    print("moving in water.")
```

This method belongs specifically to Fish.

## 7. Creating a child object

The lesson creates:

```python
nemo = Fish()
```

`nemo` is an instance of Fish.

## 8. Python slicing

The general slicing syntax is:

```python
sequence[start:stop:step]
```

The stop index is not included.

## 9. Slice between two indexes

```python
piano_keys[2:5]
```

starts at index 2 and stops before index 5.

## 10. Slice from an index to the end

```python
piano_keys[2:]
```

starts at index 2 and continues to the end.

## 11. Slice from the beginning

```python
piano_keys[:5]
```

starts at the beginning and stops before index 5.

## 12. Slice with a step

```python
piano_keys[2:5:2]
```

uses a step of 2.

## 13. Take every second item

```python
piano_keys[::2]
```

uses the whole list and takes every second element.

## 14. Reverse a sequence

```python
piano_keys[::-1]
```

uses a step of `-1`, which traverses the sequence backwards.

## 15. Slicing tuples

The lesson also uses:

```python
piano_tuple[2:5]
```

showing that slicing works with tuples too.

## 16. Connection with Day 20

Day 20 used:

```python
snake.segments[1:]
```

for tail-collision detection.

Day 21 explains why that works.

Because the snake head is at index 0, starting the slice at index 1 excludes the head and keeps only the body segments.

## Running Day 21

From the repository root:

```bash
python "Day 21 - Inheritance and Slicing/main.py"
```

Run only the inheritance lesson:

```bash
python "Day 21 - Inheritance and Slicing/lessons/class_inheritance.py"
```

Run only the slicing lesson:

```bash
python "Day 21 - Inheritance and Slicing/lessons/list_and_tuple_slicing.py"
```

## Dependencies

Day 21 does not require external Python packages.
