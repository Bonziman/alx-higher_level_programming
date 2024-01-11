#!/usr/bin/python3
"""Module that defines an empty class"""


class BaseGeometry():
    """ An empty class"""

    def area(self):
        """
            Calculate the area of the geometry.
            Raises:
                Exception: this method is not implemented.
        """
        raise Exception("Area() is not implemented")
