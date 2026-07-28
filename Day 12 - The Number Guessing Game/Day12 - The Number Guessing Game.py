# =============================================================================
# DAY 12 - THE NUMBER GUESSING GAME
# =============================================================================
#
# Main lessons:
# 1. Namespaces
# 2. Local scope
# 3. Global scope
# 4. Block scope
# 5. Modifying global variables
# 6. Returning values instead of modifying global variables
# 7. Global constants
#
# The lesson examples remain commented because some of them intentionally
# demonstrate errors. The three challenge solutions are uncommented exactly
# as written in the original Day 12 file.
#
# When this file is executed, the three Number Guessing Game solutions run
# one after another.
# =============================================================================


# =============================================================================
# LESSON 1: NAMESPACES AND SCOPES
# =============================================================================
#
# A namespace is where Python keeps names such as variables and functions.
#
# The variable created outside the function is global.
# The variable created inside increase_enemies() is local.
#
# Even though both variables have the name enemies, they are different
# variables because they exist in different scopes.
#
# Expected output:
# enemies inside function: 2
# enemies outside function: 1
#
# enemies = 1 
#
# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# =============================================================================
# LESSON 2: LOCAL SCOPE
# =============================================================================
#
# A variable created inside a function only exists inside that function.
#
# potion_strength can be printed inside drink_potion().
# It cannot be accessed outside drink_potion().
#
# The last line intentionally causes a NameError because potion_strength
# does not exist in the global scope.
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)


# =============================================================================
# LESSON 3: GLOBAL SCOPE
# =============================================================================
#
# player_health is created outside every function, so it has global scope.
#
# A function can read a global variable without using the global keyword.
# The global keyword is only needed when a function assigns a new value to
# the global variable.
#
# game() contains another function named drink_potion().
# This is called a nested function.
#
# In this exact example, game() is not called. Only print(player_health)
# executes, so the output is 10.
#
# player_health = 10 
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#
#     drink_potion()
#
# print(player_health)


# =============================================================================
# LESSON 4: PYTHON DOES NOT HAVE BLOCK SCOPE
# =============================================================================
#
# An if statement does not create a separate scope in Python.
#
# Because game_level is 3, the condition game_level < 5 is True.
# new_enemy is created inside the if statement and can still be accessed
# after the if statement.
#
# game_level = 3
# enemies = ["Skeletion", "Zombie", "Alien"]
#
# if game_level < 5: 
#     new_enemy = enemies[0]
#
# print(new_enemy)


# =============================================================================
# LESSON 5: BLOCKS INSIDE A FUNCTION
# =============================================================================
#
# The if statement does not create a new scope, but create_enemy() does.
#
# new_enemy belongs to the local scope of create_enemy().
# If game_level < 5 is False, new_enemy will not be created and attempting
# to print it will cause an error.
#
# def create_enemy(): 
#     if game_level < 5: 
#         new_enemy = enemies[0]
#
#     print(new_enemy)


# =============================================================================
# CODING EXERCISE: PRIME NUMBER CHECKER
# =============================================================================
#
# A prime number is greater than 1 and can only be divided evenly by 1 and
# itself.
#
# num % i gives the remainder after division.
# If the remainder is 0, num can be divided evenly by i, so it is not prime.
#
# return False is inside the loop because the function should stop as soon
# as it finds one divisor.
#
# The final return True is outside the loop. Python reaches it only after
# checking every possible divisor without finding one.
#
# def is_prime(num):
#     if num == 2:
#         return True
#     if num == 1:
#         return False
#
#     # Loop through all the numbers between 2 and the number
#     for i in range(2, num):
#         # Check if the number (num) can be divided by the potential prime number
#         if num % i == 0:
#             return False
#
#     # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
#     return True


# =============================================================================
# LESSON 6: MODIFYING GLOBAL SCOPE
# =============================================================================
#
# enemies is a global variable.
#
# The global keyword tells Python that enemies inside the function refers to
# the global variable instead of a new local variable.
#
# enemies += 1 means:
# enemies = enemies + 1
#
# The global value changes from 1 to 2.
#
# enemies = 1 
#
# def increase_enemies():
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# =============================================================================
# LESSON 7: RETURNING A MODIFIED VALUE
# =============================================================================
#
# A better practice is to pass the current value into a function and return
# the new value instead of directly modifying a global variable.
#
# increase_enemies(enemies) receives the current value.
# return enemy + 1 sends the new value back.
# The returned value is saved again in enemies.
#
# enemies = 1 
#
# def increase_enemies(enemy):
#     print(f"enemies inside function: {enemies}")
#     return enemy + 1
#
# enemies = increase_enemies(enemies)
# print(f"enemies outside function : {enemies}")


