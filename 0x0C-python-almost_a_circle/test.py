#!/usr/bin/python3
from models.square import Square
from models.rectangle import Rectangle

r1 = Rectangle(10, 2, 1, 9)
print(r1)
r1_dictionary = r1.to_dictionary()
print(r1_dictionary)
print(type(r1_dictionary))

r2 = Rectangle(1, 1)
print(r2)
r2.update(**r1_dictionary)
print(r2)
print(r1 == r2)
