#!/usr/bin/python3
"""Model that defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Square class that inherits from Rectangle class directly
    and from Base class indirectly
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize a square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overide the default str representation
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Retrieve the size(width or height) of a square instance
        """
        return self.width

    @size.setter
    def size(self, value):
        """Assign size ro a square instance

        Args:
            value: the value to be assigned to size
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = value
            self.width = value
            self.height = value
