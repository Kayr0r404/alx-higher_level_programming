#!/usr/bin/python3
"""
contains a function that adds two integers/ floats,
with the second parameter assigned to 98 in case the not passed
Ath the bottom of the function we testing the function using
docstring
"""


def add_integer(a, b=98):
    """a function that adds 2 integers.
    Arguments/parameters:
    @a: input int/ float
    @b: input int/ float
    Return: sum of a and b"""

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a + b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
