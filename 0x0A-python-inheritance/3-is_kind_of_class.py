#!/usr/bin/python3
"""Module that defines a is kind of class function"""


def is_kind_of_class(obj, a_class):
    """ Function that checks if an obj is an instance of a class or of
    a class that inherites form it.
    Args:
        obj: the object to check.
        a_class: the class to check
    Returns:
        True if the obj is an instance of a_class or of a class that
        inherites from it, otherwise False.
    """
    return isinstance(obj, a_class)
