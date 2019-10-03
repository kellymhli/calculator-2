"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def do_setup(tokens):
    """Prompt the user"""

    # Create a dictionary for the user input command that correspond to the functions in the arithmetic module.
    lookup = {'+': add, '-': subtract, '*': multiply, '/': divide,
              'square': square, 'cube': cube, 'mod': mod, 'pow': power,
              'x+' : add_mult, 'cubes+' : add_cubes}

    command = tokens[0]
    num1 = float(tokens[1])
    num2 = float(tokens[2])

    # Look up the command that in the dictionary and run the arithetic function using the provided numbers. 
    if command in lookup:
        print(lookup[command](num1,num2))
    # If no such arithmetic function exists, print an error and exit our of the function.
    else:
        print("That function is not one of your options.")
        return


def split_token(user_input):
    """Split string by white space and return the resulting list."""

    tokens = user_input.split(" ")
    return(tokens)


def main():
    user_input = ""

    while user_input != "q":
        user_input = input("> ")
        tokens = split_token(user_input)
        do_setup(tokens)


main()