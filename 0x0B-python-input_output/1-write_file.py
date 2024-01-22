#!/usr/bin/python3
"""Model that produces a function to write into files"""


def write_file(filename="", text=""):
    """Function to write into UTF8 file
        Args:
            filename(str):name of the file to write into
            text(str): the text to be written
        Returns: the number of characters written
        """
    with open(filename, 'w') as f:
        return f.write(text)
