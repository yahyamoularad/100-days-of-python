"""
Day 7: Hangman

This revision uses only concepts already present in the original Day 7 code:

1. import
2. random.choice()
3. variables
4. lists
5. for loops
6. while loops
7. if, elif, and else
8. len()
9. input()
10. lower()
11. append()
12. in and not in
13. f-strings
"""

import random

from hangman_words import word_list
from hangman_art import stages, logo


# ============================================================
# LESSON 1: CHOOSE A RANDOM WORD
# ============================================================

chosen_word = random.choice(word_list)


# ============================================================
# LESSON 2: CREATE THE PLACEHOLDER
# ============================================================

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"


# ============================================================
# LESSON 3: STARTING GAME VALUES
# ============================================================

lives = 6
game_over = False

# This list stores every letter already guessed.
guessed_letters = []


# ============================================================
# DAY 7 PROJECT: HANGMAN
# ============================================================

print(logo)
print("Welcome to Hangman.")
print("Word to guess: " + placeholder)


while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    # Check whether the player already entered this guess.
    if guess in guessed_letters:
        print(f"You have already guessed {guess}.")

    else:
        guessed_letters.append(guess)

        display = ""

        # Rebuild the displayed word after every new guess.
        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        # Remove one life only when this is a new wrong guess.
        if guess not in chosen_word:
            lives -= 1
            print(
                f"You guessed {guess}, that is not in the word. "
                "You lose a life."
            )

            if lives == 0:
                game_over = True
                print(
                    f"***********************IT WAS {chosen_word}! "
                    "YOU LOSE***********************"
                )

        # If no underscore remains, every letter was guessed.
        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

        print(stages[lives])


# ============================================================
# DAY 7 REVISION NOTES
# ============================================================

# random.choice(word_list)
#     Chooses one random word from the list.
#
# len(chosen_word)
#     Returns the number of letters in the chosen word.
#
# for position in range(word_length):
#     Repeats once for every letter in the word.
#
# while not game_over:
#     Keeps running while game_over is False.
#
# guess in guessed_letters
#     Checks whether the guess was already saved.
#
# guess not in chosen_word
#     Checks whether the guessed letter is absent from the word.
#
# guessed_letters.append(guess)
#     Adds the guess to the list.
#
# "_" not in display
#     Means every hidden letter has been revealed.
#
# lower()
#     Converts the user's input to lowercase.
#
# Why guessed_letters is a list:
#
# The program needs to remember many previous guesses.
# A string such as display has another purpose:
# it represents the current visible version of the hidden word.
#
# Why display is rebuilt:
#
# Python strings cannot be changed one character at a time.
# The program creates a new display string during every turn.
