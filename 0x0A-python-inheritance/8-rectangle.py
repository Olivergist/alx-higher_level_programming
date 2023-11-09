#!/usr/bin/python3
"""Defines a Rectangle class inheriting from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle"""


def __init__(self, width, height):
    """Initialize a new Rectangle

    Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
    """
    self.__width = width
    self.__height = height
    self.integer_validator("width", width)
    self.integer_validator("height", height)
