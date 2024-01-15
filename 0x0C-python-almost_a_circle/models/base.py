#!/usr/bin/python3
"""The Base Model"""


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
