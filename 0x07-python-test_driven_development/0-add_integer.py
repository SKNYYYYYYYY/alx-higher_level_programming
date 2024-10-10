#!/usr/bin/python3
"""defines the integer addition function
    checks if a and b is integer
    checks if a is float
    checks if b is a float
"""
def add_integer(a, b=98):
    """ Args: a and b; Returns: int: The sum of a and b, after converting floats to integers.
    Raises: TypeError: If a or b are not integers or floats.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
