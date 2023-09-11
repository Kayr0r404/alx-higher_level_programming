#!/usr/bin/python3
"""implementing an Base Geometry class"""


class BaseGeometry:
    """class:"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not (isinstance(value, int)):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
        

class Rectangle(BaseGeometry):
    """define instanges of BaseGeometry"""

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
