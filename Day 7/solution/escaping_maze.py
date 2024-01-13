import random
from hangman_art import logo, stages
from hangman_words import word_list

#Join all the elements in the list and turn it into a String.
def print_word(word_list):
    word = ''
    for item in word_list:
        word += item
    print(word+ "\n")    

#User lifes
lifes = 6
#Create blanks
display = []
print("Welcome to the Hangman game")
print(logo)
chosen_word = random.choice(word_list)
word_len = len(chosen_word)
# for debugging 
#print(chosen_word)
for n in range(word_len):
    display.append("_")
while "_" in  display and lifes >= 0:
    # get user inpurt
    guess = input("Guess a letter: ").lower()
     #Check guessed letter
    if guess in display:
        # If the user has entered a letter they've already guessed, print the letter and let them know.
        print(f"You've already guessed {guess}.")
        print_word(display) 
    elif guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display[idx] = guess
        print_word(display)
    # if user is wrong.
    else:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print_word(display) 
        print(stages[lifes])
        lifes -=1
if lifes < 0:
    # Check if user has no lifes left.
    print("You lose!")
else:
    # Check if user has got all letters.
    print("You Win")
    
#Join all the elements in the list and turn it into a String.
# print(f"{' '.join(display)}")