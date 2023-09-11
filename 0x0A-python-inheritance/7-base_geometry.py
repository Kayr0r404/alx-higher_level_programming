#!/usr/bin/python3
"""implementing an Base Geometry class"""


class BaseGeometry:
    """class:"""
    def __init__(self):
        pass
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "validates if value is an int, else raise typeerror"
        if not (isinstance(value, int)):
            raise TypeError("{:s} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))

