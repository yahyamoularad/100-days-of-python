# Day 21 Lesson: Class Inheritance
#
# This example comes from the original Day 21 file.
#
# Inheritance allows a child class to use attributes and methods
# defined by a parent class.


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        # Call the parent class constructor.
        super().__init__()

    def breathe(self):
        # Call the parent method first.
        super().breathe()

        # Then add behavior specific to Fish.
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
