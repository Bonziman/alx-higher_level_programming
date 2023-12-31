#!/usr/bin/python3
"""A mopdel that priduces a function to print a square"""


def print_square(size):
    """ A function that prints a square using #
    Args:
        size(int): the size of the square to be printed
    """
    if not size:
        raise TypeError("print_square() missing 1 required positional "
                        "argument: 'size'")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for n in range(size):
        for i in range(size):
            print("#", end="")
        print("")
