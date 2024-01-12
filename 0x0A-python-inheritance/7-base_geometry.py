#!/usr/bin/python3
"""Module that defines an empty class"""


class BaseGeometry():
    """ An empty class"""

    def area(self):
        """
        Calculate the area of the geometry.
        Raises:
                Exception: this method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check and validate value
        Raises:
            TypeError: name must be an integer
            ValueError: name must be greater than 0
        """
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if type(value) is int and value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
