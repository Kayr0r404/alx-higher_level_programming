#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if (idx < 0) or (len(my_list) - 1 < idx):
        return (None)
    else:
        for i in range(len(my_list) + 1):
            print("{:d}".format(my_list[-i]))
