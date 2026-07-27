# Day 8: Function Parameters and Caesar Cipher
#
# Topics included:
# 1. Defining and calling functions
# 2. Functions with one input
# 3. Functions with more than one input
# 4. Positional arguments
# 5. Keyword arguments
# 6. Counting letters in strings
# 7. Caesar Cipher coding challenge
#
# The Caesar Cipher challenge at the end is kept exactly as written
# in the original Day 8 file.


# ============================================================
# LESSON 1: A BASIC FUNCTION
# ============================================================

def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice")


greet()


# ============================================================
# LESSON 2: A FUNCTION WITH ONE INPUT
# ============================================================

def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")


life_in_weeks(12)


# ============================================================
# LESSON 3: A FUNCTION WITH MORE THAN ONE INPUT
# ============================================================

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# Keyword arguments make it clear which value belongs
# to which parameter.
greet_with(name="Hadda", location="Marrakech")


# ============================================================
# LESSON 4: LOVE SCORE EXERCISE
# ============================================================

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")


# ============================================================
# REVISION NOTES
# ============================================================

# A function is defined with def:
#
# def function_name():
#     print("Code inside the function")
#
# A parameter is the name written inside the function definition:
#
# def greet_with(name, location):
#
# An argument is the value passed when the function is called:
#
# greet_with("Hadda", "Marrakech")
#
# Positional arguments depend on their order:
#
# greet_with("Hadda", "Marrakech")
#
# Keyword arguments use the parameter names:
#
# greet_with(name="Hadda", location="Marrakech")
#
# lower() changes text to lowercase.
#
# count("t") counts how many times "t" occurs in a string.
#
# str() changes a value into a string.
#
# int() changes a compatible value into an integer.
#
# The Caesar Cipher uses:
#
# alphabet.index(letter)
#     Finds the position of a letter in the alphabet list.
#
# len(alphabet)
#     Gives the number of letters in the alphabet list.
#
# shifted_position %= len(alphabet)
#     Keeps the shifted position inside the alphabet list.
#
# If the direction is decode, the shift becomes negative.
#
# Characters not found in alphabet are added without changing them.


#Day 8 coding challenge 
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
