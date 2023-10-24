#!/usr/bin/python3
# functions that divides 2 int

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
