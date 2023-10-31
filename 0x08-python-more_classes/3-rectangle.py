#!/usr/bin/python3
"""
    This module defines a Rectangle class.
"""


class Rectangle:
    """
    class Rectangle defines a rectangle

    Attr:
        width: width of the rectangle
        height: height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the instances

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """
        Getter function for the private attribute width

        Returns:
            int: width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for the private attribute width

        Args:
            value (int): new width value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter function for the private attribute height

        Returns:
            int: height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function for the private attribute height

        Args:
            value (int): new height value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Public instance method to calculate the area of the rectangle

        Returns:
            int: Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Public instance method to calculate the perimeter of the rectangle

        Returns:
            int: Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return string representation of a rectangle

        Returns:
            str: String representation of the rectangle
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.__height - 1):
            rectangle += "#" * self.__width + "\n"
        rectangle += "#" * self.__width

        return rectangle
