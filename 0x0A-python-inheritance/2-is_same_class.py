#!/usr/bin/python3
"""Model that defines a is_same_class function"""


def is_same_class(obj, a_class):
    """Function that returns True if the obj is an instance of the specified
    class, otherwise False.
    Args:
        obj: An object to check.
        a_class: The specified class.
    Returns:
        True if obj is an instance of a_class, otherwise False
    """
    return type(obj) is a_class
