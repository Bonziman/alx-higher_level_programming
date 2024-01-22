#!/usr/bin/python3
"""Module that procudes a function to save an object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Fucntion to write an object to a text file using json string rep
    Args:
        my_obj: the object to be written as json str representation
        filename: name of the file to be written to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
