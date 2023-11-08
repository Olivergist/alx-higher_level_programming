#!/usr/bin/python3
"""This module defines a function to read a text
  file and print its content to stdout.
"""


def read_file(filename=""):
    """Read the specified text file and print its content to stdout."""
    try:
        with open(filename, encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        pass
