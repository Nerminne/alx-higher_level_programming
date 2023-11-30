#!/usr/bin/python3
"""
Write a class  that prevents the user from creating
new instance attributes, except when it called first_name
"""


class LockedClass:
    """ class with no class or object attribute """
    __slots__ = ['first_name']
