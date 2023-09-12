#!/usr/bin/python3
"""Implementation of how to append a file"""


def append_write(filename="", text=''):
    "appends a file at the EOF and return number of chars added"

    with open(file=filename, mode='a', encoding='utf-8') as file:
        contents = file.write(text)
    return contents
