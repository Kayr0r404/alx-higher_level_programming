#!/usr/bin/python3
"""How to covert python objects into json string"""
import json


def to_json_string(my_obj):
    """converts python objects into json string"""
    return json.dumps(my_obj)
