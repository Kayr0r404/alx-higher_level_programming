#!/usr/bin/python3

def add_integer(a, b=98):
    """
    a function that adds 2 integers.
    Args:
    @a: input int/ float
    @b: input int/ float
    Return: sum of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a + b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")