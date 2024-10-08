#!/usr/bin/python3
"""This module contains a class that defines a square"""

class Square:
    """This class defines a square with size and position attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square
        Args:
            size (int): The size of the square
            position (tuple): The position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square
        Returns: int, area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters"""
        if self.__size == 0:
            print()
            return

        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
