#!/usr/bin/puthon3
"""Mudule that defines a MyInt class"""


class MyInt(int):
    """rebel class that has the '==' and '!=' operators
    inverted
    """

    def __eq__(self, other):
        return not self.__eq__(other)

    def __ne_(self, other):
        if isinstance(other, MyInt):
            return self.value == other.value
        else:
            return False
