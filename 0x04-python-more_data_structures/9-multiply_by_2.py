#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict = {}
    for key, value in a_dictionary.items():
            value = value * 2
            dict[key] = value
    return dict
