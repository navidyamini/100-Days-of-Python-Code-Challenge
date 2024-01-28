from art import logo
import os

def get_bid():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_dic[name] = bid

clear = lambda: os.system('cls')
continue_bid  = True
bid_dic = {}
print(logo)
print("Welcome to the secret auction program.")
while continue_bid:
    get_bid()
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == 'yes':
        clear()
    elif other_bidders == 'no':
        clear()
        continue_bid = False
    else:
        print("Wrong Input!")
    
max_value = max(bid_dic.values())
max_key = max(bid_dic, key=bid_dic.get)

print(f"The winner is {max_key} with a bid of ${max_value}")