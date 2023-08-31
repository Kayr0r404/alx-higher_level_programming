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
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculates the are of a square
        return: the are of a square
        """
        return (self.__size ** 2)