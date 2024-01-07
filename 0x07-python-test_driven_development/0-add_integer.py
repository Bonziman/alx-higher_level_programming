#!/usr/bin/python3
""" This is a module that has an addition function"""


def add_integer(a, b=98):
    """A function that adds 2 integers.
    Args:
        a(int): first number to be added.
        b(int): second number to be added.
    Returns: result(the result of the addition of the 2 numbers)
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return int(a + b)
