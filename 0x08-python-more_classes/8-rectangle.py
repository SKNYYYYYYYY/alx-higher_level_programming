#!/usr/bin/python3
"""module with one class"""


class Rectangle:
    """rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor"""
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """string representation"""
        new_list = []
        for i in range(self.__height):
            row_string = Rectangle.print_symbol*self.__width
            row_string += "\n"
            new_list.append(row_string)
        formatted = "".join(new_list)
        return formatted.strip()

    def __repr__(self):
        """string representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deleting object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 == area_2:
            return rect_1
        if area_1 > area_2:
            return rect_1
        else:
            return rect_2
