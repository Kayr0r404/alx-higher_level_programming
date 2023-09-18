#!/usr/bin/python3
"""Inherits Rectangle"""
from rectangle import Rectangle


class Square(Rectangle):
    """extension of Rectangle,s it defines a rectangle when dith=height"""
    def __init__(self, size, x=0, y=0, id=None) -> None:
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size"""
        return self.height

    @size.setter
    def size(self, size):
        """setter method for size"""
        self.width = size
        self.height = size

    def __str__(self):
        """string representatio of a square"""
        return "[Square] ({:d}) {:d}/\
            {:d} - {:d}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) != 0:
            list = ["id", "size", "x", "y"]
            for val, name in zip(args, list):
                setattr(self, name, val)
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of the object(square)"""
        my_dict = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
        return my_dict
