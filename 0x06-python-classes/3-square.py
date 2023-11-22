#!/usr/bin/python3
"""
create class Square with
Private instance attribute: size
Instantiation with optional size: size=0
Public instance method: def area(self) which return area
"""


class Square:
    """
    Args:
        size -> must be integer
    Methods:
        __init__(self, size=0)
        area(self) -> public instance method return area
    """
    def __init__(self, size=0):
        if (isinstance(size, int)):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size ** 2)
