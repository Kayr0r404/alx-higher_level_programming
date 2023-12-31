#!/usr/bin/python3

"""
contains 5 methods, including the constructor,
two setters and two getters
"""


class Rectangle:
    """
    implemnets the rectange
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        The constructor:
        Args:
        width: input int, that is the width of the rectangles
        height: input int, the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """The getter for the width of the width
        Return: the width value
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        set the width value
        """
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculate the are of the rectangle
        Return: product length and width of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Finds the parameter of the rectangle
        Return: the parameter of the rectangle
        """
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns representation of rectange as string"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle_str += '#'
            if (i + 1 < self.__height):
                rectangle_str += '\n'

        return rectangle_str

    def __repr__(self) -> str:
        """Returns representation of rectange as string"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """The destructor: Deletes instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
