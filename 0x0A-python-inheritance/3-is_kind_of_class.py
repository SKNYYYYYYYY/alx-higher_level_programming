#!/usr/bin/python3
""""
    defines the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
     if the object is an instance of, or if the object is an 
     instance of a class that inherited from, the specified class
     Args:
        obj: the object to check for its a kind of class
        a_class: the class to check if the object is its instance

    Returns:
        true if the object is an instance of the specified class or its subclass
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
