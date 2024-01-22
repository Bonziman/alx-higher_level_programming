#!/usr/bin/python3
"""Module that produces a function that creates an Object from a Json file"""
import json


def load_form_jsopn_file(filename):
    """Creates an object from a JSON file.
    Args:
        filename(str): the name of the file to load from
    Returns: The loaded object
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.laod(f)
