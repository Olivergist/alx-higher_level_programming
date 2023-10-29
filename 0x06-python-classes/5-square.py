#!/usr/bin/python3

"""Definer the class"""


class Square:
    """
    This class defines a square with a private instance attribute 'size'.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        size (int, optional): The size of the square. Default is 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Parameters:
        value (int): The new size of the square.

        Raises:
        TypeError: If 'value' is not an integer.
        ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using '#' characters.

        If the size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
