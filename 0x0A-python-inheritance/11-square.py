#!/usr/bin/python3
"""
Module with a class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class with square"""
    def __init__(self, size):
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """calculating area of square"""
        return self.__size * self.__size

    def __str__(self):
        """returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
