#!/usr/bin/python3

def uppercase(str):
    # Iterate through each character 'c' in the input string 'str'
    for c in str:
        # Check if the ASCII value of 'c' represents a lowercase letter
        if ord(c) >= 97 and ord(c) <= 122:
            # Convert the lowercase letter to uppercase
            c = chr(ord(c) - 32)
        # Print the character 'c'
        print("{}".format(c), end="")

    # Print an empty line to separate the output
    print("")
