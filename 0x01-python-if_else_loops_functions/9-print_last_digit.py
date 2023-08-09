#!/usr/bin/python3
def print_last_digit(numb):
    lst = abs(numb) % 10
    print(f"{lst}", end="")
    return (lst)
