#!/usr/bin/python3
"""Adds attribute to object if possible"""


def add_attribute(obj, name, value):
    """Add attribute to obj if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
