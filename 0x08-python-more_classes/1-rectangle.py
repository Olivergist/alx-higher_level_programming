#!/usr/bin/python3

"""A Class that defines rectangle"""


class Rectangle:
    """Private Getter and setter for the width and height"""
    def __init__(self, width=0, height=0):
        """
        Seperate the Width from the height
        Args:
             width = int
             height = int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Decorator for the width
        Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Decorator for the height
        Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
