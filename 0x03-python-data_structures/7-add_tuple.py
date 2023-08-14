#!/usr/nin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) == 0 or len(tuple_b) == 0):
        a, b = 0, 0
    else:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]

    tuple = (a, b)
    return (tuple)
