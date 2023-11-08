#!/usr/bin/python3
"""Function to read text file and print to stdout"""


def read_file(filename=""):
    """Read text file and print to stdout
    Use with statement to open file
    No need to manage file permissions or exceptions
    Not allowed to import modules
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
