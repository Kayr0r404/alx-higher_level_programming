#!/usr/bin/python3
"""Implemantation"""


def read_file(filename=""):
    """reads file contents and ptint to the stdout"""
    with open(filename, encoding='utf-8') as file:
        print(file.rstrip())
