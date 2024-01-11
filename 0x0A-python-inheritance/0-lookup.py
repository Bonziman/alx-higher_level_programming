#!/usr/bin/python3
"""A module that defines a lookup function"""


def lookup(obj):
    """Function that returns a list of all available attributes
    and methods of an obj
    Args:
        Obj(class): the object to return it's available attributes.
    """
    return dir(obj)
