#!/usr/bin/python3
"""
This script defines a class
called BaseGeometry with an area method.
"""


class BaseGeometry:
    """
    An empty class that provides
      a method to raise an exception.
    """
    def area(self):
        """Raise an exception with the message
          'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
