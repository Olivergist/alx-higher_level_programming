#!/usr/bin/python3
"""Write a string to a text."""


def write_file(filename="", text=""):
    """Write a text filename
       Return Number
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
