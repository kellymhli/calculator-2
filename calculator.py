"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def do_setup():

    input_element = input_token() #[pow. 2. 3]
    num1 = input_element[1]
    num2 = input_element[2]
    num3 = input_element[3]
    user_input = input_element[0]

    while user_input != "q":
        if user_input == "+":
            return (add(num1, num2))
        elif user_input == "-":
            return (substract(num1, num2))
        elif user_input == "*":
            return (multiply(num1. num2))
        elif user_input == "/":
            return (divide(num1, num2))
        elif user_input == "square":
            return (square(num1))
        elif user_input == "cube":
            return (cube(num1))
        elif user_input == "power":
            return (power(num1, num2))
        elif user_input == "mod":
            return (mod(num1, num2))
        elif user_input == "x+":
            return (add_mult(num1, num2, num3))
        elif user_input == "cubes+":
            return (add_cubes(num1, num2))


def input_token():
    """Take in user input and split elements into a list."""

    user_input = input("")
    tokens = user_input.split(" ")
    return(tokens)

do_setup()


# Your code goes here
