#!/usr/bin/python3
"""Module that procudes a text append function"""


def append_write(filename="", text=""):
    """function to append a text into a text file
        Args:
            filename(str): the file name
            text(str): the text to append to the file
        Returns: the number of characters appended
    """
    with open(filename, 'a') as f:
        return f.write(text)
