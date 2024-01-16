#!/usr/bin/python3
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

r1 = Rectangle(10, 7, 2, 8)
dictionary = r1.to_dictionary()
json_dictionary = Base.to_json_string([dictionary])
print(dictionary)
print(type(dictionary))
print(json_dictionary)
print(type(json_dictionary))
