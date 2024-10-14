#!/usr/bin/python3
"""This module defines the class Mylist that inherits from the built-in list"""
class MyList(list):
    """
    A subclass of list that implements the method to print the list in sorted order
    """
    def print_sorted(self):
        """
        A function that prints a sorted list
        """
        print(sorted(self))
