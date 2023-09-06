#!/usr/bin/python3

"""
contains 5 methods, including the constructor,
two setters and two getters
"""


class Rectangle:
    """
    implemnets the rectange
    """

    def __init__(self, width=0, height=0):
        """
        The constructor:
        Args:
        width: input int, that is the width of the rectangles
        height: input int, the height of the rectangle
        """
        self.width = width
        self.height = height

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
