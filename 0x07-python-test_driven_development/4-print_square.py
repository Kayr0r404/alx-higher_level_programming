#!/usr/bin/python3
"""Implementation"""


def print_square(size):
    """
    function  prints a square with the character #
    Arg:
    size: is the size of the aquare
    """
    if not (isinstance(size, int)):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    if (isinstance(size, (list, str, float))):
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
