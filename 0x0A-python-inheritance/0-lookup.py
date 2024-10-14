#!/usr/bin/python3
"""
This module defines the lookup function that returns the list
of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    Args:
        obj: the object to lookup

    Returns:
        A list of attributes and methods of the object
    """
    return dir(obj)
