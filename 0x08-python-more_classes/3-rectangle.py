#!/usr/bin/python3
"""module with one class"""


class Rectangle:
    """rectangle class"""
    def __init__(self, width=0, height=0):
        """Constructor"""
        self.__height = height
        self.__width = width

    def __str__(self):
        """string representation"""
        new_list = []
        for i in range(self.__height):
            row_string = "#"*self.__width
            row_string += "\n"
            new_list.append(row_string)
        formatted = "".join(new_list)
        return formatted.strip()

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    def area(self):
        """calculating area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculating perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)
