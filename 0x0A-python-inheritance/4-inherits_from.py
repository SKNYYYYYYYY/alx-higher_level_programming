#!usr/bin/python3
"""
This module defines the function inherits
"""


def inherits(obj, a_class):
    """
    A function that checks if object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    Args:
        obj:
            the object that is to be checkedy
        a_class:
            the class in which an object is to be checked at
    Returns:
        bool: True if object is an instance of a class that inherited
    """
    return issubclass(obj, a_class)
