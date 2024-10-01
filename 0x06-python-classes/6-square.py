#!/usr/bin/python3
"""This module defines a Square class with size and position attributes."""


class Square:
    """Class to define a square with a given size and position."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a size and position."""
        self.size = size  # Using the property setter
        self.position = position  # Using the property setter

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.size * self.size

    def my_print(self):
        """Print the square using the '#' character."""
        if self.size == 0:
            print("")
            return

        # Print the empty lines based on position[1]
        print("\n" * self.position[1], end="")

        # Print the square
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
