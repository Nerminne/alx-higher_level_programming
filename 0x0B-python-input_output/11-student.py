#!/usr/bin/python3
"""
Write a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
"""


class Student:
    """ class contain student info """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            new_dict = {}
        for key in attrs:
            if key in self.__dict__.keys():
                new_dict[key] = self.__dict__[key]
        return (new_dict)

    def reload_from_json(self, json):
        for keys in json.keys():
            if keys in self.__dict__.keys():
                self.__dict__[keys] = json[keys]
