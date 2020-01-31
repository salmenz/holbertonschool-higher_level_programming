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

    @staticmethod
    def from_json_string(json_string):
        """Returns json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of class"""
        New = cls(69, 1, 2)
        New.update(**dictionary)
        return New

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances from the json file
        """
        try:
            with open(cls.__name__+'.json', encoding='utf-8') as File:
                data = File.read()
                object = cls.from_json_string(data)
                list = []
                for i in object:
                    list.append(cls.create(**i))
                return list
        except FileNotFoundError:
            return []
