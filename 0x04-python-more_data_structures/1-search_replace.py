#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = []

    # Iterate through the elements of the original list
    for element in my_list:
        # If the element matches the 'search' element
        if element == search:
            new_list.append(replace)
        else:
            # If the element doesn't match, add it as is to the new list
            new_list.append(element)

    return (new_list)
