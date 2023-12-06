#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """ store converted python data structure in object """
    with open(filename, "r") as json_file:
        py_object = json.load(json_file)
        return (py_object)
