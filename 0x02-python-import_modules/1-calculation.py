#!/usr/bin/python3
from calculator_1 import div, mul, sub, add
if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}".format(a, b, add(a, b), a, b, sub(a, b), a, b, mul(a, b), a, b, div(a, b)))
