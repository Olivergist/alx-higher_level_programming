#!/usr/bin/python3
""" Student class """


class Student:
    """ Represent a student"""
    def __init__(self, first_name, last_name, age):
        """ Initializing student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Get dict representation of student """
        return self.__dict__
