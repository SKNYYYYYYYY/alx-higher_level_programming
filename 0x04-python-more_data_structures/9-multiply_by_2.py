#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict = a_dictionary
    for key, value in dict.items():
            value = value * 2
            dict[key] = value
    return dict
