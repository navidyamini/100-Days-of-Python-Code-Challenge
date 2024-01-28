from art import logo
import random
import os

def calculate_score(values):
    """Calculates the sum of the int List"""
    if sum(values) == 21 and len(values) == 2:
        return 0
    if 11 in values and  sum(values) > 21:
        values.remove(11)
        values.append(1)
    return sum(values)

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =  random.choices(cards)
    return card[0]

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🙃"
    elif user_score > 21 and computer_score > 21:
        return "You went over. You lose! 😤"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack! 😱"
    elif user_score == 0:
        return "Win with a Blackjack! 😎"
    elif user_score > 21:
        return "You went over. You lose! 😭"
    elif computer_score > 21:
        return "Opponent went over. You win! 😁"
    elif user_score > computer_score:
        return "You win! 😃"
    else:
        return "You lose! 😤"       
     

clear = lambda: os.system('cls')

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    print(logo)
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score >21: 
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final cards: {user_cards}, final score: {user_score}")
    print(f"    Computer's final cards: {computer_cards}, final score: {computer_score}")    
    print(compare(user_score, computer_score))
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()
