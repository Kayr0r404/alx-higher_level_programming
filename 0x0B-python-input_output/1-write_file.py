#!/usr/bin/python3
"""implementation"""


def write_file(filenam="", text=""):
    """Writes text to filename, if file alrady exists it overwrite it"""
    with open(file=filenam, mode='w', encoding='utf-8') as file:
        contents = file.write(text)
    return contents
