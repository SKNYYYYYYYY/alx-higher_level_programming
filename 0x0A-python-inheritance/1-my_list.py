#!/usr/bin/python3
"""Module with one class"""
class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """A function that prints a sorted list"""
        print(sorted(self))
