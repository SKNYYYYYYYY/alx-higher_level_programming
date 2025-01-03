#!/usr/bin/python3
"""
This module contains the function write_file
"""


def write_file(filename="", text=""):
    """
    Function that writes a file
    Args:
        filename: the name of the file
        text: the text to write
    Returns:
        the length of the text written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
