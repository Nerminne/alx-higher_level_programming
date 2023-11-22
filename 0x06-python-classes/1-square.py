#!/usr/bin/python3

"""
create class Square with
Private instance attribute: size
"""


class Square:
    """
    Args:
        size -> (no type/value verification)
    Attributes:
        size -> size of square (Private instance attribute)
    """
    def __init__(self, size):
        self.__size = size
