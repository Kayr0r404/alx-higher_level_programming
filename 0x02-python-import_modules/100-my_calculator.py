#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit()
    a, b = int(argv[1]), int(argv[3])
    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit()