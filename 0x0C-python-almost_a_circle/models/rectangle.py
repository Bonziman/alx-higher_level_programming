#!/usr/bin/python3
""" a rectangle class model"""
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """retrieve width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the size of the square.

        Args:
            value (int): The size value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(self))
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of a rectangle

        Args:
            value(int) the height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(self))
        else:
            self.__height = value

    @property
    def x(self):
        """retrieve the x of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x of a rectangle

        Args:
            value(int): the x of the rectangle
        """
        if value < 0:
            raise ValueError("{} must be >= 0".format(self))
        else:
            self.__x = value

    @property
    def y(self):
        """retrieve y of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y of a rectangle

        Args:
            value(int): the y of the rectangle
        """
        if value < 0:
            raise ValueError("{} must be >= 0".format(self))
        else:
            self.__y = value
