#!/usr/bin/python3
# This is the safe Function

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
