#!/usr/bin/python3

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