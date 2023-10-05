#!/usr/bin/python3

# Define a function 'remove_char_at' that removes the character
def remove_char_at(str, n):
    # Check if 'n' is negative; if so, return the original string unchanged.
    if n < 0:
        return (str)

    # Return the string with the character at index 'n' removed.
    return (str[:n] + str[n+1:])
