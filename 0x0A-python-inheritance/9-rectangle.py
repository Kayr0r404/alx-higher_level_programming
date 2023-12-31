#!/usr/bin/python3
"""implementing an Base Geometry class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """define instanges of BaseGeometry"""

    def __init__(self, width, height):

        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__height * self.__width)

    def __str__(self):
        return "[Ractange] {:d}/{:d}".format(self.__width, self.__height)
