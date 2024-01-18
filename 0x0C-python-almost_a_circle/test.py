#!/usr/bin/python3
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

r1 = Rectangle(3, 5, 1)
r1_dictionary = r1.to_dictionary()
r2 = Rectangle.create(**r1_dictionary)
print(r1)
print(r2)
print(r1 is r2)
print(r1 == r2)
s1 = Square(1, 3, 4)
s1_dictionary = s1.to_dictionary()
s2 = Square.create(**s1_dictionary)
print(s1)
print(s2)
