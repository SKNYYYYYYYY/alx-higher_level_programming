#!/usr/bin/python3
"""defines the integer addition function"""
def add_integer(a, b=98):
    """
    Adds two integers or floats (cast to integers).

    Args:
        a (int, float): First number.
        b (int, float, optional): Second number, defaults to 98.

    Returns:
        int: The sum of a and b, after converting floats to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
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
