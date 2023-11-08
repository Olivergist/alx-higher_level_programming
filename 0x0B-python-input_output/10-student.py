#!/usr/bin/python3
"""Student class """


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initializing a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
