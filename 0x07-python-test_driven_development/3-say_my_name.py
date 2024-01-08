#!/usr/bin/python3
"""A model that presents a function to say your name"""


def say_my_name(first_name, last_name=""):
    """ A function to say your name
    Args:
        first_name(str): your first name
        last_name(str): your last name
    """
    if not first_name:
        raise TypeError("say_my_name() missing 1 required positional argument: 'first_name'")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
