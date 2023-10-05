#!/usr/bin/python3

# Define a function to print and return the last digit of a number
def print_last_digit(number):
    # Print the absolute value of the number modulo 10 (last digit)
    print(abs(number) % 10, end="")
    # Return the last digit
    return (abs(number) % 10)
