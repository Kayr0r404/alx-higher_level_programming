#!/usr/bin/python3

def uppercase(input_str):
    output_str = ""

    for char in input_str:
        if 'a' <= char <= 'z':
            output_str += chr(ord(char) - 32)
        else:
            output_str += char

    print("{}".format(output_str))
