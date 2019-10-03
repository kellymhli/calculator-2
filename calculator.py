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

    # Look up the command that in the dictionary and run the arithetic function using the provided numbers. 
    if command in lookup:
        token_len = len(tokens)
        num1 = float(tokens[1])

        # These two functions take in a single number.
        if (command == "square" or command == "cube") and token_len > 1:
            print(lookup[command](num1))

        # This function takes in 3 numbers.
        elif command == 'x+' and token_len > 3:
            num2 = float(tokens[2])
            num3 = float(tokens[3])
            print(lookup[command](num1, num2, num3))

        # All the other functions take in 2 numbers
        elif token_len > 2:
            num2 = float(tokens[2])
            print(lookup[command](num1, num2,))

    # If no such arithmetic function exists, exit out of the function.
    else:
        return


def split_token(user_input):
    """Split string by white space and return the resulting list."""

    tokens = user_input.split(" ")
    return(tokens)


def main():

    user_input = "" # Set inital user_input to an empty string so while loop is run at least once. 

    # Calculate user inputted arithmetic functions until the user enters q
    while user_input != "q":
        user_input = input("> ")
        tokens = split_token(user_input)
        do_setup(tokens)

    print("You will exit.")


main()