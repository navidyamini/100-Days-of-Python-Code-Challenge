import string
import random

print("Welcome to the Password Generator!")
letters_no = int(input("How many letters would you like in your password?\n"))
symbols_no = int(input("How many symbols would you like?\n"))
numbers_no = int(input("How many numbers would you like?\n"))

# Easy Version (Step 1)
print("Easy Version (Step 1)")
password = ''
for n in range(0,letters_no):
    password += random.choice(string.ascii_letters)
for n in range(0, numbers_no):
    password += random.choice(string.punctuation) 
for n in range(0, numbers_no):
    password += random.choice(string.digits)     
print(password)
print("********************************************")
# Hard Version (Step 2)
print("Hard Version (Step 2)")
password = ''
password_list = []
for n in range(0,letters_no):
    password_list.append(random.choice(string.ascii_letters))
for n in range(0, numbers_no):
    password_list.append(random.choice(string.punctuation)) 
for n in range(0, numbers_no):
    password_list.append(random.choice(string.digits))
random.shuffle(password_list)         
for item in password_list:
    password += item
print(password)