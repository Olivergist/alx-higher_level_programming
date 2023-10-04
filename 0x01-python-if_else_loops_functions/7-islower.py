#!/usr/bin/python3
def islower(c):
    # Check if the ASCII value of 'c' is within the range of lowercase letters
    return ord('a') <= ord(c) <= ord('z')

# Test the function with some examples
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('z'))  # True
print(islower('Z'))  # False
print(islower('5'))  # False
