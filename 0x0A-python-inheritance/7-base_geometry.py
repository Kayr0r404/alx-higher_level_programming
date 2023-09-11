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
            raise TypeError(f"{name} must be an integer")
        if (value <= 0):
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
