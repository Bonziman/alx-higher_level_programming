#!/usr/bin/python3
"""Module that has a script to add all arguments to a python list"""
import sys
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

if __name__ == "__main__":
    try:
        items = load_from_json_file("add_items.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_items.json")
