#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create a set to store unique integers
    unique_integers = set()

    # Initialize the sum
    total = 0

    # Iterate through the elements of the list
    for element in my_list:
        # If the element is not in the set, it's unique
        if element not in unique_integers:
            unique_integers.add(element)
            total += element

    return (total)
