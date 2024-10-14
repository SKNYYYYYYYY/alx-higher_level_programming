#!/usr/bin/python3
"""
This module defines the lookup function that returns the list
of available attributes and methods of an object.
"""
def lookup(obj):
    """
    args: obj - the object to looku
    returns the object attributes and methods
    """
    return dir(obj)
