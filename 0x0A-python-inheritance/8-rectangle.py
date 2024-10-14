#!/usr/bin/python3
"""
    This module contains    a  function
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """a class rectangle"""
    def __init__(self, width, height):
        """Constructor"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
