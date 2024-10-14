#!/usr/bin/python3
"""
This module contains a class
"""


class MyInt(int):
    """class MyInt"""
    def __eq__(self, other):
        """return True if the other is a MyInt"""
        return super().__ne__(other)

    def __ne__(self, other):
        """return False if the other is not a MyInt"""
        return super().__eq__(other)
