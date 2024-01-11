#!/usr/bin/python3
"""Model that defines a MyList class"""


class MyList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print_sorted(self):
        sorted_list = sorted(self, reverse=False)
        print(sorted_list)
