#!/usr/bin/python3
"""
create class Square with
Private instance attribute: size
Instantiation with optional size: size=0
"""


class Square:
    """
    Args:
        size -> must be integer
    """
    def __init__(self, size=0):
        if (isinstance(size, int)):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
