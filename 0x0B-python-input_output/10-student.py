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

    def to_json(self, attrs=None):
        """return a json representation of this object"""
        if attrs is None:
            return self.__dict__

        return {key: value for key, value in self.__dict__.items() if key in attrs}
