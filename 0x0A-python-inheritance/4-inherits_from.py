#!/usr/bin/python3
"""
This script defines a function to check if
an object is an instance of a class that
inherits (directly or indirectly)
from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class
    that inherits (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a class
        that inherits from a_class, False otherwise.
    """
    if isinstance(obj, a_class) and not isinstance(obj, a_class):
        return True
    else:
        return False
