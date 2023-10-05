#!/usr/bin/python3

# Define a function 'magic_calculation' with three parameters
def magic_calculation(a, b, c):
    # Check if 'a' is less than 'b'; if true, return 'c'.
    if a < b:
        return (c)

    # Check if 'c' is greater than 'b'; if true, return the sum of 'a' and 'b'.
    if c > b:
        return (a + b)

    # If none of the above conditions are met, return the result
    return (a * b - c)
