#!/usr/bin/python3
"""
Class Relationship Checker Module

This module provides utility functions for checking relationships
between objects and classes. It defines the following function:

- is_kind_of_class: Determines if an object is an instance of a given class
                    or any of its subclasses.

Usage:
    from module_name import is_kind_of_class
    result = is_kind_of_class(obj, class_name)
"""



def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    Args:
        obj: the object to check
        a_class: the class to check against

    Returns:
        True if the object is an instance of the specified class or its subclass, False otherwise
    """
    return isinstance(obj, a_class)
