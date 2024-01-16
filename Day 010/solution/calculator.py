from art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide}

clear = lambda: os.system('cls')

def calculator():
    print(logo)
    continue_cal = True
    first_num = float(input("What's the first number?: "))
    while continue_cal:
        for key in operations:
            print(key)
        
        operation = input("Pick an operation: ")
        second_num = float(input("What's the next number?: "))

        cal_function = operations[operation]
        result = cal_function(first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {result}")
        
        new_operation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if new_operation == 'n':
            continue_cal = False
            clear()
            calculator()
        elif new_operation == 'y':
            first_num = result
            clear()
            print(first_num)
        else:
            clear()
            print("Error!")
            calculator()

calculator()