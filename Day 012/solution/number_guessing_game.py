from art import logo
import os
from random import randint

clear = lambda: os.system('cls')
HARD_LEVEL_TURNS = 10
EASY_LEVEL_TURNS = 5
clear()
print(logo)

def select_number():
    return randint(1,100)

def set_difficulty(answer):
    if answer == 'hard':
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS
    
def check_answer(guess, number):
    if guess > number:
        print("Too Low!")
        return False
    if guess < number:
        print("Too High")
        return False
    else:
        print("It's correct, You Win!")
        return True

def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number bewtween 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    number = select_number()
    turns = set_difficulty(level)
    while not result:
        print(f"You have {turns} attemts remaining to guess the number.")
        user_guess = int(input("Make a guess': "))
        result = check_answer(guess=user_guess, number=number)

game()