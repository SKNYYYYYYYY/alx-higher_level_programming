#!/usr/bin/python3
"""
This is a module that contains  a class
"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
