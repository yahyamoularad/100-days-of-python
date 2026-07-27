# Day 9: Dictionaries and Nesting
#
# Topics included:
# 1. Creating dictionaries
# 2. Reading dictionary values
# 3. Adding dictionary entries
# 4. Editing dictionary entries
# 5. Creating an empty dictionary
# 6. Looping through a dictionary
# 7. Lists inside dictionaries
# 8. Dictionaries inside dictionaries
# 9. Student Grades coding challenge
# 10. Blind Auction coding challenge
#
# The two coding challenge sections are kept exactly as written
# in the original Day 9 file.


# ============================================================
# LESSON 1: CREATING A DICTIONARY
# ============================================================

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary)


# ============================================================
# LESSON 2: READING A VALUE
# ============================================================

print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])


# ============================================================
# LESSON 3: ADDING A NEW ENTRY
# ============================================================

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)


# ============================================================
# LESSON 4: EDITING AN EXISTING ENTRY
# ============================================================

programming_dictionary["Bug"] = "A moth in your computer."

print(programming_dictionary["Bug"])


# ============================================================
# LESSON 5: AN EMPTY DICTIONARY
# ============================================================

empty_dictionary = {}

print(empty_dictionary)


# ============================================================
# LESSON 6: LOOPING THROUGH A DICTIONARY
# ============================================================

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# ============================================================
# CODING CHALLENGE: STUDENT GRADES
# ============================================================

#coding challenge: 

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# # Create an empty dictionary to collect the new values.
# student_grades = {}

# # Loop through each key in the student_scores dictionary
# for student in student_scores:

#     #Get the value (student score) by using the key each time.
#     score = student_scores[student]

#     #Check what grade the score would get, then add it to student_grades
#     if score >= 91:
#         student_grades[student] = 'Outstanding'
#     elif score >= 81:
#         student_grades[student] = 'Exceeds Expectations'
#     elif score >= 71:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = 'Fail'


# ============================================================
# LESSON 7: A LIST INSIDE A DICTIONARY
# ============================================================

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

print(travel_log["France"][1])


# ============================================================
# LESSON 8: A LIST INSIDE ANOTHER LIST
# ============================================================

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])


# ============================================================
# LESSON 9: A DICTIONARY INSIDE A DICTIONARY
# ============================================================

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][2])


# ============================================================
# DAY 9 REVISION NOTES
# ============================================================

# A dictionary stores information as key and value pairs.
#
# Create a dictionary:
#
# programming_dictionary = {
#     "Bug": "An error in a program.",
#     "Function": "Reusable code.",
# }
#
# Read a value by using its key:
#
# programming_dictionary["Bug"]
#
# Add a new entry:
#
# programming_dictionary["Loop"] = "Repeated action."
#
# Edit an existing entry:
#
# programming_dictionary["Bug"] = "A new definition."
#
# Create an empty dictionary:
#
# empty_dictionary = {}
#
# Loop through a dictionary:
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#
# A dictionary can contain a list:
#
# travel_log["France"][1]
#
# A dictionary can also contain another dictionary:
#
# travel_log["Germany"]["cities_visited"][2]
#
# In the Blind Auction project:
#
# bids[name] = price
#
# stores each bidder's name as a key and the bid as its value.
#
# The find_highest_bidder function loops through every bidder,
# compares every bid with highest_bid, and remembers the winner.


# ============================================================
# DAY 9 CODING CHALLENGE: BLIND AUCTION
# ============================================================

#Day 9 coding challenge: 
# #my version
# import art
# print(art.logo)

# # TODO-1: Ask the user for input
# name = input("What is your name ?: ")
# price = int(input("What is your bid?: $"))
# # TODO-2: Save data into dictionary {name: price}
# participant = {
#     name : price,
# }

# # TODO-3: Whether if new bids need to be added
# bid_over = False
# while not bid_over: 
#     other_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
#     if other_bidders == "yes":
#         print("\n" * 18)
#         name = input("What is your name ?: ")
#         price = int(input("What is your bid?: $"))
#         participant[name] = price
#         print("\n" * 18)
#     else:
#             bid_over = True
# # TODO-4: Compare bids in dictionary

# winner_name = max(participant, key=participant.get)
# winner_bid = participant[winner_name]
    



# print(f"The winner is {winner_name} with a bid of ${winner_bid}")

# #Chatgpt corrected version : 
# import art

# print(art.logo)

# # Store all bidders and their bids
# participants = {}

# bid_over = False

# while not bid_over:
#     # Ask for bidder information
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))

#     # Save the bidder in the dictionary
#     participants[name] = price

#     # Ask whether another bidder should be added
#     other_bidders = input(
#         "Are there any other bidders? Type 'yes' or 'no'.\n"
#     ).lower()

#     if other_bidders == "yes":
#         print("\n" * 18)

#     elif other_bidders == "no":
#         bid_over = True

#     else:
#         print("Invalid answer. The auction will end.")
#         bid_over = True

# # Find the winner after all bids have been collected
# winner_name = max(participants, key=participants.get)
# winner_bid = participants[winner_name]

# print(f"The winner is {winner_name} with a bid of ${winner_bid}.")

#Angela's version:
from art import logo
print(logo)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)
