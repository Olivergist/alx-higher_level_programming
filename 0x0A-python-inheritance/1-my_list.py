#!/usr/bin/python3
"""
This script defines a class MyList that inherits
from the list class and provides a method to
print the list in ascending sorted order.

"""


class MyList(list):
    """
       A custom list class that inherits
       from the built-in list class.

    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.

        Args:
        None

        Returns:
        None
        """
        sorted_list = sorted(self)
        print(sorted_list)
