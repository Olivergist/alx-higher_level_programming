#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Check if elements in the list are divisible by 2."""
    multiples = []

    # Iterate through the list and check if each element is by 2
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True) 
            # Append True if divisible by 2
        else:
            multiples.append(False) 
            # Append False if not divisible by 2
            
    return (multiples)
