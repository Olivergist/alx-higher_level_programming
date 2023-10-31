#!/usr/bin/python3
"""The LockedClass is a class that restricts the creation of new attributes."""

class LockedClass:
    """`__slots__ = ['first_name']` is a special attribute in Python that restricts the creation of new
    attributes in instances of the class.
    """
    __slots__ = ['first_name']
