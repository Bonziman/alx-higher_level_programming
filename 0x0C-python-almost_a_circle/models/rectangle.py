#!/usr/bin/python3
""" a rectangle class model"""
from models.base import Base


class Rectangle(Base):
    """ A rectangle class that inherites from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Method to calculate the area of a rectangle instance

        Returns: the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Method to print the rectangle
        using the # character
        """
        for k in range(self.y):
            print("")
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for n in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        Return string representation of rectangle
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args):
        self.id = args[0]
        self.width = args[1]
        self.height = args[2]
        self.x = args[3]
        self.y = args[4]


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
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
