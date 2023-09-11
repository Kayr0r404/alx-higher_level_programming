#!/usr/bin/python3
"""implementing an Base Geometry class"""


class BaseGeometry:
    """class:"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "validates if value is an int, else raise typeerror"
        if (isinstance(value, int)):
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
