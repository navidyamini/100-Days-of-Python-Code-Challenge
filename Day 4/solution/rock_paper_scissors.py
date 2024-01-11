import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Rock Paper Scissors")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
choices = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
if (user_choice >= 3 or user_choice < 0):
    print("WRONG INPUT!")
else:
    print("You choosed " + choices[user_choice] + " and computer choosed " + choices[computer_choice])
    if user_choice == computer_choice:
        print("Draw!")
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
        print("Computer Won!")
    else:
        print("You Won!")
        

    