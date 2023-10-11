#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Check if tuple_a has fewer than 2 elements
    if len(tuple_a) < 2:
        # If tuple_a is empty, pad with (0, 0)
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        # If tuple_a has only 1 element, pad with a 0 for the second element
    else:
        tuple_a = tuple_a[0], 0

    # Check if tuple_b has fewer than 2 elements
    if len(tuple_b) < 2:
        # If tuple_b is empty, pad with (0, 0)
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        # If tuple_b has only 1 element, pad with a 0 for the second element
    else:
        tuple_b = tuple_b[0], 0

    # Calculate the sum of the first and second elements of the two tuples
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

