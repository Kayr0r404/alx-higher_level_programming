#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, b = int(argv[1]), int(argv[3])
    if argv[2] == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif argv[2] == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif argv[2] == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif argv[2] == '/':
        print(f"{a} / {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
