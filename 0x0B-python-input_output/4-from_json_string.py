#!/usr/bin/python3
"""
function that returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """ convert JSON str to python data structure """
    python_data = json.loads(my_str)
    return (python_data)
