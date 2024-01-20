from art import logo, vs
import os
import random
from game_data import data

clear = lambda: os.system('cls')
clear()

def clear_screan():
    """clears the screen and prints the logo"""
    clear()
    print(logo)
    
def compare(follower_count_a, follower_count_b, score, answer ):
    """it compares user answer with what is selected by the program, if the user's answer was right it increases the score"""
    if follower_count_a >= follower_count_b and answer == 'a':
        score +=1
        clear_screan()
        print(f"You're right! Current score: {score}.")
        return score, True
    elif follower_count_a <= follower_count_b and answer == 'b':
        score +=1
        clear_screan()
        print(f"You're right! Current score: {score}.")
        return score, True
    else:
        clear_screan()
        print(f"Sorry, that's wrong. Final score: {score}\n")
        return score, False

def select():
    """selects two random cells from the data list"""
    return random.choice(data)

def game():
    clear_screan()
    right_answer = True
    score = 0
    # until when the user gives the right answer the game continues
    first_choice = select()
    second_choice = select()
    while right_answer:
        first_choice = second_choice
        second_choice = select()
        while first_choice == second_choice:
            second_choice = select()
        print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}.")
        print(vs)
        print(f"Compare B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}.")
        # To check the logic
        # print(first_choice)
        # print(second_choice)
        user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        score, right_answer = compare(follower_count_a = first_choice['follower_count'], 
                                    follower_count_b = second_choice['follower_count'],
                                    score = score, answer = user_answer)

game()
