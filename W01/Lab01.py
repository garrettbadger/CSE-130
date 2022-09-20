# 1. Name: 
#    Garrett Badger
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    Create a random number guessing game
# 4. What was the hardest part? Be as specific as possible.
#    -The hardest part of this assignment was remembering how python works. I did an intership over the summer all in Java
#     so it was a little tricky remembering the syntax. I also had a hard time with the list at first but that was because, again, 
#     I was used to working with lists in Java and not Python but once I got through those hiccups it went pretty smoothly.    
# 5. How long did it take for you to complete the assignment?
#    For this assignment it took about 2.5 hours total with the reading and the assignment.

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
            print(f"You guessed it! The number was {value_random} and you guessed it in {len(guesses)} tries! \n {guesses}")
# Give the user a report: How many guesses and what the guesses where
game(guess, guesses, difficulty, value_random)
