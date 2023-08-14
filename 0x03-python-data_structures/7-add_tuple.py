#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if (len(tuple_a) == 0 and len(tuple_b) == 0):
        return (())
    #if one of the tuple is empty
    if (len(tuple_a) == 0):
        a1, a0 = 0, 0
    if (len(tuple_b) == 0):
        b0, b1 = 0, 0
    #if the tuple has one element
    if (len(tuple_a) == 1):
        a0, a1 = tuple_a[0], 0
    if (len(tuple_b) == 1):
        b0, b1 = tuple_b[0], 0
    #if the tuple has 2 or more elements
    if (len(tuple_a) >= 2):
        a0, a1 = tuple_a[0], tuple_a[1]
    if (len(tuple_b) >= 2):
        b0, b1 = tuple_b[0], tuple_b[1]
    #addition of tuple elements
    tuple = (a0 + b0, a1 + b1)
    return (tuple)
