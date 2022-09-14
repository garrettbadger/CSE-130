# 1. Name: 
#    Garrett Badger
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    Create a random number guessing game
# 4. What was the hardest part? Be as specific as possible.
#    -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#    -total time in hours including reading the assignment and submitting the program-  

import random

# Game introduction

# Prompt the user for how difficult the game will be. Ask for an integer
difficulty = int(input("How high do you want the number cap? Please enter integer: "))
# Generate a random number between 1 and the chosen value

value_random = random.randint(1, difficulty)
guess = -1
# Give the user instructions as to what he or she will be doing
print("You will be given a hint after you guess until you guess the correct number.")
# Initialize the sentinal and the array of guesses
guesses = []
# Play the guessing game
def game(guess, guesses, difficulty, value_random):

    
    while guess != value_random:
        # Prompt the user for a number
        guess = int(input(f"Please enter an integer in between 1 and {difficulty}: "))
    # Store the number in an array so it can be displayed later
        guesses.append(guess)
    # Make a decision: was the guess too high, too low, or just right
        if guess > value_random:
            print("That was too high!")
        elif guess < value_random:
            print("That was too low!")
        else:
            print(f"You guessed it! The number was {value_random} and you guessed it in {len(guesses)} \n {guesses}")
# Give the user a report: How many guesses and what the guesses where
game(guess, guesses, difficulty, value_random)
