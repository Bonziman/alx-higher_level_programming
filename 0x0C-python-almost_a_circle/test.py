#!/usr/bin/python3
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
Rectangle.save_to_file([r1, r2])

with open("Rectangle.json", "r") as file:
    print(file.read())
