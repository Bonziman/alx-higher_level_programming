#!/usr/bin/python3
""" A module that defines a Rectangle class"""


class Rectangle:
    """Creates a rectangle class"""

    def __init__(self, width, height):
        """initializing a rectangle with a given
        width and height.

        Args:
            width (int) the width of the rectangle
            height (int) the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of a rectangle."""
        return self.__width
    def height(self):
        """Returns the height of a rectangle."""
        return self.__height
    @width.setter
    def width(slef, value):
        """set the width of a rectangle.
        Args:
            value (int): the width value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @height.setter
    def height(self, value):
        """Sets the height of a rectangle object.
        Args:
            value (int): the height to be set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
