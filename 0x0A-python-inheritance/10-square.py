#!/usr/bin/python3
"""Defines a Square class inheriting from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size):
        """Initialize a new square

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
