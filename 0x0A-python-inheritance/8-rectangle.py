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
