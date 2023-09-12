#!/usr/bin/python3
"""How to load from a json file"""
import json


def load_from_json_file(filename):
    """craetes an object from a JSON FILE"""

    with open(file=filename, mode='r', encoding='utf-8'):
        json.load(filename)
