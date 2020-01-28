#!/usr/bin/python3
"""
This module for class Base
"""
import json


class Base:
    """
    class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        with open('{}.json'.format(cls.__name__), 'w+') as File:
            if list_objs is None:
                File.write(cls.to_json_string([]))
            else:
                list = []
                for i in list_objs:
                    i = i.to_dictionary()
                    list.append(i)
                File.write(cls.to_json_string(list))
