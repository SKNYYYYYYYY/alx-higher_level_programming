#!/usr/bin/python3
"""
This module contains a class
"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a json representation of this object"""
        return self.__dict__
