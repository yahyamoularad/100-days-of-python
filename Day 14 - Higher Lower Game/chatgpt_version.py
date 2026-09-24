# Day 14: Higher Lower Game
# ChatGPT version from the original Day 14 file
#
# This version is uncommented from the original file.
# Its structure is preserved.
#
# Main ideas:
# - display_comparison() handles the display.
# - get_correct_answer() returns "a" or "b".
# - The winner becomes A for the next round.
# - A and B are prevented from being the same account.

# Chatgpt version : 
import random
import art
from game_data import data


def star_generator():
    return random.choice(data)


def display_comparison(person_a, person_b):
    print(art.logo)

    print(
        f"Compare A: {person_a['name']}, "
        f"{person_a['description']}, "
        f"{person_a['country']}"
    )
    print(person_a["follower_count"])

    print(art.vs)

    print(
        f"Against B: {person_b['name']}, "
        f"{person_b['description']}, "
        f"{person_b['country']}"
    )
    print(person_b["follower_count"])


def get_correct_answer(person_a, person_b):
    if person_a["follower_count"] > person_b["follower_count"]:
        return "a"
    else:
        return "b"


A = star_generator()
B = star_generator()

# Prevent comparing the same person
while A == B:
    B = star_generator()

score = 0
game_over = False

while not game_over:
    display_comparison(A, B)

    correct_answer = get_correct_answer(A, B)

    choice = input(
        "Who has more followers? Type 'A' or 'B': "
    ).lower()

    if choice == correct_answer:
        score += 1

        print("\n" * 18)
        print(f"You're right! Current score: {score}")

        # The winner becomes A in the next round
        if correct_answer == "b":
            A = B

        # If A won, A simply stays unchanged

        B = star_generator()

        # Prevent comparing the same person
        while A == B:
            B = star_generator()

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
