# Day 17: Classes, Constructors, Attributes, and Methods
#
# These examples come from the original Day17-start.py file.
# Previously commented code has been uncommented and organized.
#
# No new lesson logic has been added.


# ============================================================
# LESSON 1: NAMING STYLES
# ============================================================

# PascalCase:
# The first letter of every word is capitalized.
#
# Example:
# CarCamshaftPulley
#
# camelCase:
# The first word begins with lowercase, and later words
# begin with uppercase letters.
#
# snake_case:
# Words are lowercase and separated with underscores.
#
# Class names are normally written using PascalCase.


# ============================================================
# LESSON 2: CREATING AN EMPTY CLASS
# ============================================================

class User:
    pass


# Create an object from the User class.
user_1 = User()

# Add attributes to the object.
user_1.id = "001"
user_1.username = "yahya"

print(user_1.username)


# Create another object from the same class.
user_2 = User()
user_2.id = "002"
user_2.name = "jack"


# ============================================================
# LESSON 3: USING THE CONSTRUCTOR
# ============================================================

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # A method always receives self as its first parameter.
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "yahya")
user_2 = User("002", "jack")


# ============================================================
# LESSON 4: OBJECTS INTERACTING THROUGH A METHOD
# ============================================================

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
