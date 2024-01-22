#!/usr/bin/python3
"""Module that procudes a function to return JSON"""
import json


def to_json_string(my_obj):
    """Function to return the JSON representation of an object (string)
    Args:
        my_obj: the obj to be represented
    Returns: str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
