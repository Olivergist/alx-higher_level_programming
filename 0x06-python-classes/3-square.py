#!/usr/bin/python3

"""Define the square"""


class Square:
    """Class with a private attribute"""
    def __init__(self, size=0):
        """ Initializes a new Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate and return the area
        Returns:
        int: The area of the square
        """
        return self.__size ** 2
