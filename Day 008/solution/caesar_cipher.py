import string
from art import logo

def encrypt(text, shift):
    encrypted_text =[]
    # split the sentence and convert it to the list of words
    words_list = text.split(" ")
    for word in words_list:
        new_word = ''
        for letter in word:
            # check if there is a special character in the string
            if letter in string.punctuation or letter in string.digits:
                new_word += letter
            else:
                letter_index = alphabet.index(letter)
                #shift to right
                new_index = letter_index + shift
                # check if the new index is out of range
                if new_index >= len(alphabet):
                    new_index = new_index % len(alphabet)
                new_word += alphabet[new_index]
        encrypted_text.append(new_word)
    print("The encoded text is " + f"{' '.join(encrypted_text)}")
    
def decrypt(text, shift):
    decrypted_text =[]
    # split the sentence and convert it to the list of words
    words_list = text.split(" ")
    for word in words_list:
        new_word = ''
        for letter in word:
            # check if there is a special character in the string
            if letter in string.punctuation or letter in string.digits:
                new_word += letter
            else:
                letter_index = alphabet.index(letter)
                # shift to left
                new_index = letter_index - shift
                # check if the new index is out of range
                while new_index < 0:
                    new_index = new_index + len(alphabet)
                new_word += alphabet[new_index]
        decrypted_text.append(new_word)
    print("The decoded text is " + f"{' '.join(decrypted_text)}")
    
def caesar(text, shift, direction):
    # calling the encrypt function
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Wrong Input!")
    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the: ")
print(logo)

wants_play = True

while wants_play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart == 'no':
        wants_play = False