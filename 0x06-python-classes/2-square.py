#!/usr/bin/python3
"""This module contains a class that has a constructor"""
try:
    class Square:
        """This class has a constructor"""
        def __init__(self, size=0):
            """This is a method that checks whether the size provided is a
              positive integer
            args: size, size parameter provided during calling
            """
            self.__size = size
            if not isinstance(self.__size, int):
                raise TypeError("size must be an integer")
            if self.__size < 0:
                raise ValueError("size must be >= 0")
except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)
