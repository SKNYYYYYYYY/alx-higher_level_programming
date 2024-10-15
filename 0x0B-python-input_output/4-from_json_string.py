#!/usr/bin/python3
"""
This module defines from_json_string
"""


import json


def from_json_string(my_str):
    """
    A decoding function that converts a json string into a Python object
    Args:
        my_str: json string to be converted
    Returns:
        python object: Python object
    """
    return json.loads(my_str)
