#!/usr/bin/python3
"""The Base Model"""
import json

class Base:
    """ Base class
    which is a base for other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Init function for the class
        Args:
            id(int): the id of the class objects
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json representaion of a list_dictionaries

        Args:
            list_dictionaries(list): the list to return
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON string representation of a list_objs into a file
        """
        if list_objs is None:
            list_objs = []

        file_name = "{}.json".format(cls.__name__)
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
        )

        with open(file_name, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes set provided in dictionary
        """
        dummy_instance = cls(1, 1)
        if hasattr(dummy_instance, 'update'):
            dummy_instance.update(**dictionary)
        return dummy_instance
