#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dictionary = {}
    for keys in sorted(a_dictionary):
        new_dictionary[keys] = a_dictionary[keys]
    print(new_dictionary)
    