# Day 11: Blackjack Capstone Project
#
# Topics reviewed in this project:
# 1. Functions
# 2. Functions with outputs
# 3. Lists
# 4. Dictionaries are not used in this project
# 5. while loops
# 6. for loops
# 7. if, elif, and else
# 8. Boolean variables
# 9. Importing modules
# 10. random.choice()
# 11. sum()
# 12. len()
# 13. append()
# 14. remove()
# 15. return
# 16. Docstrings
#
# The Blackjack project below is kept exactly as written
# in the original Day 11 file.


# #blackjack capstone project: 
# #my version

# import random
# import art

# def deal_card():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     return random.choice(cards)


# def calculate_score(list_of_cards):
#     score = sum(list_of_cards)

#     # Blackjack: exactly two cards with a total of 21
#     if score == 21 and len(list_of_cards) == 2:
#         return 0

#     # Change an Ace from 11 to 1 if the score is over 21
#     if score > 21 and 11 in list_of_cards:
#         list_of_cards.remove(11)
#         list_of_cards.append(1)

#     return sum(list_of_cards)


# def compare(user_score, computer_score):
#     if user_score == computer_score:
#         print("It's a draw.")

#     elif computer_score == 0:
#         print("You lose. Computer has blackjack.")

#     elif user_score == 0:
#         print("You win with blackjack.")

#     elif user_score > 21:
#         print("You lose. Your score is over 21.")

#     elif computer_score > 21:
#         print("You win. Computer's score is over 21.")

#     elif user_score > computer_score:
#         print("You win.")

#     else:
#         print("You lose.")


# keep_playing = True

# while keep_playing:
#     choice = input(
#         "Do you want to play a game of Blackjack? Type 'y' or 'n': "
#     ).lower()

#     if choice == "n":
#         keep_playing = False
#         print("Goodbye.")
#         continue

#     if choice != "y":
#         print("Invalid choice. Type 'y' or 'n'.")
#         continue

#     # Clear the previous output and display the logo
#     print("\n" * 18)
#     print(art.logo)
    
#     user_cards = []
#     computer_cards = []

#     user_cards.append(deal_card())
#     user_cards.append(deal_card())

#     computer_cards.append(deal_card())
#     computer_cards.append(deal_card())

#     game_over = False

#     # User's turn
#     while not game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)

#         print(f"Your cards: {user_cards}")
#         print(f"Your score: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")

#         if user_score == 0:
#             game_over = True

#         elif computer_score == 0:
#             game_over = True

#         elif user_score > 21:
#             game_over = True

#         elif user_score == 21:
#             game_over = True

#         else:
#             another_card = input(
#                 "Type 'y' to get another card, type 'n' to pass: "
#             ).lower()

#             if another_card == "y":
#                 user_cards.append(deal_card())

#             elif another_card == "n":
#                 game_over = True

#             else:
#                 print("Invalid choice. Type 'y' or 'n'.")

#     # Recalculate after the user's final card
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)

#     # Computer's turn
#     if user_score <= 21 and user_score != 0 and computer_score != 0:
#         while computer_score < 17:
#             computer_cards.append(deal_card())
#             computer_score = calculate_score(computer_cards)

#     print(f"\nYour final cards: {user_cards}")
#     print(f"Your final score: {user_score}")
#     print(f"Computer's final cards: {computer_cards}")
#     print(f"Computer's final score: {computer_score}")

#     compare(user_score, computer_score)


#Angela's version
import random
from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards """
    if sum(cards) == 21 and len(cards) == 2: 
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over, You lose 😭"
    elif c_score > 21:
        return "Opponent went over, You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else: 
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()

# ============================================================
# DAY 11 REVISION NOTES
# ============================================================

# deal_card()
#     Chooses and returns one random card from the cards list.
#
# calculate_score(cards)
#     Calculates the current hand score.
#
# A score of 0 represents Blackjack:
#
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#
# If an Ace causes the score to go over 21:
#
#     cards.remove(11)
#     cards.append(1)
#
# This changes one Ace from 11 to 1.
#
# compare(u_score, c_score)
#     Compares the final user and computer scores.
#
# play_game()
#     Controls one complete game of Blackjack.
#
# The first for loop deals two cards:
#
#     for _ in range(2):
#
# The user's turn continues with:
#
#     while not is_game_over:
#
# The computer draws until reaching at least 17:
#
#     while computer_score != 0 and computer_score < 17:
#
# The outer while loop starts a new game whenever the user types "y".
#
# The value -1 is used before the first real score is calculated.
#
# The logo is stored in art.py and imported with:
#
#     from art import logo
#
# Keep Day_11_Complete_Revision.py and art.py in the same folder.

