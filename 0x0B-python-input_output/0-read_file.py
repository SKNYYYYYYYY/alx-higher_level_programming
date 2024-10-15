#!/usr/bin/python3
"""
This module defines read_file function
"""


def read_file(filename=""):
    """Read file my_file_0.txt"""
    with open('my_file_0.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
        print(text)
