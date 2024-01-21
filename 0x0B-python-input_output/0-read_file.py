#!/usr/bin/python3
""" Model that produces a function to read and print files
    using the UTF8 encoding mode
"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
