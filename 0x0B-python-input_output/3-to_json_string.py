#!/usr/bin/python3
"""
This Module Defines the function to_json_string
"""


import json


def to_json_string(my_obj):
    """returns a json string representation of the object"""
    return json.dumps(my_obj)
