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

        r = {key: val for key, val in self.__dict__.items() if key in attrs}
        return r

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance:"""
        for key, val in json.items():
            setattr(self, key, val)
