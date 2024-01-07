#!/usr/bin/puthon3
"""A model that produces a function to manipulate a text string"""


def text_indentation(text):
    """ A function that prints a string and 2 new lines after
    ., ? and :
    Args:
        text(str): the string to be manipulated and printed
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    skip_next = False
    for i in text:
        if skip_next:
            skip_next = False
            continue
        if i == "\\":
            skip_next = True
            continue
        print(i, end="")
        if i == "." or i == "?" or i == ":":
            print("")
            print("")
            skip_next = True
