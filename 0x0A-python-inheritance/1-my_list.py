#!/usr/bin/python3
"""Model that defines a MyList class"""


class MyList(list):
    """MyList class that inherites from the list"""
    def __init__(self, *args, **kwargs):
        """Initialisation method"""

        super().__init__(*args, **kwargs)

    def print_sorted(self):
        """Method to print the list sorted from smallest to biggest"""

        sorted_list = sorted(self, reverse=False)
        print(sorted_list)
