#!/usr/bin/python3
"""A module that defines a Rectangle class."""


class Rectangle:
    """Creates a rectangle class."""

    def __init__(self, width=0, height=0):
        """initializing a rectangle with a given
        width and height.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """calculate the area of a rectangle

        Rreturns:
            int: the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """calculate the perimeter of the rectangle

        Returns:
            int: the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @property
    def width(self):
        """Returns the width of a rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of a rectangle.
        Args:
            value (int): the width value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of a rectangle."""
        return self.__height

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
    def __str__(self):
        """Prints the rectangle with '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += '#' * self.width + '\n'
        return rectangle_str.rstrip('\n')
