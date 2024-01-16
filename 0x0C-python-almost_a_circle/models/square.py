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
