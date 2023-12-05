#!/usr/bin/python3
import math

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    if (n < 0):
        raise ValueError("n must be >= 0")
    if (math.floor(n) != n):
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    else:
        prod = 1
        if (math.floor(n) == n):
            n = int(n)
        for i in range(n, 0, -1):
            prod *= i
    
    return (prod)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testfile("example.txt")