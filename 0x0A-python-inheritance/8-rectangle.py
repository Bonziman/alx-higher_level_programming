#!/usr/bin/python3
"""Model that defines a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle claas that inherites from
    BaseGeometry class
    """

    def __init__(self, width, height):
        if self.integer_validator("width", width):
            self.width = width
        if self.integer_validator("height", height):
            self.height = height
