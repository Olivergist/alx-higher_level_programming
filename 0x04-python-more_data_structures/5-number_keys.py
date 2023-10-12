def number_keys(a_dictionary):
    # Use the len() function to get the number of keys in the dictionary
    star = 0
    list_keys =list(a_dictionary.keys())

    for i in list_keys:
        star += 1

    return (star)
