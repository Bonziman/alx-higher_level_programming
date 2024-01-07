#!/usr/bin/python3
"""A mopdel that priduces a function to print a square"""

def print_square(size):
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
