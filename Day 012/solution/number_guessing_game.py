from art import logo
import os
from random import randint

clear = lambda: os.system('cls')
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 in hard mode).
HARD_LEVEL_TURNS = 5
EASY_LEVEL_TURNS = 10
clear()
print(logo)

def select_number():
    """ Returns an integer random number between 1 and 100 """
    return randint(1,100)

def set_difficulty(answer):
    """ Set the difficulty of the level """
    if answer == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS
    
def check_answer(guess, number):
    """ Check the user answer and compare it with the random number created by the computer """
    # Check the user's guess against the actual answer. Print "Too high." or "Too low." depending on the user's answer. 
    if guess > number:
        print("Too High!")
        return False
    elif guess < number:
        print("Too Low!")
        return False
    else:
        # If they got the answer correct, show the actual answer to the player.
        print(f"You got it! The answer was {guess}.\nYou Win!\n")
        return True

def game():
    """The Game Function, the main one"""
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number bewtween 1 and 100.")
    # ask about the difficulty level of the user
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    # set the random number that the user has to guess
    number = select_number()
    # set the turns
    turns = set_difficulty(level)
    result = False
    # While the result is false the while loop will continue
    while not result:
        # Track the number of turns remaining.
        print(f"You have {turns} attemts remaining to guess the number.")
        # Allow the player to submit a guess for a number between 1 and 100.
        user_guess = int(input("Make a guess: "))
        # Check the user's guess against the actual answer.
        result = check_answer(guess=user_guess, number=number)
        # Track the number of turns remaining.
        turns -=1
        # If they run out of turns, provide feedback to the player. 
        if turns == 0 and not result:
            result = True
            print("Ran out of turns, You Loss!\nGAME OVER!\n")
        elif not result:
            print("Guess again.")
game()
