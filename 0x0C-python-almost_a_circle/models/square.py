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

    def update(self, *args, **kwargs):
        """
        update the square instance using args or kwargs
        Args:
            **kwargs: if not args then kwargs will be used to assign
                values to the keywords to update the instance attributes
            *args: if exist will be used to update instance attributes
                in this order:
                args[0]: will update the id
                args[1]: will update the size
                args[2]: will update the x
                args[3]: will update the y
        """

        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return the dict representation of a square instance
        """
        return {
                "id": self.id,
                "width": self.size,
                "height": self.size,
                "x": self.x,
                "y": self.y
        }

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
