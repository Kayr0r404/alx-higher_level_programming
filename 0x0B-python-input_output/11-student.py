#!/usr/bin/python3
"""defines a student"""


class Student:
    """student information"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and all(type(att) == str for att in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        return self.__dict__

    def reload_from_json(self, json):
        """reset attributes"""
        for key, val in json.items():
            setattr(self, key, val)
