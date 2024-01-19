from art import logo
import os
from random import randint

clear = lambda: os.system('cls')
clear()
print(logo)
############DEBUGGING#####################

# # Describe Problem
def my_function():
# Why it is not printing anything?
# The index goes until 19 and never becomes equal to 20
# Change the 20 to 21 in the for loop
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
# The cell index in the list starts from 0, 
# and the randint(), can choose from the start to end range, 
# so here it is possible to choose 6, 
# and it gives a "list index out of range" error. 
# also, 0 will never be chosen by the code.
# to solve the problem change the range to (0,5)
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# Play Computer
# for year == 1994, nothing will be printed
# change the elif condition to year >= 1994
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# Fix the Errors
# it is expected to have an indented block
# need to convert the input to int
# to print the age you need to use f string
age = input("How old are you?")
if age > 18:
print("You can drive at age {age}.")

#Print is Your Friend
# word_per_page is always 0
# the code does not assign the input to it
# change "==" to "="
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
# the code is appending only the last value into b_list
# since the b_list out of for loop, indent b_list into for loop
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])