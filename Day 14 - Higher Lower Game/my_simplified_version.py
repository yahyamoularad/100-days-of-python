# Day 14: Higher Lower Game
# My simplified version
#
# This version is uncommented from the original Day 14 file.
# The code structure is preserved as written.
#
# Main change in this version:
# The repeated display code is placed inside game().

# Simplified version: 
import random
import art
from game_data import data

print(art.logo)

def star_generator():
    return random.choice(data)

A = star_generator()
print(f"Compare A: {A["name"]}, {A["description"]}, {A["country"]}")

print(art.vs)
B = star_generator()
print(f"Against B: {B["name"]}, {B["description"]}, {B["country"]}")

def compare_followers(follower_a, follower_b): 
    if follower_a > follower_b: 
        return follower_a
    else: 
        return follower_b

def game(player_A , player_B): 
    print("\n" * 18)
    print(art.logo)
    print(f"Compare A: {player_A["name"]}, {player_A["description"]}, {player_A["country"]}")
    print(art.vs)
    print(f"Against B: {player_B["name"]}, {player_B["description"]}, {player_B["country"]}")


correct_answer = compare_followers(A["follower_count"], B["follower_count"])

score = 0
game_over = False 
while not game_over: 
    choice = input("Who has more followers? Type 'A' or 'B':\t").lower()
    if (choice == "a" and correct_answer == A["follower_count"]) or (choice == "b" and correct_answer == B["follower_count"]):
        score += 1
        print(f"You're right! Current score: {score}")
        if correct_answer == A["follower_count"]: 
            B = star_generator()
            correct_answer = compare_followers(A["follower_count"], B["follower_count"])
            game(A, B)

        elif correct_answer == B["follower_count"]:
            A = B
            B = star_generator()
            correct_answer = compare_followers(A["follower_count"], B["follower_count"])
            game(A, B)  
        else: 
            print(f"Sorry that's wrong. Final score: {score}")
            game_over = True 

    else:
        print(f"Sorry that's wrong. Final score: {score}")
        game_over = True
