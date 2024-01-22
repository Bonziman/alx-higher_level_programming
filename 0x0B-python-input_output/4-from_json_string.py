#!/usr/bin/python3
"""Module that produces a function to return an obj from json"""
import json


def from_json_string(my_obj):
    """Function to return an object represented by a JSON string
    Args:
        my_obj: the input string.
    Returns: an object represented by a json string.
    """
    return json.loads(my_obj)
