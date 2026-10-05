# Day 21: Class Inheritance and Slicing
#
# This day contains lesson examples rather than a separate new final project.
#
# The original Day 21 notes explicitly say:
# "Go back to day 20 for the remaining parts of the snake game"
#
# The two Day 21 topics are:
# 1. Class inheritance
# 2. Python slicing for lists and tuples


# ============================================================
# CLASS INHERITANCE
# ============================================================

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        # Run the parent constructor so Fish receives
        # attributes initialized by Animal.
        super().__init__()

    def breathe(self):
        # Run Animal.breathe() first, then add Fish behavior.
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()


# ============================================================
# LIST AND TUPLE SLICING
# ============================================================

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

# Index 2 up to, but not including, index 5.
print(piano_keys[2:5])

# Index 2 to the end.
print(piano_keys[2:])

# Beginning up to, but not including, index 5.
print(piano_keys[:5])

# Index 2 to 5, taking every second item.
print(piano_keys[2:5:2])

# Entire list, taking every second item.
print(piano_keys[::2])

# Reverse the list.
print(piano_keys[::-1])

# Tuples can also be sliced.
print(piano_tuple[2:5])
