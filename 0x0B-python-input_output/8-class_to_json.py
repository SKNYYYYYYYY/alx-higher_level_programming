#!/usr/bin/python3
"""
This module contains a function called class_to_json
"""


def class_to_json(obj):
    """Function that returns the dictionary description"""
    return obj.__dict__
