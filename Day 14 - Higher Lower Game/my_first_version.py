# Day 14: Higher Lower Game
# My first version
#
# This version is uncommented from the original Day 14 file.
# The code structure is preserved as written.
#
# Flow:
# 1. Pick account A and account B.
# 2. Compare their follower counts.
# 3. Ask the user to choose A or B.
# 4. Increase the score when the answer is correct.
# 5. Generate the next comparison.

import random
import art
from game_data import data

print(art.logo)

def star_generator():
    return random.choice(data)


A = star_generator()
print(f"Compare A: {A["name"]}, {A["description"]}, {A["country"]}")
print(A["follower_count"])

print(art.vs)
B = star_generator()
print(f"Against B: {B["name"]}, {B["description"]}, {B["country"]}")
print(B["follower_count"])

def compare_followers(follower_a, follower_b): 
    if follower_a > follower_b: 
        return follower_a
    else: 
        return follower_b


result = compare_followers(A["follower_count"], B["follower_count"])
print(result)


score = 0
game_over = False 
while not game_over: 
    choice = input("Who has more followers? Type 'A' or 'B':\t").lower()
    if (choice == "a" and result == A["follower_count"]) or (choice == "b" and result == B["follower_count"]):
        score += 1
        print(f"You're right! Current score: {score}")
        if result == A["follower_count"]: 
            B = star_generator()
            result = compare_followers(A["follower_count"], B["follower_count"])
            print(result)
            print("\n" * 18)
            print(art.logo)
            print(f"Compare A: {A["name"]}, {A["description"]}, {A["country"]}")
            print(A["follower_count"])
            print(art.vs)
            print(f"Against B: {B["name"]}, {B["description"]}, {B["country"]}")
            print(B["follower_count"])

        elif result == B["follower_count"]:
            A = B
            B = star_generator()
            result = compare_followers(A["follower_count"], B["follower_count"])
            print(result)
            print("\n" * 18)
            print(art.logo)
            print(f"Compare A: {A['name']}, {A['description']}, {A['country']}")
            print(A["follower_count"])
            print(art.vs)
            print(f"Against B: {B['name']}, {B['description']}, {B['country']}")
            print(B["follower_count"])   
        else: 
            print(f"Sorry that's wrong. Final score: {score}")
            game_over = True 

    else:
        print(f"Sorry that's wrong. Final score: {score}")
        game_over = True
