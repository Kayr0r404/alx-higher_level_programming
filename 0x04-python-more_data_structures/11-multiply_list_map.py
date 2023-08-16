#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mul = lambda x: x * number
    return list(map(mul, my_list))
