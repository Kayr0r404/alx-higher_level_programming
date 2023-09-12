#!/usr/bin/python3
"""How to export to json"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using json representation"""

    with open(file=filename, mode="w", encoding='utf-8') as file:
        json.dump(my_obj, file)
