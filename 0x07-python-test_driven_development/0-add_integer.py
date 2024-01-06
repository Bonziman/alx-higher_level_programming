#!/usr/bin/python3
""" This is a module that has an addition function"""

def add_integer(a, b=98):
    """A function that adds 2 integers.
    Args:
        a(int): first number to be added.
        b(int): second number to be added.
    Returns: result(the result of the addition of the 2 numbers)
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    result = a + b
    return result
