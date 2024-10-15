#!/usr/bin/python3
"""
This module defines the function apppend
"""


def append_write(filename="", text=""):
    """
    Function that writes a file
    Args:
        filename: the name of the file
        text: the text to write
    Returns:
        the length of the text written
    """
    with open(filename, 'a') as f:
        return f.write(text)
