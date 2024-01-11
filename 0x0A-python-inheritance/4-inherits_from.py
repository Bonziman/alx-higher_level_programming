#!/usr/bin/python3
"""Module that defines a inherits_from function"""


def inherits_from(obj, a_class):
    """Function that check s if an obj is an instance of a class that
    inherited (directly or indirectly) from a specific class.
    Args:
        obj: the obj to check
        a_class: the class to check
    Returns:
        True if obj is an instance of a class that inherited form a_class
        otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
