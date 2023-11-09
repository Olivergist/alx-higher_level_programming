#!/usr/bin/python3
"""
This script defines a class called BaseGeometry
with area and integer_validator methods.

"""


class BaseGeometry:
    """

    A class that provides area and integer validation methods.

    """
    def area(self):
        """
        area method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
        name: A string that represents the name of the value.
        value: The value to validate.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
