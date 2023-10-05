#!/usr/bin/python3

# Define a function named 'uppercase' that takes a string 'str' as input
def uppercase(str):
    # Iterate through each character 'c' in the input string 'str'
    for c in str:
        # Check if the ASCII value of 'c' represents a lowercase letter (between 'a' and 'z')
        if ord(c) >= 97 and ord(c) <= 122:
            # Convert the lowercase letter to uppercase by subtracting 32 from its ASCII value
            c = chr(ord(c) - 32)
        # Print the character 'c' (either unchanged or converted to uppercase), without a newline
        print("{}".format(c), end="")
    
    # Print an empty line to separate the output
    print("")
