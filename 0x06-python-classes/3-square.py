#!/usr/bin/python3
"""this module defies a Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """initialization of the square with a size.
        Args:
        size (int, optional): the size of the square dflt to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = s
    def area(self):
        """Calculate the area of a square
        Returns:
            int: the area of the square
        """
        return self.__size * self.__size
