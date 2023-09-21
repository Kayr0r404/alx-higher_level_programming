#!/usr/bin/python3
"""Implementation of Base object"""
import json


class Base:
    """
    Base class:
    private class attribute: nb_object- number of objects created
    """
    __bn_objects = 0

    def __init__(self, id=None) -> None:
        """
        The class constructor, that takes an id of type int,
        if not provided, we increment the class attribute
        and assign id to the class attibute
        """
        if id is not None:
            self.id = id
        else:
            Base.__bn_objects += 1
            self.id = Base.__bn_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list of dictionaries
        if the list is null or empty, string '[]' is returned
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries, ensure_ascii=False)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        the method writes the JSON string representation of
        list_objs to a  json file
        list_objs: is a list of instances who inherits of Base
        if list_objs is None, save an empty json file
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(file=filename, mode='w', encoding='utf-8') as file:
            json_string =\
                cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_string,)

    @staticmethod
    def from_json_string(json_string):
        """
        the mothod returns the list of the
        JSON string representation
        json_string i a string representing a list of dictionaries
        if the string is None or empty, return an empty list
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Args:
            dictionary:
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)  # Default values for Rectangle
        elif cls.__name__ == "Square":
            new_instance = cls(1)     # Default value for Square
        else:
            new_instance = cls()      # Default value for other classes

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
         Returns a list of instances:
        """
        filename = cls.__name__ + '.json'
        # data = cls.from_json_string(filename)
        try:
            with open(file=filename, mode='r', encoding='utf-8') as f:
                data = cls.from_json_string(f)
        except:
            return []
        return [cls.create(instance) for instance in data]
