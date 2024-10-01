#!/usr/bin/python3
"""This module contains a class that has a constructor"""
try:
    class Square:
        """This class has a constructor"""
        def __init__(self, size=0, position=(0, 0)):
            """This is a method that checks whether the size provided is a
              positive integer
            args: size, size parameter provided during calling
            """
            self.__size = size
            self.__position = position
        @property
        def size(self):
            """Getter method for size"""
            return self.__size

        @size.setter
        def size(self, value):
            """Setter method for size"""
            self.__size = value
            if not isinstance(self.__size, int):
                raise TypeError("size must be an integer")
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        @property
        def position(self):
            """Get the position"""
            return self.__position
        
        @position.setter
        def position(self, value):
            if not isinstance(self.__position, tuple) and not all(x > 0 for x in self.__position):
                raise TypeError("position must be a tuple of positive integers")
        def area(self):
            """This function calculates the area of the square
            Returns: float, area of the square
            """
            area = self.__size * self.__size
            return area

        def my_print(self):
            """This function prints a square using the symbol #"""
            if self.__size == 0:
                print()
            i = 0
            while i < self.__size:
                j = 0
                print(" " * self.__position[0], end="")
                while j < self.__size:
                    print("#", end="")
                    j += 1
                print()
                i += 1

except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)
