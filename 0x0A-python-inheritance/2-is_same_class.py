#!/usr/bin/python3
"""
    This module defines the function is_same_class method
    that checks if the class is an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
        function that checks if the class is an instance of the specified class
        Args:
            obj: useed to check if its an instance of the specified class
            a_class: the class to check

        Returns:
            True if the class is an instance of the specified class
            otherwise False
    """
    if not type(obj) is a_class:
        return False
    else:
        return True
