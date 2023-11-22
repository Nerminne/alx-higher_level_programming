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
        def size(self) -> getter
        def size(self, value) -> setter
        area(self) -> public instance method return area
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (isinstance(value, int)):
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if (self.__size == 0):
            print("")
        else:
            for lines in range(0, self.__size):
                    print("#" * self.__size)