# =============================================================================
# LESSON 8: GLOBAL CONSTANTS
# =============================================================================
#
# Constants are values that are not intended to change while the program runs.
#
# Python does not prevent a constant from being changed. Writing its name in
# uppercase is a convention that tells programmers to treat it as fixed.
#
# A function can read a global constant.
#
# PI = 3.14159
# GOOGLE_URL = "https://www.google.com"
#
#
# def my_func():
#     print(GOOGLE_URL)
#
# my_func()


# =============================================================================
# CODING CHALLENGE DAY 12
# SOLUTION 1: MY ORIGINAL VERSION
# =============================================================================
#
# This solution uses separate loops and attempt variables for easy and hard.
#
# break stops the while loop when the player guesses correctly.
# Each wrong guess reduces the appropriate attempts variable by 1.
#
# This solution is preserved exactly as written.
# =============================================================================

import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
choosen_number = random.randint(0, 100)
print(choosen_number)


hard_attempts = 5
easy_attempts = 10

if difficulty == "hard": 
    while hard_attempts > 0: 
        guess = int(input("Make a guess: "))
        if guess == choosen_number: 
            print(f"You got it! The answer was {choosen_number}")
            break
        elif guess > choosen_number: 
            print("Too High")
            print("Guess again.")
            hard_attempts -= 1
            print(f"You have {hard_attempts} remaining to guess the number.")
        elif guess < choosen_number:  
            print("Too Low")
            print("Guess again.")
            hard_attempts -= 1 
            if hard_attempts == 0: 
                print("You lose. ")
            else:
                print(f"You have {hard_attempts} remaining to guess the number.") 

elif difficulty == "easy": 
    while easy_attempts > 0: 
        guess = int(input("Make a guess: "))
        if guess == choosen_number: 
            print(f"You got it! The answer was {choosen_number}")
            break
        elif guess > choosen_number: 
            print("Too High")
            print("Guess again.")
            easy_attempts -= 1
            print(f"You have {easy_attempts} remaining to guess the number.")
        elif guess < choosen_number:  
            print("Too Low")
            print("Guess again.")
            easy_attempts -= 1 
            if easy_attempts == 0: 
                print("You lose. ")
            else:
                print(f"You have {easy_attempts} remaining to guess the number.")


# =============================================================================
# CODING CHALLENGE DAY 12
# SOLUTION 2: FUNCTION VERSION
# =============================================================================
#
# This version uses one attempts variable for both difficulty levels.
#
# The game() function receives the guess, answer, and remaining attempts.
# It returns two values:
# 1. The updated attempts
# 2. A Boolean that says whether the game is over
#
# attempts -= 1 appears after the correct-answer check because a correct
# guess should not remove an attempt.
#
# It appears before the high-or-low check because both a high guess and a
# low guess are wrong and must remove one attempt.
#
# This solution is preserved exactly as written.
# =============================================================================

import random
from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

chosen_number = random.randint(1, 100)

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10


def game(player_number, right_number, attempts):
    if player_number == right_number:
        print(f"You got it! The answer was {right_number}.")
        return attempts, True

    attempts -= 1

    if player_number > right_number:
        print("Too high.")
    else:
        print("Too low.")

    if attempts == 0:
        print(f"You lose. The correct answer was {right_number}.")
        return attempts, True

    print("Guess again.")
    print(f"You have {attempts} attempts remaining.")
    return attempts, False


if difficulty == "hard":
    attempts = HARD_ATTEMPTS
elif difficulty == "easy":
    attempts = EASY_ATTEMPTS
else:
    print("Invalid difficulty.")
    attempts = 0

game_over = False

while attempts > 0 and not game_over:
    guess = int(input("Make a guess: "))

    attempts, game_over = game(
        guess,
        chosen_number,
        attempts
    )


# =============================================================================
# CODING CHALLENGE DAY 12
# SOLUTION 3: ANGELA'S VERSION
# =============================================================================
#
# check_answer() has one job: compare the guess with the actual answer and
# return the number of turns remaining.
#
# set_difficulty() has one job: return 10 turns for easy or 5 turns otherwise.
#
# game() organizes the complete game.
#
# return turns - 1 calculates the reduced value and sends it back.
# turns = check_answer(...) saves the returned value into turns.
#
# return inside game() stops the entire function when the attempts reach 0.
#
# This solution is preserved exactly as written.
# =============================================================================

from random import randint
from art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")




game()
