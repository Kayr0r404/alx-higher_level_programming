#!/usr/bin/python3
""" empty square class """


class Square:
    """ empty square class """

    def __init__(self, size=0):
        """
        a class Square that defines a square by: (based on 1-square.py)
        args:
        size (int): input int
        """
        self.size = size

    def area(self):
        """
        calculates the are of a square
        return: the are of a square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        getter:to retrieve it
        return: private instane
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter: set size to value
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
