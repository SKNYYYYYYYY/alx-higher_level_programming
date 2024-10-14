#!/usr/bin/python3
"""
    Only the lookup function over here
"""
def lookup(obj):
    """
    args: obj - the object to lookup
    returns the object attributes and methods
    """
    return dir(obj)
