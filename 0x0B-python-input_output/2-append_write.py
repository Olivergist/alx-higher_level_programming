#!/usr/bin/python3
"""Appends a string of a text file
   and return num chars added
"""


def append_write(filename="", text=""):
    """Append text to end of filename
    Create file if it doesn't exist
    Return num chars appended
    Use with statement for file handling
    No need to manage file permissions or exceptions
    Not allowed to import modules
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
