#!/usr/bin/python3

""" Adding two integers in this functions"""


def add_intergers(a, b=98):
    """
    Add two Intergers.

    param a: The First interger.
    param b: The second interger (default is 98).
    Returns: The Addition of a and b as an interger.

    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an interger or b must be an interger")

    a = int(a)
    b = int(b)

    return a + b
