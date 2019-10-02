"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def do_setup():

    user_input = ""
    
    lookup = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
              'square': square,
              'cube': cube,
              'mod': mod,
              'pow': power,
              'x+' : add_mult,
              'cubes+' : add_cubes}

    while user_input != "q":
        input_element = input_token() #[pow. 2. 3]
        num1 = int(input_element[1])
        num2 = int(input_element[2])
        user_input = input_element[0]
        print(lookup[user_input](num1,num2))




def input_token():
    """Take in user input and split elements into a list."""

    user_input = input("")
    tokens = user_input.split(" ")
    return(tokens)

do_setup()


# Your code goes here
