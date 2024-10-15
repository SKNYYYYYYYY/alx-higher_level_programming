#!/usr/bin/python3
"""
This module defines read_file function
"""


def read_file(filename=""):
    """
    Read file my_file_0.txt
    Args:
        filename: a file to read
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        print(f.read())
