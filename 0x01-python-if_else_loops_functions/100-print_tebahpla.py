#!/usr/bin/python3

# Initialize a variable 'i' to control the case change
i = 0

# Loop through the ASCII values of lowercase letters from 'z' to 'a'
for c in range(ord('z'), ord('a') - 1, -1):
    # Print the character converted to uppercase or lowercase based on 'i'
    print("{}".format(chr(c - i)), end="")
    # Toggle 'i' between 32
    i = 32 if i == 0 else 0
