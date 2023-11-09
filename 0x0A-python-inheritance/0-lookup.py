#!/usr/bin/python3
"""
This script defines a function to return the
list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
    obj: The object to inspect.

    Returns:
    A list of attribute and method names associated with the object.
    """
    return dir(obj)
