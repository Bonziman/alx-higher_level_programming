#!/usr/bin/python3
"""Model that defines a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherites from the rectangle class
    (inderect inheritance from BaseGeometry)
    """
    def __init__(self, size):
        if self.integer_validator("size", size):
            self.size = size

    def area(self):
        """
        Method to calculate the area of a square
        Returns: the area of the square
        """
        return self.size * self.size
    def __str__(self):
        """
        method to return the string representation of a square
        """
        return "[Square] {}/{}". format(self.size, self.size)
